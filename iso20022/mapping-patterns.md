# ISO 20022 Mapping Patterns  
*Placeholder File — Authored by Neeraj Aggarwal*

This file will include mapping rules, transformation logic, and semantic enrichment patterns.

# ISO 20022 Mapping Patterns  
### Authored by Neeraj Aggarwal  
### Infosys Topaz COE • State Street Senior Program Manager

## 1. Overview
ISO 20022 introduces structured, semantically rich financial messages that require precise mapping from legacy formats (ACH, Fedwire, SWIFT MT, proprietary bank formats).  
This document provides canonical mapping patterns, transformation rules, and semantic alignment strategies for enterprise payment systems.

## 2. Mapping Principles

### 2.1 Canonical First
All legacy formats must map into a **canonical payment object** before ISO 20022 transformation.

### 2.2 Semantic Preservation
Mappings must preserve:
- Business intent  
- Regulatory meaning  
- Customer context  
- Transaction semantics  

### 2.3 Lossless Transformation
No critical data should be lost when converting from legacy formats to ISO 20022.

### 2.4 Rail‑Specific Extensions
Each rail may require:
- Additional fields  
- Conditional elements  
- Local regulatory attributes  

## 3. Common Mapping Patterns

### Pattern 1 — Flat → Structured
Legacy flat files (e.g., NACHA) map into nested ISO 20022 structures.

### Pattern 2 — Code → Meaning
Legacy codes (e.g., reason codes, transaction types) map to ISO 20022 enumerations.

### Pattern 3 — Free‑Text → Structured Fields
Unstructured remittance data is parsed into:
- `<RmtInf>`  
- `<Ustrd>`  
- `<Strd>`  

### Pattern 4 — Multi‑Field Consolidation
Multiple legacy fields combine into a single ISO 20022 element.

### Pattern 5 — Conditional Expansion
ISO 20022 requires fields that legacy formats do not provide; these must be enriched.

## 4. Mapping Example (Simplified)

Legacy (ACH):
- SEC Code  
- Company Entry Description  
- Addenda Record  

ISO 20022:
- `<PmtTpInf>`  
- `<CtgyPurp>`  
- `<RmtInf>`  

## 5. Validation Requirements
- Mandatory field checks  
- Semantic consistency  
- Rail‑specific constraints  
- Regulatory compliance  

## 6. Output
A fully mapped, semantically correct ISO 20022 payment instruction ready for validation and execution.
