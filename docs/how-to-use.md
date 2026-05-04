# How to Use the SOC 2 + NIST CSF Compliance Gap Analysis

## What This Project Contains

| File | Description |
|---|---|
| gap-analysis/soc2-gap-analysis.md | Full gap analysis of 24 SOC 2 controls |
| remediation-roadmap/remediation-roadmap.md | Prioritized remediation plan |
| compliance-dashboard/soc2-compliance-dashboard.html | HTML compliance dashboard |
| compliance_dashboard_generator.py | Python script to regenerate dashboard |

---

## Running the Dashboard Generator

1. Open Command Prompt
2. Navigate to the project folder
3. Run: python compliance_dashboard_generator.py
4. Open compliance-dashboard/soc2-compliance-dashboard.html in browser

---

## How to Adapt This for a Real Company

1. Open gap-analysis/soc2-gap-analysis.md
2. Update the Status column for each control based on actual assessment
3. Update Current State and Gap columns with real findings
4. Run the dashboard generator to refresh the HTML report
5. Use the remediation roadmap to track remediation progress

---

## Status Key

| Code | Meaning |
|---|---|
| FM | Fully Met — control is fully implemented |
| PM | Partially Met — control is partially implemented |
| NM | Not Met — control is not implemented |
| NA | Not Applicable — control does not apply |

---

## Frameworks Referenced

- SOC 2 Trust Service Criteria — aicpa.org
- NIST CSF 2.0 — nvlpubs.nist.gov
- ISO/IEC 27001:2022
- NIST SP 800-82 Rev 3