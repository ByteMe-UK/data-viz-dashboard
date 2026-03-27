"""
Data loader module for COVID-19 dashboard.
Fetches and caches data from Our World in Data (OWID) public dataset.
"""

import io
import streamlit as st
import pandas as pd
import requests


# OWID COVID-19 public dataset (CSV hosted on GitHub — always up to date)
DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

# Columns we actually need (keeps memory low)
COLUMNS = [
    "iso_code",
    "continent",
    "location",
    "date",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_vaccinations",
    "people_vaccinated",
    "people_fully_vaccinated",
    "population",
    "gdp_per_capita",
    "life_expectancy",
]


@st.cache_data(ttl=3600, show_spinner="Loading COVID-19 data...")
def load_data() -> pd.DataFrame:
    """
    Load and clean the OWID COVID-19 dataset.
    Uses requests library for reliable HTTPS downloads.
    Cached for 1 hour to avoid re-downloading on every interaction.
    """
    try:
        response = requests.get(DATA_URL, timeout=30)
        response.raise_for_status()
        df = pd.read_csv(
            io.StringIO(response.text),
            usecols=COLUMNS,
            parse_dates=["date"],
        )
    except Exception as e:
        st.error(f"❌ Failed to load data from OWID: {e}")
        return pd.DataFrame(columns=COLUMNS)

    # Drop aggregate rows (World, continents, income groups)
    aggregates = [
        "World", "Asia", "Africa", "Europe", "North America",
        "South America", "Oceania", "European Union",
        "High income", "Upper middle income",
        "Lower middle income", "Low income",
    ]
    df = df[~df["location"].isin(aggregates)].copy()

    # Drop rows with no continent (non-country entries)
    df = df.dropna(subset=["continent"])

    # Sort by location and date
    df = df.sort_values(["location", "date"]).reset_index(drop=True)

    return df


def get_latest_per_country(df: pd.DataFrame) -> pd.DataFrame:
    """Get the most recent data point for each country."""
    return df.groupby("location").last().reset_index()


def get_country_list(df: pd.DataFrame) -> list[str]:
    """Return sorted list of unique country names."""
    return sorted(df["location"].unique().tolist())


def get_continent_list(df: pd.DataFrame) -> list[str]:
    """Return sorted list of unique continent names."""
    return sorted(df["continent"].dropna().unique().tolist())
