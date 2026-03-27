# 🌍 Global COVID-19 Interactive Dashboard

An interactive data dashboard visualising the **global COVID-19 pandemic** with 6 chart types, live data from Our World in Data, and continent/country-level filtering — built with **Python**, **Streamlit**, and **Plotly**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo

> 🔗 **[Open Dashboard on Streamlit Cloud →](https://byteme-uk-data-viz-dashboard.streamlit.app)**

## ✨ Features

- 🗺️ **World Choropleth Map** — colour-coded by any metric
- 📈 **Time-Series Trends** — track selected countries over time
- 🏆 **Top N Bar Chart** — see which countries lead in any metric
- 🍩 **Continent Donut Chart** — breakdown by region
- 📉 **Daily Area Chart** — stacked daily new cases/deaths
- 💰 **GDP Scatter Plot** — GDP per capita vs COVID metrics (bubble = population)
- 🦠 **KPI Cards** — total cases, deaths, vaccinations, countries tracked
- 🎛️ **Interactive Filters** — continent, country, metric, and top-N controls

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10+ | Core language |
| Streamlit | Web framework & UI |
| Plotly | Interactive charts (hover, zoom, pan) |
| Pandas | Data wrangling |
| Requests | HTTP client for data fetching |

## 📊 Data Source

Live data from **[Our World in Data (OWID)](https://ourworldindata.org/covid-deaths)** — a public COVID-19 dataset updated regularly.

- ~430K rows, 67 columns (only 14 loaded to save memory)
- Fetched live on startup, cached for 1 hour via `@st.cache_data`
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 📦 Getting Started

```bash
# Clone the repo
git clone https://github.com/ByteMe-UK/data-viz-dashboard.git
cd data-viz-dashboard

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## 📁 Project Structure

```
data-viz-dashboard/
├── app.py                     ← Entry point — page config, CSS, layout, sidebar
├── requirements.txt
├── .streamlit/
│   └── config.toml            ← Dark theme colours (primaryColor: #6C63FF)
├── data/
│   └── loader.py              ← OWID data fetch, cache, filter, helpers
├── components/
│   ├── charts.py              ← 6 Plotly chart functions
│   └── metrics.py             ← KPI cards (cases, deaths, vaccinations, countries)
├── LICENSE
└── README.md
```

## 🚢 Deploy Your Own

Free deployment on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Fork this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in
3. Click **New app** → select your fork → branch `main` → `app.py`
4. Click **Deploy** — live in ~60 seconds

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Part of the [ByteMe-UK](https://github.com/ByteMe-UK) portfolio collection.**
