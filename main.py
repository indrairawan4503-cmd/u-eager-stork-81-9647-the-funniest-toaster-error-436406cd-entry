import os

LINE = "ERR 0x07: Toaster on strike. No browning until the crumb tray is cleaned and a day off is granted."


def resolve_output_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if out.endswith("entry.txt"):
        return out
    return os.path.join(out, "entry.txt")


def write_entry(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main():
    write_entry(resolve_output_path(), LINE)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        write_entry(os.path.join(here, "entry.txt"), LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
