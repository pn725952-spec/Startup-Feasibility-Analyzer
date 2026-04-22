import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Helper Functions ---
def calculate_npv(rate, initial_investment, monthly_profit, years):
    annual_cash_flow = monthly_profit * 12
    cash_flows = [-initial_investment] + [annual_cash_flow] * years
    return np.npv(rate / 100, cash_flows)

def calculate_payback_period(initial_investment, monthly_profit):
    annual_profit = monthly_profit * 12
    if annual_profit <= 0:
        return float('inf')
    return initial_investment / annual_profit

def investment_decision(monthly_profit, npv, payback_period):
    if npv > 0 and payback_period < 5:
        return "Good Investment"
    elif npv > 0 or monthly_profit > 0:
        return "Moderate Risk"
    else:
        return "Poor Investment"

# --- 2. Sidebar Inputs ---
st.sidebar.header("Project Inputs")
project_name = st.sidebar.text_input("Project Name", "New Factory Line")
project_category = st.sidebar.selectbox("Category", ["Manufacturing", "Tech", "Retail"])
initial_investment = st.sidebar.number_input("Initial Investment (₹)", value=1000000)
fixed_cost = st.sidebar.number_input("Monthly Fixed Cost (₹)", value=50000)
variable_cost_per_unit = st.sidebar.number_input("Variable Cost per Unit (₹)", value=200)
selling_price = st.sidebar.number_input("Selling Price per Unit (₹)", value=500)
units_sold = st.sidebar.number_input("Monthly Units Sold", value=500)
interest_rate = st.sidebar.slider("Interest Rate (%)", 0.0, 20.0, 8.0)
project_years = st.sidebar.number_input("Project Duration (Years)", value=5)

# --- 3. Calculations ---
monthly_profit = (units_sold * (selling_price - variable_cost_per_unit)) - fixed_cost
break_even_units = fixed_cost / (selling_price - variable_cost_per_unit) if selling_price > variable_cost_per_unit else 0

# Financial Metrics
# Future Value Formula: FV = PV * (1 + r)^n
future_value = initial_investment * ((1 + (interest_rate / 100)) ** project_years)
# Present Value Formula: PV = FV / (1 + r)^n
present_value = initial_investment # Simplified for this context

npv = calculate_npv(interest_rate, initial_investment, monthly_profit, project_years)
payback_period = calculate_payback_period(initial_investment, monthly_profit)
decision = investment_decision(monthly_profit, npv, payback_period)

# --- 4. Display Metrics ---
st.title("Financial Analysis Dashboard")
st.subheader(f"Project: {project_name}")
st.caption(f"Category: {project_category}")

col1, col2, col3 = st.columns(3)
col1.metric("Monthly Profit", f"₹ {monthly_profit:,.0f}")
col2.metric("Break-even Units", f"{break_even_units:.0f}")
col3.metric("NPV", f"₹ {npv:,.0f}")

col4, col5, col6 = st.columns(3)
col4.metric("Payback Period", f"{payback_period:.2f} years")
col5.metric("Future Value", f"₹ {future_value:,.0f}")
col6.metric("Present Value", f"₹ {present_value:,.0f}")

# --- 5. Decision Output ---
st.subheader("Investment Decision")
if decision == "Good Investment":
    st.success(f"✅ {decision}")
elif decision == "Moderate Risk":
    st.warning(f"⚠️ {decision}")
else:
    st.error(f"❌ {decision}")

# --- 6. Charts ---
st.subheader("Financial Visualizations")

# Cost Distribution Pie Chart
fig1, ax1 = plt.subplots()
variable_cost_total = variable_cost_per_unit * units_sold
ax1.pie([fixed_cost, variable_cost_total], labels=['Fixed Cost', 'Variable Cost'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
st.pyplot(fig1)

# Profit Projection Line Chart
years = np.arange(1, project_years + 1)
cumulative_profit = (monthly_profit * 12 * years) - initial_investment
st.line_chart(pd.DataFrame({"Cumulative Profit": cumulative_profit}, index=years))
