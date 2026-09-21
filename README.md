# Rohit Shidid

**AI/ML Engineer — Agentic AI, LLM Systems & Production ML Pipelines**

I build ML systems that are honest about their own failures. The thread running through my work is verification: RAG pipelines that detect and repair their own hallucinations, model registries that refuse promotion until quality gates clear, anomaly detectors validated against real vehicle behavior. Anyone can ship a model that works on the happy path — I'm interested in what happens when it doesn't.

- **Now:** MS Computer Engineering @ NYU Tandon (expected May 2027) · Graduate Teaching Assistant (Operating Systems, Cyber Risk Management)
- **Previously:** Software Engineer @ Citi · AI Engineer @ Elespa HEV · Software Developer @ FinIQ · Co-founder @ SaveNotes
- **Focus:** Agentic AI & RAG, MLOps and model governance, distributed data pipelines, embedded AI
- **Location:** New York, NY — open to relocating across the US
- **Open to:** Full-time ML / AI / Software Engineering roles

### Contact

[Portfolio](https://rohitshidid.github.io) · [LinkedIn](https://linkedin.com/in/rohitshidid) · [Email](mailto:rrs6770@nyu.edu) · [All links](https://linktr.ee/rohitshidid)

---

## Technical Skills

| Area | Tools |
|---|---|
| **Agentic AI & LLMs** | LangChain, LangGraph, MCP protocol, RAG pipelines, hybrid retrieval (BM25 + dense), Reciprocal Rank Fusion, cross-encoder reranking, HyDE, query rewriting, NLI hallucination detection, prompt engineering, fine-tuning, Claude / OpenAI / Groq / Gemini APIs |
| **ML & MLOps** | PyTorch, scikit-learn, XGBoost, Spark MLlib, HuggingFace, MLflow, Ray Tune, ASHA early-stopping, distributed hyperparameter search, feature stores, model registries, champion–challenger promotion gates |
| **Data & Pipelines** | PySpark 4.0, Apache Kafka, Redpanda, Parquet, Hive, pandas, NumPy, PyArrow, PostgreSQL, MinIO, FAISS, LanceDB, ETL design |
| **Languages** | Python, C++, Go, TypeScript, Swift, SQL |
| **Systems & Embedded** | ARM Cortex-M4, CMSIS-DSP, STM32, Mbed OS, BLE, I2C, digital signal processing, OpenCV |
| **Infrastructure** | Docker, Kubernetes, Chameleon Cloud, AWS (S3, Lambda, SageMaker), GitHub Actions, CI/CD, FastAPI, Streamlit, Redis |

---

## Featured Projects

### Self-Healing RAG — Failure-Detecting Retrieval-Augmented Generation
[**Live Demo**](https://huggingface.co/spaces/rohitshidid/Self_healing_RAG_demo) · [**Repo**](https://github.com/rohitshidid/Self-Healing-RAG-Failure-Detecting-Retrieval-Augmented-Generation)

A RAG pipeline that catches and recovers from its own failures instead of returning bad answers silently — the failure-handling layer most RAG projects skip. It verifies its work at two checkpoints: **retrieval quality** (embedding similarity plus a query–passage cross-encoder for semantic relevance) and **answer groundedness** (per-sentence NLI entailment against retrieved evidence, to catch hallucinations). When a check fails, the matching repair fires automatically — LLM query rewriting, HyDE, claim-targeted re-retrieval, or context expansion — capped to guarantee termination. A live "healing log" makes the system catching and fixing itself visible in real time.

**Results** on a 20-question eval vs. a standard RAG baseline: fully-grounded answer rate **69% → 81%**, ungrounded responses **down 40%**, with honest refusals on out-of-corpus questions. All verification runs locally at zero API cost, covered by 8 unit tests across every failure→repair route.

`Python` `FAISS` `sentence-transformers (MiniLM)` `DeBERTa-v3 NLI` `ms-marco cross-encoder` `Groq (Llama-3.3-70B)` `Streamlit`

---

### Research Copilot — Agentic RAG over Academic Literature
[**Repo**](https://github.com/rohitshidid/Research-Copilot)

An agentic research assistant that answers literature questions over arXiv and Semantic Scholar papers and returns a synthesized answer with **inline citations** — every claim traceable to a retrieved source, with unmapped claims explicitly flagged `[n]` rather than quietly passed off as sourced. Retrieval fuses BM25 lexical search with BGE dense embeddings through Reciprocal Rank Fusion, then reranks candidates with a cross-encoder before generation.

Built provider-agnostic: routes across Claude, GPT-4o, and Llama-3.3-70B via independent `/ask`, `/verify`, and `/followup` endpoints, so each retrieval component's contribution can be isolated per-stage. A section-aware PDF chunker preserves page and section provenance for every ingested paper.

`Python` `LanceDB` `BM25` `BGE embeddings` `cross-encoder reranking` `FastAPI` `Claude API` `Groq API`

---

### GemSpot — ML Training Subsystem & Model Registry
[**Repo**](https://github.com/rohitshididnyu/GemSpot_training)

The training and promotion subsystem for an XGBoost recommendation model, built around a **quality gate that blocks registry promotion** unless ROC-AUC, recall, and margin-over-baseline all clear — rejected candidates get routed to a quarantine folder with a machine-readable reason file, so a failed promotion is auditable rather than invisible.

Tracks three MLflow-logged candidates (majority-class baseline, default-parameter XGBoost, tuned XGBoost with class-imbalance handling) and reached **0.835–0.836 ROC-AUC** on Google Maps review classification over 337,698 real review records. Ray Tune with ASHA early-stopping and fault-tolerant MinIO checkpointing; containerized and deployed to a Chameleon Cloud bare-metal node. The full feedback loop closes: live app → PostgreSQL → Kafka/Redpanda → feature store → next model version, audit-logged end to end.

`scikit-learn` `XGBoost` `MLflow` `Ray Tune` `Docker` `PostgreSQL` `Redpanda` `MinIO` `Chameleon Cloud`

---

### GDELT Real-Time News Intelligence Pipeline
[**Live Dashboard**](https://huggingface.co/spaces/rohitshidid/GlobalCrisisMonitor) · [**Repo**](https://github.com/rohitshidid/GlobalCrisisMonitor)

A global crisis monitoring pipeline over the GDELT 2.0 news dataset: parallel download and PySpark ETL ingest **250K+ news events per run** into a Hive-style Parquet warehouse, feeding **8 models** tracked across classification, regression, anomaly detection, and forecasting.

**Results:** 92% F1 on event-conflict classification (held-out test split) and MAE 0.73 on 0–100 severity prediction, using a PyTorch feed-forward network over engineered geopolitical and media-coverage features drawn from the partitioned Parquet warehouse — with per-run MLOps metric logging across all model types.

`PySpark 4.0` `Spark MLlib` `PyTorch` `Parquet` `Plotly Dash`

---

### Parkinson's Motor Symptom Classifier — Embedded AI
[**Repo**](https://github.com/rohitshidid/Parkinson-Detection)

On-device, four-class real-time motor-symptom classification with **no cloud dependency**: a 6-axis IMU read over I2C at 52 Hz, Hamming windowing, and a 256-point real FFT via ARM CMSIS-DSP, thresholding dominant frequencies into resting tremor (3–5 Hz), dyskinesia (5–7 Hz), freeze of gait, and normal walking (1–2 Hz).

A custom GATT service streams results over BLE with sub-second latency for live remote monitoring, with automatic gyroscope calibration and moving-average filtering to suppress drift and noise before transmission. Validated by correct state labeling across repeated bench-test trials.

`C++` `ARM Cortex-M4` `CMSIS-DSP` `STM32` `Mbed OS` `LSM6DSL IMU` `BLE` `I2C`

---

### EEG Independent Component Classification — *Published*
[**Published Paper (DOI)**](https://doi.org/10.5281/zenodo.13909560) · [**Repo**](https://github.com/rohitshidid/EEG-independent-component-classification-using-ensemble-based-technique)

Published ensemble machine learning for classifying independent components extracted from EEG brain-signal recordings — separating genuine neural signal from artifacts like eye movement and muscle activity. Evaluates CNNs across activation functions, hyperparameters, and data representations (time series vs. power spectral density), with architectural modifications that improved classification accuracy for cognitive research per published evaluation metrics.

`Python` `scikit-learn` `ensemble methods` `CNNs` `signal processing`

---

## More AI/ML Systems

| Project | What it does | Stack | Links |
|---|---|---|---|
| **OmniRoute** | Self-hosted LLM gateway routing across 77+ models from multiple providers behind one OpenAI-compatible API — switching model or provider never means rewriting app code. Paired with a hosted chat client demonstrating live routing and streaming end to end. | LLM infra, API design, multi-model routing | [Demo](https://omiroute-chat.onrender.com/) · [Repo](https://github.com/rohitshidid/omiroute-chat) |
| **Synapse** | Two-answer fact checker that adjudicates between competing answers to the same question using free-tier models via OpenRouter, backed by live web search for verification rather than the model's own memory. | Node.js, OpenRouter API, web search | [Demo](https://openrouter-chatbot-8qv6.onrender.com/) · [Repo](https://github.com/rohitshidid/openrouter-chatbot) |
| **Bandageboard** | Full-stack Medicare Part B wound-care billing triage, built for the ABI Frameworks hackathon. Ingests from a mock EHR API, extracts clinical data from unstructured notes via a regex-first pipeline with an LLM fallback, and routes billing decisions to a biller-facing dashboard with full CRUD — 300 synthetic patients, zero real PHI. | Next.js 14, TypeScript, Claude API, Vercel Postgres, Drizzle ORM | [Video Demo](https://drive.google.com/file/d/1IDWhbeCqQkupWy_Kk9bw5q-T1JQSINli/view?usp=share_link) · [Repo](https://github.com/rohitshidid/bandageboard) |
| **Real-Time Cricket Ball Tracker** | Detects a cricket ball in real time from a side-on camera using tuned HSV masking and contour analysis, tracks its trajectory, and finds the exact bounce point. A 4-point homography calibration maps 2D image coordinates to real pitch dimensions, classifying delivery length into five categories (Yorker, Full, Good, Back of Length, Short). | Python, OpenCV, NumPy | [Video Demo](https://drive.google.com/file/d/1G6c9ihMt4wW3GS0FW_Ywf_uf73rV7VpU/view?usp=share_link) · [Repo](https://github.com/rohitshidid/Computer-Vision-Cricket-Tracker-) |
| **Murmur** | Push-to-talk dictation that transcribes speech **entirely on-device** — hold a key, talk, release, and cleaned-up text lands at the cursor. No audio or text leaves the machine. Native macOS (Swift) and Windows (C#/Avalonia) share one behavioural contract for the correction dictionary. | Swift, C#/Avalonia, on-device speech-to-text | [Demo Site](https://rohitshidid.github.io/murmur/) · [Repo](https://github.com/rohitshidid/murmur) |
| **Layoff Predictor** | Estimates a public company's layoff risk from live financial signals — pull a ticker, fetch current fundamentals via yfinance, score with a trained classifier, served through a Flask app. | Python, Flask, scikit-learn, yfinance | [Demo](https://layoff-predictor.onrender.com/)\* · [Repo](https://github.com/rohitshidid/layoff-predictor) |
| **Mutation Simulator** | Interactive visualizer comparing two reinforcement-learning approaches side by side — neuroevolution (mutation-driven population search) against REINFORCE (policy gradient) — so convergence behavior is visible, not just described. | Reinforcement learning, neuroevolution, policy gradients | [Demo](https://rohitshidid.github.io/mutation-simulator/index.html) · [Repo](https://github.com/rohitshidid/mutation-simulator) |

<sub>\* Free-tier Render deploy — may take up to a minute to wake from idle on first load.</sub>

### In Progress — repos not yet public

- **OracleLoop — Autonomous, Self-Resolving Prediction Markets.** A multi-agent pipeline that generates verified prediction-market questions from live sports coverage: a research agent searches the web for coverage of any sport or match and drafts a binary question, which is then gated by a second, independent Gemini verification pass that rejects any candidate found unsolvable before it reaches a user. Published questions render as two-option cards with a live countdown timer and a probability-weighted prediction, and expired cards route to a resolution agent that re-searches the web and settles the market with no manual input. `Node.js` `TypeScript` `Gemini API` `multi-agent orchestration`
- **Chaos-Engineered Self-Healing Raft Cluster.** A distributed consensus cluster validated under deliberate fault injection — leader kills, network partitions, and node failures — to verify that recovery and leader re-election behave correctly under real adversarial conditions rather than only on the happy path. `distributed systems` `Raft consensus` `chaos engineering`

*Available on request while the repositories are being prepared for release.*

---

## Developer Tools

| Project | What it does | Stack | Links |
|---|---|---|---|
| **bak** | Published Go CLI for isolated per-file version control — `cp file.bak` upgraded with automatic timestamped versions, a custom hunk-style and full-file diffing engine, interactive restore, `--keep N` retention pruning, and garbage collection, all backed by zstd-compressed, SHA-256-deduplicated centralized storage in `~/.bak`. Zero workspace clutter, no git repo required. | Go, zstd, Homebrew | [Demo Site](https://rohitshidid.github.io/bak/) · [Repo](https://github.com/rohitshidid/bak) · `brew tap rohitshidid/bak` |
| **portmap** | Published Go CLI that replaces five separate diagnostics (`lsof`, `ss`, `netstat`, `docker ps`, `/etc/services`) with one table: every listening port, its owning process, the Docker container behind it, and a known-service label — as clean text or JSON. | Go, networking, Docker, CLI | [Demo Site](https://rohitshidid.github.io/Homebrew-portman/) · [Repo](https://github.com/rohitshidid/Homebrew-portman) · `brew tap rohitshidid/portman` |
| **Disk Manager** | Visual disk-usage explorer for macOS that scans your disk and shows exactly where the space went, surfacing hidden files and their true sizes — with reversible deletion, so nothing is erased without explicit confirmation. | macOS, JavaScript, systems tooling | [Demo Site](https://rohitshidid.github.io/Disk-manager/) · [Repo](https://github.com/rohitshidid/Disk-manager) |

---

## Web & Utilities

| Project | What it does | Stack | Links |
|---|---|---|---|
| **AirControl** | Browser-based hand-gesture controller — navigate a webpage using nothing but a webcam. Hand tracking runs entirely on-device via Google's MediaPipe: zero installs, zero data leaving the browser. | MediaPipe, JavaScript, on-device ML | [Demo](https://rohitshidid.github.io/Aircontrol/) · [Repo](https://github.com/rohitshidid/Aircontrol) |
| **Hexagon** | Real-time multiplayer Catan-style board game for 2–10 players, built on an authoritative Node.js server over WebSockets so every move is validated server-side and no client can cheat. Playable over LAN or hosted online. | Node.js, WebSockets, real-time systems | [Demo](https://hexagon-zwye.onrender.com) · [Repo](https://github.com/rohitshidid/hexagon) |
| **Splitplus** | Group expense-splitting web app designed so your expense data stays yours rather than living in a third-party database. | Next.js, React, TypeScript | [Demo](https://rohitshidid.github.io/splitplus/) · [Repo](https://github.com/rohitshidid/splitplus) |

---

## Open Source

**[Odysseus](https://github.com/pewdiepie-archdaemon/odysseus)** — 85k★ self-hosted AI workspace · [**Merged PR #2113**](https://github.com/pewdiepie-archdaemon/odysseus/pull/2113)

Diagnosed and fixed a full-stack bug in the `/todo` slash command: a `note_type` payload mismatch in the JavaScript frontend (`slashCommands.js`) caused `/todo` to silently fail. Added structured list-item support and `note_type` filtering to the payload sent to the notes API, plus new pytest API-level regression coverage validating the corrected payload shape — catching the same class of frontend/backend mismatch across the notes API surface.

---

## GitHub Activity

![Contribution graph](https://raw.githubusercontent.com/rohitshidid/rohitshidid/output/snake.svg)

<!-- GITHUB-STATS:START -->
### Rohit's · GitHub Stats

| Metric | Count |
|--------|-------|
| Total Stars Earned | `4` |
| Total Commits (All Time) | `704` |
| Total Commits (Last Year) | `515` |
| Total PRs Authored | `115` |
| Total PRs Merged | `100` |
<!-- GITHUB-STATS:END -->

---

## Experience

| Role | Organization | Period |
|---|---|---|
| Graduate Teaching Assistant — Operating Systems, Cyber Risk Management | New York University | Sep 2025 – Present |
| Software Engineer | Citi | Jul 2024 – Aug 2025 |
| AI Engineer | Elespa HEV | Feb 2021 – Jul 2024 |
| Software Developer | FinIQ Consulting | May 2023 – Jul 2023 |
| Co-founder & Software Engineer | SaveNotes | Sep 2022 – Jul 2023 |

## Education

- **New York University**, Tandon School of Engineering — MS, Computer Engineering *(expected May 2027)*
- **College of Engineering Pune (COEP)** — B.Tech, Computer Engineering *(May 2024)*
