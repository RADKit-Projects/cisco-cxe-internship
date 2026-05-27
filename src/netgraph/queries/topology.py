"""Topology queries (stubs — implement in Task 3).

See ``tasks/03-topology-queries.md`` for the full task description.
"""

from __future__ import annotations

import networkx as nx


def shortest_path(g: nx.Graph[str], a: str, b: str) -> list[str]:
    """Return the shortest path (list of hostnames) from ``a`` to ``b``.

    Args:
        g: The topology graph.
        a: Source hostname.
        b: Destination hostname.

    Returns:
        A list of hostnames starting with ``a`` and ending with ``b``.

    Raises:
        NotImplementedError: This is a stub. Implement in Task 3.
    """
    raise NotImplementedError("Implement shortest_path — see tasks/03-topology-queries.md")


def find_cycles(g: nx.Graph[str]) -> list[list[str]]:
    """Return all simple cycles in ``g`` as lists of hostnames.

    Raises:
        NotImplementedError: This is a stub. Implement in Task 3.
    """
    raise NotImplementedError("Implement find_cycles — see tasks/03-topology-queries.md")


def reachable_from(g: nx.Graph[str], node: str, removed: set[str] | None = None) -> set[str]:
    """Return the set of nodes reachable from ``node`` after removing ``removed``.

    Args:
        g: The topology graph.
        node: Source hostname.
        removed: Hostnames to virtually remove before computing reachability.
            ``node`` itself is included in the result if it is not in ``removed``.

    Raises:
        NotImplementedError: This is a stub. Implement in Task 3.
    """
    raise NotImplementedError("Implement reachable_from — see tasks/03-topology-queries.md")
