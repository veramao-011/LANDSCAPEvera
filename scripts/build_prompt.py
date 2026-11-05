#!/usr/bin/env python3
"""Build a Studio A architectural illustration prompt without network access."""

import argparse
import json

SCENES = {
    "general": "Make the intended spatial relationship clear through composition and line hierarchy.",
    "entrance": "Show a clear transition from the urban edge to the site, with an access threshold and planted buffer.",
    "bridgehead": "Show the bridgehead, landward route and riverside path; make level changes legible without inventing crossings.",
    "meander": "Show a river bend and a peripheral path set back from a sensitive habitat core.",
    "courtyard": "Show spatial enclosure, circulation and planted edges with clear ground planes.",
}
PALETTE = {"background": "#FFFFFF", "primary_line": "#5656D9", "secondary_line": "#8C91DF", "shadow": "#E4E0FA", "accent": "#A7DDED", "water": "#EAF7FC"}


def build_prompt(args):
    parts = [
        f"Create a {args.view} architectural or landscape illustration of {args.subject}.",
        f"Context: {args.location}. {SCENES[args.scene]}",
        "Use white background, fine blue-violet outlines with stronger principal contours, restrained pale lavender shading and pale-cyan accents. Crisp drafting and open white space. Fine parallel horizontal sky hatching; sparse linear water reflections.",
        "Use a few plants with slender open branches and sharp irregular leaf contours, plus sparse grasses. Avoid fuzzy silhouettes, cartoon crowns and dense leaves.",
        "No text, people, animals, vehicles, decorative objects, cloud icons, stippled sky, paper texture or watercolor bleed. Keep functional elements needed to explain the design.",
        "Preserve supplied site geometry, orientation and design relationships; do not infer precise structures from ambiguous inputs.",
    ]
    if args.constraints:
        parts.append(f"Project-specific instructions override defaults: {args.constraints}")
    return "\n\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subject", required=True, help="Site and design action")
    parser.add_argument("--location", default="As specified by the user")
    parser.add_argument("--view", choices=("perspective", "section", "axonometric", "plan"), default="perspective")
    parser.add_argument("--scene", choices=tuple(SCENES), default="general")
    parser.add_argument("--constraints", default="", help="Project-specific overrides and invariants")
    parser.add_argument("--json", action="store_true", help="Return JSON with palette targets")
    args = parser.parse_args()
    if not args.subject.strip():
        parser.error("--subject must not be empty")
    prompt = build_prompt(args)
    print(json.dumps({"prompt": prompt, "palette": PALETTE, "scene": args.scene, "view": args.view}, ensure_ascii=False, indent=2) if args.json else prompt)


if __name__ == "__main__":
    main()
