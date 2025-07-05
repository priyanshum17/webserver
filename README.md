# Rick Astley Web Server Project

This project implements a simple web server designed to host a fan page dedicated to Rick Astley and his iconic song "Never Gonna Give You Up." It serves as a practical exercise for understanding web server technologies, content management, performance testing, and caching mechanisms.

## Key Features & Recent Enhancements

*   **Content Management:** Transitioned from Markdown files to direct HTML templates for all content pages, providing granular control over layout and styling.
*   **Professional Styling:** Utilizes Bootstrap for a responsive and modern design, ensuring a consistent and visually appealing user interface.
*   **Rich Media Integration:** Features an embedded YouTube video on the homepage.
*   **Consistent Image Presentation:** Images across all content pages are now uniformly sized, centered, and styled for a polished look.
*   **Comprehensive Documentation:** Includes detailed reports on architecture, performance, and project learnings.

## Project Structure

- `app.py`: The main Flask application file, handling routing and serving content.
- `requirements.txt`: Lists Python dependencies for the project.
- `SUMMARY.md`: A high-level overview of the project content.
- `templates/`: Contains all HTML templates for the web pages (e.g., `home.html`, `the_song.html`, `base.html`).
- `static/`: Stores static assets like images and custom CSS.
    - `static/images/`: All image files used across the website.
    - `static/css/`: Custom CSS for styling the application.
- `docs/`: Contains project documentation, including architecture and the final report.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd webserver
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Web Server

To start the Flask development server:

```bash
python app.py
```

The server will typically run on `http://127.0.0.1:8080/` (or another port if configured).

## Documentation

- **[Architecture Overview](docs/architecture.md)**: Details the design and components of the web server, including the use of HTML templates and Bootstrap.
- **[Project Report](docs/REPORT.md)**: A comprehensive report addressing the requirements of Problem 1, covering web server configuration, performance testing, stress testing, caching, and key learnings from the development process.