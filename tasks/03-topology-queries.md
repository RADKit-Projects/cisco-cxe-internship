# Task 3 — Topology Queries

**Estimated time:** 1–2 days
**File to implement:** `src/netgraph/queries/topology.py`
**Tests to make pass:** `tests/test_topology_queries.py`

## What to Build

Three functions over the graph from Task 2:

1. **`shortest_path(g, a, b)`** — hop-count shortest path as a list of hostnames.
2. **`find_cycles(g)`** — all simple cycles in the graph.
3. **`reachable_from(g, node, removed=...)`** — set of nodes reachable from
   `node` after virtually removing the hostnames in `removed`.

`networkx` is allowed and encouraged. Don't reimplement Dijkstra from scratch
unless you want to.

## Bonus — Neo4j

A `docker-compose.yml` at the repo root brings up a single-node Neo4j 5
instance with no auth on `bolt://localhost:7687`.

```bash
docker compose up -d
```

Bonus credit: load your graph into Neo4j and reproduce one of the three
queries above in Cypher. A small script under `scripts/` or a notebook is
enough. You don't need to make it production-grade — we want to see how you
think about graph databases.

## Tips

- The fixtures have intentional asymmetries; your graph in Task 2 should
  already be sensible regardless of those.
- "Removed" in `reachable_from` means "pretend this node and its edges
  don't exist for this query" — don't mutate `g`.

## When You're Done

```bash
uv run pytest tests/test_topology_queries.py -v
uv run mypy --strict src tests
```
