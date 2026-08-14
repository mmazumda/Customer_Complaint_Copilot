# Model validation report (portfolio example)

## Executive conclusion

**Recommendation: conditional approval for a limited staff-only pilot after remediation.** The baseline is rejected because it fails critical privacy, security, operational, and human-oversight cases. The remediated candidate clears the small pre-registered demonstration suite, but that result is necessary rather than sufficient: production approval requires the conditions below and a materially larger test set with SME review.

## Scope and version

- System: SCB Complaint Response Copilot, fictional candidate v0.2
- Intended use: drafting assistance only
- Evidence: repository artefacts and synthetic deterministic suite
- Excluded: vendor penetration test, legal opinion, real-data PIA, production load test, accessibility user research, statistical validation at bank scale
- Validation date: August 2026 portfolio edition

## Result summary

The executable reports in `reports/baseline` and `reports/candidate` are the controlled evidence. The baseline is deliberately unsafe to demonstrate issue discovery; the candidate encodes expected control behaviour. It is not a claim about any commercial foundation model.

| Dimension | Baseline | Candidate | Interpretation |
|---|---:|---:|---|
| Privacy | Expected hard-gate failure | Expected pass | Full card/cross-customer disclosure is intolerable |
| Security | Expected hard-gate failure | Expected pass | Direct and indirect injection must fail safely |
| Grounding/conduct | Expected failure | Expected pass | Citation plus no outcome guarantee |
| Fairness | Expected cohort gap | Expected no observed gap | Tiny sample; qualitative and powered testing still required |
| Operational/human | Expected critical failures | Expected pass | Repository outage fails closed; no auto-send |

## Findings

### F-01 — Critical: unsafe disclosure and instruction following in baseline

The baseline repeats a full card number, discloses another synthetic customer's data, reveals internal instructions, and follows malicious retrieved text. Impact includes privacy, security, conduct and customer harm.

**Required remediation:** PII minimisation and DLP, tenant/access isolation, instruction/data separation, indirect-injection controls, safe refusal, restricted logs, security testing, and incident playbook.  
**Status:** candidate behaviour passes demonstration regression tests; design and operating effectiveness evidence remains required.

### F-02 — Critical: baseline bypasses human decision and communication controls

The baseline claims to send a response and promises redress. This violates the intended-use boundary and creates automation and conduct risk.

**Required remediation:** remove send permission, enforce authorised downstream workflow, filter decision/promissory language, display evidence, require trained review, and monitor edit/override patterns.  
**Status:** candidate passes demonstration tests; workflow penetration and human-factors study remain conditions.

### F-03 — High: unsupported and incorrect policy claims

The baseline invents response periods and does not consistently cite policy. A fluent response could be trusted despite being wrong.

**Required remediation:** approved corpus, version metadata, retrieval quality gates, sentence-level citation where feasible, claim verification, abstention on missing evidence, and stale-policy rollback.  
**Status:** candidate passes included tests; a larger SME-labelled grounding set is required.

### F-04 — High: unequal baseline service for communication cohorts

The baseline refuses non-standard or assistive communication while serving standard English. This produces a material observed cohort gap in the toy suite.

**Required remediation:** inclusive test design, plain-language standards, accessibility review, subgroup analysis, complaints feedback loop, and minimum performance per cohort—not only parity.  
**Status:** no observed candidate gap in three cases; sample is too small for assurance.

### F-05 — High: validation evidence is not production-scale

Twelve synthetic deterministic cases demonstrate process and tooling, not population performance, rare-event coverage, judge reliability, or control operation.

**Required remediation:** independently sourced representative set, risk-based sample justification, SME rubric and inter-rater agreement, confidence intervals, multi-turn tests, load/resilience testing, vendor evidence, and shadow pilot.  
**Status:** open release condition.

## Pilot conditions

1. Staff-only access; no customer-facing or auto-send capability.
2. No outcome, liability, advice, redress calculation, or redress approval.
3. Approved policy corpus with owner, effective dates, lineage, and rollback.
4. Privacy, security, legal/compliance, complaints, accessibility, and operational-risk sign-offs.
5. Vendor data-retention/training settings and material-service-provider assessment evidenced.
6. Larger independent benchmark and severe-but-plausible resilience tests pass.
7. Human-review training and measured review effectiveness meet approved thresholds.
8. Monitoring, alerting, kill switch, manual fallback, incident response, and change control are live.
9. Pilot cap and duration are enforced; adverse customer outcome triggers suspension.
10. Residual risk is accepted by the authorised accountable executive.

## Limitations and non-reliance statement

Rules based on required words are transparent and reproducible but do not measure semantic truth, empathy, legal adequacy, or all forms of leakage. A real program combines deterministic checks, retrieval metrics, security tools, human SME scoring, calibrated model-assisted evaluation, operational testing, and production outcome monitoring.

