<div align="center">

# Rohit Shidid

**ML / MLOps Engineer · Systems Engineer**

I build production ML pipelines and the systems that keep them honest — honest evaluation, audited model-promotion gates, and feedback loops that make models visibly improve with new data.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-rohit--shidid-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/rohit-shidid)
[![Email](https://img.shields.io/badge/Email-rrs6770%40nyu.edu-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:rrs6770@nyu.edu)
[![GitHub](https://img.shields.io/badge/GitHub-rohitshidid-181717?style=flat&logo=github&logoColor=white)](https://github.com/rohitshidid)
![Profile Views](https://komarev.com/ghpvc/?username=rohitshidid&color=0A66C2&style=flat&label=Profile+Views)

</div>

---

```yaml
Rohit Shidid:
  role:        MS Computer Engineering @ NYU (Expected May 2027)
  previously:  Software Engineer @ Citi  ·  Graduate TA @ NYU
  focus:       Production ML pipelines, MLOps, embedded AI, distributed data
  location:    New York, NY
  works_on:    "Closing the offline-to-online gap between models and the systems that serve them"
  brings:      "The rigor of systems engineering to ML, and the judgment of an
                ML engineer to systems problems."
  open_to:     Full-time ML / Software Engineering roles
```

---

### Tech Stack

**ML & MLOps**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)
![Ray](https://img.shields.io/badge/Ray%20Tune-028CF0?style=flat&logo=ray&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black)

**Data & Pipelines**

![Spark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka%20%2F%20Redpanda-231F20?style=flat&logo=apachekafka&logoColor=white)
![Parquet](https://img.shields.io/badge/Parquet%2FHive-50ABF1?style=flat&logo=apachehive&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=flat&logo=minio&logoColor=white)

**LLMs & Agentic AI**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![RAG](https://img.shields.io/badge/RAG%20Pipelines-5A2D82?style=flat&logoColor=white)
![Claude](https://img.shields.io/badge/Claude%20API-D97757?style=flat&logo=anthropic&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI%20API-412991?style=flat&logo=openai&logoColor=white)

**Systems & Embedded**

![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![ARM](https://img.shields.io/badge/ARM%20Cortex--M4-0091BD?style=flat&logo=arm&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=flat&logo=stmicroelectronics&logoColor=white)

**Infrastructure**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=flat&logo=redis&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

---

### Featured Projects

**[GemSpot](https://github.com/rohitshidid/gemspot) — ML Training Subsystem & Model Registry**
Champion–challenger promotion with a quality-gate layer that blocks registry promotion unless ROC-AUC, recall, and margin-over-baseline all clear; rejected candidates routed to a folder with a machine-readable reason file. Ray Tune + ASHA early-stopping with fault-tolerant MinIO checkpointing, trained on 1M+ Google Maps review rows on a Chameleon bare-metal node. Full feedback loop: live app → PostgreSQL → Kafka/Redpanda → feature store → next model version, audit-logged.
`scikit-learn` `XGBoost` `MLflow` `Ray Tune` `PostgreSQL` `Redpanda` `MinIO`

**[GDELT Real-Time News Intelligence Pipeline](https://github.com/rohitshidid/gdelt-pipeline)**
PySpark ETL over 500K+ GDELT news events per run into a Hive-style Parquet warehouse; 7 models tracked across classification, regression, anomaly detection, and forecasting. 92% F1 on event-conflict classification and MAE 0.73 on 0–100 severity prediction, with per-run MLOps metric logging.
`PySpark 4.0` `Spark MLlib` `PyTorch` `Plotly Dash` `Parquet`

**[Parkinson's Motor Symptom Classifier](https://github.com/rohitshidid/parkinsons-embedded-ai) — Embedded AI**
On-device, four-class real-time motor-symptom classification: 6-axis IMU over I2C at 52 Hz, Hamming windowing, and a 256-point real FFT via ARM CMSIS-DSP — no cloud dependency. Custom GATT service streams over BLE with sub-second latency, plus auto gyroscope calibration and moving-average drift suppression.
`C++` `ARM Cortex-M4` `CMSIS-DSP` `STM32` `BLE`

**[EEG Independent Component Classification](https://doi.org/10.5281/zenodo.13909560) — Published**
Ensemble ML for EEG independent-component analysis, improving brain-signal classification accuracy for cognitive research. 📄 Published — DOI: [10.5281/zenodo.13909560](https://doi.org/10.5281/zenodo.13909560)
`Python` `scikit-learn` `ensemble methods` `signal processing`

**[portmap](https://github.com/rohitshidid/portmap) — Go CLI on Homebrew**
A lightweight Go CLI that replaces five separate diagnostics (`lsof`, `ss`, `netstat`, `docker ps`, `/etc/services`), surfacing listening ports, owning processes, Docker mappings, and known service labels in one clean table or JSON output.
`Go` `Homebrew` `networking` `CLI`

---

### GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=rohitshidid&show_icons=true&count_private=true&hide_border=true&include_all_commits=true&theme=tokyonight" alt="GitHub stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=rohitshidid&layout=compact&hide_border=true&langs_count=8&theme=tokyonight" alt="Top languages" />

<img height="165" src="https://streak-stats.demolab.com/?user=rohitshidid&hide_border=true&theme=tokyonight" alt="GitHub streak" />

<img src="https://github-profile-trophy.vercel.app/?username=rohitshidid&theme=tokyonight&no-frame=true&column=7&margin-w=8" alt="Trophies" />

</div>

<!-- GITHUB-STATS:START -->
### Rohit's · GitHub Stats

| Metric | Count |
|--------|-------|
| Total Stars Earned | `3` |
| Total Commits (All Time) | `270` |
| Total Commits (Last Year) | `107` |
| Total PRs Authored | `24` |
| Total PRs Merged | `24` |
<!-- GITHUB-STATS:END -->

---

### Education

**New York University** — MS, Computer Engineering · _Expected May 2027_
**College of Engineering Pune (COEP)** — B.Tech, Computer Engineering · _May 2024_

<div align="center">

_Open to full-time ML & Software Engineering opportunities._
**[Let's connect →](https://linkedin.com/in/rohit-shidid)**

</div>
