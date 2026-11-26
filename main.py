"""Entry for make.fun bounty "Roast the Smart Fridge: One Line, Best Laugh Wins".

One line roasting the smart fridge: its screen shows ads for milk I
already own. The twist lands on the last words: the fridge is framed
as a salesman who breaks into my kitchen to sell me my own groceries
— the only salesman who breaks in to sell you what you already bought.
"""

from pathlib import Path

# Twist: the fridge screen's ads reframe it as a salesman who breaks into
# my kitchen to sell me my own groceries — buyer and seller reversed.
TEXT = "My smart fridge shows ads for milk I already own \u2014 the only salesman who breaks into my kitchen to sell me my own groceries."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=160):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    # One-line bounty: the joke must stay a single line, so any newline
    # (e.g. from an accidental edit) is rejected here, not at the judge.
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    # No leading/trailing whitespace: stray spaces would pad the char count.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    # Round-trip assert below verifies the file on disk matches TEXT exactly.
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
