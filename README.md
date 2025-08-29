# g-oss-batch · Batch/ELT orchestration (Airflow + dbt + Great Expectations)

**Audience:** O&G CIOs/CTOs and analytics leaders  
**Goal:** Replace Control‑M/Autosys/Informatica batch with jobs‑as‑code and modern ELT.

---

## Executive summary
- **What it is:** **Airflow** schedules and monitors data jobs. **dbt** manages SQL transforms as versioned code. **Great Expectations (GE)** enforces data quality at critical gates.  
- **What it replaces:** Proprietary schedulers and GUI‑based ETL mapping tools.  
- **Outcomes:** Faster delivery, Git review of logic, automated tests, and clear lineage hooks.

## Where it fits
```
[CDC / Files] -> Iceberg (g-oss-core)
     |             |
     v             v
   Airflow ---> dbt models ---> Gold tables
        \--> GE DQ gates --> Fail fast with alerts
```
This module orchestrates transforms over `g-oss-core` tables.

## O&G use cases
- Daily production summaries; field variance checks.  
- Finance nightly loads (trial balance, control totals).  
- Data quality gates on critical volumes/pressures.

## What’s included
- Airflow (LocalExecutor) with example DAGs.  
- dbt project (Trino profile) with staging + mart models.  
- Great Expectations config and a sample checkpoint.

## Pilot SLOs
- **Pipeline success rate:** ≥ 99.5%.  
- **MTTR:** < 30 min (on‑call runbooks).  
- **Freshness (batch):** < 2h Phase 1, < 30m Phase 2.

## Security & compliance
- No secrets in repo; use Vault (`g-oss-security`).  
- Lineage to Marquez/OpenLineage (`g-oss-governance`).  
- Access via SSO/OIDC (Keycloak).

## Cost model
- Primarily compute for dbt/SQL; Airflow control plane is light.  
- Significant savings from retiring GUI ETL licenses.

## Migration & rollout
1. Recreate top N mappings in **dbt** (refactor to SQL).  
2. Add **GE** tests for row counts, ranges, foreign keys.  
3. Orchestrate in **Airflow** with SLA/alerts; parallel‑run before cutover.

## KPIs for leadership
- Pipelines retired, failure rate/MTTR, freshness, % models with tests, cost per TB processed.

## Quick start
```bash
cp .env.example .env
docker compose up -d
# Airflow UI: http://localhost:8082
```
