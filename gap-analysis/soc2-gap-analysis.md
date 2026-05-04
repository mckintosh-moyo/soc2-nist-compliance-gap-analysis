# SOC 2 + NIST CSF Compliance Gap Analysis
# Company: Fictional Embedded Hardware Manufacturer
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Date: May 2026
# Status Key: FM = Fully Met | PM = Partially Met | NM = Not Met | NA = Not Applicable

---

## How to Use This Document

For each control assess the current status and document:
- Current State: What is in place today
- Gap: What is missing
- Priority: Critical / High / Medium / Low
- Effort: High / Medium / Low

---

## CATEGORY 1: Common Criteria — Logical and Physical Access (CC6)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| CC6.1 | Logical access security measures restrict access to information assets | PR.AA-05 | PM | Basic RBAC implemented but no least privilege enforcement. Service accounts overprivileged. | Implement least privilege roles. Remove excess permissions from service accounts. | Critical | Medium |
| CC6.2 | Prior to issuing credentials new users are registered and authorized | PR.AA-01 | PM | User registration process exists but no formal approval workflow documented. | Implement formal access request and approval workflow. | High | Low |
| CC6.3 | Access is removed when no longer needed | PR.AA-01 | NM | No formal offboarding process. Former employee accounts not consistently disabled. | Implement automated account deprovisioning tied to HR system. | Critical | Medium |
| CC6.4 | Access credentials are reviewed periodically | PR.AA-05 | NM | No periodic access reviews conducted. No documented review cadence. | Implement quarterly access reviews with manager attestation. | Critical | Low |
| CC6.5 | Logical access controls restrict access to confidential data | PR.DS-01 | PM | Encryption at rest implemented for databases but inconsistent for file storage. | Apply encryption consistently across all confidential data stores. | High | Medium |
| CC6.6 | Logical access is restricted from outside the system boundaries | PR.AA-03 | NM | VPN not enforced for remote access. MFA not implemented for all users. | Enforce MFA for all accounts. Require VPN for all remote access. | Critical | Medium |
| CC6.7 | Transmission of confidential information is encrypted | PR.DS-02 | PM | HTTPS enforced for external APIs but some internal services use HTTP. | Enforce TLS 1.2 minimum for all internal and external communication. | High | Low |
| CC6.8 | Controls prevent unauthorized access to system components | PR.PS-01 | PM | Baseline hardening applied to servers but not consistently to embedded devices. | Apply CIS hardening benchmarks to all embedded hardware platforms. | High | High |

---

## CATEGORY 2: Common Criteria — System Operations (CC7)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| CC7.1 | Vulnerability management detects and monitors for new vulnerabilities | DE.CM-08 | NM | No formal vulnerability management program. CVEs not tracked for embedded components. | Implement CVE tracking and vulnerability management program for all components. | Critical | Medium |
| CC7.2 | System monitors for anomalies and indicators of compromise | DE.CM-01 | NM | No SIEM deployed. Limited logging on embedded devices. No alerting configured. | Deploy SIEM. Enable comprehensive logging. Configure alert rules. | Critical | High |
| CC7.3 | Evaluated security events are communicated to appropriate personnel | DE.AE-02 | NM | No incident escalation process documented. Security alerts not consistently reviewed. | Document and implement incident escalation procedures with defined SLAs. | High | Low |
| CC7.4 | Security incidents are identified and responded to | RS.MA-01 | PM | General IT incident response plan exists but no hardware-specific procedures. | Develop hardware-specific incident response playbooks. | High | Medium |
| CC7.5 | Incident response is evaluated and improvements are made | RC.IM-01 | NM | No post-incident review process. Lessons learned not documented or applied. | Implement post-incident review process with documented lessons learned. | Medium | Low |

---

## CATEGORY 3: Common Criteria — Change Management (CC8)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| CC8.1 | Changes to infrastructure are authorized and managed | PR.PS-01 | NM | No formal change management process. Infrastructure changes made ad-hoc. | Implement formal change management process with approval workflows. | Critical | Medium |
| CC8.2 | Emergency changes are authorized and documented | PR.PS-01 | NM | No emergency change process. Emergency changes undocumented. | Define and implement emergency change procedures. | High | Low |

---

## CATEGORY 4: Common Criteria — Risk Management (CC9)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| CC9.1 | Risk assessment process identifies threats and vulnerabilities | ID.RA-01 | PM | Annual risk assessment conducted but does not cover embedded hardware specifically. | Extend risk assessment to include embedded hardware threat modeling. | High | Medium |
| CC9.2 | Risk mitigation activities are implemented | ID.RA-06 | PM | Some risks mitigated but no formal risk register maintained. | Implement and maintain formal risk register with tracking. | High | Low |

---

## CATEGORY 5: Availability (A1)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| A1.1 | Availability commitments are communicated to users | GV.OC-01 | FM | SLAs defined and communicated to customers in contracts. | None — fully met. | — | — |
| A1.2 | System performance is monitored | DE.CM-09 | PM | Basic uptime monitoring in place but no capacity planning process. | Implement capacity planning and performance trend analysis. | Medium | Medium |
| A1.3 | Recovery plan is tested | RC.RP-01 | NM | DR plan documented but never tested. No evidence of recovery testing. | Conduct annual DR test and document results as audit evidence. | Critical | High |

---

## CATEGORY 6: Confidentiality (C1)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| C1.1 | Confidential information is identified and classified | ID.AM-05 | NM | No data classification policy. Confidential data not consistently labeled. | Implement data classification policy and labeling procedures. | High | Medium |
| C1.2 | Confidential information is protected during disposal | PR.DS-03 | NM | No secure disposal procedures for hardware containing confidential data. | Implement secure hardware disposal and data destruction procedures. | High | Low |

---

## CATEGORY 7: Processing Integrity (PI1)

| Control ID | SOC 2 Control | NIST CSF | Status | Current State | Gap | Priority | Effort |
|---|---|---|---|---|---|---|---|
| PI1.1 | Processing is complete accurate and timely | PR.DS-10 | PM | Basic input validation in place but no end-to-end integrity verification. | Implement cryptographic integrity verification for all data processing pipelines. | Medium | High |
| PI1.2 | Processing errors are identified and corrected | RS.AN-03 | PM | Error logging exists but no formal error review process. | Implement formal error review and correction process with documentation. | Medium | Low |

---

## Gap Analysis Summary

| Category | Total Controls | Fully Met | Partially Met | Not Met | Not Applicable |
|---|---|---|---|---|---|
| Logical and Physical Access (CC6) | 8 | 0 | 4 | 4 | 0 |
| System Operations (CC7) | 5 | 0 | 1 | 4 | 0 |
| Change Management (CC8) | 2 | 0 | 0 | 2 | 0 |
| Risk Management (CC9) | 2 | 0 | 2 | 0 | 0 |
| Availability (A1) | 3 | 1 | 1 | 1 | 0 |
| Confidentiality (C1) | 2 | 0 | 0 | 2 | 0 |
| Processing Integrity (PI1) | 2 | 0 | 2 | 0 | 0 |
| **TOTAL** | **24** | **1** | **10** | **13** | **0** |

---

## Overall Compliance Score

| Metric | Value |
|---|---|
| Total Controls | 24 |
| Fully Met | 1 (4%) |
| Partially Met | 10 (42%) |
| Not Met | 13 (54%) |
| Overall Readiness | NOT READY FOR AUDIT |
| Recommended Action | Complete Critical and High remediation before scheduling audit |