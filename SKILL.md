---
name: product-design-deconstruction
description: "Turn product photos, screenshots, or product links into industrial-design deconstruction: identify the main object, classify its product category and attributes, separate visible facts from inferred mechanisms, apply category-specific design principles, and produce design-analysis notes, exploded-view concepts, three-view sketch prompts, CMF notes, Chinese handwritten-style annotation overlays, and responsible AI image-generation prompts. Use when the user asks to analyze a product such as a shaver, tea canister, lamp, cup, appliance, stationery item, package, tool, or consumer object and convert it into design sketches, structure diagrams, exploded diagrams, or product-design learning material."
---

# Product Design Deconstruction

## Core Rule

Treat the output as design analysis and concept reconstruction, not verified teardown evidence. Always separate:

- Visible facts: what can be seen directly in the photo.
- Category-based inference: likely structures or mechanisms based on common products in the same category.
- Creative reconstruction: optional design improvements or stylized sketch directions.

Do not claim hidden internal structure is real unless the user provides teardown photos, CAD, drawings, manuals, patents, or measurements.

## Workflow

1. Identify the main object in the image or link. Distinguish the product from props, hands, background, packaging, and scene decoration.
2. Classify the object by product attributes, not just name. Use multiple labels when helpful, such as `handheld electronic product`, `ceramic container`, `food-storage packaging`, `skin-contact appliance`, `desktop lighting`, `children's product`, or `gift object`.
3. Extract visible design facts: silhouette, proportions, parting lines, seams, buttons, openings, surface texture, materials, colors, finish, logo/branding, user-contact areas, safety clues, and manufacturing hints.
4. Match the category to design principles. Read `references/category-principles.md` when a concrete product category is involved or when making mechanism/structure inferences.
5. Infer likely structure conservatively. Use wording such as "likely", "possibly", "common in this category", and "conceptual assumption".
6. Classify each feature as either a separable part, an integral molded/thrown/formed feature, surface decoration, or optional accessory. Read `references/structure-consistency-cases.md` before generating exploded views, section views, three-view boards, or any image that implies product construction. Do not explode integral features as independent parts.
7. Run a structure-consistency check before finalizing: the exploded view, section view, three-view drawings, labels, and written explanation must describe the same construction logic.
8. Produce the requested deliverable: design observation, structure hypothesis, exploded diagram description, sketch-generation prompt, three-view prompt, CMF board, Chinese annotation overlay, improvement proposal, or Xiaohongshu-safe post.
9. For images intended for publication, add an AI/assumption disclaimer and avoid brand infringement. Recommend removing or masking visible trademarks if the product is branded and the output is commercial or public.

## Output Menu

Choose only the sections that fit the user's request. For a full analysis, use this order:

1. Subject and category
2. Visible facts
3. Product attributes and design principles
4. Inferred structure
5. Part/integral-feature classification
6. Exploded-view layer plan
7. Structure-consistency check
8. Sketch prompt
9. CMF notes
10. Design improvement directions
11. Disclaimer and publishing safety notes

## Sketch Prompt Requirements

When generating prompts for image tools, include:

- Canvas policy: use a 9:16 vertical composition by default, preferably `1080x1920` for saved outputs. Override only when the user explicitly asks for another ratio or when the target format requires it.
- Product category and viewpoint.
- Drawing type: industrial design sketch, exploded view, three-view sheet, function zoning diagram, CMF study, detail callout, or concept redesign.
- Evidence discipline: visible exterior preserved, inferred interior shown as conceptual, hidden parts labeled as assumptions.
- Structural discipline: only separate actual or likely separable parts. Do not visually explode one-piece ceramic/plastic/metal features such as molded feet, thrown foot rings, ribs, lips, or shoulders unless the category normally uses an added insert or the photo shows a seam.
- Materials and finish.
- Line quality and composition.
- Text policy: generate a no-readable-text base image by default. Do not allow English labels in the base image either. For Chinese annotations, add a local overlay after image generation rather than asking the image model to write Chinese.

For actual image generation, use the `imagegen` skill or available image-generation tool after this analytical step.

## Default Image Set

When the user provides a product photo and asks for generated images without specifying a layout, create one 9:16 vertical design board rather than mixed-size images. Use this hierarchy:

1. Top area: intact product sketch or hero perspective.
2. Middle area: main conceptual exploded view or structure diagram.
3. Lower area: three-view thumbnails, section detail, or CMF swatches.
4. Side margins and intentional white space: Chinese handwritten labels. Do not place text on top of the product, structure parts, thumbnails, CMF swatches, or existing diagram details.

Keep all final saved images in the same dimensions within one task. Use semantic version filenames, such as `商品名_设计拆解图组_v1.0.png`, `商品名_无文字底图_v1.0.png`, and `商品名_中文标注版_v1.0.png`.

If a tool returns a different aspect ratio, crop or pad non-destructively to 9:16 before final delivery. Prefer padding with a clean white or paper-like background over cropping product details.

## Structure-Consistency Check

Before generating or delivering an image, write a compact construction model:

- Separable parts: pieces a user/manufacturer could plausibly remove or assemble separately.
- Integral features: shapes formed as part of the same material/body.
- Surface layers: paint, decal, glaze, label, coating, texture, printing.
- Optional assumptions: only shown when useful, visually marked as conceptual, and kept consistent across all views.

Then verify:

1. Exploded view separates only separable parts and optional conceptual inserts.
2. Section view shows the same construction model as the exploded view.
3. Three-view drawings do not imply seams or extra parts that the structure model rejects.
4. Labels name integral features as features, not standalone components. Use `底足/圈足` for ceramic foot rings, not `独立底座`, unless an added base is visible.
5. If an AI-generated image creates a contradiction, either regenerate or explicitly reject that part of the image as inaccurate.

## Chinese Handwritten Annotation Workflow

Use this workflow whenever the user wants Chinese handwritten-style labels, publishable diagrams, or Xiaohongshu-ready images:

1. Generate the base diagram with no readable text in any language, no fake labels, and enough blank side/bottom space for annotations. Explicitly ask for no English words such as "front", "side", "cap", "notes", or material labels.
2. Write a short Chinese label list. Keep each label under 8 Chinese characters when possible, such as `外盖`, `密封圈`, `内胆`, `主板`, `电池`, `口沿`, `罐身`, `底足`, `材质`, `开合区`.
3. Add the labels locally with `scripts/add_handwritten_labels.py` instead of relying on AI-generated Chinese text.
4. Use a real local Chinese handwritten or handwritten-adjacent font when available. Prefer `Alimama DongFangDaKai` or a Chinese kaiti/handwriting font. If unavailable, fall back to an installed Chinese font such as `Hiragino Sans GB`, `STHeiti`, or `Arial Unicode`, and report that it is a font fallback.
5. Use all-Chinese labels by default. English is allowed only for real industry abbreviations or material codes, such as `PCB`, `CMF`, `LED`, `USB-C`, `PP`, `ABS`, `PET`, or `IPX7`.
6. Place labels outside the drawing content, preferably in left/right side columns or bottom white space. Use thin leader lines to point at the relevant part. Do not let label boxes cover product silhouettes, exploded parts, section views, three-view drawings, material swatches, or important linework.
7. Visually inspect the final image for wrong characters, English leakage, overlapping labels, broken leader lines, and labels covering the main product.

Label JSON format for the script:

```json
[
  {"text": "外盖", "xy": [120, 180], "anchor": [300, 220]},
  {"text": "罐身", "xy": [760, 520], "anchor": [650, 610]}
]
```

Run:

```bash
python /Users/admin/.codex/skills/product-design-deconstruction/scripts/add_handwritten_labels.py \
  --input no-text-base.png \
  --labels labels.json \
  --output labeled.png \
  --canvas 1080x1920 \
  --font-size 34
```

The script enforces Chinese labels by default. Use `--allow-english "USB-C,IPX7"` only when a real industry term is needed.

For fast internal drafts only, it is acceptable to ask image generation for loose handwritten-looking annotation strokes, but do not use AI-generated Chinese characters as final publishable text.

## Xiaohongshu Publishing Safety

When the user wants to publish this skill/process on Xiaohongshu, frame it as design-learning or design-observation content, not as an AI tool advertisement. Avoid external links, QR codes, contact details, "private message to get", absolute claims, and "one-click/seconds/professional replacement" wording. Use no more than 10 hashtags by default.

Suggested disclaimer:

`图中结构为基于照片和同类产品原理的概念推测，不代表真实拆机结构；如使用 AI 生成图，请按平台要求标识 AI 辅助创作。`

## References

- Read `references/category-principles.md` when analyzing a specific product category, inferring mechanisms, writing prompts for exploded views, or preparing a publishable case study.
- Read `references/structure-consistency-cases.md` when deciding whether a feature is a separable part or an integral/surface feature, and before generating or approving exploded-view, section-view, or three-view images.
