def future_investment(investment_amount, monthly_interest_rate, years):
	future_investment_value = investment_amount*(1 + monthly_interest_rate)**years
	return future_investment_value
print(future_investment	(10000, 0.78, 10))