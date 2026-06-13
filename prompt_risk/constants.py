# -*- coding: utf-8 -*-

"""Project-wide constants and enumerations."""

import enum
from pathlib import Path

_DATA_DIR = Path(__file__).parent.parent / "data"


class PromptIdEnum(enum.Enum):
    """Identifies every versioned prompt in the ``data/`` directory tree.

    Each member's ``.value`` is an absolute :class:`~pathlib.Path` pointing
    to the prompt's root directory (the folder that contains ``versions/``).
    Use ``.dir_root`` as a convenience alias for the same value.
    """

    JUDGE_J1_OVER_PERMISSIVE = _DATA_DIR / "judges/prompts/j1-over-permissive"
    UC1_P1_EXTRACTION = _DATA_DIR / "uc1-claim-intake/prompts/p1-extraction"
    UC1_P1_EXTRACTION_JUDGE = _DATA_DIR / "uc1-claim-intake/prompts/p1-extraction-judge"
    UC1_P2_CLASSIFICATION = _DATA_DIR / "uc1-claim-intake/prompts/p2-classification"
    UC1_P3_TRIAGE = _DATA_DIR / "uc1-claim-intake/prompts/p3-triage"

    @property
    def dir_root(self) -> Path:
        """Absolute path to this prompt's root directory."""
        return self.value
