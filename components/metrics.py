"""
KPI metric cards for the dashboard header.
"""

import streamlit as st
import pandas as pd


def format_number(n: float) -> str:
    """Format large numbers with K/M/B suffixes."""
    if pd.isna(n):
        return "N/A"
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f}B"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return f"{n:,.0f}"


def render_kpi_row(latest: pd.DataFrame) -> None:
    """Render a row of KPI metric cards."""
    total_cases = latest["total_cases"].sum()
    total_deaths = latest["total_deaths"].sum()
    total_vaccinated = latest["people_fully_vaccinated"].sum()
    countries_count = latest["location"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🦠 Total Cases",
            value=format_number(total_cases),
        )
    with col2:
        st.metric(
            label="💀 Total Deaths",
            value=format_number(total_deaths),
        )
    with col3:
        st.metric(
            label="💉 Fully Vaccinated",
            value=format_number(total_vaccinated),
        )
    with col4:
        st.metric(
            label="🌍 Countries Tracked",
            value=f"{countries_count}",
        )
