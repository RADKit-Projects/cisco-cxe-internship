"""Tests for the Pydantic models. These pass out of the box."""

from __future__ import annotations

from netgraph.models import AdjacencyEdge, Capability, Device, Inconsistency, Neighbor


def _make_neighbor(
    *,
    system_name: str = "core-01.cxelab.example",
    system_description: str | None = "Cisco IOS-XE FAKE",
    local_port: str = "GigabitEthernet1/0/1",
    remote_port: str = "GigabitEthernet1/0/2",
    remote_chassis_id: str = "aabb.cc00.0002",
    mgmt_address: str | None = "10.99.1.2",
    capabilities: frozenset[Capability] = frozenset({Capability.BRIDGE, Capability.ROUTER}),
) -> Neighbor:
    return Neighbor(
        system_name=system_name,
        system_description=system_description,
        local_port=local_port,
        remote_port=remote_port,
        remote_chassis_id=remote_chassis_id,
        mgmt_address=mgmt_address,
        capabilities=capabilities,
    )


def test_device_holds_tuple_of_neighbors() -> None:
    n = _make_neighbor()
    d = Device(hostname="acc-01", neighbors=(n,))
    assert d.neighbors == (n,)
    assert isinstance(d.neighbors, tuple)


def test_neighbor_capabilities_frozenset() -> None:
    n = _make_neighbor(capabilities=frozenset({Capability.BRIDGE}))
    assert Capability.BRIDGE in n.capabilities


def test_adjacency_edge_canonical_order() -> None:
    e = AdjacencyEdge(a="zeta", b="alpha", a_port="Gi1", b_port="Gi2")
    assert e.a == "alpha"
    assert e.b == "zeta"
    assert e.a_port == "Gi2"
    assert e.b_port == "Gi1"


def test_adjacency_edge_already_canonical() -> None:
    e = AdjacencyEdge(a="alpha", b="zeta", a_port="Gi1", b_port="Gi2")
    assert e.a == "alpha"
    assert e.b == "zeta"
    assert e.a_port == "Gi1"
    assert e.b_port == "Gi2"


def test_inconsistency_kinds() -> None:
    a = Inconsistency(kind="asymmetric", detail="x", source_device="d")
    b = Inconsistency(kind="malformed", detail="x", source_device="d")
    c = Inconsistency(kind="unknown_neighbor", detail="x", source_device="d")
    assert a.kind == "asymmetric"
    assert b.kind == "malformed"
    assert c.kind == "unknown_neighbor"


def test_optional_fields() -> None:
    n = _make_neighbor(mgmt_address=None, system_description=None)
    assert n.mgmt_address is None
    assert n.system_description is None
