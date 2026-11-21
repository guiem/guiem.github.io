# CV timeline illustrations — approved art direction (revision 5)

## Goal

Recreate all 13 illustrations in `images/timeline/` as **recognizably stick-figure drawings**, with the warm, slightly richer, handcrafted **blue ballpoint-pen** look of the recently approved individual examples (`guiem_ai`, `guiem_caish`, `guiem_mabrian`, `guiem_signaturit`). **Retain the actual version of Guiem shown in each original illustration.**

**Golden rule: Change the drawing style, not the character, scene, or story.**

## Source priority

1. **Original files on `master`** are authoritative for the character's appearance, hair, facial hair, glasses, clothing, pose, props, objects, readable wording, and composition.
2. **Approved blue-ink examples** are authoritative for the *hand-drawn stick-figure visual style*, level of detail, and general line quality only.
3. The present simplified JPEGs in PR #18 are **not** reliable content references. Do not trace them, recolor them, or use them as the sole source.

## Drawing style — stick figures with handmade personality

- The person remains **unmistakably a stick figure**: round imperfect head, dot-like or simple eyes, expressive little mouth, slender simplified torso and limbs.
- Moderate extra detail is welcome for identifying characteristics, distinctive clothing, hands/gestures, and scene objects. Do **not** turn the body into a fully rendered cartoon person.
- Draw with slightly uneven, overlapping, naturally wandering **blue ballpoint pen strokes** on a white background. Vary line weight and ink density; some loose hatching and sketch construction strokes are fine.
- Make circles, glasses, pages, monitors, and other objects look hand-sketched, **not constructed from perfect geometric primitives**.
- Charming and playful, a little rough, not sterile. Avoid polished vector art, precision curves, glossy effects, gradients, flat cartoon fills, and uniform digital outlines.
- Preserve visual simplicity **without deleting meaningful content**. Think of a detailed, spontaneous notebook doodle, not an ultraminimal icon and not a realistic pencil portrait.

## Per-illustration character fidelity — mandatory

Do **not** apply one generic hairstyle or face to every version of Guiem. Match the **original of that specific filename**.

- **Short hair remains short. Long hair remains long**, at roughly the same length, texture, and silhouette.
- **Ponytails remain ponytails; buns remain buns.** Preserve their position and characteristic loose strands. Do not turn long hair, ponytails, or buns into the default short spiky hairstyle.
- **Beard length, shape, fullness, and presence** follow the original. When there is a fuller hipster-like beard, draw its full, organic shape using loose pen strokes and restrained hatching, rather than a few uniform chin spikes.
- **Mustaches appear only when present in the original.** Make the mustache natural, with hairs pointing **downward and slightly outward** and blending into the beard where relevant. **Never draw upward-curled, handlebar, or twirled mustache ends.**
- **Glasses are typically rounded**, so when present in the original, use two recognizable slightly irregular *round* frames with a visible bridge and small temple arms — not square or rectangular glasses unless the original specifically requires them.
- Preserve original age impression, facial expression, clothing outline, posture, gesture, and recognizable accessories. Do not add glasses to originals that lack them.

The facial-hair and glasses instructions apply to each historical portrayal as appropriate; they do not override the actual original reference.

## Preserve the original scene

For each image preserve the original main action, composition, relationships and meaningful objects: e.g. graduation cap, EEG headset, wheelchair, train, airplane, security shield/robot, charts, clipboard, signed document, laptop, books, and yoga pose, **only where shown in the corresponding original**. Keep distinctive details and icon meanings instead of substituting generic symbols or giving every scene the same laptop setup.

## Handwritten lettering — mandatory

- Keep **every legible, meaningful word, letter, number, symbol and diagram label** from the original, with the original spelling and approximate placement; examples include `ERP` and `CS`.
- All lettering should look **written with the same blue pen** as the drawing, with organically imperfect strokes, irregular baseline, and natural spacing.
- No digital fonts, sterile typography, or fake unreadable pseudo-text.
- Review text character by character. If the source is unclear, flag it for review rather than inventing a word.
- Do not insert decorative milestone names that were *not* in the original merely to fill space.

## Working procedure and checks

For each of the 13 images:

1. Open the **original JPEG from `master`** and note its hairstyle, glasses, beard, mustache, clothes, expression, pose, props, and all legible text.
2. Recreate it in the approved blue-pen stick-figure style, keeping those specifics intact. This must be a new drawing, not programmatic recoloring and overlaid geometric accessories.
3. Check side-by-side at full size: does the hair length/type match (including bun or ponytail)? Are rounded glasses present only if appropriate? Does the mustache point down, not up? Does the beard match? Is *all* meaningful text present and handwritten? Is the original story recognizable?
4. Reject and revise any draft that changes the person's historical appearance, omits words/props, looks vectorized, or ceases to look like a stick figure.
5. Compare the entire batch for consistent blue-ink character, natural linework, handwriting, and level of complexity without homogenizing the hairstyles or facial features.

## Delivery and repository safety

- Output exactly 13 valid JPEG files with **unchanged filenames** under `images/timeline/`, compatible with the website's current layout (prefer 900 × 900 pixels).
- Produce a contact sheet and, ideally, original-versus-revised comparisons for review.
- Commit completed artwork to existing branch `art/stick-figure-cv-timeline` / PR #18 **only after the images are actually generated and inspected**.
- **Do not merge PR #18.** Documentation updates alone do not constitute regenerated artwork.

## Negative prompt

Generic short spiky hairstyle on everyone; turning ponytails or long hair into short hair; upward-curled handlebar mustache; default rectangular spectacles; missing or altered original features; full polished cartoon bodies; realism; typographic fonts; geometric perfect curves; Pillow/SVG-drawn overlays; undifferentiated backgrounds; generic laptop scene; missing props; illegible or invented text; overly minimal iconography.

**Acceptance criterion:** The person is instantly a charming handcrafted blue-pen *stick figure*, but comparing each image to its `master` original reveals the **same Guiem**, including the exact historical hairstyle, facial hair, glasses, clothing, and scene details.
