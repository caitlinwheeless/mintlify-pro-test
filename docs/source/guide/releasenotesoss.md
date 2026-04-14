---
title: release notes 2
short: release notes 2
type: guide
tier: enterprise
order: 2
order_enterprise: 2
section: "Integrate & Extend"
---

# 🌟 What's new

## 🎉 New features

### 🎨 Annotate images with vector lines

There are two new tags for image annotation: [**Vector**](https://labelstud.io/tags/vector) and [**VectorLabels**](https://labelstud.io/tags/vectorlabels).

You can use these tags for point-based vector annotation (polylines, polygons, skeletons).

<img width="898" height="564" alt="image" src="https://github.com/user-attachments/assets/7fe9cc47-7949-4215-b67c-3cd4e2aa8543" />


## ✅ Feature updates 

### 🪄 Interactive view for task source

When clicking **Show task source <>** from the Data Manager, you will see a new **Interactive** view. (#9245, #9318)

From here you can filter, search, and expand/collapse sections in the task source. You can also selectively copy sections of the JSON.

You can also now toggle whether to show the resolved URIs. 

<img width="1397" height="615" alt="image" src="https://github.com/user-attachments/assets/5cdbed4e-a196-4f62-a626-df096ea0413f" />


### 📌 Data Manager filter enhancements

Data Manager filters have the following enhancements (#9488):

- New copy and paste actions that you can use to copy filters between tabs within the same project or to tabs within other projects (any inapplicable fields will be automatically removed when pasting between projects).
- The ability to copy filters as JSON so that you can edit them elsewhere.
- The three most recent filter selections will appear at the top of the drop-down menu.
- When adding new filters, it will pre-populate with your most recent selections.

<img width="1011" height="328" alt="image" src="https://github.com/user-attachments/assets/9746c941-d506-4dcc-9340-e775531eae9d" />

<img width="2876" height="1334" alt="image" src="https://github.com/user-attachments/assets/edde49dd-3007-4064-8374-efb0416f0dd3" />

### 🎯 Context menu for Data Manager rows

When you right-click a Data Manager row, you will now see a context menu (#9386):

<img width="1046" height="474" alt="image" src="https://github.com/user-attachments/assets/678f6687-a46f-458a-9c87-f3a47cd8346c" />

### 🔎 Press Ctrl + F to search the Code tab

When working in the template builder, you can now use Ctrl + F to search the your labeling configuration XML (#9346, #9424).

<img width="726" height="527" alt="image" src="https://github.com/user-attachments/assets/cf49ad74-672a-4445-9298-79e036499a80" />

### ↔️ Resize panel widths in the template builder

You can now click and drag to adjust panel widths when configuring your labeling interface (#9171).

https://github.com/user-attachments/assets/3ef83d2f-819b-4402-9522-7bcf2cc31d61

### ⬆️ Use Shift to select multiple Data Manager rows

You can now select a Data Manager row, and then while holding shift, select another Data Manager row to select all rows between your selections (#9067).

### 🧩 Task navigation and ID moved to the bottom of the labeling interface

To better utilize space, the annotation ID and the navigation controls for the labeling stream have been moved to below the labeling interface (#8822).

<img width="1011" height="579" alt="image" src="https://github.com/user-attachments/assets/97e2c850-1960-4712-912b-4fc5ab98c1f0" />


### ✨ Miscellaneous UX/UI improvements

- The **Recent Projects** list on the Home page will now include the most recently visited projects at the top of the list instead of pinned projects (#8993).
- How time is displayed across the app has been standardized to use the following format (#9134):

    `[n]h [n]m [n]s`

    For example: **10h 5m 22s**
- When you hover over an annotation tab in Quick View, you will now see metadata for the annotation (#9140).

    <img width="721" height="498" alt="image" src="https://github.com/user-attachments/assets/583c72e4-847a-46ad-af49-00ae2013f816" />


- For YOLO, COCO, and VOC conversion warnings, the task_id is now used instead of the sequence number to improve clarity (#9248, #9269).
- It is now clearer how to access the task summary view. The icon has been replaced with a **Compare All** button (#9271).
- Text area components have an updated appearance and guidance text (#9319).
- Improved how timeouts for exports are handled and communicated in the UI (#9063). 
- Improved visual contrast to between active and inactive tabs on the Data Manager (#9423).

### 📦 SDK improvements

- The Membership detail endpoint now includes `created_projects` and `contributed_to_projects` fields.  
- In the Membership list endpoint, fields nested under `user` have been deprecated and promoted to the root of the response.
- Optimizations have been made to both endpoints (#9066).

### 🚀 Performance improvements and optimizations

- Improved performance when clicking between different tasks in the Data Manager to open the Quick View interface (#9495, #9498).


# 🔒 Security

- Fixed an XSS issue with custom hotkeys (#9084).

# 🚨 Breaking changes

Starting with this release, we will be using an [Alpine Docker image](https://hub.docker.com/_/alpine). Previously we used Debian Trixie. (#9108)

If you build on top of our image, update your **`FROM`** line and replace **`apt-get`** with **`apk`**.


# 🐞 Bug fixes

- Fixed an issue affecting how filter values appeared (#8995).

- Fixed an issue where embedded YouTube videos were not working in `<HyperText>` tags (#9003).

- Fixed an issue where import jobs through the API could fail silently (#9010, #9043).

- Fixed an issue where the **Copy region link** action from the overflow menu for a region disappeared on hover (#9016).

- Fixed an issue with prediction validation for the Ranker tag (#9012, #9044).

- Fixed several out-of-memory issues (#9045, #9223).

- Fixed an issue with missing images when exporting YOLO/COCO formats when images were uploaded through the UI (#9058).

- Fixed an issue where SDK calls using PATs could not handle trailing slashes in the base URL (#9099).

- Fixed an issue with how the Enterprise tag appeared on templates when creating a project (#9120).

- Fixed an issue that prevents loading Label Studio in an airgapped environment (#9136).

- Fixed a small UI issue in Firefox related to horizontal scrolling (#9131).

- Fixed an issue with row margins in the Data Manager (#9162).

- Fixed an issue where extra space appeared at the end of Data Manager table rows (#9210).

- Fixed an issue with default permissions with using Docker (#9243).

- Fixed an issue with the  `ls.ml.list` SDK endpoint (#9249).

- Fixed an issue with a validation error when importing HypertextLabels predictions (#9282).

- Fixed an issue where multi-channel time series plots introduced left-margin offset causing x‑axis misalignment with standard channel rows (#9296).

- Fixed an issue with the autocomplete pop-up width when editing code under the **Code** tab of the labeling configuration (#9317).

- Fixed an issue where Ranker tag styling was broken (#9330).

- Fixed an issue where, when importing predictions with `PolygonLabels`/`RectangleLabels`, users would see an error if their labeling config used `Polygon`/`Rectangle` + `Labels` tags instead (#9364).

- Fixes spacing of items on data manager/project dropdowns and spacing of tabs (#9422).

- Fixed an issue where the `minPlaybackSpeed` parameter could be configured with a value greater than the `defaultPlaybackSpeed` parameter on the Video tag (#9387).

- Fixed an issue with importing predictions for BrushLabels (#9453).

# 🤩 Contributors

## ❤️ HumanSignal team

- @ricardoantoniocm 
- @makseq 
- @mcanu 
- @yyassi-heartex 
- @matt-bernstein 
- @nikitabelonogov 
- @nick-skriabin 
- @hakan458 
- @bmartel 
- @nass600 
- @hlomzik 
- @farioas  


## Deep Dive: How OVERLAP Works for Text Spans

When two annotators highlight spans of text (such as named entities in NER), OVERLAP measures how much their highlighted regions coincide. It is the default metric for `Labels`, `ParagraphLabels`, `TimeSeriesLabels`, and `TimelineLabels`.

### The core formula: Intersection over Union (IoU)

Each span has a `start` position and an `end` position (character offsets in the text). For two spans, the system computes:

```
overlap_score = intersection / union
```

- **Intersection** = the length of the region where both spans overlap
- **Union** = the total length covered by both spans combined

More precisely:

```
intersection = min(end_1, end_2) - max(start_1, start_2)
union        = max(end_1, end_2) - min(start_1, start_2)
overlap      = intersection / union
```

If the spans don't overlap at all, the score is `0.0`. If they are identical, the score is `1.0`.

### Concrete example

Imagine a sentence: `"Barack Obama visited Paris"`

- **Annotator A** highlights characters 0–12 as "Person" (covering "Barack Obama")
- **Annotator B** highlights characters 0–10 as "Person" (covering "Barack Oba")

The math:

- **Intersection**: the overlap region is characters 0–10, length = **10**
- **Union**: the total covered region is characters 0–12, length = **12**
- **Score**: 10 / 12 = **0.83** (83% agreement)

A few more intuitive cases:

| Scenario | Score |
|---|---|
| Both annotators highlight the exact same span | **1.0** (perfect) |
| Spans partially overlap | **Between 0 and 1** (partial credit) |
| Spans don't overlap at all | **0.0** |
| One span fully contains the other (e.g., 0–20 vs 5–15) | **0.5** (10/20) |

### Labels must match too

The overlap score only counts if both annotators assigned the **same label**. If Annotator A labels a span as "Person" and Annotator B labels the exact same span as "Organization", the score is **0.0** regardless of positional overlap.

### Multiple spans: greedy matching

When annotators create multiple spans on the same text, the system uses a **greedy matching algorithm**:

1. It builds a matrix of every possible pair between Annotator A's spans and Annotator B's spans.
2. For each span, it finds the **best-matching** span from the other annotator.
3. It averages all those best-match scores together.

So if Annotator A drew 2 spans and Annotator B drew 2 spans, each span gets paired with its best counterpart, and the final score is the average.

### Variants built on OVERLAP

| Variant | What it does |
|---|---|
| `OVERLAP` | Returns the raw IoU score (e.g., 0.83). Pairwise only. |
| `OVERLAP_T` (Threshold) | Converts to binary: is the IoU above your threshold? Yes → 1, No → 0. Required for consensus methodology. |
| `OVERLAP_JACCARD` | First checks spatial overlap, then compares the *label sets* using Jaccard similarity. Useful when spans can have multiple labels. |
| `OVERLAP_TEXTSIM` | First checks spatial overlap, then compares *transcribed text* using edit distance (Levenshtein by default). |

Each of these also has a `_T` (threshold) variant for use with consensus methodology.

---

## Deep Dive: How IOU Works for Bounding Boxes (RectangleLabels / Rectangle)

When two annotators draw bounding boxes around objects in an image (e.g., object detection tasks), IOU (Intersection over Union) measures how much their boxes overlap. It is the default metric for `RectangleLabels` and `Rectangle`.

### The core formula: Area-based Intersection over Union

Each bounding box is defined by four values: `x` and `y` (the top-left corner), plus `width` and `height`. The system computes:

```
IoU = Area(Intersection) / Area(Union)
```

- **Intersection** = the area of the rectangular region where both boxes overlap
- **Union** = the total area covered by both boxes combined (Area A + Area B − Intersection)

More precisely:

```
intersection = (overlap_width) × (overlap_height)
union        = (width_A × height_A) + (width_B × height_B) − intersection
IoU          = intersection / union
```

If the boxes don't overlap at all, the score is `0.0`. If they are identical, the score is `1.0`.

### How it differs from span OVERLAP

Span OVERLAP is one-dimensional — it only considers start and end positions along a line of text. Bounding box IOU is **two-dimensional** — it considers overlap across both the x-axis and y-axis, computing overlap by **area** rather than by length.

| | Span OVERLAP | Bounding Box IOU |
|---|---|---|
| **Dimensions** | 1D (start/end positions) | 2D (x, y, width, height) |
| **What's compared** | Length of overlapping region | Area of overlapping region |
| **Typical use case** | NER / text highlighting | Object detection in images |

### Concrete example

Imagine an image where two annotators draw boxes around a cat:

- **Annotator A** draws a box at position (10, 10) with width 20 and height 20 → area = **400**
- **Annotator B** draws a box at position (15, 15) with width 20 and height 20 → area = **400**

The overlapping rectangle runs from (15, 15) to (30, 30):
- **Intersection area**: 15 × 15 = **225**
- **Union area**: 400 + 400 − 225 = **575**
- **IoU**: 225 / 575 = **0.39** (39% agreement)

A few more intuitive cases:

| Scenario | Score |
|---|---|
| Both annotators draw the exact same box | **1.0** (perfect) |
| Boxes partially overlap | **Between 0 and 1** (partial credit) |
| Boxes don't overlap at all | **0.0** |
| One box fully contains the other (e.g., a 10×10 box inside a 20×20 box) | **0.25** (100/400) |
| Two boxes of the same size, slightly offset by 2px on each axis | **~0.47** |

### Labels must match too

Just like span OVERLAP, the IoU score only counts if both annotators assigned the **same label**. If Annotator A labels a box as "Cat" and Annotator B labels the identical box as "Dog", the score is **0.0** regardless of positional overlap.

Label comparison is order-independent: `['cat', 'dog']` is treated the same as `['dog', 'cat']`.

### Multiple boxes: greedy matching

When annotators draw multiple boxes on the same image, the system uses the same **greedy matching algorithm** as span OVERLAP:

1. It builds a matrix of every possible pair between Annotator A's boxes and Annotator B's boxes.
2. For each box, it finds the **best-matching** box from the other annotator.
3. It averages all those best-match scores together.

For example, if Annotator A draws 1 box (Cat) and Annotator B draws 2 boxes (Cat + Dog):
- A's Cat box matches B's Cat box → IoU = 1.0
- B's Cat box matches A's Cat box → IoU = 1.0
- B's Dog box has no match in A → score = 0.0
- **Final score**: (1.0 + 1.0 + 0.0) / 3 = **0.67**

This penalizes missing or extra annotations proportionally.

### Label weights: disabling labels

You can assign **weights** to labels. Labels with a weight of 0 are effectively invisible to the metric:

- If both annotators only drew boxes with disabled labels, the result is **1.0** (vacuous agreement — both said "nothing enabled here").
- If one annotator drew a disabled-label box and the other drew an enabled-label box, the result is **0.0** (they disagree on whether anything was present).
- A box with mixed labels like `['dog', 'cat']` where `dog` has weight 0 is still kept in the comparison because `cat` is still enabled. After filtering, both sides are compared on `{'cat'}` only.

### Variants built on IOU

| Variant | What it does |
|---|---|
| `IOU` | Returns the raw IoU score (e.g., 0.39). Pairwise only. |
| `IOU_T` (Threshold) | Converts to binary: is the IoU above your threshold? Yes → 1, No → 0. Required for consensus methodology. |
| `IOU_JACCARD` | First checks bounding box overlap (IoU gate), then compares the *label sets* using Jaccard similarity. Default for `Choices (per RectangleLabels)`. |
| `IOU_TEXTSIM` | First checks bounding box overlap (IoU gate), then compares *transcribed text* using edit distance. Default for `TextArea (per RectangleLabels)`. |

Each of these also has a `_T` (threshold) variant for use with consensus methodology.
