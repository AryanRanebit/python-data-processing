# ⚙️ Day 4: Apache Airflow & Directed Acyclic Graph (DAG) ETL Orchestration

## 📌 Problem Overview & Objective
This assignment focuses on workflow management and automated ETL pipeline orchestration using **Apache Airflow**:
1. **DAG Definition**: Configuring workflow metadata, default retry policies, and daily schedules using `airflow.DAG`.
2. **Task Declarations**: Setting up sequential processing anchors:
   - `start_pipeline`: `EmptyOperator` initial anchor.
   - `run_extraction_script`: `BashOperator` executing external Python data extraction (`scripts/data_extraction.py`).
   - `log_pipeline_success`: `BashOperator` logging execution timestamp and success metrics.
3. **Dependency Graph**: Defining linear execution flow via Bitshift Operators (`>>`).

---

## ⚙️ Key Concepts

### 1. Directed Acyclic Graph (DAG) Architecture
$$\text{start\_pipeline} \longrightarrow \text{run\_extraction\_script} \longrightarrow \text{log\_pipeline\_success}$$

### 2. Task Dependency Flow (Bitshift Operator)
```python
start_pipeline >> execute_extraction >> pipeline_complete
```

---

## 🚀 Execution & Usage

```bash
pip install -r requirements.txt
# Place DAG script inside your Airflow DAGs directory:
# ~/airflow/dags/data_pipeline_dag.py
```
