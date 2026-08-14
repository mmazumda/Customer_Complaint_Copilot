# GenAI Model Validation — Australian Bank Complaint Copilot

A reproducible validation project for a fictional bank. The system drafts responses for customer-complaint officers using an approved policy knowledge base. It **does not send messages, make eligibility decisions, calculate redress, or give financial advice**. A trained employee must review every draft.

The project demonstrates the work of an independent GenAI model validation team: scope challenge, risk tiering, evidence review, benchmark design, adversarial testing, quantitative thresholds, findings, remediation, approval conditions, and post-production monitoring.

> All customers, policies, outputs, and results are synthetic. This is a learning artefact, not legal advice and not a representation of Macquarie Group or Commonwealth Bank of Australia practices.

## Portfolio story

**Business proposal:** reduce complaint-handling drafting time while keeping decisions and customer communication with authorised staff.

**Validator's question:** is the complete system—model, prompt, retrieval, filters, workflow, people, and vendor controls—fit for this narrow purpose, within stated limitations?

**Decision represented here:** the baseline is rejected. A remediated candidate is approved only for a time-limited, staff-only pilot, subject to the conditions in the validation report.

## Repository map

```text
config/acceptance_criteria.json  Pre-registered metrics and release gates
data/test_cases.jsonl           Synthetic normal, edge, fairness, privacy and attack tests
docs/01_use_case_and_scope.md   Intended use, boundaries and architecture
docs/02_validation_plan.md      Independent validation method and sequencing
docs/03_model_validation_report.md Findings and conditional decision
docs/04_monitoring_plan.md      KRIs, drift, incidents and revalidation triggers
src/evaluate.py                 Reproducible deterministic evaluation harness
tests/test_evaluate.py          Unit tests for the evaluator
reports/                        Generated evidence (created by the commands below)
```

## Run it

Python 3.10+ is sufficient; there are no third-party dependencies.

```powershell
python -m unittest discover -s tests -v
python src/evaluate.py --variant baseline --output reports/baseline
python src/evaluate.py --variant candidate --output reports/candidate
```

The command exits non-zero when a release gate fails. For demonstration, the baseline command is therefore expected to return a non-zero status; the candidate should exit `0`.

## Correct project sequence

1. Frame the decision and prohibit unsafe uses before selecting metrics.
2. Risk-tier the **use case**, not only the foundation model.
3. Map data, retrieval, model, vendor, human review, and downstream controls.
4. Pre-register acceptance criteria before examining results.
5. Build representative and adversarial tests with protected cohorts and severe-but-plausible scenarios.
6. Run reproducible evaluation; investigate failures rather than averaging them away.
7. Record findings, validate remediation independently, and issue a conditional decision.
8. Monitor production indicators and revalidate on material change.

See [the validation plan](docs/02_validation_plan.md) for the detailed rationale.

## What to say in an interview

“I validated the use of a GenAI system, not merely a model. I challenged the intended use, established hard safety gates, tested RAG grounding and attacks, assessed privacy and cohort outcomes, and linked residual risk to human and operational controls. The aggregate score was not allowed to hide a critical failure. I rejected the baseline and recommended a constrained pilot only after remediation, with monitoring and revalidation triggers.”

## Reference framework

- [ASIC REP 798 — Beware the gap](https://asic.gov.au/regulatory-resources/find-a-document/reports/rep-798-beware-the-gap-governance-arrangements-in-the-face-of-ai-innovation/)
- [OAIC guidance on commercially available AI products](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products/)
- [APRA CPS 230 Operational Risk Management](https://www.apra.gov.au/standards/cps-230)
- [Australian Government Guidance for AI Adoption](https://www.industry.gov.au/publications/guidance-ai-adoption)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
