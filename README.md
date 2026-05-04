# SOC 2 + NIST CSF Compliance Gap Analysis

A structured compliance gap analysis framework for embedded hardware
companies preparing for SOC 2 Type II audit, mapped to NIST CSF 2.0.

Built by Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University

---

## What This Project Is

![SOC 2 Compliance Gap Analysis Demo](demo.gif)

This project simulates the compliance gap analysis process that a GRC
analyst would perform for an embedded hardware company preparing for a
SOC 2 Type II audit.

It evaluates security controls across the five SOC 2 Trust Service
Criteria — Security, Availability, Confidentiality, Processing
Integrity, and Privacy — and maps each control to NIST CSF 2.0.

Each control is assessed as Fully Met, Partially Met, Not Met, or
Not Applicable, with a remediation priority and effort estimate
for closing identified gaps.

---

## Repository Structure

| Folder | Contents |
|---|---|
| `gap-analysis/` | SOC 2 control gap analysis mapped to NIST CSF 2.0 |
| `remediation-roadmap/` | Prioritized remediation plan for identified gaps |
| `compliance-dashboard/` | Auto-generated HTML compliance dashboard |
| `docs/` | Documentation and usage guide |

---

## SOC 2 Trust Service Criteria Covered

| Criteria | Description |
|---|---|
| CC — Common Criteria (Security) | Core security controls covering access, risk, and monitoring |
| A — Availability | System availability and performance monitoring |
| C — Confidentiality | Protection of confidential information |
| PI — Processing Integrity | Complete and accurate data processing |
| P — Privacy | Collection and use of personal information |

---

## Frameworks Used

- SOC 2 Trust Service Criteria (AICPA)
- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001:2022
- NIST SP 800-82 Rev 3 — Guide to OT/ICS Security

---

## Industry Application

This gap analysis framework is applicable to any embedded hardware
company preparing for SOC 2 Type II audit — including smart building
automation, medical device, industrial control, and IoT platform
manufacturers.

---

## Author

**Mckintosh Mpumelelo Moyo**
MS Cybersecurity — Yeshiva University, Katz School of Science and Health
[LinkedIn](https://www.linkedin.com/in/mckintosh-moyo)

### Related Projects
- [Project 1 — Hardware Security Assessment Framework](https://github.com/mckintosh-moyo/embedded-hardware-security-assessment)
- [Project 2 — Embedded Systems STRIDE Threat Model](https://github.com/mckintosh-moyo/embedded-stride-threat-model)
- [Project 3 — Hardware Security Policy Library](https://github.com/mckintosh-moyo/hardware-security-policy-library)
- [Project 4 — Hardware CVE Tracker](https://github.com/mckintosh-moyo/hardware-cve-tracker)