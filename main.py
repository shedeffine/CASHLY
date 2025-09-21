# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional

# Import the CORRECT functions
from app.finance_calculator import calculate_metrics  # This was missing!
from app.feedback_generator import generate_feedback

app = FastAPI(title="Financial Health API", version="1.0.0")

# Add CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Loan(BaseModel):
    name: str
    type: Optional[str] = "debt"
    monthly_payment: Optional[float] = 0
    remaining_balance: Optional[float] = 0
    interest_rate: Optional[float] = 0

class FinancialData(BaseModel):
    income: Dict[str, float] = {}
    expenditure: Dict[str, float] = {}
    savings: Dict[str, float] = {}
    loans: List[Loan] = []

class AnalysisRequest(BaseModel):
    user_id: str
    financial_data: FinancialData

@app.post("/analyze")
async def analyze_finances(request: AnalysisRequest):
    try:
        # Convert Pydantic model to dictionary for calculations
        financial_data_dict = request.financial_data.dict()
        
        # Calculate all metrics using the correct function
        calculations = calculate_metrics(financial_data_dict)
        
        # Generate feedback
        advice = generate_feedback(calculations)
        
        # Prepare response
        response = {
            "user_id": request.user_id,
            "calculations": {
                "monthly_income": calculations.get('monthly_income', 0),
                "monthly_expenses": calculations.get('monthly_expenses', 0),
                "cashflow": calculations.get('monthly_cashflow', 0),
                "debt_to_income_ratio": calculations.get('dti_ratio', 0),
                "emergency_fund_coverage": calculations.get('emergency_coverage', 0)
            },
            "feedback": advice
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Financial Health API is working! Use POST /analyze"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "financial-health-api"}
