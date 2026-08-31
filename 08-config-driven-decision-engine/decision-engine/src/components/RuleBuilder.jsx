import { useState } from "react";
import { saveRules } from "../api";
import { PlusIcon, TrashIcon, CheckCircleIcon } from "@heroicons/react/24/outline";

const DECISIONS = ["accept", "reject", "review"];

const createCondition = () => ({
  id: Date.now() + Math.random(),
  field: "",
  operator: "",
  value: ""
});

const createRule = () => ({
  id: Date.now() + Math.random(),
  priority: 1,
  decision: "accept",
  reason: "",
  conditions: [createCondition()]
});

export default function RuleBuilder({ schema, metadata, onRulesSaved }) {

  const [rules, setRules] = useState([createRule()]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [saved, setSaved] = useState(false);

  const fields = schema ? Object.keys(schema) : [];

  const getOperators = (field) => {
    if (!field || !metadata) return [];
    return metadata?.operators?.[field] || [];
  };

  const updateRule = (ruleId, key, value) => {
    setRules(prev =>
      prev.map(r => r.id === ruleId ? { ...r, [key]: value } : r)
    );
    setSaved(false);
  };

  const updateCondition = (ruleId, condId, key, value) => {
    setRules(prev =>
      prev.map(rule => {
        if (rule.id !== ruleId) return rule;

        return {
          ...rule,
          conditions: rule.conditions.map(c =>
            c.id === condId ? { ...c, [key]: value } : c
          )
        };
      })
    );
    setSaved(false);
  };

  const addRule = () => {
    setRules(prev => [...prev, createRule()]);
  };

  const removeRule = (ruleId) => {
    setRules(prev => prev.filter(r => r.id !== ruleId));
  };

  const addCondition = (ruleId) => {
    setRules(prev =>
      prev.map(rule =>
        rule.id === ruleId
          ? { ...rule, conditions: [...rule.conditions, createCondition()] }
          : rule
      )
    );
  };

  const removeCondition = (ruleId, condId) => {
    setRules(prev =>
      prev.map(rule =>
        rule.id === ruleId
          ? { ...rule, conditions: rule.conditions.filter(c => c.id !== condId) }
          : rule
      )
    );
  };

  const parseValue = (field, operator, value) => {

    const type = metadata?.types?.[field];

    if (operator === "between") {
      return value.map(v => Number(v));
    }

    if (type === "int") {
      return Number(value);
    }

    if (type === "bool") {
      return value === true || value === "true";
    }

    return value;
  };

  const handleSave = async () => {

    const userRules = rules.map((rule, idx) => ({
      rule_id: `R${idx + 1}`,
      priority: Number(rule.priority),
      decision: rule.decision,
      stop_on_match: true,
      reason: rule.reason || "Generated rule",
      conditions: rule.conditions.map(({ id, field, operator, value }) => ({
        field,
        operator,
        value: parseValue(field, operator, value)
      }))
    }));

    const defaultRule = {
      rule_id: "R999_DEFAULT_ACCEPT",
      priority: 999,
      decision: "accept",
      stop_on_match: true,
      reason: "Default rule – no other rules matched",
      conditions: []
    };

    const payload = {
      rules: [...userRules, defaultRule]
    };

    try {

      setLoading(true);

      const res = await saveRules(payload);

      onRulesSaved(res.rules_id);

      setSaved(true);
      setError(null);

    } catch (e) {

      setError("Failed to save rules.");

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8">

      <div className="mb-6">
        <h2 className="text-lg font-semibold text-gray-900">
          Rule Builder
        </h2>
        <p className="text-sm text-gray-400">
          Build rules using your dataset fields
        </p>
      </div>

      {!schema ? (
        <p className="text-gray-300 text-sm">
          Upload a dataset first
        </p>
      ) : (
        <>
          {rules.map((rule, ruleIndex) => (

            <div
              key={rule.id}
              className="border rounded-xl p-4 mb-4 bg-gray-50"
            >

              <div className="flex justify-between items-center mb-3">

                <h3 className="font-medium">
                  Rule #{ruleIndex + 1}
                </h3>

                <button
                  onClick={() => removeRule(rule.id)}
                  className="text-red-400 hover:text-red-600"
                >
                  <TrashIcon className="w-4 h-4" />
                </button>

              </div>

              {rule.conditions.map(cond => (

                <div
                  key={cond.id}
                  className="flex gap-3 mb-3 items-center"
                >

                  <select
                    value={cond.field}
                    onChange={(e) =>
                      updateCondition(rule.id, cond.id, "field", e.target.value)
                    }
                    className="border rounded px-3 py-2 text-sm"
                  >

                    <option value="">Field</option>

                    {fields.map(f => (
                      <option key={f} value={f}>
                        {f}
                      </option>
                    ))}

                  </select>

                  <select
                    value={cond.operator}
                    disabled={!cond.field}
                    onChange={(e) =>
                      updateCondition(rule.id, cond.id, "operator", e.target.value)
                    }
                    className="border rounded px-3 py-2 text-sm disabled:opacity-40"
                  >

                    <option value="">Operator</option>

                    {getOperators(cond.field).map(op => (
                      <option key={op} value={op}>
                        {op}
                      </option>
                    ))}

                  </select>

                  {cond.operator === "between" ? (

                    <div className="flex gap-2">

                      <input
                        type="number"
                        placeholder="Min"
                        value={cond.value?.[0] || ""}
                        onChange={(e) =>
                          updateCondition(rule.id, cond.id, "value", [
                            e.target.value,
                            cond.value?.[1] || ""
                          ])
                        }
                        className="border rounded px-3 py-2 text-sm w-24"
                      />

                      <input
                        type="number"
                        placeholder="Max"
                        value={cond.value?.[1] || ""}
                        onChange={(e) =>
                          updateCondition(rule.id, cond.id, "value", [
                            cond.value?.[0] || "",
                            e.target.value
                          ])
                        }
                        className="border rounded px-3 py-2 text-sm w-24"
                      />

                    </div>

                  ) : (

                    <input
                      type="text"
                      placeholder="Value"
                      value={cond.value}
                      onChange={(e) =>
                        updateCondition(rule.id, cond.id, "value", e.target.value)
                      }
                      className="border rounded px-3 py-2 text-sm"
                    />

                  )}

                  <button
                    onClick={() => removeCondition(rule.id, cond.id)}
                    className="text-gray-400 hover:text-red-500"
                  >
                    <TrashIcon className="w-4 h-4" />
                  </button>

                </div>

              ))}

              <button
                onClick={() => addCondition(rule.id)}
                className="text-indigo-600 text-sm flex items-center gap-1 mb-3"
              >
                <PlusIcon className="w-4 h-4" />
                Add Condition
              </button>

              <div className="flex gap-3 items-center">

                <select
                  value={rule.decision}
                  onChange={(e) =>
                    updateRule(rule.id, "decision", e.target.value)
                  }
                  className="border rounded px-3 py-2 text-sm"
                >

                  {DECISIONS.map(d => (
                    <option key={d} value={d}>
                      {d}
                    </option>
                  ))}

                </select>

                <input
                  type="number"
                  value={rule.priority}
                  onChange={(e) =>
                    updateRule(rule.id, "priority", e.target.value)
                  }
                  className="border rounded px-3 py-2 text-sm w-20"
                />

              </div>

            </div>

          ))}

          <div className="flex gap-3 mt-4">

            <button
              onClick={addRule}
              className="flex items-center gap-2 bg-indigo-50 text-indigo-600 px-4 py-2 rounded"
            >
              <PlusIcon className="w-4 h-4" />
              Add Rule
            </button>

            <button
              onClick={handleSave}
              className="bg-indigo-600 text-white px-5 py-2 rounded"
            >
              {loading ? "Saving..." : "Save Rules"}
            </button>

            {saved && (
              <span className="text-green-600 text-sm flex items-center gap-1">
                <CheckCircleIcon className="w-4 h-4" />
                Rules Saved
              </span>
            )}

          </div>

          {error && (
            <p className="text-red-500 text-sm mt-3">
              {error}
            </p>
          )}

        </>
      )}

    </div>
  );
}