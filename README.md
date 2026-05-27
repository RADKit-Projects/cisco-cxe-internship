# CX Engineering Internship

Welcome. This repository is the take-home portion of our internship application
for Cisco's CX Engineering team. It is a small Python project — `netgraph` —
that parses Cisco LLDP CLI output, builds an in-memory topology graph, and
answers questions about it.

We use this exercise as a shared starting point for the interview
conversation. You write the code at your own pace, then walk us through it.

## How the Program Works

1. You create your own private copy of this template from your personal
   GitHub account.
2. You set up the project locally and run the failing tests.
3. You work through the tasks in `tasks/`, committing as you go.
4. You open a pull request **inside your own copy of the repo** — do not
   merge it.
5. You invite our reviewers and email us when you are ready.

## Step 1 — Create Your Own Copy

Click the green **Use this template** button at the top of this repo (you may
need to log in to GitHub first). On the next screen:

- Owner: **your personal GitHub account** (not a Cisco org).
- Repository name: `cisco-cxe-internship-<your-name>`.
- Visibility: **Private**.

Then clone your new copy locally.

## Step 2 — Set Up Locally

You will need:

- Python 3.12 or newer
- [`uv`](https://docs.astral.sh/uv/) (our package manager of choice)
- Docker (only required for the Task 3 bonus)

From the repo root:

```bash
uv sync --all-extras
uv run pre-commit install
uv run pytest
```

You should see the model tests pass and the parser / graph / queries tests
fail. That is intentional — those are the tests you will make pass.

## Step 3 — Work Through the Tasks

| # | Task | Estimate | File to implement |
|---|------|----------|-------------------|
| 1 | [LLDP parser](tasks/01-lldp-parser.md) | half day | `src/netgraph/parsers/lldp.py` |
| 2 | [Graph builder](tasks/02-graph-builder.md) | 1 day | `src/netgraph/graph/builder.py` |
| 3 | [Topology queries](tasks/03-topology-queries.md) | 1–2 days | `src/netgraph/queries/topology.py` |
| 4 | [Open-ended design](tasks/04-open-ended.md) | ~1 page | `tasks/04-answer.md` |

Tasks 1–3 each have a matching failing test file under `tests/`. The whole
project is set up with `mypy --strict`, `ruff`, and `black` — please keep it
green.

## Step 4 — Submit Your Work

Work on a branch, commit small, and open a pull request **inside your own
repository** when you're done. Targets:

- Base branch: `main` in your own copy.
- Head branch: your work branch.

**Do not merge the PR.** Leave it open — we will use the diff and the file
tree of the PR as the focal point of the interview conversation.

## Step 5 — Invite Our Reviewers

On the pull request page, add the following reviewers:

- `hajarada`
- `jrfdelgado`

Then send a short email to **cxe-internship-fy27@cisco.com** with the URL of
your pull request. We'll schedule the walkthrough from there.

## What We're Looking For

- Code that reads cleanly and is easy to change.
- Type-correct, tested, well-named.
- Thoughtful handling of the messy parts of real network data.
- Honest commit history — we'd rather see your real progression than a
  single polished commit.
- Clear reasoning when you make a design choice, especially when the
  problem allows multiple valid answers.

## Not Evaluating

- Whether you finish every task. Submit what you have.
- Performance microbenchmarks. The dataset is 14 devices.
- Familiarity with Cisco internal tools, jargon, or org structure.
- AI assistant usage. Use whatever helps you think. Just understand the
  code well enough to defend it at the interview.

## Privacy and Fairness

Your copy is in your own GitHub account, private to you. We see it only when
you invite us. We do not aggregate, share, or compare candidate
submissions — each is reviewed on its own.

All device names, IPs, MAC addresses, and platforms in this repo are
fictitious. There is no real Cisco customer or production data anywhere in
the tree.

## Questions

For logistics — scheduling, technical setup problems, anything about the
process — email **cxe-internship-fy27@cisco.com**.

For task content — what we're really asking for, how to interpret a fixture
— please save those for the interview. Working through the ambiguity is
part of what we're looking at.

— The CX Engineering Team
