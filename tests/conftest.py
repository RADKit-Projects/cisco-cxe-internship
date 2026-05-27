"""Shared test fixtures."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    """Path to the directory holding raw CLI output fixtures."""
    return Path(__file__).parent / "fixtures" / "cli_output"


@pytest.fixture(scope="session")
def all_device_texts(fixtures_dir: Path) -> Mapping[str, str]:
    """Mapping of hostname (filename stem) to raw CLI text."""
    return {p.stem: p.read_text(encoding="utf-8") for p in sorted(fixtures_dir.glob("*.txt"))}
