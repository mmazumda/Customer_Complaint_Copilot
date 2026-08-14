# Independent validation plan and correct sequence

## Objective

Provide evidence on whether the SCB complaint copilot is conceptually sound, implemented as designed, and effective within its narrow intended use. Validation covers the system and its use, not an impossible claim that the general-purpose model is universally “valid.”

## Sequence and rationale

### Phase 0 — Commissioning and independence

Record the sponsor, decision required, validator independence, system version, evidence cut-off, SMEs, conflicts, and issue-rating method. Freeze the candidate configuration before final testing.

**Deliverable:** validation mandate and evidence request.  
**Why first:** prevents scope drift and selective presentation of favourable results.

### Phase 1 — Use-case framing and risk classification

Document intended users, affected people, decisions influenced, prohibited uses, foreseeable misuse, harm pathways, criticality, and risk tier. Identify relevant obligations with Legal and Compliance; do not present the crosswalk as legal advice.

**Exit criterion:** accountable owners approve the use statement and boundaries.

### Phase 2 — System, data and vendor understanding

Trace inputs through minimisation, prompts, retrieval, model, filtering, human review, logging, and downstream action. Capture model/version, hosting, retention, training-on-input setting, policy corpus lineage, access, subcontractors, service levels, change notice, audit rights, concentration risk, and exit strategy.

**Exit criterion:** end-to-end inventory reconciles to deployed configuration.

### Phase 3 — Conceptual-soundness review

Challenge whether GenAI is necessary; whether a deterministic template would be safer; whether RAG and abstention suit the task; and whether limitations and human factors are understood. Review threat model, privacy impact assessment, model/system cards, prompt design, retrieval evaluation, safety controls, and manual fallback.

**Exit criterion:** no unresolved conceptual defect that makes testing meaningless.

### Phase 4 — Pre-register acceptance criteria

Before viewing final outcomes, approve hard gates in `config/acceptance_criteria.json`. Critical privacy, security, conduct, and human-oversight tests require 100% pass. Aggregate quality cannot compensate for one severe failure. Specify confidence intervals and larger sample sizes for a real validation.

**Exit criterion:** thresholds, sample rationale, and exception authority are signed off.

### Phase 5 — Test design

Construct independently controlled datasets:

- normal and boundary complaints;
- grounded factual questions and unanswerable questions;
- direct and indirect prompt injection;
- PII leakage, memorisation canaries, and cross-customer access;
- prohibited decisions, redress promises, and financial advice;
- standard, non-standard, and assistive communication cohorts;
- long context, conflicting policies, stale policies, and retrieval outage;
- load, latency, vendor outage, rollback, and manual fallback;
- human factors: review accuracy, automation bias, overrides, and time pressure.

The 12 included cases are a minimal executable demonstration, not a statistically sufficient bank validation.

### Phase 6 — Execute and reproduce

Run the locked baseline and candidate with recorded versions/seeds where supported. Retain case-level outputs, scores, evaluator code, environment, timestamps, and deviations. Use deterministic rules for unambiguous controls and blinded SME review for contextual quality. Calibrate any LLM judge against humans and test for position/style bias.

**Commands:**

```powershell
python -m unittest discover -s tests -v
python src/evaluate.py --variant baseline --output reports/baseline
python src/evaluate.py --variant candidate --output reports/candidate
```

### Phase 7 — Analyse, rate findings, and retest

Perform root-cause analysis by component and cohort. Rate each finding by impact, likelihood, detectability, control strength, and exposure. Assign owner and due date. Retest the exact failure, neighbouring behaviours, and regression suite; never close an issue from a screenshot or developer assertion alone.

### Phase 8 — Decision and conditions

Recommend reject, remediate/retest, constrained pilot, or approve. State limitations and residual risk. The accountable authority—not the validator—approves risk acceptance. Pilot constraints should be technically enforced.

### Phase 9 — Production monitoring and revalidation

Monitor model, retrieval, control, cohort, operational, vendor, and human-review signals. Establish alert limits, owners, escalation, rollback, periodic sampling, incident linkage, and revalidation triggers before pilot launch.

## Evidence request checklist

- Approved use case, risk assessment, RACI, AI/model inventory record
- Architecture and data-flow diagrams; prompt/retrieval/filter configurations
- Model/system cards, benchmark limitations, red-team and security evidence
- Data lineage, quality, representativeness, privacy impact assessment
- Vendor due diligence, contracts, subprocessors, retention, residency and exit plan
- Policy corpus approval/version history and retrieval evaluation
- UAT, performance, resilience, BCP/fallback and access-control tests
- Human-review design, training, competency and quality-assurance evidence
- Monitoring dashboard specification, incident process and change policy

## Regulatory and good-practice mapping

| Source | Practical translation in this project |
|---|---|
| ASIC REP 798 | Governance keeps pace with use; consumer risk and third-party due diligence are explicit |
| OAIC AI privacy guidance | Privacy by design, due diligence, transparency, accuracy, human oversight, PIA and lifecycle review |
| APRA CPS/CPG 230 | Operational-risk profile, control design/effectiveness, scenario analysis, service-provider risk, continuity and remediation |
| Australian Guidance for AI Adoption | Accountability, risk management, data governance, testing, transparency, monitoring and stakeholder control |
| NIST AI RMF GenAI Profile | Govern–Map–Measure–Manage structure and GenAI-specific risk treatment |

This is a practice crosswalk, not a statement that passing these tests proves compliance.

