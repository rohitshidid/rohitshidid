# Rohit Shidid

ML / MLOps Engineer and Systems Engineer.

I build production ML pipelines and the systems that keep them honest: honest evaluation, audited model-promotion gates, and feedback loops that make models visibly improve with new data. I bring the rigor of systems engineering to ML work and the judgment of an ML engineer to systems problems.

- Role: MS Computer Engineering @ NYU (expected May 2027)
- Previously: Software Engineer @ Citi; Graduate Teaching Assistant @ NYU
- Focus: Production ML pipelines, MLOps, embedded AI, distributed data
- Location: New York, NY
- Open to: Full-time ML / Software Engineering roles

## Contact

- LinkedIn: https://linkedin.com/in/rohitshidid
- Email: rrs6770@nyu.edu
- GitHub: https://github.com/rohitshidid

## Technical Skills

- ML and MLOps: Python, PyTorch, scikit-learn, XGBoost, Spark MLlib, HuggingFace, MLflow, Ray Tune, ASHA early-stopping, distributed hyperparameter search, feature stores, model registries
- Data and Pipelines: PySpark 4.0, Apache Kafka, Redpanda, Parquet, Hive, pandas, NumPy, PyArrow, PostgreSQL, MinIO, ETL design
- LLMs and Agentic AI: LangChain, RAG pipelines, prompt engineering, fine-tuning, Claude API, OpenAI API
- Systems and Embedded: C++, Go, ARM Cortex-M4, CMSIS-DSP, BLE, STM32, digital signal processing
- Infrastructure: Docker, Kubernetes, Chameleon Cloud, AWS (S3, Lambda, SageMaker), Git, GitHub Actions, CI/CD, FastAPI, Redis

## Featured Projects

### GemSpot — ML Training Subsystem and Model Registry
Champion-challenger promotion with a quality-gate layer that blocks registry promotion unless ROC-AUC, recall, and margin over baseline all clear; rejected candidates are routed to a folder with a machine-readable reason file. Ray Tune with ASHA early-stopping and fault-tolerant MinIO checkpointing, trained on 1M+ Google Maps review rows on a Chameleon bare-metal node. Full feedback loop: live app to PostgreSQL to Kafka/Redpanda to feature store to the next model version, audit-logged.
Stack: scikit-learn, XGBoost, MLflow, Ray Tune, PostgreSQL, Redpanda, MinIO.
Repo: https://github.com/rohitshidid/gemspot

### GDELT Real-Time News Intelligence Pipeline
PySpark ETL over 500K+ GDELT news events per run into a Hive-style Parquet warehouse; 7 models tracked across classification, regression, anomaly detection, and forecasting. 92% F1 on event-conflict classification and MAE 0.73 on 0-100 severity prediction, with per-run MLOps metric logging.
Stack: PySpark 4.0, Spark MLlib, PyTorch, Plotly Dash, Parquet.
Repo: https://github.com/rohitshidid/gdelt-pipeline

### Parkinson's Motor Symptom Classifier — Embedded AI
On-device, four-class real-time motor-symptom classification: 6-axis IMU over I2C at 52 Hz, Hamming windowing, and a 256-point real FFT via ARM CMSIS-DSP, with no cloud dependency. Custom GATT service streams over BLE with sub-second latency, plus automatic gyroscope calibration and moving-average drift suppression.
Stack: C++, ARM Cortex-M4, CMSIS-DSP, STM32, BLE.
Repo: https://github.com/rohitshidid/parkinsons-embedded-ai

### EEG Independent Component Classification (Published)
Ensemble ML for EEG independent-component analysis, improving brain-signal classification accuracy for cognitive research.
Stack: Python, scikit-learn, ensemble methods, signal processing.
Published, DOI: https://doi.org/10.5281/zenodo.13909560

### portmap — Go CLI on Homebrew
A lightweight Go CLI that replaces five separate diagnostics (lsof, ss, netstat, docker ps, /etc/services), surfacing listening ports, owning processes, Docker mappings, and known service labels in one clean table or JSON output.
Stack: Go, Homebrew, networking, CLI.
Repo: https://github.com/rohitshidid/portmap

### bak - A Lightweight CLI for Per-File Versioning 
bak is a fast, lightweight command-line utility written in Go that provides local, per-file version control without the overhead of initializing full git repositories. Designed to prevent workspace clutter (like file.txt.bak, file.txt.old), bak securely stores timestamped, zstd-compressed snapshots of individual files in a centralized local directory (~/.bak). It features built-in unified diffing (both hunk-style and full-file), interactive restorations, and automatic history pruning. Whether you are quickly iterating on a config file or drafting a document, bak offers a seamless way to track file states on the fly.
Repo: https://github.com/rohitshidid/bak

## GitHub Stats

<!-- GITHUB-STATS:START -->
### Rohit's · GitHub Stats

| Metric | Count |
|--------|-------|
| Total Stars Earned | `3` |
| Total Commits (All Time) | `377` |
| Total Commits (Last Year) | `190` |
| Total PRs Authored | `32` |
| Total PRs Merged | `26` |
<!-- GITHUB-STATS:END -->

## Education

- New York University — MS, Computer Engineering (expected May 2027)
- College of Engineering Pune (COEP) — B.Tech, Computer Engineering (May 2024)
