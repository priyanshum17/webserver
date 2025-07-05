# Web Server Architecture

This project utilizes a simple web server architecture based on Python's Flask framework. Flask is a lightweight WSGI web application framework, suitable for small to medium-sized applications and for learning purposes.

## Core Components

1.  **Flask Application (`app.py`):**
    *   **Routing:** Defines URL routes (e.g., `/`, `/<page_name>`) and maps them to specific Python functions.
    *   **Request Handling:** Processes incoming HTTP requests.
    *   **Template Rendering:** Uses Jinja2 templating engine to render HTML pages directly from the `templates/` directory. This replaces the previous Markdown processing, allowing for full control over HTML structure and Bootstrap integration.
    *   **Static File Serving:** Configured to serve static assets (images, CSS, JavaScript) from the `static/` directory.
    *   **In-memory Caching:** Implements a simple in-memory cache for rendered HTML templates to improve performance on repeated requests.

2.  **HTML Templates (`templates/`):**
    *   **`base.html`:** The foundational template providing the common structure (header, navigation, footer) for all pages. It includes links to Bootstrap CSS and our custom `style.css`.
    *   **Content Templates (e.g., `home.html`, `the_song.html`, `the_artist.html`, `the_meme.html`, `the_legacy.html`):** These files now directly contain the HTML content for each page. They extend `base.html` and utilize Bootstrap classes (e.g., `container`, `row`, `col-md-X`, `img-fluid`, `text-center`) for responsive layout, consistent image sizing, and professional presentation. Video embeds are also directly integrated here.

3.  **Static Assets (`static/`):**
    *   **`static/images/`:** Stores all image files used across the website.
    *   **`static/css/style.css`:** Contains custom CSS rules to enhance Bootstrap's default styling, ensuring consistent image appearance (fixed size, centering, shadows) and overall visual polish.

## Data Flow

1.  A user's web browser sends an HTTP request to the web server (e.g., `GET /the_song`).
2.  The Flask application (`app.py`) receives the request.
3.  Based on the URL, the appropriate route handler (`page` function) is invoked.
4.  The handler first checks its in-memory cache. If the requested HTML template is found and is not expired, the cached content is returned immediately.
5.  If a cache miss occurs, the handler identifies the corresponding HTML template file (e.g., `the_song.html`) in the `templates/` directory.
6.  The Jinja2 templating engine renders the specified HTML template. This process directly uses the pre-defined HTML structure and Bootstrap classes within the template.
7.  The rendered HTML page is then stored in the cache and sent back as an HTTP response to the user's browser.
8.  The browser renders the HTML, and if there are references to static assets (like images or CSS), it sends separate requests for those, which are served directly from the `static/` directory by Flask.

## Scalability and Performance Considerations

*   **WSGI Server:** For production deployment, Flask applications are typically run with a production-ready WSGI server like Gunicorn or uWSGI, fronted by a reverse proxy like Nginx or Apache.
*   **Caching:** The implemented in-memory cache helps reduce rendering time for frequently accessed pages. For larger applications, external caching solutions (e.g., Redis, Memcached) would be more suitable.
*   **CDN:** Using a Content Delivery Network (CDN) for static assets can significantly improve load times for geographically dispersed users.
*   **Database:** For dynamic content beyond static HTML, integrating a database (e.g., PostgreSQL, MySQL) would be necessary.

This architecture provides a clear separation of concerns and leverages Flask's templating capabilities with Bootstrap's styling for a robust and visually appealing web application.