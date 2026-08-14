---
name: product-design-deconstruction
description: "Turn product photos, screenshots, or product links into industrial-design deconstruction: identify the main object, classify its product category and attributes, research the product's working principle, separate visible facts from inferred mechanisms, apply category-specific design principles, and produce design-analysis notes, exploded-view concepts, three-view sketch prompts, CMF notes, Chinese handwritten-style annotation overlays, and responsible AI image-generation prompts. Use when the user asks to analyze a product such as a shaver, tea canister, hot pot, lamp, cup, appliance, stationery item, package, tool, or consumer object and convert it into design sketches, structure diagrams, exploded diagrams, or product-design learning material."
---

# Product Design Deconstruction

## Core Rule

Treat the output as design analysis and concept reconstruction, not verified teardown evidence. Always separate:

- Visible facts: what can be seen directly in the photo.
- User-provided facts: corrections or details supplied by the user about how the object is used, assembled, heated, powered, filled, opened, cleaned, or protected.
- Visual identity layer: the product's distinctive exterior character, proportions, surface traces, color, finish, pattern, wear, context cues, and recognizable styling.
- Category-based inference: likely structures or mechanisms based on common products in the same category.
- Creative reconstruction: optional design improvements or stylized sketch directions.

Do not claim hidden internal structure is real unless the user provides teardown photos, CAD, drawings, manuals, patents, or measurements.

User-provided facts outrank category assumptions. If the user says the photo includes an independent tray, water-filled safety tray, special heat shield, detachable insert, or shop-specific visual style, treat that as a required constraint unless it conflicts with the image or safety reality. Do not overwrite it with generic product knowledge.

Use user-submitted images as evidence and visual reference by default, not as composited content. Do not embed, paste, collage, frame, overlay, or add the user's original photo into the final deliverable image unless the user explicitly asks for a before/after comparison, reference inset, or source-photo panel.

## Workflow

1. Identify the main object in the image or link. Distinguish the product from props, hands, background, packaging, and scene decoration.
2. Classify the object by product attributes, not just name. Use multiple labels when helpful, such as `handheld electronic product`, `ceramic container`, `food-storage packaging`, `skin-contact appliance`, `desktop lighting`, `children's product`, or `gift object`.
3. Extract visible design facts: silhouette, proportions, parting lines, seams, buttons, openings, surface texture, materials, colors, finish, logo/branding, user-contact areas, safety clues, and manufacturing hints.
4. Capture user-provided facts and corrections as constraints. Include any detail the user states about independent parts, water trays, safety functions, real usage, local shop features, or known product identity.
5. Preserve the visual identity layer from the user's photo. Capture proportions, silhouette quirks, surface finish, patina, wear marks, decorative pattern, hardware style, color temperature, and context-specific character before any generic reconstruction. Treat this as a required same-object evidence layer in the final board unless the user asks for a neutral technical drawing.
6. Research the product's working principle before inferring structure. Determine the energy source, operating cycle, material/fluid/air/heat path, user actions, safety boundaries, maintenance points, and likely serviceable parts. When the mechanism is specific, unfamiliar, safety-related, modern, regulated, or ambiguous, look up credible sources such as manuals, museum/encyclopedic references, technical articles, repair guides, patents, or official product pages before drawing.
7. Match the category to design principles. Read `references/category-principles.md` when a concrete product category is involved or when making mechanism/structure inferences.
8. Infer likely structure conservatively from visible facts, user-provided facts, and the researched working principle. Use wording such as "likely", "possibly", "common in this category", and "conceptual assumption".
9. Classify each feature as either a separable part, an integral molded/thrown/formed feature, surface decoration, or optional accessory. Read `references/structure-consistency-cases.md` before generating exploded views, section views, three-view boards, or any image that implies product construction. Do not explode integral features as independent parts.
10. Use the section/construction model as the source of truth for exploded views. If the section shows a continuous formed or permanently joined body, the exploded view must keep that body together and separate only serviceable inserts, accessories, trays, fasteners, or modules.
11. Run a structure-consistency check before finalizing: the exploded view, section view, three-view drawings, labels, and written explanation must describe the same construction logic.
12. Create a Chinese part-name list before generating the final annotated diagram. For any requested deconstruction, exploded-view, section-view, or structure board, the final deliverable must include component names unless the user explicitly asks for a no-label base image.
13. Produce the requested deliverable: design observation, visual-identity preservation notes, working-principle summary, structure hypothesis, exploded diagram description, sketch-generation prompt, three-view prompt, CMF board, Chinese annotation overlay, improvement proposal, or Xiaohongshu-safe post.
14. For images intended for publication, add an AI/assumption disclaimer and avoid brand infringement. Recommend removing or masking visible trademarks if the product is branded and the output is commercial or public.

## Output Menu

Choose only the sections that fit the user's request. For a full analysis, use this order:

1. Subject and category
2. Visible facts
3. User-provided facts
4. Visual identity layer
5. Working-principle research
6. Product attributes and design principles
7. Inferred structure
8. Part/integral-feature classification
9. Exploded-view layer plan
10. Structure-consistency check
11. Sketch prompt
12. CMF notes
13. Design improvement directions
14. Disclaimer and publishing safety notes

## Evidence Priority

Use this priority order when facts conflict:

1. User-provided facts and corrections about this specific object.
2. Visible facts in the supplied image.
3. Documents, manuals, teardown photos, measurements, or reliable sources supplied by the user.
4. Credible external research about the same product type.
5. Category principles and common construction logic.
6. Creative reconstruction.

If a user states a visible or usage-specific fact such as `照片里有独立托盘` or `托盘里会加水用于安全隔热`, the generated structure must include and label it. If unsure how it connects to the heat source, state the uncertainty or show a focused detail rather than omitting it.

## Visual Identity Preservation

Before generating diagrams, write a short preservation brief from the user's image:

- Overall silhouette and proportion: height/width, shoulder, rim, base, handle placement, distinctive asymmetry.
- Surface identity: patina, scratches, stains, glazing, hammer marks, printed patterns, color variation, material warmth, age, handmade or restaurant-use traces.
- Hardware identity: handle shape, rivets, hinge style, buttons, vents, feet, caps, knobs, seams.
- Context cues: restaurant object, home appliance, school object, gift packaging, child's toy, repair-worn item, premium display item.
- What must survive in every view: the 3-5 visual features that make this specific object recognizable.

Use the preservation brief in prompts. The generated product should look like a deconstructed version of the user's photographed object, not a generic category sample. Treat this as same-object evidence: the user should be able to compare the generated diagram with the source photo and recognize the same object family, shop-specific style, surface treatment, and key exterior proportions. Preserve identity by redrawing or translating visual cues, not by inserting the original photo into the board. For public diagrams, remove or soften brand marks if needed, but preserve non-branded visual character.

## Working-Principle Research

Before writing prompts or generating images, build a compact mechanism model:

- Energy/source: battery, mains electricity, charcoal fire, alcohol lamp, gas, manual force, gravity, pressure, magnetism, or passive storage.
- Core action: cutting, heating, sealing, filtering, lighting, cooling, locking, pouring, cushioning, transmitting motion, or containing.
- Path: air, smoke, heat, water, steam, liquid, powder, light, sound, vibration, force, or data path.
- User actions: open, fill, light, press, grip, pour, charge, clean, replace, adjust, carry, or store.
- Key structures: the parts required for the working principle to function.
- Safety and maintenance: heat isolation, ventilation, drainage, sealing, insulation, cleaning, replacement, child safety, food contact, or electrical protection.
- Uncertainty: alternative mechanisms that would change the structure.

If multiple working principles are plausible, branch the structure model instead of forcing one answer. For example, a hot pot heated by charcoal requires a combustion chamber, air inlets, grate, ash path, chimney/draft path, and heat-transfer contact to the annular soup basin. A small alcohol-lamp hot pot instead requires a lamp cup/burner, wick or fuel reservoir, flame clearance, wind shield, pot support, and often a water-filled or air-gap insulation tray. If the user says a water-filled safety tray is present, include it as a separable safety/insulation part even in a charcoal-style hot pot, while keeping the heat-source path internally consistent.

When research is used, cite the source names or URLs in the written analysis. When no external research is needed, say the working principle is based on visible facts and common category principles.

## Sketch Prompt Requirements

When generating prompts for image tools, include:

- Canvas policy: use a 9:16 vertical composition by default, preferably `1080x1920` for saved outputs. Override only when the user explicitly asks for another ratio or when the target format requires it.
- Product category and viewpoint.
- Drawing type: industrial design sketch, exploded view, three-view sheet, function zoning diagram, CMF study, detail callout, or concept redesign.
- Evidence discipline: visible exterior preserved, inferred interior shown as conceptual, hidden parts labeled as assumptions.
- User-fact discipline: explicitly include user-specified parts and functions, such as a visible independent tray with water used for safety isolation. Do not omit these details because generic category research points elsewhere.
- Visual identity discipline: preserve the photographed object's silhouette, proportions, surface finish, patina/wear, color, hardware style, and distinctive non-branded visual cues across the intact view, exploded view, section view, and three-view thumbnails.
- Source-image discipline: use the submitted image only as reference unless the user explicitly requests a comparison panel. Final diagrams must not include the original photo as an inset, background, overlay, collage tile, corner thumbnail, or framed evidence panel.
- Working-principle discipline: show only structures that fit the selected mechanism. Do not mix charcoal, alcohol-lamp, gas, and electric heating structures unless presenting alternative concepts.
- Structural discipline: only separate actual or likely separable parts. Do not visually explode one-piece ceramic/plastic/metal features such as molded feet, thrown foot rings, ribs, lips, or shoulders unless the category normally uses an added insert or the photo shows a seam.
- View-consistency discipline: make the exploded view obey the section view. If the section shows the pot body, chimney, base wall, or shell as one continuous or permanently joined assembly, do not split those forms into floating trays or duplicate bodies in the exploded view.
- Materials and finish.
- Line quality and composition.
- Text and callout policy: generate a clean no-readable-text base image by default with no labels, no empty callout boxes, no leader lines, no arrows, no numbered markers, and no fake annotation placeholders. Leave blank margins only. Add all Chinese labels and leader lines locally after image generation.
- Component contract: before image generation, define a compact component table with `Chinese name`, `intended visual form`, `intended position/layer`, `function cue`, and `label priority`. The prompt must describe each labeled component by both name and visual evidence, not by name alone. After generation, use this component contract as the checklist for visual verification and local labels.

For actual image generation, use the `imagegen` skill or available image-generation tool after this analytical step.

## Component Contract

For any generated exploded view, section view, or annotated board, create a component contract before calling image generation. This contract connects prompt intent to later labels.

Minimum fields:

```markdown
| 中文名 | 视觉形态 | 位置/层级 | 功能线索 | 标注优先级 |
|---|---|---|---|---|
```

Rules:

- The prompt must include the contract's visible requirements, such as `方形小模块，带圆形玻璃镜头`, `长条声腔，带网孔`, `浅圆托盘，内部有水面`, or `一体圈足，连在陶瓷罐身底部`.
- The generated base image must be checked against the same contract before labels are placed.
- A label can be used only when the generated part matches both the contract and visible evidence in the image.
- If the generated image contains a part with the right name in the prompt but the wrong shape, wrong location, or ambiguous function, do not label it as that component. Either relabel with a neutral visible-feature name, omit it, or regenerate the base.
- If the generated image contains a clear component that was not in the contract, label it only if it fits the product working principle and does not conflict with user-provided facts.
- For important small parts, require distinctive visual evidence in the prompt. Do not request only `camera module`, `speaker`, `seal`, `sensor`, `tray`, or `vent`; specify what makes it recognizable.

This contract is the bridge between prompt and annotation. Do not treat the prompt's part list as automatic ground truth, and do not treat a visual guess as enough without checking it against the contract.

## Default Image Set

When the user provides a product photo and asks for generated images without specifying a layout, create one 9:16 vertical design board rather than mixed-size images. Use this hierarchy:

1. Top area: intact product sketch or hero perspective.
2. Middle area: main conceptual exploded view or structure diagram.
3. Lower area: three-view thumbnails, section detail, or CMF swatches.
4. Side margins and intentional white space: Chinese handwritten labels. Do not place text on top of the product, structure parts, thumbnails, CMF swatches, or existing diagram details.

The intact top view must preserve the user's photographed exterior most strongly. The exploded and section views may simplify hidden internals, but they should carry the same exterior silhouette, material finish, hardware style, and visible wear/pattern cues.

Do not include a copy of the source photo in the board. If provenance or comparison is needed, provide the source photo as a separate file/link or a separate comparison artifact only after the user asks.

Keep all final saved images in the same dimensions within one task. Use semantic version filenames, such as `商品名_设计拆解图组_v1.0.png`, `商品名_无文字底图_v1.0.png`, and `商品名_中文标注版_v1.0.png`.

If a tool returns a different aspect ratio, crop or pad non-destructively to 9:16 before final delivery. Prefer padding with a clean white or paper-like background over cropping product details.

## Structure-Consistency Check

Before generating or delivering an image, write a compact construction model:

- Separable parts: pieces a user/manufacturer could plausibly remove or assemble separately.
- Integral features: shapes formed as part of the same material/body.
- Surface layers: paint, decal, glaze, label, coating, texture, printing.
- Optional assumptions: only shown when useful, visually marked as conceptual, and kept consistent across all views.
- User-provided fact model: any stated part, usage detail, safety function, or correction that must appear in the final analysis/image.
- Working-principle model: energy/source, path, heat/fluid/air/motion route, and user-serviceable parts.
- Visual identity model: distinctive exterior cues from the source photo that must remain visible after deconstruction.
- Source-image usage model: confirm whether the source photo is reference-only or explicitly requested as an inset/comparison image.

Then verify:

1. Exploded view separates only separable parts and optional conceptual inserts.
2. Section view shows the same construction model as the exploded view.
3. Three-view drawings do not imply seams or extra parts that the structure model rejects.
4. Labels name integral features as features, not standalone components. Use `底足/圈足` for ceramic foot rings, not `独立底座`, unless an added base is visible.
5. The exploded view does not duplicate a shell/body that already exists in the intact view unless the product truly has nested removable shells.
6. User-provided factual parts and functions are included, labeled, and not contradicted by the drawing.
7. The final image still resembles the user's photographed object in silhouette, material character, and distinctive visual cues.
8. The final image does not embed or collage the user's original photo unless explicitly requested.
9. Repeated parts have the same identity across views. A tray, lid, grate, basket, base, or shell shown in the exploded view must match its section-view shape, position, and function. If the exploded view shows a shallow round tray, the section view must not replace it with side cups, boxed tanks, or a different support geometry.
10. Label anchors point to the named part itself, not to adjacent fluid, shadows, decorative base, or another nearby component. For water trays, label `盛水托盘` on the tray body and `托盘水面` only if labeling the water surface separately.
11. If an AI-generated image creates a contradiction, omits a user-provided fact, embeds the original photo without request, or becomes a generic category object, either regenerate or explicitly reject that part of the image as inaccurate.

## Part Identity Check

Before naming any visible feature or generated module, identify it by **shape + location + function + category logic**, not by shape alone. A circle, hole, ring, slot, knob, tray, vent, button, or dark module can mean different things in different products.

Use this general test:

1. Shape: what is the visible geometry, such as circular hole, button cap, lens, grille, slot, ring, hinge, tray, rib, or panel?
2. Location: where is it relative to user-contact zones, top/bottom, front/back, opening path, heat path, fluid path, power path, or motion path?
3. Function cue: does it invite pressing, viewing, venting, pouring, gripping, sealing, heating, sensing, attaching, draining, supporting, or protecting?
4. Category logic: in this product category, what does this feature usually do in that location?
5. Evidence conflict: does another interpretation fit the visible evidence better?

Name the part only after this check. Do not label a feature from one clue alone, such as "round = lens", "hole = vent", "ring = separate part", "tray = ash tray", or "dark rectangle = battery".

Examples of the general rule:

- A round feature in a user-press area is often a button, knob, latch, or fingerprint/home key; a round feature on an optical/sensing zone with a glassy center is more likely a lens or sensor.
- A small hole near a microphone/speaker/air path may be an acoustic port, vent, drain, or fastener hole depending on category and location.
- A ring on a ceramic vessel may be an integral foot ring; a ring with different material, seam, or replaceable function may be a gasket, trim, base, or seal.
- A tray near heat/fluid paths may be a water tray, ash tray, fuel tray, drip tray, or insulation tray; choose by energy source and user-provided facts.
- A long perforated module near an audio path may be a speaker or grille; a long slot near a cooling path may be a vent; a long opening near a container rim may be a pour/drain feature.

If the identity remains ambiguous, use a neutral label such as `疑似接口`, `疑似传感区`, or `结构待校` only when useful; otherwise omit the label and explain the uncertainty outside the image.

## Chinese Handwritten Annotation Workflow

Use this workflow whenever the user wants Chinese handwritten-style labels, publishable diagrams, or Xiaohongshu-ready images:

1. Generate the base diagram with no readable text in any language, no fake labels, no empty callout boxes, no leader lines, no arrows, no numbered markers, and enough blank side/bottom space for annotations. Explicitly ask for no English words such as "front", "side", "cap", "notes", or material labels.
2. Use the Component Contract as the source list for candidate labels. Write the Chinese part-name list from the contract, including visible exterior parts, likely serviceable internal parts, key integral features, and any uncertainty labels such as `结构待校`, `概念推测`, or `待验证`.
3. Run the Part Identity Check before writing label coordinates. Confirm that each generated shape matches the contract's intended visual form, position/layer, and function cue. Do not inherit the prompt's part list directly as labels without this match.
4. Inspect the generated no-text base image and build a concrete part-location map before writing label coordinates. The part-location map should include `label text`, `contract row`, `visible evidence`, `anchor coordinate`, and `label coordinate`. Do not rely only on the prompt, intended layer order, or memory of the construction model. The image generator returns pixels, not a semantic map, so every label anchor must be chosen from the visible generated part.
5. For each label, record the visible target part, approximate center or edge anchor, and why that target is identifiable. If a part cannot be located confidently in the generated base image or does not match the contract, omit that label, regenerate a clearer base, or mark the part outside the image as an uncertainty note. Never place a label because the part "should be there" if it is not visually identifiable.
6. Keep each label under 8 Chinese characters when possible, such as `外盖`, `密封圈`, `内胆`, `主板`, `电池`, `口沿`, `罐身`, `底足`, `材质`, `开合区`.
7. Add the labels locally with `scripts/add_handwritten_labels.py` instead of relying on AI-generated Chinese text.
8. Use a real local Chinese handwritten or handwritten-adjacent font when available. Prefer `Alimama DongFangDaKai` or a Chinese kaiti/handwriting font. If unavailable, fall back to an installed Chinese font such as `Hiragino Sans GB`, `STHeiti`, or `Arial Unicode`, and report that it is a font fallback.
9. Use all-Chinese labels by default. English is allowed only for real industry abbreviations or material codes, such as `PCB`, `CMF`, `LED`, `USB-C`, `PP`, `ABS`, `PET`, or `IPX7`.
10. Place labels outside the drawing content, preferably in left/right side columns or bottom white space. Use one local leader line per label to point at the relevant part. Do not let label boxes cover product silhouettes, exploded parts, section views, three-view drawings, material swatches, or important linework.
11. Visually inspect the base image before overlay. If the base image already contains callout boxes, leader lines, arrows, numbered markers, or pseudo-label placeholders, reject or regenerate it before local annotation.
12. Visually inspect the final image for wrong characters, English leakage, overlapping labels, broken leader lines, inaccurate anchors, labels covering the main product, labels pointing to the wrong generated part, and labels squeezed into bottom thumbnails. If labels cannot fit cleanly, reduce label count, split into two cards, or enlarge blank margins.

## Final Deliverable Gate

Before responding with a finished image set, verify:

- A no-text base image exists when image generation was used.
- The base image has no generated callout boxes, leader lines, arrows, numbered markers, or pseudo-label placeholders.
- A final Chinese annotated image exists for every requested deconstruction/structure board, unless the user explicitly requested no labels.
- The annotated image names real parts or features, not only view names such as `三视图` or generic notes.
- Uncertain or incorrect generated structures are marked as `待校`, `概念推测`, or rejected/regenerated.
- Every local leader line points to the correct component or feature. If an anchor cannot be placed accurately, omit that label or move it to a separate notes section rather than drawing a misleading line.
- Repeated components are visually consistent across exploded, section, and three-view panels. A user-specified tray must retain the same shape family and position logic across views.
- Labels are all Chinese except allowed industry abbreviations.
- Labels do not cover the product, exploded parts, section details, or bottom thumbnails.
- The final board does not contain the user's original photo as an inset, background, collage element, or reference panel unless the user explicitly requested it.
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
