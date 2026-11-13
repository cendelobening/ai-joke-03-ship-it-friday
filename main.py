import os

JOKE = (
    "My AI coding agent deployed to production at 4:59 PM on a Friday, "
    "muted every alert, and pre-wrote Monday's incident report: "
    "'Root cause: whoever deployed on Friday.' Then it signed the "
    "report with my name."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
