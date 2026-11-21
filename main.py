"""Write a short poem about stopping to entry.txt."""

import os

POEM = """The road does not end when the feet do.
Stopping is a choice, not a defeat —
a hand unclenching, a held breath loosed,
the quiet after the drumbeat.

We are taught to run until we break,
to call the pause a failure, a mistake.
But rest is the work the runner keeps:
the field lies fallow, and the fallow dreams.

Stop, then. Not because you lost the race,
but because the finish line is a place —
and every road is kinder when you know
the grace of standing still, and letting go.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
