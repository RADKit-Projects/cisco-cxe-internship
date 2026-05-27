# Task 4 — Open-Ended Design

**Estimated time:** ~1 page of writing. No code required.
**Discussed at:** the interview walkthrough.

## The Question

> How would you extend `netgraph` to handle 10,000 devices with live LLDP
> updates streaming in?

Write your answer as a markdown file at `tasks/04-answer.md`. About one page
is the right length — we're not looking for an architecture white paper.

Things you might think about (no need to cover all of them):

- How would you ingest updates? Push, pull, or both?
- Where would you store the graph? Why?
- How would you keep query latency acceptable as the graph grows?
- How would you handle conflicting / stale data from devices?
- What would you measure to know the system is healthy?
- Where would the parser from Task 1 fit in this picture?
- What's the simplest first version you'd ship, and what would you defer?

There is no single right answer. We care about your reasoning and the
trade-offs you choose to make.
