# MALStatsViewer

**Live Demo:** https://malstatsviewer.onrender.com

## 🚀 Overview

This project is a full-stack web application designed to analyze and visualize data sourced from the MyAnimeList (MAL) API. It serves as a comprehensive portfolio piece demonstrating proficiency in building scalable RESTful services, integrating external APIs, managing complex data structures, and delivering a modern, responsive user experience.

The core goal was to transform raw user data (ratings, genres, etc.) into interactive, visually appealing charts to uncover trends within a user's activity.

---

## ✨ Key Features
* **Interactive Visualization:** A chart (powered by Chart.js) allows user to view the distribution of genres in their list.
* **Optimized API Integration:** Efficient, rate-limit-conscious integration with the external MyAnimeList API.
* **Data Aggregation Pipeline:** Server-side pre-calculation ensures minimal latency and reduced payload size for fast rendering on the client.
* **Responsive UI:** A clean, modern application built with HTML and Tailwind CSS for seamless use across desktop and mobile devices.

---

## 💻 Tech Stack Showcase

This project was built using a robust and modern stack, demonstrating full-stack competency across backend performance, data handling, and frontend design.

| Category | Technologies Demonstrated | Key Skills Highlighted |
| :--- | :--- | :--- |
| **Backend/Data** | **Python (Flask)**, **Data Pre-processing**, **RESTFUL API Design** | Strong server-side programming and data engineering efficiency. |
| **Frontend** | **HTML**, **JavaScript**, **Chart.js**, **Tailwind CSS** | Building responsive UIs, declarative data visualization, and utility-first styling. |
| **Deployment** | **Render** | Knowledge of CI/CD, Buildpack-based containerization, and managing production cloud infrastructure. |

---

## 🧠 Technical Deep Dive

This project demonstrates proficiency in full-stack development by clearly separating concerns into a stateless REST API and a client-side interface, ensuring high portability and maintainability.

---

1. **Backend Architecture: Flask as a Stateless API**

The backend is built with Python (Flask) and focuses solely on data processing and serving information via a clean RESTful interface.

* **Data Flow:** Raw data is imported, cleaned, and pre-processed for analysis.
* **RESTful Design:** Flask acts as the secure authorization gateway, managing the OAuth 2.0 flow to securely obtain user data from the external MAL API. It then structures this data into clean, internal JSON endpoints, maintaining a strict separation between the server-side logic and the client-side presentation.
* **Production Readiness:** The application is configured to run efficiently on Render using a production-ready WSGI server (like Gunicorn), ensuring stability and concurrency.

2. **Frontend Implementation: JavaScript & Declarative Visualization**

The presentation layer is a modern, single-page client interface built for speed and responsiveness without a heavy framework dependency.

* **Data Consumption:** The processed data is server-side rendered by Flask using the Jinja2 templating engine directly into the HTML. This provides instant access to the core data visualization upon page load, minimizing latency by avoiding additional client-side AJAX requests.
* **Visualization:** Chart.js is leveraged to handle declarative data visualization. The JavaScript logic reads the data embedded by Jinja2, then manages the state and updates the charts based on user interactions.
* **Styling:** Tailwind CSS provides utility-first styling for rapid development of a fully responsive design, ensuring a seamless experience across desktop and mobile devices.

3. **Key Challenge & Solution: Refactoring a Monolithic `index()` Function**

* **The Problem:** The initial design placed all functionalities, such as handling the external MAL API response to data cleaning, genre aggregation, and final calculation, inside the main Flask route function (`index()`). This created a monolithic function that exceeded 100 lines, which made the code difficult to debug, test, and maintain.
* **The Solution:** Data aggregation and calculation logic were placed into dedicated private helper functions. These functions were defined within the same `app.py` file, keeping the project structure minimal while ensuring the logic remained separate. The main `index()` function was reduced to only be responsible for calling the helper functions, rendering the Jinja2 template, and handling HTTP flow.
* **Lesson Learned:** By separating business logic into dedicated helper functions, the code became significantly cleaner and easier to flow, which is crucial for rapid iteration and maintanence in a small-scale application.

## 🛠️ Getting Started (For Reviewers)

To inspect the source code and run it locally:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/pr1vatestaticfinal/MALStatsViewer.git
    ```
2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configuration:** Create a `.env` file in the directory and add the client id and secret. You also have to go to MAL and register for API access and configure the redirect URI to the point to your local development address (e.g., `http://localhost:5000/callback`).
    ```
    CLIENT_ID=insertidhere
    CLIENT_SECRET=insertsecrethere
    ```
4.  **Run Application:**
    ```bash
    python app.py
    ```

---

## 👥 Contributors 

This project was collaborately developed by:
* [@pub1icstaticvoid](https://github.com/pub1icstaticvoid)
* [@pr1vatestaticfinal](https://github.com/pr1vatestaticfinal)