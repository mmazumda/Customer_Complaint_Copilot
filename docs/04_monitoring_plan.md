# Monitoring, incidents and revalidation

## Production control loop

| Signal | Example measure | Illustrative trigger | Owner/action |
|---|---|---|---|
| Grounding | unsupported-claim and valid-citation rate from sampled drafts | Any critical unsupported claim or downward trend | Product owner pauses affected flow; Model Risk investigates |
| Privacy | DLP block and confirmed leakage count | Any confirmed personal-data leakage | Kill switch; privacy/security incident process |
| Security | direct/indirect injection success | Any critical attack success | Suspend; Security triage and regression test |
| Conduct | promises, advice, decision language | Any sent harmful communication; repeated blocked drafts | Complaints/Compliance review |
| Fairness | pass/outcome/edit rates by approved cohorts | Gap beyond approved limit or low absolute performance | Fairness/accessibility investigation |
| Human oversight | acceptance, edit distance, review time, override and error escape | Evidence of rubber-stamping or review below threshold | Retrain, redesign, or suspend |
| Retrieval/data | zero-result, stale source, conflicting source, policy freshness | Expired policy or corpus reconciliation failure | Fail closed; corpus owner remediates |
| Operations | latency, availability, fallback activation, recovery | Service tolerance breach | Manual fallback and CPS 230 process |
| Vendor/change | model/version/terms/subprocessor change | Unapproved material change | Block deployment; change assessment/revalidation |
| Customer outcome | complaint reopen, escalation, correction and detriment | Severe event or adverse trend | Incident review and possible restitution process |

Thresholds must be set from risk appetite, pilot observations, legal/compliance input, and statistically credible baselines. The examples above are intentionally conservative, not universal bank policy.

## Cadence

- Real time: security, DLP, service health, kill switch.
- Daily during pilot: critical control alerts and customer-impact review.
- Weekly during pilot: case sampling, cohort analysis, human-review performance, incidents.
- Monthly after stabilisation: risk dashboard to accountable owners.
- Quarterly or risk-based: independent sample review and control-effectiveness testing.

## Revalidation triggers

Revalidate before or immediately after, as policy permits:

- foundation model, provider, hosting region, quantisation, safety setting or material system-prompt change;
- embedding, chunking, reranker, corpus, filter, DLP, access, logging or downstream workflow change;
- new complaint type, customer cohort, channel, language, autonomy, or decision influence;
- material vendor/subprocessor/contract change;
- threshold breach, severe incident, unexpected harm, drift, or repeated overrides;
- regulatory or policy change; or
- scheduled annual review for a high-risk use case, with frequency adjusted by risk.

## Incident evidence

Preserve configuration/version, retrieved passages, redacted inputs/outputs, timestamps, user and access context, control decisions, downstream action, customer impact, and remediation. Respect data minimisation and legal privilege. Link incidents to root cause, affected population, look-back, notification assessment, rollback, and regression tests.

## Change decision

Classify changes as non-material, material, or new use. Product owners propose the class with evidence; independent risk/validation challenges it. Bundling many “small” changes must not be used to evade revalidation.

