from typing import List, Dict, Any
from google.cloud import bigquery

def query_bigquery(query: str, proj_id: str) -> List[Dict[str, Any]]:
    try:
        client = bigquery.Client(project=proj_id)
        query_job = client.query(query)
        return [dict(row) for row in query_job.result()]
    except Exception as e:
        return [{"error": f"BigQuery error: {e}"}]
