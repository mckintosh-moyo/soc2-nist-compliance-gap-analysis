# Compliance Remediation Roadmap
# Company: Fictional Embedded Hardware Manufacturer
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Date: May 2026
# Based on: SOC 2 + NIST CSF Gap Analysis findings

---

## Overview

This roadmap prioritizes remediation of the 13 Not Met and 10
Partially Met controls identified in the SOC 2 gap analysis.
Actions are sequenced across three horizons based on risk level
and effort required.

---

## HORIZON 1: Immediate — Critical Gaps (0-30 Days)

These items must be addressed before any other remediation work.
They represent the highest risk to the organization and would
result in immediate audit failure.

| Priority | Control | Action | Owner | Effort |
|---|---|---|---|---|
| 1 | CC6.3 — Account deprovisioning | Implement automated account deprovisioning tied to HR offboarding process. Audit all existing accounts and disable any belonging to former employees. | IT Security | Low |
| 2 | CC6.4 — Access reviews | Conduct immediate access review of all privileged accounts. Implement quarterly review cadence going forward with manager attestation. | IT Security | Low |
| 3 | CC6.6 — MFA enforcement | Enable MFA for all user accounts immediately. Enforce VPN for all remote access. | IT Security | Medium |
| 4 | CC7.1 — Vulnerability management | Implement CVE tracking program using NVD API. Establish triage SLAs: Critical 30 days, High 60 days. | Security Team | Medium |
| 5 | CC7.2 — SIEM and monitoring | Deploy SIEM solution. Enable comprehensive logging on all systems including embedded devices. Configure alert rules for critical events. | Security Team | High |
| 6 | CC8.1 — Change management | Implement formal change management process with documented approval workflows. All infrastructure changes must go through CAB review. | IT Operations | Medium |
| 7 | A1.3 — DR testing | Schedule and conduct DR test within 30 days. Document results as audit evidence. | IT Operations | High |

---

## HORIZON 2: Short Term — High Gaps (30-90 Days)

These items address significant control gaps that would result
in audit findings if not remediated before the audit.

| Priority | Control | Action | Owner | Effort |
|---|---|---|---|---|
| 8 | CC6.1 — Least privilege | Implement least privilege roles for all users and service accounts. Remove excess permissions identified in access review. | IT Security | Medium |
| 9 | CC6.2 — Access approval | Document and implement formal access request and approval workflow. | IT Security | Low |
| 10 | CC6.5 — Encryption at rest | Apply encryption consistently across all confidential data stores including file storage and embedded device memory. | Engineering | Medium |
| 11 | CC6.7 — Encryption in transit | Enforce TLS 1.2 minimum for all internal and external communication. Disable unencrypted protocols. | Engineering | Low |
| 12 | CC6.8 — System hardening | Apply CIS hardening benchmarks to all embedded hardware platforms. Document baseline configurations. | Engineering | High |
| 13 | CC7.3 — Incident escalation | Document and implement incident escalation procedures with defined SLAs for each severity level. | Security Team | Low |
| 14 | CC7.4 — IR playbooks | Develop hardware-specific incident response playbooks covering firmware compromise, physical tampering, and supply chain attacks. | Security Team | Medium |
| 15 | CC8.2 — Emergency changes | Define and implement emergency change procedures with post-implementation review requirements. | IT Operations | Low |
| 16 | CC9.1 — Risk assessment | Extend annual risk assessment to include embedded hardware threat modeling using STRIDE methodology. | Security Team | Medium |
| 17 | CC9.2 — Risk register | Implement and maintain formal risk register with owner assignment and remediation tracking. | Security Team | Low |
| 18 | C1.1 — Data classification | Implement data classification policy with four tiers: Public, Internal, Confidential, Restricted. | Security Team | Medium |
| 19 | C1.2 — Secure disposal | Implement secure hardware disposal and data destruction procedures with certificate of destruction. | IT Operations | Low |

---

## HORIZON 3: Strategic — Medium Gaps (90-180 Days)

These items complete the compliance program and address
longer-term strategic improvements.

| Priority | Control | Action | Owner | Effort |
|---|---|---|---|---|
| 20 | CC7.5 — Post incident review | Implement post-incident review process with documented lessons learned template. | Security Team | Low |
| 21 | A1.2 — Capacity planning | Implement capacity planning process with quarterly performance trend analysis. | IT Operations | Medium |
| 22 | PI1.1 — Processing integrity | Implement cryptographic integrity verification for all data processing pipelines. | Engineering | High |
| 23 | PI1.2 — Error review | Implement formal error review and correction process with documentation requirements. | Engineering | Low |

---

## Remediation Progress Tracker

| Horizon | Total Actions | Completed | In Progress | Not Started |
|---|---|---|---|---|
| Horizon 1 — Immediate (0-30 days) | 7 | 0 | 0 | 7 |
| Horizon 2 — Short Term (30-90 days) | 12 | 0 | 0 | 12 |
| Horizon 3 — Strategic (90-180 days) | 4 | 0 | 0 | 4 |
| **TOTAL** | **23** | **0** | **0** | **23** |

---

## Audit Readiness Criteria

The organization will be ready to schedule the SOC 2 Type II
audit when the following criteria are met:

- [ ] All Horizon 1 Critical items completed and evidenced
- [ ] All Horizon 2 High items completed and evidenced
- [ ] SIEM operational with minimum 90 days of log data
- [ ] Access reviews completed and documented
- [ ] DR test completed and documented
- [ ] Incident response playbooks tested through tabletop exercise
- [ ] All policies reviewed, approved, and distributed

---

## Evidence Requirements

For each remediated control the following evidence must be collected
and retained for the audit:

| Evidence Type | Examples |
|---|---|
| Policy documents | Written and approved policies with version history |
| Configuration screenshots | System settings showing controls are enabled |
| Access review records | Signed attestations from managers |
| Test results | DR test results, tabletop exercise outcomes |
| Training records | Security awareness training completion records |
| Vendor assessments | Third party security assessment reports |