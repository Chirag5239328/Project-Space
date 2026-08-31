import { useState } from "react";
import UploadPanel from "./components/UploadPanel";
import RuleBuilder from "./components/RuleBuilder";
import RunPanel from "./components/RunPanel";
import ResultsPanel from "./components/ResultsPanel";

export default function App() {
  const [csvId, setCsvId] = useState(null);
  const [rulesId, setRulesId] = useState(null);
  const [runId, setRunId] = useState(null);
  const [schema, setSchema] = useState(null);
  const [metadata, setMetadata] = useState(null);

  const handleUploadSuccess = (id, schemaData, metaData) => {
    setCsvId(id);
    setSchema(schemaData);
    setMetadata(metaData);
    setRulesId(null);
    setRunId(null);
  };

  const handleRulesSaved = (id) => {
    setRulesId(id);
    setRunId(null);
  };

  const handleRunComplete = (id) => {
    setRunId(id);
  };

  return (
    <div className="min-h-screen bg-[#f8f8fb]" style={{ fontFamily: "'DM Sans', 'Inter', sans-serif" }}>
      {/* Header */}
      <header className="bg-white border-b border-gray-100 sticky top-0 z-10">
        <div className="max-w-4xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center shadow-sm">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M2 4h4v4H2V4zm8 0h4v4h-4V4zM6 8h4v4H6V8z" fill="white" />
              </svg>
            </div>
            <span className="text-base font-semibold text-gray-900 tracking-tight">Decision Engine</span>
          </div>

          {/* Progress indicator */}
          <div className="hidden sm:flex items-center gap-1.5">
            {[
              { label: "Upload", done: !!csvId },
              { label: "Rules", done: !!rulesId },
              { label: "Run", done: !!runId },
              { label: "Results", done: !!runId },
            ].map((step, i, arr) => (
              <div key={step.label} className="flex items-center gap-1.5">
                <div className={`flex items-center gap-1.5 text-xs font-medium px-2.5 py-1 rounded-full transition
                  ${step.done ? "text-indigo-600 bg-indigo-50" : "text-gray-300 bg-gray-50"}`}>
                  <span className={`w-1.5 h-1.5 rounded-full ${step.done ? "bg-indigo-500" : "bg-gray-200"}`} />
                  {step.label}
                </div>
                {i < arr.length - 1 && <span className="text-gray-200 text-xs">›</span>}
              </div>
            ))}
          </div>
        </div>
      </header>

      {/* Main content */}
      <main className="max-w-4xl mx-auto px-6 py-10 space-y-5">
        <div className="mb-8">
          <h1 className="text-2xl font-bold text-gray-900 tracking-tight">Automated Decision Workflow</h1>
          <p className="text-gray-400 mt-1.5 text-sm">
            Upload your dataset, define rules, and run the decision engine to generate output with full audit trail.
          </p>
        </div>

        <UploadPanel onUploadSuccess={handleUploadSuccess} />

        <RuleBuilder
          schema={schema}
          metadata={metadata}
          onRulesSaved={handleRulesSaved}
        />

        <RunPanel
          csvId={csvId}
          rulesId={rulesId}
          onRunComplete={handleRunComplete}
        />

        <ResultsPanel runId={runId} />
      </main>

      <footer className="max-w-4xl mx-auto px-6 py-8 mt-4 border-t border-gray-100">
        <p className="text-xs text-gray-300 text-center">Decision Engine — All operations are processed locally on your server</p>
      </footer>
    </div>
  );
}
