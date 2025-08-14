# Stock Market Dashboard

## Overview

This project is a web-based **Stock Market Dashboard** that allows users to visualize and analyze stock price trends over time. The application provides interactive charts, a search option for different stock symbols, and a clean UI for better user experience.

---

## Development Approach

The development started with designing a **simple, responsive frontend** using HTML, Tailwind CSS, and Chart.js to create interactive charts. The **Flask backend** was implemented to serve dynamic stock data via REST APIs. The backend fetches stock prices (in this demo, from a sample dataset), processes them, and sends the data in JSON format to the frontend for visualization.

The approach was **modular**—the frontend and backend are kept separate, connected through AJAX requests. This ensures scalability and flexibility for integrating real-time stock APIs in the future.

---

## 🛠 Technologies Used

- **Frontend:** HTML, Tailwind CSS, Chart.js, JavaScript
- **Backend:** Python, Flask
- **Data:** CSV sample dataset (can be replaced with live APIs)
- **Version Control:** Git & GitHub

---

## ⚡ Challenges Encountered

1. **Chart.js Data Formatting:** Initially faced issues with mismatched labels and data points; solved by synchronizing date formats between backend and frontend.
2. **CORS Policy in Flask:** Encountered cross-origin issues when fetching data; fixed using Flask-CORS.
3. **Responsive UI:** Ensuring the dashboard looked good on all devices required Tailwind utility classes for better flexibility.

---
