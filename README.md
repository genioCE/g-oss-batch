# g-oss-batch

Batch/ELT: **Airflow + dbt + Great Expectations**.

## Run
```bash
cp .env.example .env
docker compose up -d
# create Airflow user
docker compose exec airflow bash -lc "airflow db upgrade && airflow users create --username $AIRFLOW_ADMIN_USER --password $AIRFLOW_ADMIN_PASSWORD --firstname Admin --lastname User --role Admin --email $AIRFLOW_ADMIN_EMAIL && airflow webserver -p 8080 & airflow scheduler & sleep 5"
```
Airflow: http://localhost:8082
