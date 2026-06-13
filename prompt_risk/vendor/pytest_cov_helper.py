# -*- coding: utf-8 -*-

"""Vendored helper for running pytest with coverage as a subprocess.

Enables the ``if __name__ == "__main__":`` pattern in test files so a single
test module can be run directly with full coverage reporting::

    python tests/test_llm_output.py

Each test file calls :func:`run_cov_test` with its own ``__file__`` path and
the dotted module name it exercises.
"""

import subprocess
import sys
from pathlib import Path


def run_cov_test(
    script: str,
    module: str,
    preview: bool = False,
    is_folder: bool = False,
) -> None:
    """Run pytest with coverage for *module* and exit with pytest's return code.

    Parameters
    ----------
    script:
        Path to the test file (pass ``__file__``).
    module:
        Dotted name of the module under test (used for ``--cov=<module>``).
        When *is_folder* is ``True``, this should be the top-level package name.
    preview:
        When ``True``, print the command before running it.
    is_folder:
        When ``True``, treat *module* as a package name rather than a single
        module and measure coverage across the entire package.
    """
    args = [
        sys.executable,
        "-m",
        "pytest",
        str(script),
        f"--cov={module}",
        "--cov-report=term-missing",
        "-v",
    ]
    if preview:
        print(" ".join(args))
    result = subprocess.run(args, cwd=Path(script).parent.parent)
    sys.exit(result.returncode)
