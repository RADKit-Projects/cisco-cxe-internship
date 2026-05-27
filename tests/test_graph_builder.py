"""Tests for the graph builder. These FAIL until Task 2 is implemented."""

from __future__ import annotations

from collections.abc import Mapping

import networkx as nx

from netgraph.graph.builder import GraphBuilder
from netgraph.models import Device
from netgraph.parsers.lldp import LldpParser


def _build_all(all_device_texts: Mapping[str, str]) -> tuple[nx.Graph[str], tuple[object, ...]]:
    parser = LldpParser()
    devices: list[Device] = [parser.parse(text, host) for host, text in all_device_texts.items()]
    g, inc = GraphBuilder().build(devices)
    return g, inc


def test_graph_has_14_nodes(all_device_texts: Mapping[str, str]) -> None:
    g, _ = _build_all(all_device_texts)
    assert g.number_of_nodes() == 14


def test_graph_has_expected_edge_count(all_device_texts: Mapping[str, str]) -> None:
    g, _ = _build_all(all_device_texts)
    # 15 expected canonical edges. Allow 14–17 to accommodate reasonable choices about:
    #   - whether the asymmetric dist-02 ↔ dc-edge-01 edge is added at all
    #   - whether the LAG (2 physical ports between dc-edge-01 and spine-01) is dedup'd
    #     into a single edge or modeled as two parallel edges in a MultiGraph
    assert 14 <= g.number_of_edges() <= 17


def test_asymmetric_edge_is_flagged(all_device_texts: Mapping[str, str]) -> None:
    _, inc = _build_all(all_device_texts)
    kinds = [getattr(i, "kind", None) for i in inc]
    details = " ".join(getattr(i, "detail", "") for i in inc)
    assert "asymmetric" in kinds
    assert "dist-02" in details and "dc-edge-01" in details


def test_known_edges_present(all_device_texts: Mapping[str, str]) -> None:
    g, _ = _build_all(all_device_texts)
    expected = {
        ("wan-edge-01.cxelab.example", "core-01.cxelab.example"),
        ("core-01.cxelab.example", "dist-01.cxelab.example"),
        ("core-01.cxelab.example", "dist-02.cxelab.example"),
        ("dist-01.cxelab.example", "dist-02.cxelab.example"),
        ("dist-01.cxelab.example", "acc-01.cxelab.example"),
        ("dist-02.cxelab.example", "acc-04.cxelab.example"),
        ("dc-edge-01.cxelab.example", "spine-01.cxelab.example"),
        ("dc-edge-01.cxelab.example", "spine-02.cxelab.example"),
        ("spine-01.cxelab.example", "leaf-01.cxelab.example"),
        ("spine-02.cxelab.example", "leaf-02.cxelab.example"),
    }
    for a, b in expected:
        assert g.has_edge(a, b), f"missing edge {a} <-> {b}"
