# Temperature Dashboard

An interactive web dashboard built with Python and Dash that displays temperature data over time. It shows a line chart alongside a summary of the minimum, maximum and average temperature.

## Features

- Line chart of daily temperature built with Plotly Express
- Summary statistics showing min, max and average temperature
- Statistics calculated directly from the data with pandas
- Runs locally in the browser, with no database or external data needed

## Tech Stack

- Python
- Dash
- Plotly Express
- pandas

## Getting Started

### Requirements

- Python 3.8 or newer

### Installation

```bash
git clone https://github.com/beeboo7/temperature-dashboard.git
cd temperature-dashboard
pip install -r requirements.txt
```

### Run the app

```bash
python TemperatueData.py
```

Then open [http://127.0.0.1:8050](http://127.0.0.1:8050) in your browser. Press `Ctrl + C` in the terminal to stop it.

## Project Structure

```
temperature-dashboard/
├── TemperatureData.py             # Dash app: data, layout and callback
├── requirements.txt   # Dependencies
└── README.md
```

## How It Works

- Sample temperature readings (date, temperature, city) are stored in a pandas DataFrame.
- The layout has a heading, a graph and a text area for the summary.
- A callback builds the line chart with `px.line` and calculates the min, max and average with pandas, then returns both to the page.

For the sample data, the summary reads: `Min: 22 C | Max: 27 C | Avg: 24.20 C`.

## Possible Improvements

- Add a city dropdown to filter the data (the dataset already has a City column)
- Load temperature data from a CSV file or weather API instead of hardcoding it
- Style the summary as a proper card with separate boxes for min, max and average
- Add a date range selector

## Author

Aimee Teppo
