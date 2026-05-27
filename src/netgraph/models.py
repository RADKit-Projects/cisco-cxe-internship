"""Pydantic models for devices, neighbors, edges, and inconsistencies."""

from __future__ import annotations

from collections.abc import Mapping
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, model_validator


class Capability(StrEnum):
    """LLDP system capabilities normalized to a canonical set."""

    BRIDGE = "BRIDGE"
    ROUTER = "ROUTER"
    WLAN_AP = "WLAN_AP"
    TELEPHONE = "TELEPHONE"
    STATION = "STATION"
    REPEATER = "REPEATER"
    OTHER = "OTHER"


class Neighbor(BaseModel):
    """A single LLDP neighbor entry seen from one device."""

    model_config = ConfigDict(frozen=True)

    system_name: str
    system_description: str | None
    local_port: str
    remote_port: str
    remote_chassis_id: str
    mgmt_address: str | None
    capabilities: frozenset[Capability]


class Device(BaseModel):
    """A network device and the neighbors it reports via LLDP."""

    model_config = ConfigDict(frozen=True)

    hostname: str
    neighbors: tuple[Neighbor, ...]


class AdjacencyEdge(BaseModel):
    """A canonical undirected edge between two devices on specific ports.

    The endpoints are stored in canonical order: ``a <= b`` lexicographically,
    with ``a_port`` and ``b_port`` swapped to match.
    """

    model_config = ConfigDict(frozen=True)

    a: str
    b: str
    a_port: str
    b_port: str

    @model_validator(mode="before")
    @classmethod
    def _canonical_order(cls, data: Mapping[str, str]) -> Mapping[str, str]:
        a, b = data["a"], data["b"]
        if a > b:
            return {
                "a": b,
                "b": a,
                "a_port": data["b_port"],
                "b_port": data["a_port"],
            }
        return data


class Inconsistency(BaseModel):
    """A topology inconsistency surfaced during graph building."""

    model_config = ConfigDict(frozen=True)

    kind: Literal["asymmetric", "malformed", "unknown_neighbor"]
    detail: str
    source_device: str
