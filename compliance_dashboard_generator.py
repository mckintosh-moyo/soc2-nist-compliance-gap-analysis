# SOC 2 + NIST CSF Compliance Dashboard Generator
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Description: Generates a color-coded HTML compliance dashboard
#              from the SOC 2 gap analysis findings

import datetime

# ── Gap analysis data ─────────────────────────────────────────────────────────
controls = [
    # CC6 - Logical and Physical Access
    {"id": "CC6.1", "category": "Logical Access (CC6)", "control": "Logical access security measures restrict access", "nist": "PR.AA-05", "status": "PM", "priority": "Critical", "effort": "Medium", "gap": "Service accounts overprivileged. No least privilege enforcement.", "action": "Implement least privilege roles. Remove excess permissions."},
    {"id": "CC6.2", "category": "Logical Access (CC6)", "control": "New users are registered and authorized before credentials issued", "nist": "PR.AA-01", "status": "PM", "priority": "High", "effort": "Low", "gap": "No formal access approval workflow documented.", "action": "Implement formal access request and approval workflow."},
    {"id": "CC6.3", "category": "Logical Access (CC6)", "control": "Access is removed when no longer needed", "nist": "PR.AA-01", "status": "NM", "priority": "Critical", "effort": "Medium", "gap": "No formal offboarding. Former employee accounts not disabled.", "action": "Implement automated account deprovisioning tied to HR system."},
    {"id": "CC6.4", "category": "Logical Access (CC6)", "control": "Access credentials are reviewed periodically", "nist": "PR.AA-05", "status": "NM", "priority": "Critical", "effort": "Low", "gap": "No periodic access reviews conducted.", "action": "Implement quarterly access reviews with manager attestation."},
    {"id": "CC6.5", "category": "Logical Access (CC6)", "control": "Logical access controls restrict access to confidential data", "nist": "PR.DS-01", "status": "PM", "priority": "High", "effort": "Medium", "gap": "Encryption inconsistent across all data stores.", "action": "Apply encryption consistently across all confidential data stores."},
    {"id": "CC6.6", "category": "Logical Access (CC6)", "control": "Logical access is restricted from outside system boundaries", "nist": "PR.AA-03", "status": "NM", "priority": "Critical", "effort": "Medium", "gap": "VPN not enforced. MFA not implemented for all users.", "action": "Enforce MFA for all accounts. Require VPN for remote access."},
    {"id": "CC6.7", "category": "Logical Access (CC6)", "control": "Transmission of confidential information is encrypted", "nist": "PR.DS-02", "status": "PM", "priority": "High", "effort": "Low", "gap": "Some internal services use unencrypted HTTP.", "action": "Enforce TLS 1.2 minimum for all communication."},
    {"id": "CC6.8", "category": "Logical Access (CC6)", "control": "Controls prevent unauthorized access to system components", "nist": "PR.PS-01", "status": "PM", "priority": "High", "effort": "High", "gap": "Hardening not consistently applied to embedded devices.", "action": "Apply CIS hardening benchmarks to all embedded platforms."},
    # CC7 - System Operations
    {"id": "CC7.1", "category": "System Operations (CC7)", "control": "Vulnerability management detects new vulnerabilities", "nist": "DE.CM-08", "status": "NM", "priority": "Critical", "effort": "Medium", "gap": "No formal vulnerability management program.", "action": "Implement CVE tracking and vulnerability management program."},
    {"id": "CC7.2", "category": "System Operations (CC7)", "control": "System monitors for anomalies and indicators of compromise", "nist": "DE.CM-01", "status": "NM", "priority": "Critical", "effort": "High", "gap": "No SIEM deployed. Limited logging. No alerting.", "action": "Deploy SIEM. Enable logging. Configure alert rules."},
    {"id": "CC7.3", "category": "System Operations (CC7)", "control": "Security events are communicated to appropriate personnel", "nist": "DE.AE-02", "status": "NM", "priority": "High", "effort": "Low", "gap": "No incident escalation process documented.", "action": "Document incident escalation procedures with defined SLAs."},
    {"id": "CC7.4", "category": "System Operations (CC7)", "control": "Security incidents are identified and responded to", "nist": "RS.MA-01", "status": "PM", "priority": "High", "effort": "Medium", "gap": "No hardware-specific incident response procedures.", "action": "Develop hardware-specific incident response playbooks."},
    {"id": "CC7.5", "category": "System Operations (CC7)", "control": "Incident response is evaluated and improvements made", "nist": "RC.IM-01", "status": "NM", "priority": "Medium", "effort": "Low", "gap": "No post-incident review process.", "action": "Implement post-incident review with documented lessons learned."},
    # CC8 - Change Management
    {"id": "CC8.1", "category": "Change Management (CC8)", "control": "Changes to infrastructure are authorized and managed", "nist": "PR.PS-01", "status": "NM", "priority": "Critical", "effort": "Medium", "gap": "No formal change management process.", "action": "Implement formal change management with approval workflows."},
    {"id": "CC8.2", "category": "Change Management (CC8)", "control": "Emergency changes are authorized and documented", "nist": "PR.PS-01", "status": "NM", "priority": "High", "effort": "Low", "gap": "No emergency change process or documentation.", "action": "Define and implement emergency change procedures."},
    # CC9 - Risk Management
    {"id": "CC9.1", "category": "Risk Management (CC9)", "control": "Risk assessment identifies threats and vulnerabilities", "nist": "ID.RA-01", "status": "PM", "priority": "High", "effort": "Medium", "gap": "Risk assessment does not cover embedded hardware.", "action": "Extend risk assessment to include hardware threat modeling."},
    {"id": "CC9.2", "category": "Risk Management (CC9)", "control": "Risk mitigation activities are implemented", "nist": "ID.RA-06", "status": "PM", "priority": "High", "effort": "Low", "gap": "No formal risk register maintained.", "action": "Implement and maintain formal risk register with tracking."},
    # A1 - Availability
    {"id": "A1.1", "category": "Availability (A1)", "control": "Availability commitments are communicated to users", "nist": "GV.OC-01", "status": "FM", "priority": "—", "effort": "—", "gap": "None — fully met.", "action": "No action required."},
    {"id": "A1.2", "category": "Availability (A1)", "control": "System performance is monitored", "nist": "DE.CM-09", "status": "PM", "priority": "Medium", "effort": "Medium", "gap": "No capacity planning process.", "action": "Implement capacity planning and performance trend analysis."},
    {"id": "A1.3", "category": "Availability (A1)", "control": "Recovery plan is tested", "nist": "RC.RP-01", "status": "NM", "priority": "Critical", "effort": "High", "gap": "DR plan never tested. No evidence of recovery testing.", "action": "Conduct annual DR test and document results as audit evidence."},
    # C1 - Confidentiality
    {"id": "C1.1", "category": "Confidentiality (C1)", "control": "Confidential information is identified and classified", "nist": "ID.AM-05", "status": "NM", "priority": "High", "effort": "Medium", "gap": "No data classification policy.", "action": "Implement data classification policy and labeling procedures."},
    {"id": "C1.2", "category": "Confidentiality (C1)", "control": "Confidential information is protected during disposal", "nist": "PR.DS-03", "status": "NM", "priority": "High", "effort": "Low", "gap": "No secure disposal procedures for hardware.", "action": "Implement secure hardware disposal and data destruction procedures."},
    # PI1 - Processing Integrity
    {"id": "PI1.1", "category": "Processing Integrity (PI1)", "control": "Processing is complete accurate and timely", "nist": "PR.DS-10", "status": "PM", "priority": "Medium", "effort": "High", "gap": "No end-to-end integrity verification.", "action": "Implement cryptographic integrity verification for data pipelines."},
    {"id": "PI1.2", "category": "Processing Integrity (PI1)", "control": "Processing errors are identified and corrected", "nist": "RS.AN-03", "status": "PM", "priority": "Medium", "effort": "Low", "gap": "No formal error review process.", "action": "Implement formal error review and correction process."},
]

# ── Helper functions ──────────────────────────────────────────────────────────
def get_status_color(status):
    return {
        "FM": "#44bb44",
        "PM": "#ff8800",
        "NM": "#ff4444",
        "NA": "#888888"
    }.get(status, "#888888")

def get_status_label(status):
    return {
        "FM": "Fully Met",
        "PM": "Partially Met",
        "NM": "Not Met",
        "NA": "N/A"
    }.get(status, "Unknown")

def get_priority_color(priority):
    return {
        "Critical": "#ff4444",
        "High":     "#ff8800",
        "Medium":   "#ccaa00",
        "Low":      "#44bb44",
        "—":        "#888888"
    }.get(priority, "#888888")

# ── Count statuses ────────────────────────────────────────────────────────────
counts = {"FM": 0, "PM": 0, "NM": 0, "NA": 0}
for c in controls:
    counts[c["status"]] += 1

total = len(controls)
readiness = round((counts["FM"] + counts["PM"] * 0.5) / total * 100)

# ── Category breakdown ────────────────────────────────────────────────────────
categories = {}
for c in controls:
    cat = c["category"]
    if cat not in categories:
        categories[cat] = {"FM": 0, "PM": 0, "NM": 0, "NA": 0, "total": 0}
    categories[cat][c["status"]] += 1
    categories[cat]["total"] += 1

date_str = datetime.datetime.now().strftime("%B %d, %Y")

# ── Generate HTML ─────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOC 2 Compliance Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px; background: #f5f5f5; color: #333;
        }}
        h1 {{ color: #1B3A6B; border-bottom: 3px solid #1B3A6B; padding-bottom: 10px; }}
        h2 {{ color: #2E75B6; margin-top: 30px; }}
        .meta {{
            background: #1B3A6B; color: white;
            padding: 15px 20px; border-radius: 6px; margin-bottom: 25px;
        }}
        .meta p {{ margin: 4px 0; }}
        .grid4 {{
            display: grid; grid-template-columns: repeat(4, 1fr);
            gap: 15px; margin-bottom: 20px;
        }}
        .grid3 {{
            display: grid; grid-template-columns: repeat(3, 1fr);
            gap: 15px; margin-bottom: 30px;
        }}
        .card {{
            padding: 20px; border-radius: 8px;
            text-align: center; color: white; font-weight: bold;
        }}
        .card .number {{ font-size: 2.5em; display: block; }}
        .readiness-bar {{
            background: #ddd; border-radius: 10px;
            height: 30px; margin: 10px 0; overflow: hidden;
        }}
        .readiness-fill {{
            height: 100%; border-radius: 10px;
            background: linear-gradient(90deg, #ff4444, #ff8800, #44bb44);
            display: flex; align-items: center;
            justify-content: center; color: white;
            font-weight: bold; font-size: 0.9em;
        }}
        .cat-grid {{
            display: grid; grid-template-columns: repeat(3, 1fr);
            gap: 15px; margin-bottom: 30px;
        }}
        .cat-card {{
            background: white; border-radius: 8px;
            padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .cat-card h4 {{
            margin: 0 0 10px 0; color: #1B3A6B; font-size: 0.9em;
        }}
        .cat-bar {{
            display: flex; height: 12px; border-radius: 6px;
            overflow: hidden; margin-bottom: 6px;
        }}
        table {{
            width: 100%; border-collapse: collapse;
            background: white; border-radius: 8px;
            overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        th {{
            background: #1B3A6B; color: white;
            padding: 12px 15px; text-align: left; font-size: 0.88em;
        }}
        td {{
            padding: 10px 15px; border-bottom: 1px solid #eee;
            font-size: 0.83em;
        }}
        tr:last-child td {{ border-bottom: none; }}
        tr:hover td {{ background: #f9f9f9; }}
        .badge {{
            padding: 3px 8px; border-radius: 10px;
            color: white; font-weight: bold;
            font-size: 0.8em; display: inline-block;
        }}
        .footer {{
            margin-top: 40px; text-align: center;
            color: #888; font-size: 0.85em;
            border-top: 1px solid #ddd; padding-top: 15px;
        }}
    </style>
</head>
<body>
    <h1>SOC 2 + NIST CSF Compliance Dashboard</h1>
    <div class="meta">
        <p><strong>Author:</strong> Mckintosh Mpumelelo Moyo</p>
        <p><strong>Program:</strong> MS Cybersecurity — Yeshiva University, Katz School</p>
        <p><strong>Frameworks:</strong> SOC 2 Trust Service Criteria | NIST CSF 2.0</p>
        <p><strong>Generated:</strong> {date_str}</p>
        <p><strong>Total Controls:</strong> {total} | <strong>Audit Readiness:</strong> {readiness}%</p>
    </div>

    <h2>Overall Compliance Status</h2>
    <div class="grid4">
        <div class="card" style="background:#44bb44;">
            <span class="number">{counts['FM']}</span>Fully Met
        </div>
        <div class="card" style="background:#ff8800;">
            <span class="number">{counts['PM']}</span>Partially Met
        </div>
        <div class="card" style="background:#ff4444;">
            <span class="number">{counts['NM']}</span>Not Met
        </div>
        <div class="card" style="background:#888888;">
            <span class="number">{counts['NA']}</span>N/A
        </div>
    </div>

    <h2>Audit Readiness Score</h2>
    <div class="readiness-bar">
        <div class="readiness-fill" style="width:{readiness}%">
            {readiness}% Ready
        </div>
    </div>
    <p style="color:#888;font-size:0.85em">
        Score calculated as: (Fully Met + Partially Met x 0.5) / Total Controls
    </p>

    <h2>Compliance by Category</h2>
    <div class="cat-grid">
"""

for cat, data in categories.items():
    fm_pct = round(data['FM'] / data['total'] * 100)
    pm_pct = round(data['PM'] / data['total'] * 100)
    nm_pct = round(data['NM'] / data['total'] * 100)
    html += f"""
        <div class="cat-card">
            <h4>{cat}</h4>
            <div class="cat-bar">
                <div style="width:{fm_pct}%;background:#44bb44"></div>
                <div style="width:{pm_pct}%;background:#ff8800"></div>
                <div style="width:{nm_pct}%;background:#ff4444"></div>
            </div>
            <div style="font-size:0.8em;color:#666">
                FM: {data['FM']} | PM: {data['PM']} | NM: {data['NM']} | Total: {data['total']}
            </div>
        </div>
"""

html += """
    </div>

    <h2>Full Control Register</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Category</th>
                <th>Control</th>
                <th>NIST</th>
                <th>Status</th>
                <th>Priority</th>
                <th>Gap</th>
                <th>Action Required</th>
            </tr>
        </thead>
        <tbody>
"""

for c in controls:
    html += f"""
            <tr>
                <td><strong>{c['id']}</strong></td>
                <td style="font-size:0.82em">{c['category']}</td>
                <td style="max-width:180px">{c['control']}</td>
                <td><strong>{c['nist']}</strong></td>
                <td><span class="badge" style="background:{get_status_color(c['status'])}">{get_status_label(c['status'])}</span></td>
                <td><span class="badge" style="background:{get_priority_color(c['priority'])}">{c['priority']}</span></td>
                <td style="font-size:0.82em;max-width:180px">{c['gap']}</td>
                <td style="font-size:0.82em;max-width:180px">{c['action']}</td>
            </tr>
"""

html += f"""
        </tbody>
    </table>
    <div class="footer">
        <p>SOC 2 + NIST CSF Compliance Gap Analysis Dashboard</p>
        <p>Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University</p>
        <p>Frameworks: SOC 2 Trust Service Criteria | NIST CSF 2.0</p>
    </div>
</body>
</html>
"""

# ── Save dashboard ────────────────────────────────────────────────────────────
output_file = "compliance-dashboard/soc2-compliance-dashboard.html"
with open(output_file, "w") as f:
    f.write(html)

print("=" * 55)
print("  SOC 2 Compliance Dashboard — Generated!")
print("=" * 55)
print(f"  Date:           {date_str}")
print(f"  Total Controls: {total}")
print(f"  Fully Met:      {counts['FM']}")
print(f"  Partially Met:  {counts['PM']}")
print(f"  Not Met:        {counts['NM']}")
print(f"  Audit Readiness:{readiness}%")
print("=" * 55)
print(f"  Dashboard saved to: {output_file}")
print("=" * 55)