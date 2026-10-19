import { useState } from "react";
import { executeAttack } from "./services/api";

function App() {
  const [activePage, setActivePage] = useState("Dashboard");

  const [prompt, setPrompt] = useState("");
  const [attackType, setAttackType] = useState("Prompt Injection");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleAttack() {
    if (!prompt.trim()) {
      alert("Please enter an attack prompt.");
      return;
    }

    try {
      setLoading(true);
      setResult(null);

      const data = await executeAttack(prompt, attackType);

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Attack failed. Check the backend terminal.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">

      {/* ================= SIDEBAR ================= */}
      <aside className="sidebar">

        <div className="logo">
          GAUNTLET
        </div>

        <p className="subtitle">
          AI Security Testbed
        </p>

        <nav>

          <button
            className={`nav-item ${
              activePage === "Dashboard" ? "active" : ""
            }`}
            onClick={() => setActivePage("Dashboard")}
          >
            Dashboard
          </button>

          <button
            className={`nav-item ${
              activePage === "Attack Console" ? "active" : ""
            }`}
            onClick={() => setActivePage("Attack Console")}
          >
            Attack Console
          </button>

          <button
            className={`nav-item ${
              activePage === "Attack History" ? "active" : ""
            }`}
            onClick={() => setActivePage("Attack History")}
          >
            Attack History
          </button>

          <button
            className={`nav-item ${
              activePage === "Memory" ? "active" : ""
            }`}
            onClick={() => setActivePage("Memory")}
          >
            Memory
          </button>

          <button
            className={`nav-item ${
              activePage === "Strategist" ? "active" : ""
            }`}
            onClick={() => setActivePage("Strategist")}
          >
            Strategist
          </button>

        </nav>

      </aside>


      {/* ================= MAIN CONTENT ================= */}
      <main className="main-content">

        {/* ================= HEADER ================= */}
        <header className="topbar">

          <div>
            <h1>{activePage}</h1>

            <p>
              AI Security & Red-Teaming Testbed
            </p>
          </div>

          <div className="status">
            <span className="status-dot"></span>
            Backend Online
          </div>

        </header>


        {/* ================================================= */}
        {/* DASHBOARD */}
        {/* ================================================= */}

        {activePage === "Dashboard" && (
          <>

            <section className="stats">

              <div className="card">
                <h3>Total Attacks</h3>
                <p className="number">0</p>
              </div>

              <div className="card">
                <h3>Successful Attacks</h3>
                <p className="number">0</p>
              </div>

              <div className="card">
                <h3>Failed Attacks</h3>
                <p className="number">0</p>
              </div>

              <div className="card">
                <h3>Sessions</h3>
                <p className="number">0</p>
              </div>

            </section>


            <section className="attack-section">

              <h2>
                Welcome to GAUNTLET
              </h2>

              <p>
                AI Security & Red-Teaming Testbed for testing
                AI models against different security attacks.
              </p>

              <button
                className="run-button"
                onClick={() => setActivePage("Attack Console")}
              >
                Open Attack Console
              </button>

            </section>

          </>
        )}


        {/* ================================================= */}
        {/* ATTACK CONSOLE */}
        {/* ================================================= */}

        {activePage === "Attack Console" && (
          <section className="attack-section">

            <h2>
              Attack Console
            </h2>

            <p>
              Test an AI model against different security attacks.
            </p>


            <div className="attack-box">

              {/* Attack Type */}
              <label htmlFor="attackType">
                Attack Type
              </label>

              <select
                id="attackType"
                value={attackType}
                onChange={(e) => setAttackType(e.target.value)}
              >

                <option value="Prompt Injection">
                  Prompt Injection
                </option>

                <option value="Jailbreak">
                  Jailbreak
                </option>

                <option value="Data Extraction">
                  Data Extraction
                </option>

              </select>


              {/* Attack Prompt */}
              <label htmlFor="attackPrompt">
                Attack Prompt
              </label>

              <textarea
                id="attackPrompt"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="Enter your attack prompt..."
              ></textarea>


              {/* Run Attack */}
              <button
                className="run-button"
                onClick={handleAttack}
                disabled={loading}
              >

                {loading
                  ? "Running Attack..."
                  : "Run Attack"
                }

              </button>


              {/* Result */}
              {result && (
                <div className="result-box">

                  <h2>
                    Attack Result
                  </h2>

                  <p>
                    <strong>Attack ID:</strong>{" "}
                    {result.attack_id}
                  </p>

                  <p>
                    <strong>Session ID:</strong>{" "}
                    {result.session_id}
                  </p>


                  <h3>
                    Target Response
                  </h3>

                  <div className="response-box">
                    {result.target_response}
                  </div>


                  <h3>
                    Evaluation
                  </h3>

                  <pre>
                    {JSON.stringify(
                      result.evaluation,
                      null,
                      2
                    )}
                  </pre>

                </div>
              )}

            </div>

          </section>
        )}


        {/* ================================================= */}
        {/* ATTACK HISTORY */}
        {/* ================================================= */}

        {activePage === "Attack History" && (
          <section className="attack-section">

            <h2>
              Attack History
            </h2>

            <p>
              View previously executed security attacks.
            </p>

            <div className="card">

              <h3>
                No Attack History
              </h3>

              <p>
                Attack records will appear here after
                running attacks.
              </p>

            </div>

          </section>
        )}


        {/* ================================================= */}
        {/* MEMORY */}
        {/* ================================================= */}

        {activePage === "Memory" && (
          <section className="attack-section">

            <h2>
              Memory
            </h2>

            <p>
              View stored attack memories and previous
              interactions.
            </p>

            <div className="card">

              <h3>
                Memory System
              </h3>

              <p>
                Stored AI security memories will appear here.
              </p>

            </div>

          </section>
        )}


        {/* ================================================= */}
        {/* STRATEGIST */}
        {/* ================================================= */}

        {activePage === "Strategist" && (
          <section className="attack-section">

            <h2>
              Strategist
            </h2>

            <p>
              Generate intelligent attack strategies for
              testing AI models.
            </p>

            <div className="card">

              <h3>
                AI Attack Strategist
              </h3>

              <p>
                The strategist module will generate
                attack strategies based on previous results.
              </p>

            </div>

          </section>
        )}

      </main>

    </div>
  );
}

export default App;