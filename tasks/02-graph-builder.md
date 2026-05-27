# Task 2 — Graph Builder

**Estimated time:** ~1 day
**File to implement:** `src/netgraph/graph/builder.py`
**Tests to make pass:** `tests/test_graph_builder.py`

## What to Build

Implement `GraphBuilder.build(devices) -> (graph, inconsistencies)`:

- Add one node per device (use the hostname from the `Device` object).
- For each `Neighbor` entry, add an undirected edge between the device and
  the named remote system.
- Return any data quirks as `Inconsistency` records.

## Inconsistencies to Surface

Your fixtures will trigger at least one of each:

- **`asymmetric`** — `dist-02` claims a neighbor on `dc-edge-01`, but
  `dc-edge-01` does not see `dist-02` on the matching port. Decide whether to
  include the half-seen edge; flag the asymmetry either way.
- **`unknown_neighbor`** — a device claims a neighbor that has no `Device`
  object in the input set. Not used by the supplied fixtures, but your code
  should still handle it.

## A Decision That's Yours

`dc-edge-01` shows `spine-01` as a neighbor on **two** local ports (a LAG bundle
`Po1` = `Gi1/0/1` + `Gi1/0/2`). The same is true from spine-01's side.

You can either:

- collapse them into a single logical edge with `bundle_size=2` on edge data, or
- keep both as parallel edges (requires `networkx.MultiGraph`).

Either is fine — be ready to explain your choice in the interview.

## Tips

- Use `networkx.Graph` (or `MultiGraph` if you go that route).
- Edges should be canonical: same edge regardless of which device's parse
  added it first.
- Strict typing applies to graph data too — annotate any helper functions
  fully.

## When You're Done

```bash
uv run pytest tests/test_graph_builder.py -v
uv run mypy --strict src tests
```
