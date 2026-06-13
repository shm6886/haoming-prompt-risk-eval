# -*- coding: utf-8 -*-

"""Project-wide path constants.

All paths are resolved relative to the repository root so they work
regardless of the current working directory.
"""

import enum
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent


class PathEnum(enum.Enum):
    """Absolute paths to key project directories and files.

    Use ``PathEnum.<member>.value`` to get the :class:`~pathlib.Path` object.
    """

    ROOT = _REPO_ROOT
    PROMPT_RISK = _REPO_ROOT / "prompt_risk"
    DATA = _REPO_ROOT / "data"
    DOCS = _REPO_ROOT / "docs"
    EXAMPLES = _REPO_ROOT / "examples"
    TESTS = _REPO_ROOT / "tests"
    TESTS_MANUAL = _REPO_ROOT / "tests_manual"

    @property
    def path(self) -> Path:
        """Return the resolved :class:`~pathlib.Path`."""
        return self.value
