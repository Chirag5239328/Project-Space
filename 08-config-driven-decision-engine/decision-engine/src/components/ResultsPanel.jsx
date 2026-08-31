import { useState, useEffect } from "react";
import { getResults, getDownloadUrl } from "../api";
import {
  ArrowDownTrayIcon,
  DocumentTextIcon,
  CircleStackIcon,
  ChartBarIcon,
} from "@heroicons/react/24/outline";

export default function ResultsPanel({ runId }) {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!runId) return;

    setLoading(true);
    setError(null);

    getResults(runId)
      .then(setResults)
      .catch((e) =>
        setError(e?.response?.data?.detail || "Failed to load results.")
      )
      .finally(() => setLoading(false));
  }, [runId]);

  if (!runId) return null;

  return (
    <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8">
      <div className="mb-6">
        <div className="flex items-center gap-3 mb-1">
          <span className="flex items-center justify-center w-7 h-7 rounded-full bg-indigo-50 text-indigo-600 text-xs font-bold">
            4
          </span>
          <h2 className="text-lg font-semibold text-gray-900">Results</h2>
        </div>
        <p className="text-sm text-gray-400 ml-10">
          Download output files and review the execution summary.
        </p>
      </div>

      {loading && (
        <div className="flex items-center gap-3 py-8 justify-center">
          <div className="w-5 h-5 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin" />
          <span className="text-sm text-gray-400">Loading results…</span>
        </div>
      )}

      {error && (
        <p className="text-sm text-red-500 bg-red-50 rounded-lg px-4 py-2">
          {error}
        </p>
      )}

      {results && (
        <div className="space-y-6">

          {/* Summary */}
          {results.summary && (
            <div className="rounded-xl border border-indigo-100 bg-indigo-50/40 p-5">
              <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-4 flex items-center gap-2">
                <ChartBarIcon className="w-4 h-4" /> Summary
              </h3>

              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                {Object.entries(results.summary).map(([key, value]) => (
                  <div
                    key={key}
                    className="bg-white rounded-xl p-4 border border-gray-100 text-center shadow-sm"
                  >
                    <p className="text-2xl font-bold text-gray-900">
                      {value}
                    </p>
                    <p className="text-xs text-gray-400 mt-1 capitalize">
                      {key.replace(/_/g, " ")}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Decision Breakdown */}
          {results.decisions && (
            <div>
              <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-3">
                Decision Breakdown
              </h3>

              <div className="flex gap-3 flex-wrap">
                {Object.entries(results.decisions).map(([decision, count]) => (
                  <div
                    key={decision}
                    className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium border
                      ${
                        decision === "accept"
                          ? "bg-emerald-50 text-emerald-700 border-emerald-100"
                          : decision === "reject"
                          ? "bg-red-50 text-red-600 border-red-100"
                          : "bg-amber-50 text-amber-700 border-amber-100"
                      }`}
                  >
                    <span className="font-bold text-base">{count}</span>
                    <span className="capitalize">{decision}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Output Files */}
          <div>
            <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-3">
              Output Files
            </h3>

            <div className="grid sm:grid-cols-3 gap-3">
              {results.files?.map((filename) => (
                <FileCard key={filename} filename={filename} runId={runId} />
              ))}
            </div>
          </div>

        </div>
      )}
    </div>
  );
}

function FileCard({ filename, runId }) {

  const isDb = filename.endsWith(".db");

  const icon = isDb
    ? <CircleStackIcon className="w-5 h-5 text-purple-500" />
    : <DocumentTextIcon className="w-5 h-5 text-indigo-500" />;

  return (
    <div className="flex items-center justify-between rounded-xl border border-gray-100 bg-gray-50/60 px-4 py-3.5 group hover:border-indigo-100 hover:bg-indigo-50/20 transition">

      <div className="flex items-center gap-3">
        {icon}
        <span className="text-sm font-medium text-gray-700">
          {filename}
        </span>
      </div>

      {/* Allow download for ALL files */}
      <a
        href={getDownloadUrl(runId, filename)}
        download={filename}
        className="p-2 rounded-lg text-gray-300 hover:text-indigo-600 hover:bg-indigo-50 transition"
        title={`Download ${filename}`}
      >
        <ArrowDownTrayIcon className="w-4 h-4" />
      </a>

    </div>
  );
}