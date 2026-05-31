import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="Bangladesh Economic Dashboard",
    page_icon="🇧🇩",
    layout="wide"
)

# --- Load Data ---
df = pd.read_csv("data/bangladesh_data.csv")

# --- Sidebar ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bangladesh.svg", width=80)
st.sidebar.title("Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=(2015, 2024)
)

df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown("This dashboard visualizes Bangladesh's key economic indicators from 2015 to 2024.")
st.sidebar.markdown("**Developed by:** [Azmain Tahmid Abir](https://www.linkedin.com/in/azmain-abir)")

# --- Title ---
st.title("🇧🇩 Bangladesh Economic Insights Dashboard")
st.markdown("**Data Source:** World Bank · Bangladesh Bank · EPB · BBS")
st.divider()

# --- KPI Cards ---
col1, col2, col3, col4 = st.columns(4)

col1.metric(label="GDP Growth (2024)", value="5.7%", delta="vs 5.8% last year")
col2.metric(label="Inflation (2024)", value="9.5%", delta="High", delta_color="inverse")
col3.metric(label="Remittance (2024)", value="$23.9B", delta="+10.7% YoY")
col4.metric(label="RMG Exports (2024)", value="$57B", delta="+2.5% YoY")

st.divider()

# --- GDP & Inflation Chart ---
st.subheader("📈 GDP Growth vs Inflation")
fig1 = px.line(
    df,
    x="Year",
    y=["GDP_Growth", "Inflation"],
    markers=True,
    labels={"value": "Percentage (%)", "variable": "Indicator"},
    color_discrete_map={"GDP_Growth": "#1D9E75", "Inflation": "#D85A30"}
)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# --- Two Charts Side by Side ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("💸 Remittance Inflow ($B)")
    fig2 = px.bar(
        df,
        x="Year",
        y="Remittance",
        color_discrete_sequence=["#378ADD"]
    )
    st.plotly_chart(fig2, use_container_width=True)

with col_b:
    st.subheader("📦 Exports vs Imports ($B)")
    fig3 = px.line(
        df,
        x="Year",
        y=["Exports", "Imports"],
        markers=True,
        color_discrete_map={"Exports": "#1D9E75", "Imports": "#D85A30"}
    )
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# --- Foreign Reserves ---
st.subheader("🏦 Foreign Exchange Reserves ($B)")
fig5 = px.bar(
    df,
    x="Year",
    y="Reserves",
    color="Reserves",
    color_continuous_scale=["#D85A30", "#EF9F27", "#1D9E75"]
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()

# --- Poverty Rate ---
st.subheader("🎯 Poverty Rate Over Time (%)")
fig4 = px.area(
    df,
    x="Year",
    y="Poverty_Rate",
    color_discrete_sequence=["#D4537E"]
)
st.plotly_chart(fig4, use_container_width=True)

st.divider()

# --- Raw Data Table ---
st.subheader("📊 Raw Data Table")
st.dataframe(df, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style='text-align: left;'>
    Developed by <strong><a href='https://www.linkedin.com/in/azmain-abir' 
    target='_blank' style='text-decoration: none; color: #00FF41;'>
    Azmain Tahmid Abir</a></strong>
</div>
""", unsafe_allow_html=True)