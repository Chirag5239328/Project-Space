# Decision Engine UI

A polished SaaS-style React frontend for the Decision Engine backend.

## Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Start dev server
npm run dev

# 3. Open http://localhost:3000
```

The app expects your FastAPI backend to be running at `http://127.0.0.1:8000`.
To change this, edit the `API_BASE` constant in `src/api.js`.

## Project Structure

```
src/
  api.js                  # All Axios API calls
  App.jsx                 # Root layout + state management
  main.jsx                # React entry point
  index.css               # Tailwind + Google Fonts
  components/
    UploadPanel.jsx        # Step 1 – CSV upload + schema viewer
    RuleBuilder.jsx        # Step 2 – Visual rule creation
    RunPanel.jsx           # Step 3 – Engine trigger
    ResultsPanel.jsx       # Step 4 – Downloads + summary
```

## API Contract

| Step | Method | Endpoint | Notes |
|------|--------|----------|-------|
| Upload | POST | `/upload` | multipart/form-data, returns `csv_id`, `schema`, `metadata` |
| Save Rules | POST | `/rules` | body `{ rules: [...] }`, returns `rules_id` |
| Run Engine | POST | `/run` | body `{ csv_id, rules_id }`, returns `run_id` |
| Get Results | GET | `/results/{run_id}` | returns `files`, `summary`, `decisions` |
| Download | GET | `/results/{run_id}/download/{filename}` | file download |

## Notes

- `csv_id`, `rules_id`, and `run_id` are **never displayed** — they flow silently through React state.
- Each panel enables automatically once its prerequisites are complete.
- Error states are handled gracefully in every panel.
