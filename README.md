<<<<<<< HEAD

# GAUNTLET — AI Security Testbed

### An AI-Powered Platform for Security Testing, Attack Simulation, and Automated Defense

GAUNTLET is an AI Security Testbed designed to explore, simulate, analyze, and evaluate security vulnerabilities in AI-powered systems. It aims to provide a unified environment for testing security threats, understanding attack behavior, and developing potential defense strategies with the assistance of Artificial Intelligence.

The platform combines a web-based interface, backend services, AI model integration, and persistent data storage to support security experimentation and analysis in a controlled environment.

---

## Overview

As AI systems become increasingly integrated into modern applications, they introduce new security challenges, including prompt injection, unauthorized tool usage, data leakage, and adversarial interactions.

GAUNTLET aims to address these challenges by providing a structured testbed where security scenarios can be executed, analyzed, and used to improve defensive mechanisms.

The project focuses on connecting attack simulation workflows with AI-assisted analysis and defense generation through a modular architecture.

## Key Features

- **AI Security Testing:** A centralized environment for experimenting with AI security scenarios.
- **Attack Simulation:** Execute supported attack workflows in a controlled test environment.
- **AI-Assisted Analysis:** Integrate AI models to help analyze attack behavior and security outcomes.
- **Automated Defense Generation:** Explore AI-assisted generation of potential mitigation strategies.
- **Persistent Storage:** Store relevant test information and results for later analysis.
- **Interactive Web Interface:** A React-based dashboard for interacting with the testbed.
- **Backend API:** A FastAPI backend for handling requests and coordinating application logic.
- **Local AI Integration:** Support for local language model workflows through Ollama.
- **Modular Architecture:** Separate frontend, backend, model integration, and data management components.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React.js |
| Build Tool | Vite |
| Backend | Python, FastAPI |
| ASGI Server | Uvicorn |
| AI Model Runtime | Ollama |
| Database | SQLite |
| Cloud Database / Services | Supabase |
| Version Control | Git and GitHub |
| Frontend Deployment | Vercel |

## System Architecture

```text
                  ┌────────────────────────┐
                  │       User             │
                  └───────────┬────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │   React + Vite UI      │
                  │   Interactive Dashboard│
                  └───────────┬────────────┘
                              │ HTTP / API
                              ▼
                  ┌────────────────────────┐
                  │   FastAPI Backend      │
                  │   Application Logic    │
                  └───────────┬────────────┘
                              │
               ┌──────────────┼──────────────┐
               ▼              ▼              ▼
       ┌──────────────┐ ┌────────────┐ ┌──────────────┐
       │ Attack       │ │ AI Model   │ │ Data Storage │
       │ Simulation   │ │ Integration│ │ SQLite /     │
       │ Workflows    │ │ Ollama     │ │ Supabase     │
       └──────┬───────┘ └─────┬──────┘ └──────────────┘
              │               │
              └───────┬───────┘
                      ▼
             ┌────────────────────┐
             │ Analysis & Defense │
             │ Evaluation         │
             └────────────────────┘
```

*Note: The diagram represents the intended high-level architecture. The exact integrations depend on the modules enabled in the current implementation.*

## Project Structure

The repository may be organized into the following components:

```text
GAUNTLET/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

The exact directory structure may vary according to the current repository implementation.

## Getting Started

### Prerequisites

Install the following tools before running the project:

- [Node.js and npm](https://nodejs.org/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Ollama](https://ollama.com/) (for local AI model integration)

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd GAUNTLET
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Set Up the Frontend

Open a terminal in the frontend directory:
=======
# GAUNTLET

GAUNTLET is an AI security and red-teaming testbed. It sends attack prompts to a configured Ollama target model, evaluates the response with multiple judges, and stores attack/session data in SQLite.

## Demo flow

1. Start the FastAPI backend.
2. Start the Vite frontend.
3. Open the frontend URL shown by Vite.
4. Open **Attack Console**, choose an attack type, enter a prompt, and select **Run Attack**.
5. Review the target response and evaluation returned by the backend.

## Requirements

- Node.js 18+ and npm
- Python 3.11+
- Ollama running locally at `http://localhost:11434`
- The configured Ollama model available locally (defaults to `llama3.2`)
- Docker (optional, for a reproducible backend run)

## Run locally

### Backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

The health check is available at `http://localhost:8000/health`.

### Docker backend

```bash
docker build -t gauntlet-backend .
docker run --rm -p 8000:8000 --env-file .env.example gauntlet-backend
```

### Frontend
>>>>>>> 82d95db (docs: prepare Gauntlet for buildathon submission)

```bash
cd frontend
npm install
npm run dev
```

<<<<<<< HEAD
Vite will display the local development URL in the terminal, usually:

```text
http://localhost:5173
```

Open the URL in your browser.

### 3. Set Up the Backend

Open a separate terminal and navigate to the backend directory:

```bash
cd backend
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will usually be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is typically available at:

```text
http://127.0.0.1:8000/docs
```

**Important:** These commands assume that `backend/main.py` defines the FastAPI application as `app`. Adjust the working directory or module path if your repository uses a different structure.

### 4. Configure Ollama

Install Ollama and download a model supported by your implementation.

For example:

```bash
ollama pull llama3.2
```

Start the Ollama service if it is not already running, then verify that the model is available:

```bash
ollama list
```

Make sure the backend's model configuration matches the installed model.

### 5. Configure Environment Variables

Create a `.env` file if required by the application.

Example:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

Add any required Supabase or other service configuration according to your implementation.

**Security:** Never commit API keys, database credentials, access tokens, or other secrets to GitHub. Keep `.env` files out of version control and provide a sanitized `.env.example` for collaborators.

## Usage

1. Start the backend services and any required AI model runtime.
2. Start the frontend development server.
3. Open the application in your browser.
4. Select or initiate an available security testing workflow.
5. Execute supported test scenarios in the authorized environment.
6. Review the resulting analysis and available mitigation recommendations.
7. Store or review test results where persistence is implemented.

Available workflows and results depend on the modules currently integrated into GAUNTLET.

## Security and Responsible Use

GAUNTLET is intended for educational research, defensive security testing, and controlled experimentation.

- Test only systems you own or have explicit permission to assess.
- Keep attack simulations within an isolated, authorized environment.
- Do not use generated attacks or security findings to compromise third-party systems.
- Protect sensitive prompts, logs, credentials, and stored test results.
- Validate AI-generated defenses before deploying them in production.
- Treat model outputs as recommendations rather than guaranteed security solutions.

## Current Development Focus

GAUNTLET is being developed as a modular AI security platform, with emphasis on:

- Frontend and backend integration.
- Reliable execution of security testing workflows.
- Local AI model connectivity.
- Persistent storage and retrieval of test information.
- Testing, debugging, and deployment.
- Improving the clarity and usability of the security testing interface.

## Future Scope

Potential future improvements include:

- Expanded prompt-injection and jailbreak test suites.
- Multi-agent attack and defense simulations.
- Persistent graph-based memory for tracking relationships between attacks, vulnerabilities, and mitigations.
- Automated evaluation of generated defenses.
- Security scoring and comparative test reports.
- Detailed audit logs and experiment history.
- Role-based access control and improved isolation.
- Integration with additional local and hosted AI models.

These items represent possible extensions and should not be interpreted as completed features unless implemented in the repository.

## Team and Contributions

GAUNTLET is developed collaboratively, with contributions across frontend development, backend integration, AI security workflows, testing, and deployment.

Contributions are welcome through bug reports, feature suggestions, documentation improvements, and pull requests.

### Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Commit your changes with a descriptive message.
5. Open a pull request describing the changes.

## License

No license has been specified yet. Unless a license is added to the repository, reuse and redistribution are subject to the applicable copyright laws.

---

**GAUNTLET — AI Security Testbed**

*Simulate. Analyze. Defend.*
=======
The frontend expects the backend at `http://localhost:8000` and sends the local API key `gauntlet-local-key`.

## Configuration

The backend reads these optional environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama endpoint |
| `TARGET_MODEL` | `llama3.2` | Model under test |
| `JUDGE_MODEL` | `llama3.2` | Model used by the LLM judge |
| `DATABASE_NAME` | `gauntlet.db` | SQLite database path |
| `GAUNTLET_API_KEY` | `gauntlet-local-key` | API key required by attack routes |

## Verification

From `frontend/`:

```bash
npm run build
```

From `backend/`:

```bash
python -m compileall -q .
python test_rule_judge.py
```

The full attack flow also requires a reachable Ollama instance with the selected model.

## Submission checklist

- [x] Frontend production build succeeds.
- [x] Backend imports and exposes `/health`.
- [x] Rule-judge smoke test succeeds.
- [x] Local run instructions are documented.
- [x] Runtime versions are pinned in `.python-version` and `.nvmrc`.
- [x] A Dockerfile provides a reproducible backend build.
- [x] Non-secret settings are listed in `.env.example`.
- [ ] Verify the end-to-end attack flow against Ollama.
- [ ] Add a final demo screenshot or recording if the event requires visual evidence.
- [ ] Confirm the event's submission form, repository visibility, and deadline.

## Known limitations

- Dashboard counters and history/memory pages are currently placeholders.
- End-to-end attack execution depends on Ollama and the selected model being available.
- The supplied Python requirements file contains many platform-specific and heavyweight packages; install only the supported environment's dependencies for the demo platform.
>>>>>>> 82d95db (docs: prepare Gauntlet for buildathon submission)
