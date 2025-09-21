# app/feedback_generator.py

def generate_detailed_feedback(calculations):
    """
    Generates a list of detailed financial suggestions based on a user's calculated metrics.
    
    Args:
        calculations (dict): A dictionary containing key financial metrics.
    
    Returns:
        list: A list of strings, each containing a detailed piece of financial advice.
    """
    feedback_list = []
    
    monthly_income = calculations.get('monthly_income', 0)
    monthly_expenses = calculations.get('monthly_expenses', 0)
    net_cashflow = calculations.get('net_cashflow', 0)
    dti_percent = calculations.get('debt_to_income_ratio_percent', 0)
    emergency_coverage = calculations.get('emergency_fund_coverage_months', 0)

    # 1. Analyze Cash Flow and Income
    if net_cashflow > 0:
        feedback_list.append(
            f"💰 **Excellent!** Your monthly cash flow is a strong ${net_cashflow:.0f}. This indicates you're earning more than you spend, which is a key to building wealth."
        )
    else:
        feedback_list.append(
            f"⚠️ **Urgent Action Needed.** Your expenses are exceeding your income by ${abs(net_cashflow):.0f} per month. To fix this, create a budget to identify where you can cut back, or explore ways to increase your earnings."
        )
        
    # 2. Evaluate Emergency Fund Coverage
    if emergency_coverage >= 6:
        feedback_list.append(
            f"🛡️ **Fortified Emergency Fund!** Your savings cover {emergency_coverage:.1f} months of expenses. You're well-prepared for unexpected events like job loss or medical emergencies. Consider redirecting new savings towards investments."
        )
    elif emergency_coverage >= 3:
        feedback_list.append(
            f"👍 **Good Start on Your Safety Net.** You have {emergency_coverage:.1f} months of expenses saved. Aim to increase this to 6 months to ensure a solid financial cushion."
        )
    else:
        feedback_list.append(
            f"🚧 **Time to Build Your Safety Net.** Your emergency fund covers only {emergency_coverage:.1f} months. Your primary financial goal should be to save at least 3 months of essential living expenses as a protective buffer."
        )

    # 3. Assess Debt-to-Income (DTI) Ratio
    if dti_percent < 15:
        feedback_list.append(
            f"📈 **Your Debt is Healthy.** With a DTI of just {dti_percent:.1f}%, your debt burden is low. Consider using your positive cash flow to accelerate payments on high-interest loans."
        )
    elif dti_percent < 35:
        feedback_list.append(
            f"🤔 **Manageable Debt.** Your DTI is {dti_percent:.1f}%. While this is considered manageable, focus on a clear debt repayment strategy, especially for high-interest loans, to improve your financial freedom."
        )
    else:
        feedback_list.append(
            f"🚨 **High Debt Warning!** Your DTI is {dti_percent:.1f}%. This indicates a significant portion of your income is going to debt. Prioritize creating a budget and a focused debt repayment plan immediately. "
        )

    # 4. Provide a forward-looking action item
    if net_cashflow > 0 and emergency_coverage >= 3:
        feedback_list.append(
            "💡 **Next Steps for Financial Growth.** With your solid foundation, it's a great time to explore investment options like a retirement account or low-cost index funds to build long-term wealth."
        )
    
    return feedback_list
