# Where this fixture came from

`cypress_results_sample.json` is a real mochawesome test-results shape, pulled
from real Cypress report files at work and anonymized. This is not invented
test data — the structure, the failure types, and the pass/fail ratios all
mirror actual reports. Only the identifying details were swapped.

## What was swapped and why

| Real (work repo)                                   | Anonymized (this project)          |
|------------------------------------------------------|-------------------------------------|
| `*.telus.com` domains                                | `checkout.example.com`              |
| `green-soe-e2e` repo name (in webpack paths)          | `storefront-e2e`                    |
| `commerce-ux-sales-summary-qe` module path            | `checkout-summary-widget`           |
| `cy.visitMFESalesSummaryShell`                        | `cy.visitCheckoutShell`             |
| `cy.bootstrapMfe`                                     | `cy.bootstrapApp`                   |
| `cy.initializeSalesSummaryMFE`                        | `cy.initializeCheckoutWidget`       |
| `cy.mountMfe`                                         | `cy.mountWidget`                    |
| `cy.validateSalesSummaryMFE`                          | `cy.validateOrderSummary`           |
| `brand: telus / koodo`                                | `region` (generic, no real values)  |
| `quoteId`                                             | `orderId` / cart concepts           |

## What was kept real, on purpose

- The full `stats` block shape (`suites`, `tests`, `passes`, `failures`,
  `duration`, `passPercent`, etc.)
- The nested `results -> suites -> tests -> err` tree structure
- The two real failure *types* that show up constantly in Cypress suites:
  1. `AssertionError: Timed out retrying ... Expected to find element` —
     a selector/timing failure (element never rendered in time)
  2. `TypeError: Cannot read properties of undefined (reading 'name')` —
     a code/data failure (something upstream returned unexpected shape)

These two failure types are deliberately different categories. Week 4's
LLM-as-Judge classifier needs real variety to prove it can tell them apart —
a fixture where every failure looks the same would not test anything.
