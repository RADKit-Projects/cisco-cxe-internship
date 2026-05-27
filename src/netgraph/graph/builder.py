"""Graph builder (stub — implement in Task 2).

See ``tasks/02-graph-builder.md`` for the full task description.
"""

from __future__ import annotations

from collections.abc import Iterable

import networkx as nx

from netgraph.models import Device, Inconsistency


class GraphBuilder:
    """Builds a :class:`networkx.Graph` from per-device LLDP neighbor data."""

    def build(self, devices: Iterable[Device]) -> tuple[nx.Graph[str], tuple[Inconsistency, ...]]:
        """Build a graph from a collection of devices.

        Args:
            devices: An iterable of :class:`Device` instances.

        Returns:
            A pair ``(graph, inconsistencies)`` where ``graph`` is an undirected
            ``networkx.Graph`` with one node per device and one edge per
            adjacency, and ``inconsistencies`` is a tuple of
            :class:`Inconsistency` records describing any asymmetric, malformed,
            or otherwise suspicious data encountered.

        Raises:
            NotImplementedError: This is a stub. Implement in Task 2.
        """
        raise NotImplementedError("Implement GraphBuilder.build — see tasks/02-graph-builder.md")
