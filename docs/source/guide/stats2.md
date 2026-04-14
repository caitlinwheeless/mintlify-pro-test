# Agreement (Label Studio Enterprise)

Label Studio Enterprise includes annotation and labeling statistics that the open-source Community Edition does not provide. If you use Label Studio Community Edition, see [Label Studio Features](https://labelstud.io/guide/label_studio_compare.html) for comparison.

Annotation statistics help you assess dataset quality, readiness for training, and the performance of annotators and reviewers.

---

## Task agreement

Task agreement (also called "labeling consensus" or "annotation consensus") measures how much annotators agree when labeling the same task. In Label Studio Enterprise you can see:

- **Per-task agreement score** — Shown in the Data Manager for each task. The [Agreement column](#agreement-column) shows how well annotations on that task match across the participants included in the calculation.
- **Selectable agreement** — You can choose which annotators, models, and ground truth to include in the calculation. In the Data Manager this is the [Agreement (Selected) column](#agreement-selected-column) or the same Agreement column with a selection filter, depending on your project configuration.
- **Inter-annotator agreement matrix** — On the project **Members** page, a matrix shows how well annotations from specific annotators agree with each other overall or for selected tasks. You can also compare annotators to predictions or to ground truth.

For where to view and use agreement in the UI, see [Verify model and annotator performance](quality.html#Verify-model-and-annotator-performance).

---



---

## Dimensions and agreement

Agreement in Label Studio Enterprise is built on **dimensions**. A **dimension** is one aspect of annotations that you want to measure for agreement. There is one dimension per **control tag** in your labeling configuration (e.g., one for `RectangleLabels`, one for `Choices`, one for `Rating`).

Each dimension defines:

- **What to extract** — Which part of the annotation JSON to use (e.g., labels, bounding boxes, text spans), based on the control tag.
- **How to compare** — The **metric** used to compare values between annotators (e.g., Exact Match, IoU, Overlap) and its parameters (e.g., threshold).

### Per-dimension and overall agreement

- **Per-dimension scores** — You see an agreement score for each dimension (each control tag) separately. This lets you see which parts of the task have higher or lower agreement (e.g., good agreement on bounding boxes but low agreement on a choice field).
- **Overall task agreement** — The system aggregates per-dimension scores into a single task-level score (by default, the mean of all dimension scores). This is what appears in the main Agreement column when you do not filter by dimension.

Example: a project with RectangleLabels, Choices, and Rating might show:

- RectangleLabels (IoU): **83%**
- Choices (Exact Match): **33%**
- Rating (Numeric Difference): **33%**  
- **Overall task agreement**: **(83 + 33 + 33) / 3 ≈ 50%**

So you get both a high-level number and a breakdown by control tag. Dimensions are created automatically from your label config; you configure the metric (and optional label weights) per dimension in **Settings → Quality**.

---

## Agreement methodology

The **agreement methodology** controls how scores from multiple annotators are combined into one task-level agreement score. Two options are available:

### Pairwise average

- **How it works**: For every unique pair of annotators, the system computes an agreement score for that pair, then averages all pairwise scores.
- **Example** (3 annotators, labels "Dog", "Dog", "Cat"):
  - Pair 1–2: Dog vs Dog → 1.0  
  - Pair 1–3: Dog vs Cat → 0.0  
  - Pair 2–3: Dog vs Cat → 0.0  
  - **Task agreement** = (1.0 + 0.0 + 0.0) / 3 = **33%**
- **Use when**: You have two annotations per task and want the raw score between them, or you want sensitivity to outliers (one disagreeing annotator can pull the score down). This matches the behavior of the previous agreement system if you need consistency with historical data.

### Consensus

- **How it works**: Agreement is computed across all annotators at once, measuring how much they converge to a common answer. The result aligns with “how many annotators agree?”
- **Example** (same 3 annotators, "Dog", "Dog", "Cat"):
  - Two out of three agree on "Dog".
  - **Task agreement** = **66%**
- **Use when**: You want agreement to reflect majority agreement and to be more robust to a single outlier. Consensus is generally recommended for new projects.

**Consensus and continuous metrics**: Consensus uses binary match/no-match. For continuous metrics (e.g., IoU), you must set a **threshold** in the dimension’s metric parameters; scores above the threshold count as match, below as no match. You configure this in **Settings → Quality** when you select the metric for that dimension (e.g., “IoU (Threshold)” with threshold 0.75).

You can switch between methodologies at any time; both pairwise and consensus scores are stored.

---

## Agreement score and metrics

The **agreement score** for a task (or for one dimension) measures how similar the annotations are, according to the metric chosen for each dimension.

### Choosing metrics per dimension

In **Settings → Quality**, under Agreement, you can:

- See the list of **dimensions** (one per control tag).
- For each dimension, select a **metric** (e.g., Exact Match, IoU, Overlap, Numeric Difference) and set its **parameters** (e.g., IoU threshold, numeric difference threshold).
- Use **label weights** to emphasize or de-emphasize certain labels in the calculation.

Default metrics are assigned by control tag type (e.g., IoU for RectangleLabels, Exact Match for Choices). You can change the metric per dimension to better match your task.

### Available agreement metrics (summary)

Metrics are grouped by the type of annotation they compare. Many metrics have a **threshold** variant (name often ends with “(Threshold)”): the raw score is turned into 0 or 1 using a threshold, which is required for [consensus](#consensus) when the base metric is continuous.

| Category | Examples | Typical control tags |
|----------|----------|------------------------|
| **Categorical / discrete** | Exact Match, Taxonomy Path Matching, Taxonomy Subtree (IoU) | Choices, Taxonomy, Pairwise, DateTime |
| **Numeric** | Numeric Difference (with optional threshold) | Number, Rating |
| **Bounding box** | IoU, IoU (Threshold), Bounding Box Labels Similarity, Bounding Box Text Similarity | RectangleLabels, Rectangle, Choices/TextArea per region |
| **Polygon** | Polygon IoU, Polygon IoU (Threshold), Polygon Labels/Text Similarity | PolygonLabels, Polygon, Choices/TextArea per region |
| **Spans / segments** | Overlap, Overlap (Threshold), Span Labels/Text Similarity | Labels, ParagraphLabels, TimeSeriesLabels, TimelineLabels, HyperTextLabels |
| **Text** | Text Similarity, Text Similarity (Threshold), Semantic Similarity | TextArea |
| **Video / landmarks** | Exact Frame Matching, Object Tracking, Keypoint Distance | VideoRectangle, KeypointLabels |
| **Custom** | Custom Metric (user-defined function) | User-defined dimensions |

For the full list of metrics, default metrics per control tag, and which support pairwise-only vs both pairwise and consensus, see the in-app metric selector in **Settings → Quality** or the internal reference `AGREEMENT_V2_METRICS.md`.



---

## Label weights

You can customize the **weight** of different labels (or choices) when calculating agreement. For example, you might weight “Critical” higher than “Optional.” Weights are configured per dimension in **Settings → Quality** (under Agreement, in the same place you set the metric). You can set:

- **Per-label weights** — A weight for each label used in that dimension.
- **Overall dimension weight** — How much this dimension contributes to the overall task agreement (default 1.0).

Label weights apply to the comparison logic of the selected metric (e.g., exact match with weights, or IoU weighted by label).

---

## Low agreement threshold

A **low agreement threshold** (in **Settings → Quality**) lets you enforce a minimum agreement level before a task is considered complete. If the task’s agreement score is below this threshold, the task is not marked complete until the threshold is met (subject to your workflow and assignment settings). Use this to ensure that overlapping annotations only “pass” when annotators agree sufficiently.

---

## Where agreement appears

- **Data Manager**  
  - **Agreement** column: overall task agreement (and, if enabled, one column per dimension).  
  - **Agreement (Selected)** (or filtered Agreement): same calculation restricted to the annotators, models, and ground truth you select.  
  - You can filter and sort by agreement to find low-agreement tasks or compare dimensions.
- **Members page**  
  - Inter-annotator agreement matrix: agreement between selected annotators (and optionally models), with the option to open tasks where both have annotated.
- **Review and quality**  
  - Agreement can be shown to reviewers and used in quality dashboards when the corresponding project settings are enabled.

For step-by-step use in the UI, see [Verify model and annotator performance](quality.html#Verify-model-and-annotator-performance) and [Project settings – Task agreement](project_settings_lse#task-agreement).

---

## Agreement column {#agreement-column}

In the Data Manager, the **Agreement** column shows the overall task-level agreement score (0–100%). It uses the methodology (pairwise or consensus) and participant selection configured for the project or view. When dimensions are enabled, the overall value is the aggregate of per-dimension scores (e.g., mean). You can also add columns for individual dimensions to see per–control-tag agreement.

---

## Agreement (Selected) column {#agreement-selected-column}

When you want agreement only among certain annotators, models, or ground truth, use the **Agreement (Selected)** column or the same Agreement column with a selection filter (depending on configuration). The calculation is the same as the main Agreement column but restricted to the participants you choose, so you can compare, for example, annotator-vs-annotator or annotator-vs-ground-truth agreement.

---

## See also

- [Verify model and annotator performance](quality.html#Verify-model-and-annotator-performance)
- [Project settings – Task agreement](project_settings_lse#task-agreement)
- [Manage data (Data Manager)](manage_data#Agreement) — Agreement and Agreement (Selected) columns
