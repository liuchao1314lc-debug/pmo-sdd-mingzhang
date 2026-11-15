#!/usr/bin/env python3
"""Install the PMO skill in a Codex project."""

import sys
from pathlib import Path


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    sys.dont_write_bytecode = True
    from install_project_skill import main

    main(default_host="codex")
