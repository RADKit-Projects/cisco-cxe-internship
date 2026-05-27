"""Tests for the LLDP parser. These FAIL until Task 1 is implemented."""

from __future__ import annotations

import logging
from collections.abc import Mapping

import pytest

from netgraph.models import Capability
from netgraph.parsers.lldp import LldpParser

# Expected neighbor count per device, derived from the fixtures.
# leaf-02 has one truncated/malformed block that should be skipped+warned.
EXPECTED_COUNTS: Mapping[str, int] = {
    "wan-edge-01": 1,
    "core-01": 3,
    "dist-01": 4,
    "dist-02": 5,
    "acc-01": 1,
    "acc-02": 1,
    "acc-03": 1,
    "acc-04": 1,
    "dc-edge-01": 3,
    "spine-01": 4,
    "spine-02": 3,
    "leaf-01": 2,
    "leaf-02": 2,
}


def test_parser_parses_every_fixture(all_device_texts: Mapping[str, str]) -> None:
    parser = LldpParser()
    for host, text in all_device_texts.items():
        # leaf-02 contains a malformed block; parser must not crash on it.
        d = parser.parse(text, host)
        assert d.hostname == host
        assert len(d.neighbors) == EXPECTED_COUNTS[host], host


def test_parser_handles_multiline_system_description(all_device_texts: Mapping[str, str]) -> None:
    parser = LldpParser()
    d = parser.parse(all_device_texts["spine-01"], "spine-01")
    dc_edge = next(n for n in d.neighbors if n.system_name.startswith("dc-edge-01"))
    assert dc_edge.system_description is not None
    # Multi-line description should be joined into a single string with all parts present.
    assert "CXE-9500" in dc_edge.system_description
    assert "FAKE-17.9.1" in dc_edge.system_description
    assert "RELEASE SOFTWARE" in dc_edge.system_description


def test_parser_normalizes_mixed_capability_format(all_device_texts: Mapping[str, str]) -> None:
    parser = LldpParser()
    # leaf-01 fixture uses "B,R" short form for its neighbors.
    d = parser.parse(all_device_texts["leaf-01"], "leaf-01")
    for n in d.neighbors:
        assert Capability.BRIDGE in n.capabilities
        assert Capability.ROUTER in n.capabilities


def test_parser_handles_missing_mgmt_address(all_device_texts: Mapping[str, str]) -> None:
    parser = LldpParser()
    # core-01's view of dist-02 has no Management Addresses block.
    d = parser.parse(all_device_texts["core-01"], "core-01")
    dist_02 = next(n for n in d.neighbors if n.system_name.startswith("dist-02"))
    assert dist_02.mgmt_address is None


def test_parser_skips_malformed_block_with_warning(
    all_device_texts: Mapping[str, str], caplog: pytest.LogCaptureFixture
) -> None:
    parser = LldpParser()
    with caplog.at_level(logging.WARNING):
        d = parser.parse(all_device_texts["leaf-02"], "leaf-02")
    assert len(d.neighbors) == 2
    # At least one warning should have been logged about the malformed entry.
    assert any("malformed" in rec.message.lower() or "skip" in rec.message.lower() for rec in caplog.records)
