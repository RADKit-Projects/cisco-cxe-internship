"""LLDP CLI parser (stub — implement in Task 1).

This module is a stub. Your job in Task 1 is to implement
:class:`LldpParser.parse` so that the fixtures under
``tests/fixtures/cli_output/`` are correctly turned into
:class:`netgraph.models.Device` instances.

See ``tasks/01-lldp-parser.md`` for the full task description.
"""

from __future__ import annotations

from netgraph.models import Device


class LldpParser:
    """Parses ``show lldp neighbors detail`` output from Cisco IOS-XE devices."""

    def parse(self, text: str, hostname: str) -> Device:
        """Parse the given LLDP CLI output.

        Args:
            text: Raw CLI output captured from the device.
            hostname: The hostname of the device whose output this is.

        Returns:
            A populated :class:`Device` instance.

        Raises:
            NotImplementedError: This is a stub. Implement in Task 1.
        """
        raise NotImplementedError("Implement LldpParser.parse — see tasks/01-lldp-parser.md")
