# Where this fixture came from

`cypress_results_sample.json` is a real mochawesome test-results shape,
modeled on production Cypress reports from prior work experience — this is
not invented test data. The structure, the failure types, and the pass/fail
ratios all mirror what a real Cypress suite reports. All identifying
details — company name, internal domains, internal tooling and command
names, repo names — have been replaced with generic equivalents.

## What was kept real, on purpose

- The full `stats` block shape (`suites`, `tests`, `passes`, `failures`,
  `duration`, `passPercent`, etc.)
- The nested `results -> suites -> tests -> err` tree structure
- Two real failure *types* that show up constantly in production Cypress
  suites:
  1. `AssertionError: Timed out retrying ... Expected to find element` —
     a selector/timing failure (element never rendered in time)
  2. `TypeError: Cannot read properties of undefined (reading 'name')` —
     a code/data failure (something upstream returned an unexpected shape)

These two failure types are deliberately different categories. Week 4's
LLM-as-Judge classifier needs real variety to prove it can tell them apart —
a fixture where every failure looks identical wouldn't test anything.
