"""Re-lay out the generated 3-stats.svg cards for the README.

The README shows the 340x200 card at 150px high, which makes its 14px text hard
to read. This widens the card to 500x200 to line up with the streak card, and
enlarges and re-spaces the text, icons and logo to fill it.

Usage: restyle_stats_card.py CARD.svg [CARD.svg ...]
"""

import re
import sys

WIDTH = 500
TITLE_SIZE = 24
TITLE_Y = 34
ROW_SIZE = 17
ROW_GAP = 28
ROWS_TOP = 12  # offset of the first row inside the action's translate(30,20) group
ICON_SCALE = 1.1
LABEL_X = 24
VALUE_X = 170
LOGO_SCALE = 6.5
LOGO_X = 362
LOGO_Y = 8


def restyle(svg):
    if 'viewBox="0 0 340 200"' not in svg:
        raise ValueError("unexpected card layout")

    svg = svg.replace('width="340" height="200" viewBox="0 0 340 200"',
                      f'width="{WIDTH}" height="200" viewBox="0 0 {WIDTH} 200"')
    svg = re.sub(r'(<rect x="1" y="1"[^>]*?) width="[0-9.]+%"', rf'\1 width="{WIDTH - 2}"', svg)

    # Title
    svg = re.sub(r'<text x="30" y="40"(.*?)font-size: 22px;',
                 rf'<text x="30" y="{TITLE_Y}"\1font-size: {TITLE_SIZE}px;', svg)

    # Rows: the action spaces them 25.2 apart starting at y=0 (icons) and y=14 (text baselines).
    svg = svg.replace('<g transform="translate(30,20)">', f'<g transform="translate(30,{ROWS_TOP})">')

    def row(y):
        return round(float(y) / 25.2)

    icon_top = 14 - ROW_SIZE * 0.35 - 8 * ICON_SCALE  # centre the icon on the text's x-height
    svg = re.sub(
        r'<g transform="translate\(0,([0-9.]+)\)" width="14" height="14"',
        lambda m: f'<g transform="translate(0,{row(m[1]) * ROW_GAP + icon_top:.1f}) scale({ICON_SCALE})" '
                  'width="14" height="14"',
        svg)
    svg = re.sub(
        r'<text x="(21|130)" y="([0-9.]+)"(.*?)font-size: 14px;',
        lambda m: f'<text x="{LABEL_X if m[1] == "21" else VALUE_X}" '
                  f'y="{(row(float(m[2]) - 14)) * ROW_GAP + 14}"{m[3]}font-size: {ROW_SIZE}px;'
                  + (" font-weight: 600;" if m[1] == "130" else ""),
        svg)

    # GitHub logo
    svg = svg.replace('<g transform="translate(220,20)"><g transform="scale(6)"',
                      f'<g transform="translate({LOGO_X},{LOGO_Y})"><g transform="scale({LOGO_SCALE})"')
    return svg


def main():
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            svg = f.read()
        try:
            svg = restyle(svg)
        except ValueError as e:
            print(f"::warning::{path}: {e}; left unchanged")
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)


if __name__ == "__main__":
    main()
