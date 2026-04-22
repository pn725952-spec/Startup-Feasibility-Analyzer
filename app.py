import streamlit as st

from utils import (
    calculate_total_cost,
    calculate_revenue,
    calculate_profit,
    calculate_break_even,
    calculate_payback_period,
    calculate_npv,
    calculate_future_value,
    calculate_present_value,
    calculate_depreciation,
    investment_decision,
)

from charts import (
    plot_profit_chart,
    plot_depreciation_chart,
    plot_cost_pie_chart,
)

st.set_page_config(page_title="Startup Feasibility Analyzer", layout="wide")

st.title("Startup Feasibility Analyzer")
st.write("Analyze whether your startup or engineering project is profitable.")

# Sidebar Inputs
st.sidebar.header("Project Inputs")

project_name = st.sidebar.text_input(
    "Project Name",
    value="Smart Irrigation System"
)

project_category = st.sidebar.selectbox(
    "Project Category",
plot_cost_pie_chart(fixed_cost, variable_cost * units_sold)
