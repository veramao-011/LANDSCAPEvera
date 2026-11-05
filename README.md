# Studio A Blueprint

A portable architectural and landscape illustration skill defined through text-based style rules: fine blue-violet linework, pale cyan accents, subtle lavender shading, a white canvas, hatched skies and sparse, sharply drawn vegetation. It supports perspectives, sections, axonometrics and illustrations accompanying site analysis.

## Install and use

Copy the entire `studio-a-blueprint` folder into the skills directory used by your Codex installation, commonly `~/.codex/skills/`. Keep its subfolders together. In a session where the skill is available:

```text
Use $studio-a-blueprint to create a landscape perspective for this site. Preserve the design geometry and use sparse planting.
```

```text
Use $studio-a-blueprint to create a city entrance, bridgehead and river-bend view. Keep my mapping unchanged and place the views alongside it.
```

The user's instructions override default style rules. The package contains no images. Image creation requires an available image generation tool; this skill supplies guidance and does not itself generate images or provide an API key.

## Optional prompt builder

Requires Python 3.9+, with no third-party packages or network access:

```bash
python scripts/build_prompt.py --scene bridgehead --subject "A riverside connection" --location "Italy" --view perspective
```

Use `--help` for scene choices, project constraints and JSON output. Color values are visual targets, not exact pixel guarantees. The output is a concept illustration, not a surveyed or engineering drawing.
