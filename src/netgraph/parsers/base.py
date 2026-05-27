"""Parser protocol."""

from __future__ import annotations

from typing import Protocol

from netgraph.models import Device


class Parser(Protocol):
    """A parser converts raw CLI output for one device into a :class:`Device`."""

    def parse(self, text: str, hostname: str) -> Device:
        """Parse ``text`` (raw CLI output) into a :class:`Device` named ``hostname``."""
        ...
