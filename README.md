@'
# Vehicle Advertisement Dashboard

This repository contains a Streamlit web application created for the TripleTen Software Development Tools project.

## Live Application

The deployed Streamlit app is available here:

https://tripleten-dataanalysis-chapter7-project.onrender.com

## Project Description

The project analyzes a dataset of used vehicle advertisements. The dashboard allows users to explore vehicle prices and the relationship between price and odometer readings.

The application includes:

- A price distribution histogram
- A price vs. odometer scatter plot
- A checkbox that changes chart behavior by excluding vehicles priced above $100,000
- An optional raw data display

## Dataset

The project uses the `vehicles_us.csv` dataset. The file is stored in the root directory of this repository.

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly Express
- Render
- GitHub

## Repository Structure

```text
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml