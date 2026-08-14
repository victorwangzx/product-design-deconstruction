# Category Principles

Use this reference to classify a product and make responsible design-structure inferences. Combine categories when an object spans multiple domains.

## Inference Discipline

- Start from visible facts before category assumptions.
- State uncertainty for hidden parts.
- Prefer common structures in mass-market products unless the photo shows a premium, specialized, handmade, or experimental product.
- Do not invent precise dimensions, materials, battery capacity, motor type, waterproof rating, safety certification, or manufacturing process unless visible or provided.
- For branded products, avoid copying proprietary internal layouts. Describe generic category principles and conceptual structures.

## Handheld Electronic Products

Examples: electric shaver, trimmer, toothbrush, facial cleansing device, massage tool, barcode scanner.

Design principles:

- Ergonomics: grip diameter, anti-slip zones, center of gravity, one-hand operation, thumb reach.
- Skin/body contact: rounded edges, cleanable surfaces, low pinch risk, detachable contact parts.
- Mechanism: motor, transmission, oscillating/rotating head, spring or floating mount, replaceable head, vibration isolation.
- Electronics: battery, PCB, button, indicator light, charging port or dock contacts.
- Protection: waterproof sealing, O-rings, ultrasonic welds, gasketed buttons, drain/cleaning paths.
- Manufacturing: injection-molded shell, parting lines, screws hidden under caps, snap fits, rubber overmold, metal mesh or blade carrier.

Common exploded layers:

1. Outer grip shell and decorative trim
2. Button/indicator lens
3. Waterproof gasket layer
4. Internal frame
5. Battery and PCB
6. Motor and transmission shaft
7. Floating head mount
8. Blade/mesh/contact assembly

## Containers and Vessels

Examples: tea canister, ceramic jar, water cup, storage box, cosmetic jar, food container.

Design principles:

- Core function: storage, pouring, sealing, holding, protection, display.
- Capacity and proportion: mouth diameter, body volume, center of gravity, stacking or shelf fit.
- Closure: lid fit, threads, cork, silicone ring, snap cap, friction fit, magnetic closure, hinged cap.
- Preservation: moisture resistance, odor isolation, light blocking, food-safe inner surface, easy cleaning.
- Material logic: ceramic wall thickness, glass transparency, metal crimping, plastic ribs, paperboard folds.
- Tactility: grip, rim comfort, lid handling, sound/feel of opening.
- Ritual/display: gift quality, pattern placement, label zone, table presence.

Ceramic construction discipline:

- Treat a ceramic jar body and its foot ring (`圈足`/`底足`) as one integral fired body by default. A thrown, slip-cast, jiggered, or molded ceramic vessel often has a foot ring shaped during forming/trimming, not a separately assembled base.
- Do not explode a ceramic foot ring as a loose part unless the photo shows a visible seam, different material, glued-on pad, metal/plastic base, protective sleeve, rubber ring, or display stand.
- In exploded views, show the foot ring as a shaped feature on the bottom of the vessel body, or use a section/detail callout. Do not show it floating below as an independent component unless it is truly an added base.
- Section view and exploded view must agree. If the section shows an integral foot ring, the exploded view must not show a separate bottom ring.
- Use `底足` or `圈足` as a feature label. Use `底座` only for an added base/stand or separate support component.

Common exploded layers:

1. Lid exterior
2. Seal ring or inner plug
3. Mouth/rim detail
4. Main vessel body, including integral shoulder, wall, bottom, and ceramic foot ring when applicable
5. Inner glaze/coating or liner
6. Added base foot, rubber pad, sleeve, or stacking insert only when visibly separate or category-justified
7. Label, sleeve, or decorative band

## Lighting Products

Examples: desk lamp, night light, pendant light, flashlight.

Design principles:

- Light path: LED source, reflector, diffuser, lens, shade, glare control.
- Adjustment: hinge, gooseneck, rotating joint, telescoping pole, weighted base.
- Thermal: heat sink, vents, metal core PCB, separation from touch zones.
- Power/control: switch, dimmer, color-temperature control, cable routing, battery, charging.
- Stability: base footprint, counterweight, anti-slip pad.

Common exploded layers:

1. Shade or lens
2. Diffuser
3. LED board
4. Heat sink
5. Joint or arm structure
6. Control PCB
7. Base shell and weight
8. Cable or battery module

## Packaging and Gift Objects

Examples: tea gift box, perfume box, premium stationery package, cosmetic set.

Design principles:

- Opening ritual: sleeve, drawer, magnetic flap, lift-off lid, hinge, layered reveal.
- Protection: insert tray, molded pulp, EVA, paperboard partitions, corner protection.
- Communication: brand mark, product story, color hierarchy, material cue, tamper evidence.
- Shelf/display: front face, stacking, unboxing composition, photo-readability.
- Sustainability: mono-material design, reusable box, reduced adhesives.

Common exploded layers:

1. Outer sleeve or cover
2. Main box shell
3. Hinge/magnet/ribbon
4. Insert tray
5. Product cavity
6. Instruction card or label
7. Protective wrap

## Children's Products

Examples: children's cup, toy appliance, school stationery, lunch box.

Design principles:

- Safety: rounded corners, no small detachable choking parts, non-toxic materials, finger-pinch avoidance.
- Cleaning: fewer dirt traps, removable washable parts, wide openings.
- Grip and scale: smaller hands, intuitive touch points, low force operation.
- Durability: drop resistance, flexible hinges, thickened corners.
- Emotional design: friendly forms, clear affordances, gentle colors, character cues without unsafe protrusions.

Call out safety assumptions clearly. Do not imply regulatory compliance unless provided.

## Structured Output Template

Use this template when the user asks for a full case:

```markdown
## 主体识别
- 主体物：
- 场景/背景：
- 可见限制：

## 商品属性
- 一级类别：
- 二级属性：
- 使用情境：
- 核心设计矛盾：

## 可见事实
- 形态：
- 材质/表面：
- 交互/开合：
- 分件/连接线索：

## 设计原理匹配
- 人机/使用：
- 结构/机构：
- 材料/工艺：
- 安全/清洁/维护：

## 合理结构推测
- 外层：
- 中层：
- 内层：
- 易损/可替换部件：
- 不确定点：

## 解构图方案
- 图面类型：
- 分层顺序：
- 标注策略：
- 不应标成事实的内容：

## 生成提示词
...

## 发布说明
...
```

## Prompt Patterns

Industrial sketch:

`vertical 9:16 industrial design sketch sheet of a [product category], 1080x1920 composition, preserving the visible exterior proportions from the reference photo, main product sketch in the upper area, multiple small perspective studies below, clean pencil and marker linework, large blank side margins for later Chinese annotation, no readable text in any language, no English words, white background`

Exploded view:

`vertical 9:16 conceptual exploded view of a [product category], 1080x1920 composition, separate only actual or likely separable parts, keep integral formed features attached to their parent body, inferred internal mechanism shown as generic category-based structure, visible parts preserved, hidden parts simplified, blank side margins and blank callout lines with no readable text in any language, no English words, precise industrial design drawing, thin black linework, subtle gray shading, no brand logos`

Three-view:

`vertical 9:16 orthographic three-view industrial design board of a [product category], 1080x1920 composition, front side top views arranged in the lower third, accurate silhouette based on reference photo, clean technical sketch style, no dimensions, no readable text in any language, no English words, white background`

CMF study:

`vertical 9:16 CMF design board for a [product category], 1080x1920 composition, material swatches for [materials], close-up surface texture studies, product silhouette thumbnail, restrained industrial design presentation, blank label areas, no readable text in any language, no English words`

Chinese handwritten overlay labels:

- Containers: `外盖`, `密封位`, `口沿`, `罐身`, `内腔`, `底足`, `纹样`, `釉面`
- Packaging tubes: `翻盖`, `防拆环`, `干燥塞`, `管身`, `标签`, `片剂`, `底座`, `密封面`
- Handheld electronics: `玻璃面板`, `屏幕层`, `中框`, `主板`, `电池`, `按键`, `后壳`, `接口`
- Lighting: `灯罩`, `扩散片`, `灯板`, `散热件`, `转轴`, `电路`, `底座`, `线缆`

Keep labels short. Put longer uncertainty notes outside the image or in the post body, not inside the diagram.

Use Chinese labels by default. Keep English only for real abbreviations or material/process codes, for example `PCB`, `CMF`, `LED`, `USB-C`, `PP`, `ABS`, `PET`, `IPX7`. Never use full English words such as `FRONT`, `SIDE`, `CAP`, `NOTES`, `MATERIALS`, or `SECTION` in final diagrams; translate them to `正视`, `侧视`, `外盖`, `说明`, `材质`, `剖面`.

Annotation placement:

- Reserve left/right side columns or lower white space for text.
- Keep label boxes outside the product silhouette and outside exploded parts.
- Use leader lines from the label box to the part.
- If there is not enough blank space, reduce label count or create a second detail card instead of covering the image.
