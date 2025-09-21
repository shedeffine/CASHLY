# app/finance_calculator.py

def calculate_monthly_cashflow(income: dict, expenditure: dict) -> float:
    """
    Calculates net monthly cashflow (income minus expenses).
    """
    try:
        total_income = sum(income.values()) if income else 0
        total_expenses = sum(expenditure.values()) if expenditure else 0
        return total_income - total_expenses
    except:
        return 0

def calculate_debt_to_income_ratio(monthly_debt_payments: float, monthly_income: float) -> float:
    """
    Calculates Debt-to-Income ratio as a percentage.
    """
    try:
        if monthly_income == 0:
            return 0
        return (monthly_debt_payments / monthly_income) * 100
    except:
        return 0

def calculate_emergency_coverage(total_savings: float, monthly_expenses: float) -> float:
    """
    Calculates how many months of expenses the savings can cover.
    """
    try:
        if monthly_expenses == 0:
            return 0
        return total_savings / monthly_expenses
    except:
        return 0

def identify_high_interest_debt(loans: list, threshold: float = 7.0) -> list:
    """
    Identifies loans with interest rates above the threshold.
    """
    try:
        high_interest_debt = []
        for loan in loans:
            interest_rate = loan.get('interest_rate', 0)
            if interest_rate > threshold:
                high_interest_debt.append(loan)
        return high_interest_debt
    except:
        return []

# NEW: Added the calculate_metrics function that was missing
def calculate_metrics(financial_data: dict) -> dict:
    """
    Calculate all financial metrics from the provided data.
    This is the function your main.py was trying to import.
    """
    try:
        income = financial_data.get('income', {})
        expenditure = financial_data.get('expenditure', {})
        savings = financial_data.get('savings', {})
        loans = financial_data.get('loans', [])
        
        monthly_income = sum(income.values()) if income else 0
        monthly_expenses = sum(expenditure.values()) if expenditure else 0
        total_savings = sum(savings.values()) if savings else 0
        total_monthly_debt = sum(loan.get('monthly_payment', 0) for loan in loans) if loans else 0
        
        monthly_cashflow = calculate_monthly_cashflow(income, expenditure)
        dti_ratio = calculate_debt_to_income_ratio(total_monthly_debt, monthly_income)
        emergency_coverage = calculate_emergency_coverage(total_savings, monthly_expenses)
        high_interest_debt = identify_high_interest_debt(loans)
        
        return {
            'monthly_cashflow': monthly_cashflow,
            'dti_ratio': dti_ratio,
            'emergency_coverage': emergency_coverage,
            'high_interest_debt': high_interest_debt,
            'monthly_income': monthly_income,
            'monthly_expenses': monthly_expenses,
            'total_savings': total_savings,
            'total_monthly_debt': total_monthly_debt
        }
        
    except Exception as e:
        print(f"Error in calculate_metrics: {e}")
        return {}
    