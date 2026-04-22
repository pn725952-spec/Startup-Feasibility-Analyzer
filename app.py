import streamlit as st
from utils import *
from charts import *

st.set_page_config(page_title="Startup Feasibility Analyzer", layout="wide")

# --- Sidebar Inputs ---
st.sidebar.header("Project Parameters")
project_name = st.sidebar.text_input("Project Name", "New Venture")
project_category = st.sidebar.selectbox("Category", ["Manufacturing", "Tech", "Retail"])
initial_investment = st.sidebar.number_input("Initial Investment (₹)", value=1000000)
fixed_cost = st.sidebar.number_input("Monthly Fixed Cost (₹)", value=50000)
variable_cost = st.sidebar.number_input("Variable Cost per Unit (₹)", value=200)
selling_price = st.sidebar.number_input("Selling Price per Unit (₹)", value=500)
units_sold = st.sidebar.number_input("Monthly Units Sold", value=500)
interest_rate = st.sidebar.slider("Interest Rate (%)", 0.0, 20.0, 8.0)
depreciation_rate = st.sidebar.slider("Depreciation Rate (%)", 0.0, 30.0, 10.0)
project_years = st.sidebar.number_input("Duration (Years)", value=5, min_value=1)

# --- Calculations ---
revenue = calculate_revenue(selling_price, units_sold)
total_cost = calculate_total_cost(fixed_cost, variable_cost, units_sold)
monthly_profit = calculate_profit(revenue, total_cost)
break_even_units = calculate_break_even(fixed_cost, selling_price, variable_cost)
npv = calculate_npv(initial_investment, monthly_profit, interest_rate, project_years)
payback_period = calculate_payback_period(initial_investment, monthly_profit)
future_value = calculate_future_value(initial_investment, interest_rate, project_years)
present_value = calculate_present_value(future_value, interest_rate, project_years)
depreciation_values = calculate_depreciation(initial_investment, depreciation_rate, project_years)
decision = investment_decision(monthly_profit, npv, payback_period)

# --- UI Display ---
st.title("Startup Feasibility Analyzer")
st.subheader(f"Project: {project_name} | {project_category}")

m1, m2, m3 = st.columns(3)
m1.metric("Monthly Profit", f"₹ {monthly_profit:,.0f}")
m2.metric("Break-even Units", f"{break_even_units:.0f}")
m3.metric("NPV", f"₹ {npv:,.0f}")

m4, m5, m6 = st.columns(3)
m4.metric("Payback Period", f"{payback_period:.2f} Years")
m5.metric("Future Value", f"₹ {future_value:,.0f}")
m6.metric("Present Value", f"₹ {present_value:,.0f}")

st.divider()

st.subheader("Investment Decision")
if decision == "Good Investment":
    st.success(f"✅ {decision}")
elif decision == "Moderate Risk":
    st.warning(f"⚠️ {decision}")
else:
    st.error(f"❌ {decision}")

st.divider()

# --- Charts ---
st.subheader("Financial Insights")
c1, c2 = st.columns(2)
with c1:
    plot_profit_chart(monthly_profit, project_years)
with c2:
    plot_cost_pie_chart(fixed_cost, (variable_cost * units_sold))

plot_depreciation_chart(depreciation_values)
