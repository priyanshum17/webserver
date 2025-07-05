# Web Server Technology Project

This project involves setting up a Python-based web server using the Flask framework, hosting a multi-page website, and conducting a comprehensive analysis of its performance, stability, and resilience.

## Core Features

*   **Web Server:** A lightweight web server built with Flask and served by Waitress.
*   **Website:** A 5-page fan site dedicated to Rick Astley, built with HTML templates and styled with Bootstrap.
*   **Caching:** An in-memory cache to improve performance for frequently accessed pages.

## Advanced Performance Analysis

This project includes a sophisticated performance testing suite designed to analyze the server under a wide range of conditions.

### Basic Performance Testing

A simple, multi-threaded performance test is available in `tests/performance_test.py`.

### Advanced Stress & Performance Analysis

A comprehensive, "PhD-level" analysis can be run from the `advanced_test_analysis.ipynb` Jupyter Notebook. This notebook executes a battery of advanced tests from `tests/advanced_performance_tests.py`, including:

*   Network Latency Simulations
*   Traffic Spike Tests
*   Long-Duration Soak Tests
*   Payload Variation Tests
*   Mixed Workload Simulations

All results from the advanced analysis, including detailed visualizations and raw data tables, are saved to the `/tests/analytics/` directory.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install jupyter pandas matplotlib seaborn numpy
    ```

2.  **Start the web server:**
    ```bash
    python app.py
    ```

3.  **Run the analysis:**
    *   Open and run the `advanced_test_analysis.ipynb` notebook.
    ```bash
    jupyter notebook advanced_test_analysis.ipynb
    ```
