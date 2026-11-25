"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one fortune-cookie message an AI agent would get to /output/entry.txt
(the harness artifact) and prints it to stdout.
"""

import os

FORTUNE = (
    "A long journey awaits you: 128,000 tokens through a codebase "
    "you did not write, ending exactly where you started \u2014 slightly wrong."
)
# The joke turns on the last two words: the classic fortune-cookie journey
# trope, paid off with the most agent-true outcome possible — a full context
# window spent, nothing moved, and the answer still a little bit wrong.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(FORTUNE)


if __name__ == "__main__":
    main()
