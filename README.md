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

### Self-Healing RAG — Failure-Detecting Retrieval-Augmented Generation
Built a RAG (Retrieval-Augmented Generation) system that detects and recovers from its own failures instead of returning bad answers silently — the failure-handling layer most RAG projects skip.
The pipeline verifies its work at two checkpoints: retrieval quality (embedding similarity + a query–passage cross-encoder for semantic relevance) and answer groundedness (per-sentence NLI entailment against retrieved evidence, to catch hallucinations). When a check fails, it automatically applies the matching repair — LLM query rewriting, HyDE, claim-targeted re-retrieval, or context expansion — capped to guarantee termination. A live "healing log" makes the system catching and fixing itself visible in real time.
Results on a 20-question eval vs. a standard RAG baseline: fully-grounded answer rate 69% → 81%, ungrounded responses down 40%, with honest refusals on out-of-corpus questions.

- **Stack**: Python, FAISS, sentence-transformers (MiniLM), cross-encoder NLI (DeBERTa-v3) + relevance (ms-marco), Groq (Llama-3.3-70B), Streamlit. Fully local verification (no API cost), free permanent hosting on Hugging Face Spaces. 8 unit tests covering every failure→repair route.
- **Repo**: https://github.com/rohitshidid/Self-Healing-RAG-Failure-Detecting-Retrieval-Augmented-Generation

### Bandageboard | Full-Stack Healthcare Billing Pipeline
A full-stack Next.js application that automates Medicare Part B wound-care billing triage. It features a robust data ingestion pipeline that pulls from a mock EHR API, extracts clinical data from unstructured notes using LLMs and Regex, and presents routing decisions in a secure, biller-facing dashboard.
- **Stack**: Next.js 14, React, Tailwind CSS, Vercel AI SDK, Anthropic, Vercel Postgres, Drizzle ORM, TypeScript
- **Repo**: https://github.com/rohitshidid/bandageboard

### Real-Time Cricket Ball Tracker
A Python-based computer vision tool designed for side-on cameras. It detects a cricket ball in real-time using tuned HSV color masking and contour analysis, tracks its trajectory, and identifies the exact bounce point. By utilizing a 4-point homography calibration, it maps the 2D image bounce to real-world pitch dimensions, automatically classifying the delivery length (Yorker, Full, Good, Back of length, Short).
- **Stack**: Python, OpenCV, NumPy
- **Repo**: https://github.com/rohitshidid/Computer-Vision-Cricket-Tracker-

### GemSpot — ML Training Subsystem and Model Registry
Champion-challenger promotion with a quality-gate layer that blocks registry promotion unless ROC-AUC, recall, and margin over baseline all clear; rejected candidates are routed to a folder with a machine-readable reason file. Ray Tune with ASHA early-stopping and fault-tolerant MinIO checkpointing, trained on 1M+ Google Maps review rows on a Chameleon bare-metal node. Full feedback loop: live app to PostgreSQL to Kafka/Redpanda to feature store to the next model version, audit-logged.
- **Stack**: scikit-learn, XGBoost, MLflow, Ray Tune, PostgreSQL, Redpanda, MinIO
- **Repo**: https://github.com/rohitshidid/gemspot

### GDELT Real-Time News Intelligence Pipeline
PySpark ETL over 500K+ GDELT news events per run into a Hive-style Parquet warehouse; 7 models tracked across classification, regression, anomaly detection, and forecasting. 92% F1 on event-conflict classification and MAE 0.73 on 0-100 severity prediction, with per-run MLOps metric logging.
- **Stack**: PySpark 4.0, Spark MLlib, PyTorch, Plotly Dash, Parquet
- **Repo**: https://github.com/rohitshidid/gdelt-pipeline
  
### portmap — Go CLI on Homebrew
A lightweight Go CLI that replaces five separate diagnostics (lsof, ss, netstat, docker ps, /etc/services), surfacing listening ports, owning processes, Docker mappings, and known service labels in one clean table or JSON output.
- **Stack**: Go, Homebrew, networking, CLI
- **Repo**: https://github.com/rohitshidid/portmap

### bak - A Lightweight CLI for Per-File Versioning 
bak is a fast, lightweight command-line utility written in Go that provides local, per-file version control without the overhead of initializing full git repositories. Designed to prevent workspace clutter (like file.txt.bak, file.txt.old), bak securely stores timestamped, zstd-compressed snapshots of individual files in a centralized local directory (~/.bak). It features built-in unified diffing (both hunk-style and full-file), interactive restorations, and automatic history pruning. Whether you are quickly iterating on a config file or drafting a document, bak offers a seamless way to track file states on the fly.
- **Repo**: https://github.com/rohitshidid/bak

### Parkinson's Motor Symptom Classifier — Embedded AI
On-device, four-class real-time motor-symptom classification: 6-axis IMU over I2C at 52 Hz, Hamming windowing, and a 256-point real FFT via ARM CMSIS-DSP, with no cloud dependency. Custom GATT service streams over BLE with sub-second latency, plus automatic gyroscope calibration and moving-average drift suppression.
- **Stack**: C++, ARM Cortex-M4, CMSIS-DSP, STM32, BLE
- **Repo**: https://github.com/rohitshidid/parkinsons-embedded-ai

### EEG Independent Component Classification (Published)
Ensemble ML for EEG independent-component analysis, improving brain-signal classification accuracy for cognitive research.
- **Stack**: Python, scikit-learn, ensemble methods, signal processing
- **Published, DOI**: https://doi.org/10.5281/zenodo.13909560

## GitHub Stats

<!-- GITHUB-STATS:START -->
### Rohit's · GitHub Stats

| Metric | Count |
|--------|-------|
| Total Stars Earned | `3` |
| Total Commits (All Time) | `396` |
| Total Commits (Last Year) | `209` |
| Total PRs Authored | `62` |
| Total PRs Merged | `53` |
<!-- GITHUB-STATS:END -->

## Education

- New York University — MS, Computer Engineering (expected May 2027)
- College of Engineering Pune (COEP) — B.Tech, Computer Engineering (May 2024)
