import numpy_financial as npf


def calculate_total_cost(fixed_cost, variable_cost, units_sold):
    return fixed_cost + (variable_cost * units_sold)


def calculate_revenue(selling_price, units_sold):
    return selling_price * units_sold


def calculate_profit(revenue, total_cost):
    return revenue - total_cost


def calculate_break_even(fixed_cost, selling_price, variable_cost):
    if selling_price == variable_cost:
        return 0
    return fixed_cost / (selling_price - variable_cost)


def calculate_payback_period(initial_investment, monthly_profit):
    if monthly_profit <= 0:
        return 0
    return initial_investment / (monthly_profit * 12)


def calculate_npv(initial_investment, monthly_profit, interest_rate, years):
    cash_flows = [-initial_investment]
    annual_profit = monthly_profit * 12

    for _ in range(years):
        cash_flows.append(annual_profit)

    return npf.npv(interest_rate / 100, cash_flows)


def calculate_future_value(initial_investment, interest_rate, years):
    return initial_investment * ((1 + interest_rate / 100) ** years)


def calculate_present_value(future_value, interest_rate, years):
    return future_value / ((1 + interest_rate / 100) ** years)


def calculate_depreciation(initial_value, depreciation_rate, years):
    values = []
    current_value = initial_value

    for _ in range(years):
        current_value = current_value * (1 - depreciation_rate / 100)
        values.append(current_value)

    return values


def investment_decision(monthly_profit, npv, payback_period):
    if monthly_profit > 50000 and npv > 0 and payback_period < 3:
        return "Good Investment"
        return "High Risk"
