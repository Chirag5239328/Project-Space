import { useState, useRef } from "react";
import { uploadCSV } from "../api";
import { CloudArrowUpIcon, CheckCircleIcon } from "@heroicons/react/24/outline";

export default function UploadPanel({ onUploadSuccess }) {
  const [dragging, setDragging] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [uploaded, setUploaded] = useState(null);
  const fileInputRef = useRef();

  const handleFile = async (file) => {
    if (!file || !file.name.endsWith(".csv")) {
      setError("Please upload a valid .csv file.");
      return;
    }

    setError(null);
    setLoading(true);

    try {
      const data = await uploadCSV(file);

      setUploaded({
        filename: file.name,
        schema: data.schema,
        metadata: data.metadata,
      });

      onUploadSuccess(data.csv_id, data.schema, data.metadata);

    } catch (e) {
      setError(e?.response?.data?.detail || "Upload failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const onDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    const file = e.dataTransfer.files[0];
    handleFile(file);
  };

  return (
    <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8">

      <div className="mb-6">
        <div className="flex items-center gap-3 mb-1">
          <span className="flex items-center justify-center w-7 h-7 rounded-full bg-indigo-50 text-indigo-600 text-xs font-bold">
            1
          </span>
          <h2 className="text-lg font-semibold text-gray-900">
            Upload Dataset
          </h2>
        </div>
        <p className="text-sm text-gray-400 ml-10">
          Upload a CSV file to begin. The engine will detect fields and types automatically.
        </p>
      </div>

      {!uploaded ? (
        <div
          onDragOver={(e) => {
            e.preventDefault();
            setDragging(true);
          }}
          onDragLeave={() => setDragging(false)}
          onDrop={onDrop}
          onClick={() => fileInputRef.current.click()}
          className={`relative cursor-pointer rounded-xl border-2 border-dashed transition-all duration-200 flex flex-col items-center justify-center py-14 px-8 gap-3
            ${
              dragging
                ? "border-indigo-400 bg-indigo-50"
                : "border-gray-200 hover:border-indigo-300 hover:bg-gray-50"
            }`}
        >

          <input
            ref={fileInputRef}
            type="file"
            accept=".csv"
            className="hidden"
            onChange={(e) => handleFile(e.target.files[0])}
          />

          {loading ? (
            <div className="flex flex-col items-center gap-3">
              <div className="w-8 h-8 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin" />
              <span className="text-sm text-gray-400">
                Processing file…
              </span>
            </div>
          ) : (
            <>
              <CloudArrowUpIcon className="w-10 h-10 text-gray-300" />

              <div className="text-center">
                <p className="text-sm font-medium text-gray-700">
                  Drag & drop your CSV here, or{" "}
                  <span className="text-indigo-600">browse</span>
                </p>
                <p className="text-xs text-gray-400 mt-1">
                  Only .csv files are supported
                </p>
              </div>
            </>
          )}

        </div>
      ) : (
        <div className="rounded-xl border border-emerald-100 bg-emerald-50 p-4 flex items-start gap-3 mb-5">
          <CheckCircleIcon className="w-5 h-5 text-emerald-500 mt-0.5 shrink-0" />

          <div>
            <p className="text-sm font-medium text-emerald-800">
              {uploaded.filename} uploaded successfully
            </p>

            <p className="text-xs text-emerald-600 mt-0.5">
              {Object.keys(uploaded.schema).length} fields detected
            </p>
          </div>

        </div>
      )}

      {error && (
        <p className="mt-3 text-sm text-red-500 bg-red-50 rounded-lg px-4 py-2">
          {error}
        </p>
      )}

      {uploaded && (
        <div className="mt-6">

          <h3 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-3">
            Detected Schema
          </h3>

          <div className="rounded-xl overflow-hidden border border-gray-100">

            <table className="w-full text-sm">

              <thead>
                <tr className="bg-gray-50 text-left">
                  <th className="px-4 py-3 text-xs font-semibold text-gray-400 uppercase tracking-wide">
                    Field
                  </th>

                  <th className="px-4 py-3 text-xs font-semibold text-gray-400 uppercase tracking-wide">
                    Type
                  </th>

                  <th className="px-4 py-3 text-xs font-semibold text-gray-400 uppercase tracking-wide">
                    Available Operators
                  </th>
                </tr>
              </thead>

              <tbody>
                {Object.entries(uploaded.schema).map(([field, schemaInfo], i) => {

                  const fieldType =
                    typeof schemaInfo === "object"
                      ? schemaInfo.type
                      : schemaInfo;

                  return (
                    <tr
                      key={field}
                      className={`border-t border-gray-50 ${
                        i % 2 === 0 ? "" : "bg-gray-50/40"
                      }`}
                    >

                      <td className="px-4 py-3 font-mono text-gray-800 text-xs">
                        {field}
                      </td>

                      <td className="px-4 py-3">
                        <span
                          className={`inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium
                          ${
                            fieldType === "number"
                              ? "bg-blue-50 text-blue-600"
                              : fieldType === "boolean"
                              ? "bg-purple-50 text-purple-600"
                              : "bg-amber-50 text-amber-600"
                          }`}
                        >
                          {fieldType}
                        </span>
                      </td>

                      <td className="px-4 py-3 text-xs text-gray-400">
                        {uploaded.metadata?.[field]?.operators?.join(", ") ||
                          "—"}
                      </td>

                    </tr>
                  );
                })}
              </tbody>

            </table>

          </div>

        </div>
      )}

    </div>
  );
}