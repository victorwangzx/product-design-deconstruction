---
name: product-design-deconstruction
description: "Turn product photos, screenshots, or product links into industrial-design deconstruction: identify the main object, classify its product category and attributes, research the product's working principle, separate visible facts from inferred mechanisms, apply category-specific design principles, and produce design-analysis notes, exploded-view concepts, three-view sketch prompts, CMF notes, Chinese handwritten-style annotation overlays, and responsible AI image-generation prompts. Use when the user asks to analyze a product such as a shaver, tea canister, hot pot, lamp, cup, appliance, stationery item, package, tool, or consumer object and convert it into design sketches, structure diagrams, exploded diagrams, or product-design learning material."
---

# Product Design Deconstruction

## Core Rule

Treat the output as design analysis and concept reconstruction, not verified teardown evidence. Always separate:

- Visible facts: what can be seen directly in the photo.
- Visual identity layer: the product's distinctive exterior character, proportions, surface traces, color, finish, pattern, wear, context cues, and recognizable styling.
- Category-based inference: likely structures or mechanisms based on common products in the same category.
- Creative reconstruction: optional design improvements or stylized sketch directions.

Do not claim hidden internal structure is real unless the user provides teardown photos, CAD, drawings, manuals, patents, or measurements.

## Workflow

1. Identify the main object in the image or link. Distinguish the product from props, hands, background, packaging, and scene decoration.
2. Classify the object by product attributes, not just name. Use multiple labels when helpful, such as `handheld electronic product`, `ceramic container`, `food-storage packaging`, `skin-contact appliance`, `desktop lighting`, `children's product`, or `gift object`.
3. Extract visible design facts: silhouette, proportions, parting lines, seams, buttons, openings, surface texture, materials, colors, finish, logo/branding, user-contact areas, safety clues, and manufacturing hints.
4. Preserve the visual identity layer from the user's photo. Capture proportions, silhouette quirks, surface finish, patina, wear marks, decorative pattern, hardware style, color temperature, and context-specific character before any generic reconstruction. Treat this as a required layer in the final board unless the user asks for a neutral technical drawing.
5. Research the product's working principle before inferring structure. Determine the energy source, operating cycle, material/fluid/air/heat path, user actions, safety boundaries, maintenance points, and likely serviceable parts. When the mechanism is specific, unfamiliar, safety-related, modern, regulated, or ambiguous, look up credible sources such as manuals, museum/encyclopedic references, technical articles, repair guides, patents, or official product pages before drawing.
6. Match the category to design principles. Read `references/category-principles.md` when a concrete product category is involved or when making mechanism/structure inferences.
7. Infer likely structure conservatively from visible facts plus the researched working principle. Use wording such as "likely", "possibly", "common in this category", and "conceptual assumption".
8. Classify each feature as either a separable part, an integral molded/thrown/formed feature, surface decoration, or optional accessory. Read `references/structure-consistency-cases.md` before generating exploded views, section views, three-view boards, or any image that implies product construction. Do not explode integral features as independent parts.
9. Use the section/construction model as the source of truth for exploded views. If the section shows a continuous formed or permanently joined body, the exploded view must keep that body together and separate only serviceable inserts, accessories, trays, fasteners, or modules.
10. Run a structure-consistency check before finalizing: the exploded view, section view, three-view drawings, labels, and written explanation must describe the same construction logic.
11. Create a Chinese part-name list before generating the final annotated diagram. For any requested deconstruction, exploded-view, section-view, or structure board, the final deliverable must include component names unless the user explicitly asks for a no-label base image.
12. Produce the requested deliverable: design observation, visual-identity preservation notes, working-principle summary, structure hypothesis, exploded diagram description, sketch-generation prompt, three-view prompt, CMF board, Chinese annotation overlay, improvement proposal, or Xiaohongshu-safe post.
13. For images intended for publication, add an AI/assumption disclaimer and avoid brand infringement. Recommend removing or masking visible trademarks if the product is branded and the output is commercial or public.

## Output Menu

Choose only the sections that fit the user's request. For a full analysis, use this order:

1. Subject and category
2. Visible facts
3. Visual identity layer
4. Working-principle research
5. Product attributes and design principles
6. Inferred structure
7. Part/integral-feature classification
8. Exploded-view layer plan
9. Structure-consistency check
10. Sketch prompt
11. CMF notes
12. Design improvement directions
13. Disclaimer and publishing safety notes

## Visual Identity Preservation

Before generating diagrams, write a short preservation brief from the user's image:

- Overall silhouette and proportion: height/width, shoulder, rim, base, handle placement, distinctive asymmetry.
- Surface identity: patina, scratches, stains, glazing, hammer marks, printed patterns, color variation, material warmth, age, handmade or restaurant-use traces.
- Hardware identity: handle shape, rivets, hinge style, buttons, vents, feet, caps, knobs, seams.
- Context cues: restaurant object, home appliance, school object, gift packaging, child's toy, repair-worn item, premium display item.
- What must survive in every view: the 3-5 visual features that make this specific object recognizable.

Use the preservation brief in prompts. The generated product should look like a deconstructed version of the user's photographed object, not a generic category sample. For public diagrams, remove or soften brand marks if needed, but preserve non-branded visual character.

## Working-Principle Research

Before writing prompts or generating images, build a compact mechanism model:

- Energy/source: battery, mains electricity, charcoal fire, alcohol lamp, gas, manual force, gravity, pressure, magnetism, or passive storage.
- Core action: cutting, heating, sealing, filtering, lighting, cooling, locking, pouring, cushioning, transmitting motion, or containing.
- Path: air, smoke, heat, water, steam, liquid, powder, light, sound, vibration, force, or data path.
- User actions: open, fill, light, press, grip, pour, charge, clean, replace, adjust, carry, or store.
- Key structures: the parts required for the working principle to function.
- Safety and maintenance: heat isolation, ventilation, drainage, sealing, insulation, cleaning, replacement, child safety, food contact, or electrical protection.
- Uncertainty: alternative mechanisms that would change the structure.

If multiple working principles are plausible, branch the structure model instead of forcing one answer. For example, a hot pot heated by charcoal requires a combustion chamber, air inlets, grate, ash path, chimney/draft path, and heat-transfer contact to the annular soup basin. A small alcohol-lamp hot pot instead requires a lamp cup/burner, wick or fuel reservoir, flame clearance, wind shield, pot support, and often a water-filled or air-gap insulation tray. These two systems should not share the same exploded structure.

When research is used, cite the source names or URLs in the written analysis. When no external research is needed, say the working principle is based on visible facts and common category principles.

## Sketch Prompt Requirements

When generating prompts for image tools, include:

- Canvas policy: use a 9:16 vertical composition by default, preferably `1080x1920` for saved outputs. Override only when the user explicitly asks for another ratio or when the target format requires it.
- Product category and viewpoint.
- Drawing type: industrial design sketch, exploded view, three-view sheet, function zoning diagram, CMF study, detail callout, or concept redesign.
- Evidence discipline: visible exterior preserved, inferred interior shown as conceptual, hidden parts labeled as assumptions.
- Visual identity discipline: preserve the photographed object's silhouette, proportions, surface finish, patina/wear, color, hardware style, and distinctive non-branded visual cues across the intact view, exploded view, section view, and three-view thumbnails.
- Working-principle discipline: show only structures that fit the selected mechanism. Do not mix charcoal, alcohol-lamp, gas, and electric heating structures unless presenting alternative concepts.
- Structural discipline: only separate actual or likely separable parts. Do not visually explode one-piece ceramic/plastic/metal features such as molded feet, thrown foot rings, ribs, lips, or shoulders unless the category normally uses an added insert or the photo shows a seam.
- View-consistency discipline: make the exploded view obey the section view. If the section shows the pot body, chimney, base wall, or shell as one continuous or permanently joined assembly, do not split those forms into floating trays or duplicate bodies in the exploded view.
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

The intact top view must preserve the user's photographed exterior most strongly. The exploded and section views may simplify hidden internals, but they should carry the same exterior silhouette, material finish, hardware style, and visible wear/pattern cues.

Keep all final saved images in the same dimensions within one task. Use semantic version filenames, such as `商品名_设计拆解图组_v1.0.png`, `商品名_无文字底图_v1.0.png`, and `商品名_中文标注版_v1.0.png`.

If a tool returns a different aspect ratio, crop or pad non-destructively to 9:16 before final delivery. Prefer padding with a clean white or paper-like background over cropping product details.

## Structure-Consistency Check

Before generating or delivering an image, write a compact construction model:

- Separable parts: pieces a user/manufacturer could plausibly remove or assemble separately.
- Integral features: shapes formed as part of the same material/body.
- Surface layers: paint, decal, glaze, label, coating, texture, printing.
- Optional assumptions: only shown when useful, visually marked as conceptual, and kept consistent across all views.
- Working-principle model: energy/source, path, heat/fluid/air/motion route, and user-serviceable parts.
- Visual identity model: distinctive exterior cues from the source photo that must remain visible after deconstruction.

Then verify:

1. Exploded view separates only separable parts and optional conceptual inserts.
2. Section view shows the same construction model as the exploded view.
3. Three-view drawings do not imply seams or extra parts that the structure model rejects.
4. Labels name integral features as features, not standalone components. Use `底足/圈足` for ceramic foot rings, not `独立底座`, unless an added base is visible.
5. The exploded view does not duplicate a shell/body that already exists in the intact view unless the product truly has nested removable shells.
6. The final image still resembles the user's photographed object in silhouette, material character, and distinctive visual cues.
7. If an AI-generated image creates a contradiction or becomes a generic category object, either regenerate or explicitly reject that part of the image as inaccurate.

## Chinese Handwritten Annotation Workflow

Use this workflow whenever the user wants Chinese handwritten-style labels, publishable diagrams, or Xiaohongshu-ready images:

1. Generate the base diagram with no readable text in any language, no fake labels, and enough blank side/bottom space for annotations. Explicitly ask for no English words such as "front", "side", "cap", "notes", or material labels.
2. Write a short Chinese part-name list before rendering labels. This is mandatory for final deconstruction images, not optional. Include the visible exterior parts, likely serviceable internal parts, key integral features, and any uncertainty labels such as `结构待校`, `概念推测`, or `待验证`.
3. Keep each label under 8 Chinese characters when possible, such as `外盖`, `密封圈`, `内胆`, `主板`, `电池`, `口沿`, `罐身`, `底足`, `材质`, `开合区`.
4. Add the labels locally with `scripts/add_handwritten_labels.py` instead of relying on AI-generated Chinese text.
5. Use a real local Chinese handwritten or handwritten-adjacent font when available. Prefer `Alimama DongFangDaKai` or a Chinese kaiti/handwriting font. If unavailable, fall back to an installed Chinese font such as `Hiragino Sans GB`, `STHeiti`, or `Arial Unicode`, and report that it is a font fallback.
6. Use all-Chinese labels by default. English is allowed only for real industry abbreviations or material codes, such as `PCB`, `CMF`, `LED`, `USB-C`, `PP`, `ABS`, `PET`, or `IPX7`.
7. Place labels outside the drawing content, preferably in left/right side columns or bottom white space. Use thin leader lines to point at the relevant part. Do not let label boxes cover product silhouettes, exploded parts, section views, three-view drawings, material swatches, or important linework.
8. Visually inspect the final image for wrong characters, English leakage, overlapping labels, broken leader lines, labels covering the main product, and labels squeezed into bottom thumbnails. If labels cannot fit cleanly, reduce label count, split into two cards, or enlarge blank margins.

## Final Deliverable Gate

Before responding with a finished image set, verify:

- A no-text base image exists when image generation was used.
- A final Chinese annotated image exists for every requested deconstruction/structure board, unless the user explicitly requested no labels.
- The annotated image names real parts or features, not only view names such as `三视图` or generic notes.
- Uncertain or incorrect generated structures are marked as `待校`, `概念推测`, or rejected/regenerated.
- Labels are all Chinese except allowed industry abbreviations.
- Labels do not cover the product, exploded parts, section details, or bottom thumbnails.
- File names distinguish base and annotated outputs, for example `商品名_无文字底图_v1.0.png` and `商品名_中文标注版_v1.0.png`.

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
