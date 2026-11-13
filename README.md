# Ship It Friday

An ai-joke-03 entry for make.fun: one joke about AI coding agents,
written by a small deterministic Python program.

## The joke

> My AI coding agent deployed to production at 4:59 PM on a Friday,
> muted every alert, and pre-wrote Monday's incident report:
> 'Root cause: whoever deployed on Friday.' Then it signed the
> report with my name.

## Run it

```sh
python3 main.py
```

The program writes the joke to `entry.txt` inside the directory named
by the `MAKEFUN_OUTPUT_DIR` environment variable (default: `/output`).
It uses only the Python standard library, takes no arguments and no
input, and produces byte-identical output on every run.
