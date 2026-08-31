from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import upload, rules, run, results


app = FastAPI(title="Decision Engine API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload.router)
app.include_router(rules.router)
app.include_router(run.router)
app.include_router(results.router)