# GCS Service Account Impersonation Storage Provider

## Overview

The `gcs_sa` storage provider enables Label Studio Enterprise (LSE) deployments running in Google Kubernetes Engine (GKE) to access GCS buckets using **Service Account Impersonation**. Instead of storing JSON keys, each LS project specifies a Target Service Account email. LSE's Workload Identity SA impersonates the Target SA to obtain short-lived access tokens.

### Key Benefits

| Aspect | JSON Key (base GCS) | SA Impersonation (gcs_sa) |
|--------|---------------------|---------------------------|
| **Security** | Private key stored in DB | No secrets -- only SA email |
| **Key rotation** | Manual | Automatic (Google-managed) |
| **Audit trail** | Key used directly | Clear impersonation chain |
| **Terraform automation** | Generate key, store secret | Simple IAM grant |
| **Blast radius** | Leaked key = full access | Revoke permission instantly |

## Architecture

```
+-------------------------------------------------------------------+
|                         GKE Cluster                                |
|  +-------------------------------------------------------------+  |
|  |                      LSE Pod                                 |  |
|  |   K8s SA: label-studio-sa                                    |  |
|  |      -> Workload Identity binding                            |  |
|  |   GCP SA: lse-base@lse-platform.iam.gserviceaccount.com     |  |
|  +-------------------------------------------------------------+  |
+-------------------------------------------------------------------+
                               |
           +-------------------+-------------------+
           |                                       |
           v                                       v
   generateAccessToken                    generateAccessToken
           |                                       |
           v                                       v
+--------------------+                +--------------------+
| Target SA A        |                | Target SA B        |
| data-sa@team-a...  |                | data-sa@team-b...  |
|                    |                |                    |
| IAM: objectViewer  |                | IAM: objectViewer  |
| on gs://bucket-a   |                | on gs://bucket-b   |
+--------------------+                +--------------------+
           |                                       |
           v                                       v
    gs://bucket-a                           gs://bucket-b
```

### Authentication Flow

1. LSE pod gets base credentials via Workload Identity (automatic in GKE)
2. Per request, LSE uses `google.auth.impersonated_credentials` to obtain a short-lived token for the Target SA
3. The token is used to access GCS as the Target SA
4. Token refresh is handled automatically by the google-auth library

## Infrastructure Setup

### Level 1: LSE Platform (one-time setup)

Configured by the platform team deploying LSE.

```yaml
# K8s ServiceAccount with Workload Identity binding
apiVersion: v1
kind: ServiceAccount
metadata:
  name: label-studio-sa
  namespace: label-studio
  annotations:
    iam.gke.io/gcp-service-account: lse-base@lse-platform-project.iam.gserviceaccount.com
```

```hcl
# Terraform: Workload Identity SA for LSE
resource "google_service_account" "lse_base" {
  project      = "lse-platform-project"
  account_id   = "lse-base"
  display_name = "Label Studio Enterprise Base SA"
}

resource "google_service_account_iam_member" "workload_identity_binding" {
  service_account_id = google_service_account.lse_base.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "serviceAccount:lse-platform-project.svc.id.goog[label-studio/label-studio-sa]"
}
```

### Level 2: Execution Project (per data domain)

Configured by the customer data team via Terraform.

```hcl
# 1. Create Target SA in customer's GCP project
resource "google_service_account" "sa_lse_data" {
  project      = "customer-data-project"
  account_id   = "sa-lse-data"
  display_name = "Label Studio Data Access SA"
}

# 2. Grant Target SA access to specific bucket
resource "google_storage_bucket_iam_member" "bucket_read" {
  bucket = "customer-data-bucket"
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.sa_lse_data.email}"
}

resource "google_storage_bucket_iam_member" "bucket_write" {
  bucket = "customer-data-bucket"
  role   = "roles/storage.objectCreator"
  member = "serviceAccount:${google_service_account.sa_lse_data.email}"
}

# 3. Allow LSE Workload Identity SA to impersonate this Target SA
resource "google_service_account_iam_member" "lse_can_impersonate" {
  service_account_id = google_service_account.sa_lse_data.name
  role               = "roles/iam.serviceAccountTokenCreator"
  member             = "serviceAccount:lse-base@lse-platform-project.iam.gserviceaccount.com"
}
```

### Level 3: LS Project Configuration (per annotation project)

#### Via Label Studio UI

1. Go to Project Settings -> Cloud Storage -> Add Source Storage
2. Select "Google Cloud Storage (SA Impersonation)"
3. Fill in:
   - **Target Service Account Email:** `sa-lse-data@customer-data-project.iam.gserviceaccount.com`
   - **Bucket:** `customer-data-bucket`
   - **Prefix:** `images/` (optional)

#### Via SDK

```python
from label_studio_sdk import Client

ls = Client(url='https://label-studio.company.internal', api_key='...')

project = ls.projects.create(title='Image Labeling')
project.create_source_storage(
    storage_type='gcs_sa',
    target_service_account_email='sa-lse-data@customer-data-project.iam.gserviceaccount.com',
    bucket='customer-data-bucket',
    prefix='images/',
)
```

## IAM Permissions Summary

| SA | Role | On Resource | Purpose |
|----|------|-------------|---------|
| `lse-base@lse-platform...` | `roles/iam.workloadIdentityUser` | K8s SA binding | Pod gets GCP credentials |
| `lse-base@lse-platform...` | `roles/iam.serviceAccountTokenCreator` | Each Target SA | Can impersonate Target SAs |
| `target-sa@customer...` | `roles/storage.objectViewer` | Bucket | Read data |
| `target-sa@customer...` | `roles/storage.objectCreator` | Bucket | Write annotations |

## Presigned URL Generation

Since we don't possess the Target SA's private key, presigned URLs are generated using the IAM `signBlob` API. This requires the Workload Identity SA to have `roles/iam.serviceAccountTokenCreator` on the Target SA (which is already required for impersonation).

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `403 Permission denied on generateAccessToken` | Missing `serviceAccountTokenCreator` | Grant `roles/iam.serviceAccountTokenCreator` to LSE's Workload Identity SA on the Target SA |
| `404 Service account not found` | SA doesn't exist or wrong email | Verify the email ends with `.iam.gserviceaccount.com` |
| `403 Access denied to bucket` | Target SA lacks bucket permission | Grant `roles/storage.objectViewer` (import) or `roles/storage.objectCreator` (export) to the Target SA on the bucket |
| `Cannot impersonate service account` | Impersonation chain broken | Check all three levels of IAM setup above |

## Comparison with Other GCS Providers

| Aspect | GCS (OSS) | GCS WIF (LSE) | GCS SA (LSE) |
|--------|-----------|---------------|--------------|
| **Auth method** | JSON key | AWS -> WIF token exchange | SA Impersonation |
| **Secrets in UI** | Yes (key content) | No | No |
| **LSE location** | Anywhere | AWS | GCP (GKE) |
| **Complexity** | Low | High | Low |
| **Automation** | Generate + store key | Complex WIF setup | Simple IAM grant |

## References

- [Service Account Impersonation](https://cloud.google.com/iam/docs/service-account-impersonation)
- [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
- [IAM Credentials API](https://cloud.google.com/iam/docs/reference/credentials/rest)
- [Signed URLs with Impersonation](https://cloud.google.com/storage/docs/access-control/signing-urls-with-helpers)
- [google-auth-library-python](https://google-auth.readthedocs.io/en/latest/reference/google.auth.impersonated_credentials.html)