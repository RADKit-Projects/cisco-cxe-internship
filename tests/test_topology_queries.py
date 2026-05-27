"""Tests for the topology queries. These FAIL until Task 3 is implemented."""

from __future__ import annotations

from collections.abc import Mapping

import networkx as nx

from netgraph.graph.builder import GraphBuilder
from netgraph.parsers.lldp import LldpParser
from netgraph.queries.topology import find_cycles, reachable_from, shortest_path

ACC_01 = "acc-01.cxelab.example"
ACC_02 = "acc-02.cxelab.example"
LEAF_01 = "leaf-01.cxelab.example"
LEAF_02 = "leaf-02.cxelab.example"
WAN_EDGE = "wan-edge-01.cxelab.example"
CORE = "core-01.cxelab.example"
DIST_01 = "dist-01.cxelab.example"
DIST_02 = "dist-02.cxelab.example"


def _graph(all_device_texts: Mapping[str, str]) -> nx.Graph[str]:
    parser = LldpParser()
    devices = [parser.parse(text, host) for host, text in all_device_texts.items()]
    g, _ = GraphBuilder().build(devices)
    return g


def test_shortest_path_acc01_to_leaf02(all_device_texts: Mapping[str, str]) -> None:
    g = _graph(all_device_texts)
    path = shortest_path(g, ACC_01, LEAF_02)
    assert path[0] == ACC_01
    assert path[-1] == LEAF_02
    # acc-01 -> dist-01 -> dist-02 -> dc-edge-01 -> spine-(1|2) -> leaf-02 = 6 nodes
    assert len(path) == 6


def test_shortest_path_wan_edge_to_leaf01(all_device_texts: Mapping[str, str]) -> None:
    g = _graph(all_device_texts)
    path = shortest_path(g, WAN_EDGE, LEAF_01)
    assert path[0] == WAN_EDGE
    assert path[-1] == LEAF_01
    assert len(path) >= 5


def test_campus_dist_pair_creates_cycle(all_device_texts: Mapping[str, str]) -> None:
    g = _graph(all_device_texts)
    cycles = find_cycles(g)
    # core-01 / dist-01 / dist-02 must appear together in at least one cycle.
    assert any({CORE, DIST_01, DIST_02}.issubset(set(c)) for c in cycles)


def test_removing_core_partitions_wan_from_leaves(all_device_texts: Mapping[str, str]) -> None:
    g = _graph(all_device_texts)
    reachable = reachable_from(g, WAN_EDGE, removed={CORE})
    assert LEAF_01 not in reachable
    assert LEAF_02 not in reachable
    assert ACC_01 not in reachable


def test_reachable_from_includes_source(all_device_texts: Mapping[str, str]) -> None:
    g = _graph(all_device_texts)
    reachable = reachable_from(g, ACC_01, removed=set())
    assert ACC_01 in reachable
    assert ACC_02 in reachable
