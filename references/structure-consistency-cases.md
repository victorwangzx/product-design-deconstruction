# Structure Consistency Cases

Use these cases before writing exploded-view prompts or judging AI-generated deconstruction images. The goal is to avoid turning integral shape features into fake separable parts.

## General Test

Ask these questions for every visible feature:

1. Is there a visible seam, fastener, material change, gasket, or assembly boundary?
2. Would a user, repairer, or manufacturer plausibly remove or assemble this as a separate part?
3. Is this feature usually formed by molding, trimming, folding, bending, machining, glazing, printing, embossing, or surface finishing?
4. If the exploded view separates it, will the section view and three-view drawings still make sense?

If the answer points to forming or surface finishing, label it as an integral feature or surface layer, not a separate part.

## Ceramic Jar / Tea Canister

- Usually separable: lid; optional inner plug or seal if visible or category-justified.
- Usually integral: vessel body, shoulder, wall, bottom, foot ring (`圈足`/`底足`), rim profile.
- Surface layer: glaze, decal/painted pattern, printed mark.
- Common mistake: exploding the ceramic foot ring as a floating bottom base.
- Correct handling: keep `底足/圈足` attached to the jar body; show it in section or detail callout.
- Only separate a bottom element when there is a different material, visible seam, added rubber pad, metal/plastic base, sleeve, coaster, display stand, or protective ring.

## Plastic Bottle / Tube / Food Container

- Usually separable: cap, flip lid, tamper band after opening, gasket, inner seal film, desiccant plug, scoop, inner tray.
- Usually integral: bottle neck, screw thread, ribs, shoulder, molded grip, bottom push-up, hinge living hinge when molded with cap.
- Surface layer: printed label, shrink sleeve, coating, embossing.
- Common mistake: exploding bottle-neck threads or molded ribs as independent rings.
- Correct handling: show threads/ribs as features of the bottle or cap; separate only caps, seals, inserts, or sleeves.

## Smartphone / Tablet

- Usually separable: front glass/display module, mid-frame, battery, PCB, camera module, buttons, speaker module, rear shell when construction supports it.
- Usually integral: rounded corners, chamfers, antenna line grooves, button cutouts, port openings, decorative edge bevels.
- Surface layer: glass coating, printed black mask, logo/printing, adhesive layer if shown conceptually.
- Common mistake: treating edge chamfers or screen reflections as separate layers.
- Correct handling: separate functional modules and structural assemblies; keep fillets/chamfers attached to their parent shell or frame.

## Electric Shaver / Small Handheld Appliance

- Usually separable: outer shell halves, button cap, gasket, internal frame, battery, PCB, motor, transmission, blade head, foil/mesh, cleaning cap.
- Usually integral: grip curvature, molded ribs, overmolded texture if not shown as separate material, decorative grooves, drainage channels formed in shell.
- Surface layer: coating, rubberized finish, printed icons.
- Common mistake: exploding anti-slip texture or decorative grooves as layers.
- Correct handling: separate shell, gasket, drive, and blade modules; treat texture/grooves as surface or molded features.

## Paper Box / Packaging Carton

- Usually separable: product, insert tray, sleeve, instruction card, protective wrap, sticker/seal.
- Usually integral: fold lines, crease lines, tabs cut from the same sheet, glue flaps, die-cut windows in the same board.
- Surface layer: print, varnish, foil stamping, embossing.
- Common mistake: treating fold lines, panels, or printed regions as separate boards.
- Correct handling: explain the one-piece dieline logic; explode insert/sleeve/product layers only.

## Cup / Mug

- Usually separable: lid, straw, silicone sleeve, coaster, gasket, infuser basket.
- Usually integral: cup body, rim, ceramic foot ring, molded plastic grip texture.
- Ambiguous: handle. In production it may be attached before firing or molded with the body, but in finished-product deconstruction it is usually treated as part of the cup body unless the task is about manufacturing process.
- Common mistake: exploding a ceramic handle as a user-removable part.
- Correct handling: keep handle attached in product-structure diagrams; discuss attachment only in manufacturing notes.

## Lamp

- Usually separable: shade, diffuser, LED board, heat sink, arm/joint parts, base shell, counterweight, cable, switch.
- Usually integral: molded vents, ribbing, decorative grooves, rounded base edge, cable channel in a shell.
- Surface layer: paint, anodizing, texture, printed icons.
- Common mistake: treating vent holes or rib patterns as separate parts.
- Correct handling: separate optical, thermal, electrical, joint, and base assemblies; keep molded details attached to the shell.

## Charcoal Hot Pot / Old Beijing Copper Hot Pot

- First decide the heat-source system: charcoal fire, alcohol lamp, electric heating, or gas. The exploded structure must follow that system.
- Charcoal version usually separable/serviceable: fire grate (`火箅`), ash tray (`灰盘`) if visible or typical for the model, chimney cap/lid if present, removable charcoal basket if visible, detachable handles only when fasteners or separate mounts are visible.
- Charcoal version usually integral or permanently joined: annular soup basin (`环形汤槽`), central chimney (`中心烟囱`), rolled rim (`锅沿`), vent holes (`通风孔`), raised base/fire chamber shell, soldered/brazed/riveted seams unless the image shows a removable joint.
- Alcohol-lamp version usually separable/serviceable: alcohol lamp cup, wick/burner, extinguishing cap, pot support, wind shield, fuel tray, insulation tray or water tray when visible or category-justified.
- Alcohol-lamp version usually integral/permanent: pot body, support frame welds, punched vents, rolled rim, fixed handle mounts.
- Surface layer: copper patina, soot marks, polishing, lacquer, tin lining, decorative hammering, stamped pattern. Mark tin lining or water tray as assumptions unless visible or provided.
- Common mistake: drawing a charcoal chimney and an alcohol-lamp tray in the same exploded view; detaching the chimney or rolled rim as a loose part without a seam; omitting the air/smoke path in a charcoal hot pot.
- Common mistake: making the section view structurally plausible while the exploded view invents a different base, tray, or stacked-shell system.
- Correct handling: show heat source, air/oxygen path, exhaust/smoke path or flame clearance, heat transfer to the soup basin, and table-surface heat isolation. If the heat source is uncertain, present two small alternatives instead of one contradictory mechanism.
- View consistency: if the section view shows a charcoal fire chamber inside a raised base with vent holes, the exploded view should keep the pot/chimney/base shell as one main vessel assembly, then separate only the fire grate, ash tray, charcoal basket, lid/cap, or insulation tray when justified. Do not add an alcohol-lamp-style water tray to a charcoal version unless the user provides that detail or the object visibly has one.

## When To Add A Separate Base Or Foot

Add a separate base/foot only when at least one condition is true:

- A visible seam or gap separates it from the body.
- It uses a different material or finish.
- The category commonly uses added anti-slip pads, bumpers, stands, feet, or sleeves.
- The part has a separate function such as cushioning, heat isolation, electrical contact, counterweight, display support, charging, or replaceable protection.
- The user asks for a creative redesign rather than a faithful category-based deconstruction.

Otherwise, treat base/foot geometry as an integral feature and label it accordingly.

## Final QA

Reject or regenerate an image when:

- The exploded view separates a feature that the section view shows as integral.
- A label calls an integral feature a standalone component.
- A three-view drawing adds seams that are not present in the construction model.
- A creative assumption is visually indistinguishable from a visible fact.
- A surface decoration is shown as a structural layer without explanation.
