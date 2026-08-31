import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

const client = axios.create({
  baseURL: API_BASE,
});

/* Upload CSV */
export const uploadCSV = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await client.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return res.data;
};

/* Save Rules */
export const saveRules = async (rules) => {
  const res = await client.post("/rules", rules);
  return res.data;
};

/* Run Decision Engine */
export const runEngine = async (csv_id, rules_id) => {
  const res = await client.post("/run", {
    csv_id,
    rules_id,
  });

  return res.data;
};

/* Get Run Results */
export const getResults = async (run_id) => {
  const res = await client.get(`/results/${run_id}`);
  return res.data;
};

/* Download files */
export const getDownloadUrl = (run_id, filename) => {
  return `${API_BASE}/results/${run_id}/download/${filename}`;
};