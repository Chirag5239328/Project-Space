import { useState } from "react";
import { runEngine } from "../api";
import { BoltIcon } from "@heroicons/react/24/outline";

export default function RunPanel({ csvId, rulesId, onRunComplete }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [ran, setRan] = useState(false);

  const ready = csvId && rulesId;

  const handleRun = async () => {
    setError(null);
    setLoading(true);
    try {
      const data = await runEngine(csvId, rulesId);
      onRunComplete(data.run_id);
      setRan(true);
    } catch (e) {
      setError(e?.response?.data?.detail || "Engine run failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8">
      <div className="mb-6">
        <div className="flex items-center gap-3 mb-1">
          <span className="flex items-center justify-center w-7 h-7 rounded-full bg-indigo-50 text-indigo-600 text-xs font-bold">3</span>
          <h2 className="text-lg font-semibold text-gray-900">Run Decision Engine</h2>
        </div>
        <p className="text-sm text-gray-400 ml-10">Execute the engine against your dataset with the configured rules.</p>
      </div>

      <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4">
        <div className="flex gap-4 text-sm">
          <StatusPill label="Dataset" active={!!csvId} />
          <StatusPill label="Rules" active={!!rulesId} />
        </div>

        <button
          onClick={handleRun}
          disabled={!ready || loading || ran}
          className={`flex items-center gap-2.5 font-semibold px-6 py-3 rounded-xl transition-all shadow-sm text-sm
            ${ready && !ran
              ? "bg-indigo-600 hover:bg-indigo-700 text-white hover:shadow-indigo-200 hover:shadow-md"
              : "bg-gray-100 text-gray-300 cursor-not-allowed"
            }`}
        >
          {loading ? (
            <>
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              Running engine…
            </>
          ) : ran ? (
            <><BoltIcon className="w-4 h-4" /> Engine Complete</>
          ) : (
            <><BoltIcon className="w-4 h-4" /> Run Decision Engine</>
          )}
        </button>
      </div>

      {!ready && (
        <p className="mt-4 text-xs text-amber-600 bg-amber-50 rounded-lg px-4 py-2 w-fit">
          Complete steps 1 and 2 before running the engine.
        </p>
      )}

      {error && (
        <p className="mt-3 text-sm text-red-500 bg-red-50 rounded-lg px-4 py-2">{error}</p>
      )}
    </div>
  );
}

function StatusPill({ label, active }) {
  return (
    <div className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-medium
      ${active ? "bg-emerald-50 text-emerald-600" : "bg-gray-50 text-gray-300"}`}>
      <span className={`w-1.5 h-1.5 rounded-full ${active ? "bg-emerald-500" : "bg-gray-300"}`} />
      {label}
    </div>
  );
}
