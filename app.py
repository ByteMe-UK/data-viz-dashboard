"""
🌍 Global COVID-19 Interactive Dashboard
Built with Streamlit & Plotly | Data from Our World in Data (OWID)

Author: Laksh Menroy
Part of the ByteMe-UK portfolio collection.
"""

import streamlit as st

from data.loader import load_data, get_latest_per_country, get_country_list, get_continent_list
from components.metrics import render_kpi_row
from components.charts import (
    world_map,
    time_series,
    top_countries_bar,
    continent_donut,
    daily_area,
    scatter_gdp,
)

# ── Page config ─────────────────────────────────────────────────
st.set_page_config(
    page_title="Global COVID-19 Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* KPI metric cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1A1F2E 0%, #252B3B 100%);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 16px 20px;
    }
    div[data-testid="stMetric"] label {
        font-size: 14px;
        color: #AAA;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 700;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0E1117;
        border-right: 1px solid #222;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Load data ───────────────────────────────────────────────────
df = load_data()

if df.empty:
    st.error("⚠️ Could not load COVID-19 data. Please try refreshing the page.")
    st.stop()

latest = get_latest_per_country(df)
countries = get_country_list(df)
continents = get_continent_list(df)

# ── Sidebar filters ─────────────────────────────────────────────
with st.sidebar:
    st.title("🌍 COVID-19 Dashboard")
    st.caption("Data from [Our World in Data](https://ourworldindata.org/covid-deaths)")

    st.divider()

    # Continent filter
    selected_continents = st.multiselect(
        "🗺️ Filter by Continent",
        options=continents,
        default=continents,
    )

    # Country selector (for time-series charts)
    default_countries = ["United Kingdom", "United States", "India", "Brazil", "Germany"]
    available_defaults = [c for c in default_countries if c in countries]
    selected_countries = st.multiselect(
        "🏳️ Select Countries (for trend charts)",
        options=countries,
        default=available_defaults[:5],
    )

    st.divider()

    # Metric selector
    metric_options = {
        "Total Cases": "total_cases",
        "Total Deaths": "total_deaths",
        "New Cases (daily)": "new_cases",
        "New Deaths (daily)": "new_deaths",
        "People Vaccinated": "people_vaccinated",
        "Fully Vaccinated": "people_fully_vaccinated",
    }
    selected_metric_label = st.selectbox(
        "📊 Primary Metric",
        options=list(metric_options.keys()),
        index=0,
    )
    selected_metric = metric_options[selected_metric_label]

    # Top N slider
    top_n = st.slider("🏆 Top N Countries", min_value=5, max_value=30, value=15)

    st.divider()
    st.caption("Built by [Laksh Menroy](https://github.com/lakshmenroy) • [ByteMe-UK](https://github.com/ByteMe-UK)")

# ── Apply continent filter ──────────────────────────────────────
filtered_df = df[df["continent"].isin(selected_continents)]
filtered_latest = latest[latest["continent"].isin(selected_continents)]

# ── Header ──────────────────────────────────────────────────────
st.markdown("# 🌍 Global COVID-19 Interactive Dashboard")
st.markdown(
    "Real-time visualisation of the global COVID-19 pandemic. "
    "Use the sidebar to filter by continent, select countries, and choose metrics."
)

# ── KPI Row ─────────────────────────────────────────────────────
render_kpi_row(filtered_latest)

st.divider()

# ── Row 1: World Map + Top Countries ───────────────────────────
col_map, col_bar = st.columns([3, 2])

with col_map:
    st.plotly_chart(
        world_map(
            filtered_latest,
            selected_metric,
            f"🗺️ World Map — {selected_metric_label}",
        ),
        use_container_width=True,
    )

with col_bar:
    st.plotly_chart(
        top_countries_bar(
            filtered_latest,
            selected_metric,
            top_n,
            f"🏆 Top {top_n} Countries — {selected_metric_label}",
        ),
        use_container_width=True,
    )

st.divider()

# ── Row 2: Time Series + Daily Area ────────────────────────────
if selected_countries:
    col_line, col_area = st.columns(2)

    with col_line:
        st.plotly_chart(
            time_series(
                filtered_df,
                selected_countries,
                selected_metric,
                f"📈 Trend — {selected_metric_label}",
            ),
            use_container_width=True,
        )

    daily_metric = "new_cases" if "cases" in selected_metric else "new_deaths"
    daily_label = "New Cases" if "cases" in selected_metric else "New Deaths"

    with col_area:
        st.plotly_chart(
            daily_area(
                filtered_df,
                selected_countries,
                daily_metric,
                f"📉 Daily {daily_label}",
            ),
            use_container_width=True,
        )
else:
    st.info("👆 Select at least one country in the sidebar to see trend charts.")

st.divider()

# ── Row 3: Continent Donut + GDP Scatter ────────────────────────
col_donut, col_scatter = st.columns(2)

with col_donut:
    st.plotly_chart(
        continent_donut(
            filtered_latest,
            selected_metric,
            f"🍩 By Continent — {selected_metric_label}",
        ),
        use_container_width=True,
    )

with col_scatter:
    st.plotly_chart(
        scatter_gdp(
            filtered_latest,
            selected_metric,
            f"💰 GDP per Capita vs {selected_metric_label}",
        ),
        use_container_width=True,
    )

# ── Footer ──────────────────────────────────────────────────────
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: #666; font-size: 13px; padding: 20px 0;">
        🌍 Global COVID-19 Dashboard — Data from
        <a href="https://ourworldindata.org/covid-deaths" target="_blank">Our World in Data</a>
        <br>Built with ❤️ by
        <a href="https://github.com/lakshmenroy" target="_blank">Laksh Menroy</a>
        • Part of the
        <a href="https://github.com/ByteMe-UK" target="_blank">ByteMe-UK</a> portfolio
    </div>
    """,
    unsafe_allow_html=True,
)
