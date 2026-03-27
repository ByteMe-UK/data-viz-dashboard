"""
Chart components for the COVID-19 dashboard.
Each function returns a Plotly figure ready to render in Streamlit.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ── Colour palette ──────────────────────────────────────────────
PALETTE = {
    "cases": "#6C63FF",
    "deaths": "#FF6584",
    "vaccinations": "#00C9A7",
    "gradient": ["#6C63FF", "#00C9A7", "#FF6584", "#FFD93D", "#4ECDC4"],
}

LAYOUT_DEFAULTS = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#FAFAFA"),
    margin=dict(l=40, r=40, t=50, b=40),
    hoverlabel=dict(bgcolor="#1A1F2E", font_size=13),
)


def _apply_layout(fig: go.Figure, title: str) -> go.Figure:
    """Apply consistent styling to all charts."""
    fig.update_layout(title=title, **LAYOUT_DEFAULTS)
    return fig


# ── 1. World Choropleth Map ─────────────────────────────────────
def world_map(df: pd.DataFrame, metric: str, title: str) -> go.Figure:
    """Choropleth map coloured by the chosen metric."""
    fig = px.choropleth(
        df,
        locations="iso_code",
        color=metric,
        hover_name="location",
        hover_data={"iso_code": False, metric: ":,.0f", "population": ":,.0f"},
        color_continuous_scale="Viridis",
    )
    fig.update_geos(
        showcoastlines=True,
        coastlinecolor="#333",
        showland=True,
        landcolor="#1A1F2E",
        showocean=True,
        oceancolor="#0E1117",
        showframe=False,
    )
    return _apply_layout(fig, title)


# ── 2. Time-series line chart ───────────────────────────────────
def time_series(
    df: pd.DataFrame,
    countries: list[str],
    metric: str,
    title: str,
) -> go.Figure:
    """Line chart showing a metric over time for selected countries."""
    filtered = df[df["location"].isin(countries)]
    fig = px.line(
        filtered,
        x="date",
        y=metric,
        color="location",
        color_discrete_sequence=PALETTE["gradient"],
        hover_data={metric: ":,.0f"},
    )
    fig.update_traces(line=dict(width=2.5))
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text=metric.replace("_", " ").title())
    return _apply_layout(fig, title)


# ── 3. Bar chart — top N countries ──────────────────────────────
def top_countries_bar(
    df: pd.DataFrame,
    metric: str,
    n: int,
    title: str,
) -> go.Figure:
    """Horizontal bar chart of the top N countries by a metric."""
    top = df.nlargest(n, metric)
    fig = px.bar(
        top,
        x=metric,
        y="location",
        orientation="h",
        color=metric,
        color_continuous_scale="Viridis",
        hover_data={metric: ":,.0f"},
    )
    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False,
    )
    fig.update_yaxes(title_text="")
    fig.update_xaxes(title_text=metric.replace("_", " ").title())
    return _apply_layout(fig, title)


# ── 4. Continent breakdown (pie / donut) ────────────────────────
def continent_donut(
    df: pd.DataFrame,
    metric: str,
    title: str,
) -> go.Figure:
    """Donut chart showing metric distribution by continent."""
    continent_totals = df.groupby("continent")[metric].sum().reset_index()
    fig = px.pie(
        continent_totals,
        values=metric,
        names="continent",
        hole=0.45,
        color_discrete_sequence=PALETTE["gradient"],
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="%{label}: %{value:,.0f}<extra></extra>",
    )
    return _apply_layout(fig, title)


# ── 5. Daily new cases / deaths area chart ──────────────────────
def daily_area(
    df: pd.DataFrame,
    countries: list[str],
    metric: str,
    title: str,
) -> go.Figure:
    """Stacked area chart for daily new values."""
    filtered = df[df["location"].isin(countries)]
    fig = px.area(
        filtered,
        x="date",
        y=metric,
        color="location",
        color_discrete_sequence=PALETTE["gradient"],
        hover_data={metric: ":,.0f"},
    )
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text=metric.replace("_", " ").title())
    return _apply_layout(fig, title)


# ── 6. Scatter — GDP vs metric ──────────────────────────────────
def scatter_gdp(
    df: pd.DataFrame,
    metric: str,
    title: str,
) -> go.Figure:
    """Scatter plot: GDP per capita vs a COVID metric (bubble = population)."""
    plot_df = df.dropna(subset=["gdp_per_capita", metric, "population"])
    fig = px.scatter(
        plot_df,
        x="gdp_per_capita",
        y=metric,
        size="population",
        color="continent",
        hover_name="location",
        color_discrete_sequence=PALETTE["gradient"],
        size_max=50,
        hover_data={
            "gdp_per_capita": ":,.0f",
            metric: ":,.0f",
            "population": ":,.0f",
        },
    )
    fig.update_xaxes(title_text="GDP per Capita (USD)", type="log")
    fig.update_yaxes(title_text=metric.replace("_", " ").title())
    return _apply_layout(fig, title)
