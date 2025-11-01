# MALStatsViewer

[![Project Status](https://img.shields.io/badge/Status-Alpha_Build-red)](https://github.com/pr1vatestaticfinal/MALStatsViewer)

**MAL Stats Viewer** is an interactive web application designed to visualize user data in a concise and visually appealing way using MyAnimeList's API, summarizing a user's activity over a period of time.

***

## ⚠️ Alpha Notice

*This project is currently in the **Alpha stage**. The primary focus is on implementing core functionality and data reliability.*

- Expect **frequent, breaking changes** to the API and configuration.
- The **CSS and user interface are actively being developed** and are subject to change.
- Possible **bugs may occur** and will be fixed when discovered.

***

## 🚀 Getting Started

Since the current build of the project runs locally, this guide will get a local copy running on your machine.

### Prerequisites
- Python 3.12 or higher: We recommend installing the latest version of Python.
  - **Standard Install (Recommended):** Download the official installer from [Python Downloads](https://www.python.org/downloads).
  - **Microsoft Store (Windows Only):** For a simple, no-admin install, you may use the Microsoft Store.
- Contact us for the `.env` file as you need the keys from the MyAnimeList API to load user data.

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/pr1vatestaticfinal/MALStatsViewer.git
    cd MALStatsViewer
    ```

2.  **Install dependencies:**
    ```bash
    pip install Flask
    pip install requests
    pip install python-dotenv
    ```
3.  **Configuration:**

    Put the `.env` file in the root directory of the project.

### Running the App

Start the application by using the following command:
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000.

***

## 💻 Technical Details

This section outlines the current data focus and visualization capabilities in the Alpha build.

### Data & API Focus

**Data Source:** MyAnimeList API

| Component | Technology|
| :--- | :--- |
| **Backend** | Flask (Python) |
| **Frontend Rendering** | Jinja2 Templates (HTML/CSS/JS) |
| **Data Visualization** | **Chart.js** (JavaScript Library)|

### Key Insights & Features

| Visualization Feature | Description |
| :--- | :--- |
| **Entry Count** | The total number of entries tracked in the database. |
| **Genre Distribution** | A chart showing the breakdown of entries by genre. |
| **Top 10 Highest Rated** | A ranked list of display the top 10 entries by user score. |
| **Top 10 Recent** | A ranked list displaying the top 10 most recently added entries. |
| **Time Period Filter** | Ability to filter displayed data to reflect entries made within a date range. |

***

## 📆 Roadmap (Alpha Focus)

Our current development efforts are concentrated on the following milestones:
- Finalize types of data displayed
- Adjust and update CSS design of charts and website
- Deploy app on server

Beta (Target Q1 2026): Transition to Beta once all core visualizations are implemented and the UI is stable.

***

## ⚖️ License

Distributed under us lol
