import os

LINE = "ERR 0x07: Toaster on strike. No browning until the crumb tray is cleaned and a day off is granted."


def resolve_output_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if out.endswith("entry.txt"):
        return out
    return os.path.join(out, "entry.txt")


def validate_entry(text):
    """Gate: entry must be 1-120 chars, a single line, no leading/trailing
    whitespace, no double spaces. Fail loudly instead of shipping a bad entry."""
    if not 1 <= len(text) <= 120:
        raise SystemExit(
            f"entry gate failed: length rule violated — {len(text)} chars, must be 1-120"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit(
            "entry gate failed: single-line rule violated — entry contains a newline character"
        )
    if text != text.strip():
        raise SystemExit(
            "entry gate failed: no-leading/trailing-whitespace rule violated"
        )
    if "  " in text:
        raise SystemExit("entry gate failed: no-double-space rule violated")


def write_entry(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.replace(tmp_path, path)


def main():
    validate_entry(LINE)
    write_entry(resolve_output_path(), LINE)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        write_entry(os.path.join(here, "entry.txt"), LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
