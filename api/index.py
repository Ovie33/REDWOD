from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from typing import List, Dict, Any
import os

app = FastAPI(title="HR Expenses API")

# Path to the root directory
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(BASE_PATH, 'index.html'))

@app.get("/style.css")
async def read_css():
    return FileResponse(os.path.join(BASE_PATH, 'style.css'))


# Allow CORS so the local HTML file can fetch from this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def read_root():
    return {"message": "HR Expenses API is running"}

@app.get("/api/recent-expenses")
def get_recent_expenses() -> List[Dict[str, Any]]:
    """
    Returns mock data for the Recent Expenses table on the dashboard.
    """
    return [
        {
            "id": "HRE-00001",
            "name": "⚡ Staff welfare support [FROM API]",
            "type": "Welfare",
            "employee": "—",
            "department": "HR",
            "projectSite": "Lagos Office",
            "amount": 2091000,
            "status": "Approved",
            "date": "2025-06-16"
        },
        {
            "id": "HRE-00002",
            "name": "Training reimbursement",
            "type": "Bonuses",
            "employee": "Adaeze Ibrahim",
            "department": "Finance",
            "projectSite": "Port Harcourt Site",
            "amount": 479000,
            "status": "Approved",
            "date": "2025-06-15"
        },
        {
            "id": "HRE-00003",
            "name": "Site transport allowance",
            "type": "Incentives",
            "employee": "Olumide Bello",
            "department": "Admin",
            "projectSite": "Uyo Site",
            "amount": 681000,
            "status": "Pending",
            "date": "2025-06-15"
        },
        {
            "id": "HRE-00004",
            "name": "Recruitment interview logistics",
            "type": "Severance",
            "employee": "—",
            "department": "Procurement",
            "projectSite": "Abuja Office",
            "amount": 1051000,
            "status": "Approved",
            "date": "2025-06-14"
        },
        {
            "id": "HRE-00005",
            "name": "Staff medical support",
            "type": "Welfare",
            "employee": "Tunde Adeyemi",
            "department": "IT",
            "projectSite": "Warri Project",
            "amount": 1103000,
            "status": "Approved",
            "date": "2025-06-13"
        },
        {
            "id": "HRE-00006",
            "name": "Outstation accommodation",
            "type": "Outstation Allowance",
            "employee": "Ngozi Eze",
            "department": "Engineering",
            "projectSite": "Eket Project",
            "amount": 2441000,
            "status": "Pending",
            "date": "2025-06-12"
        }
    ]

@app.get("/api/dashboard-metrics")
def get_dashboard_metrics() -> Dict[str, Any]:
    """
    Returns mock data for the 4 top KPI cards.
    """
    return {
        "total_expenses": {"value": 372932000, "label": "300 records"},
        "approved_paid": {"value": 213911000, "label": "150 approved"},
        "pending_review": {"value": 70, "label": "Awaiting action"},
        "total_paid_out": {"value": 60673000, "label": "50 paid"}
    }
