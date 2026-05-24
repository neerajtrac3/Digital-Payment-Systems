# ISO 20022 Validation Rules  
*Placeholder File — Authored by Neeraj Aggarwal*

This file will document validation logic, schema rules, and compliance checks.

# ISO 20022 Validation Rules  
### Authored by Neeraj Aggarwal  
### Infosys Topaz COE • State Street Senior Program Manager

## 1. Overview
ISO 20022 validation ensures that payment messages are structurally correct, semantically meaningful, and compliant with regulatory and rail‑specific requirements.  
This document defines the multi‑layer validation model used in enterprise payment systems.

## 2. Validation Layers

### 2.1 Structural Validation
Ensures message integrity:
- XML schema validation  
- Mandatory element checks  
- Data type enforcement  
- Length and format rules  

### 2.2 Semantic Validation
Ensures business correctness:
- Field‑to‑field consistency  
- Currency and amount alignment  
- Creditor/debtor role validation  
- Purpose code correctness  

### 2.3 Rail‑Specific Validation
Examples:
- RTP: immediate posting rules  
- FedNow: liquidity checks  
- Wires: cutoff windows  
- Cross‑border: corridor restrictions  

### 2.4 Regulatory Validation
Includes:
- Sanctions  
- AML  
- KYC  
- Travel rule compliance  

### 2.5 AI‑Driven Validation (AIDV Integration)
Enhances validation with:
- Behavioral anomaly detection  
- Contextual enrichment  
- Predictive exception identification  
- Explainability for auditors  

## 3. Common Validation Rules

### Rule 1 — Amount > 0  
### Rule 2 — Currency must match corridor  
### Rule 3 — Debtor and creditor cannot be identical  
### Rule 4 — Purpose code required for cross‑border  
### Rule 5 — Structured remittance required for RTP  

## 4. Validation Outcomes
- **Pass** → Ready for orchestration  
- **Fail** → Exception workflow triggered  
- **Enriched** → AI‑driven repair suggestions  

## 5. Evidence Generation
All validation outcomes must be logged in the **Enterprise Evidence Fabric** for audit and regulatory review.
