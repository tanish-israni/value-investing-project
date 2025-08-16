Value Investing Portfolio Generator 📈

A full-stack web application that automates a quantitative value investing strategy for the Nifty 500 index. This tool empowers investors by analyzing market data to identify the most undervalued stocks and automatically generates a customized portfolio based on the user's capital.
---

🚀 About The Project

This application was built to solve the challenge of manual, time-consuming stock research. It implements a quantitative approach to value investing by systematically ranking stocks based on a variety of key financial metrics.

The core logic reads a dataset of Nifty 500 company fundamentals and calculates a unified "Relative Value (RV) Score" for each stock. This score is derived from the percentile ranks of five different metrics:

* Price-to-Earnings (P/E) Ratio
* Price-to-Book (P/B) Ratio
* Price-to-Sales (P/S) Ratio
* Enterprise Value to EBITDA (EV/EBITDA)
* Enterprise Value to Gross Profit (EV/GP)

The application then selects the top 50 stocks with the best RV Scores and allocates the user's capital, creating a diversified portfolio of high-value companies.

---

✨ Key Features

* **Secure User Authentication:** Full registration and login functionality to manage user sessions.
* **Quantitative Stock Analysis:** Ranks all 500 stocks based on a robust multi-factor value model.
* **Dynamic Portfolio Allocation:** Accepts a user's capital amount and calculates the exact number of shares to buy for each of the top 50 stocks.
* **Data Visualization:** Generates and saves a plot of the selected stocks' share prices.
* **Downloadable Results:** Allows users to download their personalized portfolio as a formatted Excel (`.xlsx`) file.
* **Responsive Frontend:** A modern UI built with HTML/CSS and Tailwind CSS for a great user experience.

---

🛠️ Built With

This project leverages a range of powerful libraries and frameworks:

* **Backend:** **Flask**
* **Data Analysis:** **Pandas**, **NumPy**
* **Data Visualization:** **Matplotlib**
* **Database:** **SQLite**
* **Excel Handling:** **XlsxWriter**, **openpyxl**
* **Frontend:** **HTML**, **CSS**, **Tailwind CSS**
* *(Note: `yfinance` is included for potential future integration to fetch live data.)*

---

⚙️ Getting Started

To get a local copy up and running, follow these simple steps.

**Prerequisites**

Ensure you have Python 3.x and pip installed on your system.

**Installation**

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/tanish-israni/value-investing-project.git]
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd your_project_name
    ```
3.  **Create and activate a virtual environment:**
    ```sh
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Initialize the Database:**
    *(You will need a small Python script to create the `users` table in the `users.db` SQLite database the first time you run it.)*

6.  **Prepare the Data:**
    Ensure you have the `nifty500_fundamental.csv` file in the root directory.

7.  **Run the application:**
    ```sh
    python app.py
    ```
    Open your browser and navigate to `http://127.0.0.1:5000`.
