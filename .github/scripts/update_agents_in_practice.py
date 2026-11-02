"""Rebuild the Agents in Practice summary in README.md from the published catalog.

Replaces everything between the AGENTS-IN-PRACTICE:START and :END markers.
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

SITE = "https://ari20089.github.io/agents-in-practice/"
README = Path(__file__).resolve().parents[2] / "README.md"
START = "<!-- AGENTS-IN-PRACTICE:START -->"
END = "<!-- AGENTS-IN-PRACTICE:END -->"
EXAMPLES_PER_CATEGORY = 3
ICONS = {
    "skills": "🧩",
    "prompts": "💬",
    "agent-instructions": "📋",
    "adaptive-cards": "🃏",
}


def render(catalog):
    items = catalog["items"]
    repo = catalog["repository"].removeprefix("https://github.com/")
    count = f"{len(items)} item" + ("" if len(items) == 1 else "s")

    lines = [
        f'<a href="{SITE}"><img src="https://img.shields.io/badge/Browse%20the%20catalog-'
        f'{count.replace(" ", "%20")}-0070AD?style=for-the-badge" alt="Browse the catalog: {count}"/></a>',
        f'<a href="https://github.com/{repo}"><img src="https://img.shields.io/badge/Source-'
        f'{repo.replace("/", "%2F").replace("-", "--")}-181717?style=for-the-badge&logo=github&logoColor=white" '
        f'alt="Source: {repo}"/></a>',
        "",
        "| Category | Items | Latest |",
        "|:--|:-:|:--|",
    ]
    for category in catalog["categories"]:
        members = [i for i in items if i["type"] == category["folder"]]
        if not members:
            continue
        # Newest first; the name breaks ties so the output is stable between runs.
        members.sort(key=lambda i: i["name"])
        members.sort(key=lambda i: (i["updatedAt"], i["createdAt"]), reverse=True)
        examples = " · ".join(
            f"[{i['name']}]({SITE}{i['url']})" for i in members[:EXAMPLES_PER_CATEGORY]
        )
        icon = ICONS.get(category["folder"], "📦")
        lines.append(f"| {icon} **{category['label']}** | {len(members)} | {examples} |")
    return "\n".join(lines)


def main():
    with urllib.request.urlopen(SITE + "catalog.json", timeout=30) as response:
        catalog = json.load(response)
    if not catalog.get("items"):
        sys.exit("catalog.json has no items; leaving README.md unchanged")

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        sys.exit(f"Markers not found in {README}")
    block = f"{START}\n{render(catalog)}\n{END}"
    README.write_text(pattern.sub(lambda _: block, readme), encoding="utf-8")


if __name__ == "__main__":
    main()
