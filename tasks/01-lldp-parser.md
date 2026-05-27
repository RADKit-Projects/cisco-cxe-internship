# Task 1 — LLDP Parser

**Estimated time:** half a day
**File to implement:** `src/netgraph/parsers/lldp.py`
**Tests to make pass:** `tests/test_lldp_parser.py`

## What to Build

Implement `LldpParser.parse(text, hostname) -> Device` so it correctly converts
the raw `show lldp neighbors detail` output under `tests/fixtures/cli_output/`
into `netgraph.models.Device` instances.

A neighbor block starts with a line of dashes and contains at least:

- `Local Intf:` — the local port
- `Chassis id:` — the remote chassis MAC
- `Port id:` — the remote port
- `System Name:` — the remote hostname
- `System Description:` — may span multiple lines
- `System Capabilities:` — space- or comma-separated
- `Management Addresses:` — optional, may be absent

## Quirks You Will Encounter

The fixtures intentionally contain some real-world ugliness:

1. **Multi-line `System Description`.** One device's view of `dc-edge-01`
   wraps the description across three lines.
2. **Mixed capability formats.** Most devices write `Bridge, Router`. One
   device (`leaf-01`) writes the short form `B,R`. Normalize both into the
   `Capability` enum.
3. **Missing fields.** One neighbor lacks `Management Addresses:` entirely.
   `mgmt_address` should be `None`, not an error.
4. **Malformed block.** One fixture (`leaf-02`) ends with a truncated entry.
   Your parser must **skip it and log a warning**, not crash.

## Tips

- Look at one fixture file before writing any code.
- Split on the dash-separator line, then parse each block independently.
- Use the `logging` module (`logger = logging.getLogger(__name__)`).
- Strict typing: no `Any`, no `# type: ignore`, no `hasattr`.

## When You're Done

```bash
uv run pytest tests/test_lldp_parser.py -v
uv run mypy --strict src tests
```
