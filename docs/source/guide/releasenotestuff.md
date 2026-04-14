---
title: release notes
short: release notes
type: guide
tier: enterprise
order: 2
order_enterprise: 2
section: "Integrate & Extend"
---


### New features

#### Programmable interfaces with React

We're introducing a new tag: [**`<ReactCode>`**](/tags/reactcode).

ReactCode represents new evaluation and annotation engine for building fully programmable interfaces that better fit complex, real-world labeling and evaluation use cases.

With this tag, you can:

- Build flexible interfaces for complex, multimodal data
- Embed labeling and evaluation directly into your own applications, so human feedback happens where your experts already work
- Maintain compatibility with the quality, governance, and workflow controls you use in Label Studio Enterprise

![Screenshot](/images/releases/2-33-react-audio.png)

![Screenshot](/images/releases/2-33-react-pdf.png)

![Screenshot](/images/releases/2-33-react-claims.png)

For more information, see the following resources:

- [**ReactCode tag**](/tags/reactcode)
- [**ReactCode templates**](/templates/gallery_react)
- [**Web page - The new annotation & evaluation engine**](https://humansignal.com/programmable-ui/)
- [**Blog post - Building the New Human Evaluation Layer for AI and Agentic systems**](https://humansignal.com/blog/new-evaluation-engine/)

#### Annotate images with vector lines

There are two new tags for image annotation: [**Vector**](/tags/vector) and [**VectorLabels**](/tags/vectorlabels). 

You can use these tags for point-based vector annotation (polylines, polygons, skeletons).   

![Screenshot](/images/tags/vector.png)

### Feature updates

#### Service Principal authentication for Databricks

When setting up cloud storage for Databricks, you can now select whether you want to use a personal access token, Databricks Service Principal, or Azure AD Databricks Service Principal.

For more information, see [Set up Databricks UC volume storage](storage_databricks).

![Screenshot](/images/releases/2-33-db.avif)

#### Updated project Members page

The **Project > Settings > Members** page has been fully redesigned.

It includes the following changes:

- Now, when you open the page, you will see a table with all project members, their role, when they were last active, and when they were added to your organization.
- You can now hide inherited project members.Inherited members are members who have access to the project because they inherited it by being an Administrator or Owner, or by being added as a member to the project's parent workspace.
- To add members, you can now click **Add Members** to open a modal where you can filter organization members by name, email, and last active.Depending on your organization's permissions, you can also invite new organizations members directly to the project.

##### Before

**Members** page:

![Screenshot](/images/releases/2-33-members-before.avif)

##### After

**Members** page:

![Screenshot](/images/releases/2-33-members0.avif)

**Add Members** modal:

![Screenshot](/images/releases/2-33-members1.avif)

#### Updated members table on Organization page

The members table on the Organization page has been redesigned and improved to include:

- A **Date Added** column
- Pagination and the ability to select how many members appear on each page
- When viewing a member's details, you can now click to copy their email address

Members table:

![Screenshot](/images/releases/2-33-members-table.avif)

Member details:

![Screenshot](/images/releases/2-33-members-details.avif)


#### Interactive view for task source

When clicking **Show task source <>** from the Data Manager, you will see a new **Interactive** view.

From here you can filter, search, and expand/collapse sections in the task source. You can also selectively copy sections of the JSON and toggle whether to show the resolved URIs. 

![Screenshot](/images/releases/2-33-source.avif)


#### Set strict overlap for annotators

There is a new [**Enforce strict overlap limit**](https://docs.humansignal.com/guide/project_settings_lse#overlap) setting under **Quality > Overlap of Annotations**.

Previously, it was possible to have more annotations than the number you set for **Annotations per task**.

This would most frequently happen in situations where you set a low task reservation time, meaning that task locks expired before annotators submitted their tasks -- allowing other annotators to access and then submit the task, and potentially resulting in an excess of annotations.

When this new setting is enabled, if too many annotators are try to submit a task, they will see an error message. Their draft will be saved, but they will be unable to submit their annotation.

Note that strict enforcement only applies towards annotations created by users in the Annotator role.

![Screenshot](/images/releases/2-33-strict1.png)

![Screenshot](/images/releases/2-33-strict2.avif)



#### Configure continuous annotator evaluation

Previously, when configuring [**annotator evaluation**](https://docs.humansignal.com/guide/project_settings_lse#annotator-eval) against ground truth tasks, you could configure exactly how many ground truth tasks each annotator should see as they begin annotating. The remaining ground truth tasks would be shown to each annotator depending on where they are and the task ordering method.

Now, you can set a specific number of ground truth tasks to be included in continuous evaluation.

You can use this as a way to ensure that not all annotators see the same ground truths, as some will see certain tasks during continuous evaluation and others will not.

**Before:**

![Screenshot](/images/releases/2-33-continuous1.avif)

**After:**

![Screenshot](/images/releases/2-33-continuous2.avif)



#### Restrict Prompts evaluation for tasks without predictions

There is a new option to only run a Prompt against tasks that do not already have predictions.

This is useful for when you have failed tasks or want to target newly added tasks.

![Screenshot](/images/releases/2-33-prompts.avif)


#### Improvements to the template builder

- **Resize panel widths in the template builder**
    
    You can now click and drag to adjust panel widths when configuring your labeling interface.

    <video style="max-width: 600px;" class="gif-border" autoplay loop muted>
      <source src="/images/releases/2-33-code.mp4">
    </video>
    
- **Press Ctrl + F/Command + F to search the Code tab**

    When working in the template builder, you can now use Ctrl + F to search the your labeling configuration XML.

    ![Screenshot](/images/releases/2-33-ctrf.png)


#### Improvements to analytics

There have been several improvements to analytics charts: 

- Improved colors and animations.

- The submitted annotation metrics now include annotations created from predictions. 

- The value displays have been standardized so that a long dash (--) appears when there is no data, and a zero appears with there is data present but the value is `0`. 

- When you want to select multiple users in the [Member Performance dashboard](dashboard_annotator), there is a new **All Members** option in members drop-down.

    - If you are filtering the member list, **All Members** will select all users matching your search criteria (up to 50 users).
    - If you are not filtering the member list, **All Members** will select the first 50 users.

- When viewing the Member Performance dashboard, Managers will now only be able to see users who are members of projects or workspaces in which the Manager is also a member.

    Previously, Managers could see the full organization user list, but could only see user metrics for projects in which the Manager was also a member.


#### Added support for latest Anthropic models

Added support for the following models:

`claude-sonnet-4-5`

`claude-haiku-4-5`

`claude-opus-4-5`

#### Deprecated GPT models

The following models have been deprecated:

`gpt-4.5-preview`

`gpt-4.1`

`gpt-4.1-mini`

`gpt-4.1-nano`

`gpt-4`

`gpt-4-turbo`

`gpt-4o`

`gpt-4o-mini`

`o3-mini`

`o1`

#### Additional feature updates and UI improvements

**Data Manager and labeling**

* Use Shift to select multiple Data Manager rows.

    You can now select a Data Manager row, and then while holding shift, select another Data Manager row to select all rows between your selections.

* It is now clearer how to access the task summary view. The icon has been replaced with a **Compare All** button.

    For additional clarity, the **Compare** tab has now been renamed **Side-by-Side**.

    ![Screenshot](/images/releases/2-33-compare.avif)

* When you hover over an annotation tab in Quick View, you will now see metadata for the annotation. 

    <img src="/images/releases/2-33-tooltip.png" style="max-width: 500px" alt="Screenshot"> 
* Updated appearance and guidance text for the text area component. 




**Project settings**

* You can now set [annotation overlap](https://docs.humansignal.com/guide/project_settings_lse#overlap) up to 500 annotations. Previously this was restricted to 20 when setting it through the UI.

* The [annotator evaluation](https://docs.humansignal.com/guide/project_settings_lse#annotator-eval) settings are now only available when the project is using automatic annotator assignment rather than manual assignment. 

**Other updates**

- How time is displayed across the app has been standardized to use the following format:

    `[n]h [n]m [n]s`

    For example: **10h 5m 22s**

- The **Recent Projects** list on the Home page will now include the most recently visited projects at the top of the list instead of pinned projects.

- The **Early Adopter** toggle has been removed from **Organization > Usage & License**. For on-prem deployments, you can selectively enable feature flags instead. 

- Added clarity to the messages that annotators see when they are paused. 

- If you have a published project that is in a shared workspace and you move it to your Personal Sandbox workspace, the project will automatically revert to an unpublished state.

    Note that published projects in Personal Sandboxes were never visible to other users. This change is simply to support upcoming enhancements to project work states.



### Security

- Increased the log level for SSO/SAML authentication events. Previously, certain events would only appear if the log level was set to DEBUG. 

- Fixed an XSS issue with custom hotkeys. 

#### Example Score Calculations

Example using the same simple label config as above: 

```xml
<View>
  <Image name="image_object" value="$image_url"/>
  <Choices name="image_classes" toName="image_object">
    <Choice value="Cat"/>
    <Choice value="Dog"/>
  </Choices>
</View>
```

Lets say for one task we have the following:
1. Annotation 1 from annotator 1 - `Cat` (marked as ground truth)
2. Annotation 2 from annotator 2 - `Dog`
3. Prediction 1 from model version 1 - `Dog` 
4. Prediction 2 from model version 2 - `Cat` 

Here is how the score would be calculated for various selections in the dropdown

#### `Agreement Pairs` with `All Annotators` selected
This will match the behavior of the **Agreement** column - all annotation pair's scores will be averaged:

1. Annotation 1 <> Annotation 2: Agreement score is `0`

Score displayed in column for this task: `0%`

#### `Agreement Pairs` with `All Annotators` and `All Model Versions` selected
This will average all annotation pair's scores, as well as all annotation <> model version pair's scores
1. Annotation 1 <> Annotation 2 - agreement score is `0`
4. Annotation 1 <> Prediction 1 - agreement score is `0`
5. Annotation 1 <> Prediction 2 - agreement score is `1`
6. Annotation 2 <> Prediction 1 - agreement score is `1`
7. Annotation 2 <> Prediction 2 - agreement score is `0`

Score displayed in column for this task: `40%` 

#### `Ground Truth Match` with `model version 2` selected
This will compare all ground truth annotations with all predictions from `model version 2`.

In this example, Annotation 1 is marked as ground truth and Prediction 2 is from `model version 2`:

1. Annotation 1 <> Prediction 2 - agreement score is `1`

Score displayed in column for this task: `100%` 



The practical takeaway: 

If your project uses only categorical tags, switching between pairwise average and consensus is straightforward. 

But if your project includes non-categorical tags like bounding boxes or text spans, switching to consensus means you need to think carefully about what threshold makes sense for your use case -- too strict and most annotations won't "match"; too lenient and meaningful disagreements get masked.


### 🚨🚨🚨👉👉👉😱 BREAKING CHANGES 😱👈👈👈🚨🚨🚨

LISTEN UP, PEOPLE! We got some breaking changes for you!