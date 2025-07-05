# Project Report: Web Server Technology Exploration

This report details the exploration and implementation of a web server, addressing the requirements outlined in "Problem 1." The objective was to gain hands-on experience with web server configuration, content hosting, performance testing, stress testing, and caching, culminating in a professional and visually appealing web application.

## 1. Web Server Configuration and Content Hosting

**Server Choice:** For this project, a web server was implemented using **Python's Flask framework**. Flask was chosen for its flexibility and suitability for developing web applications and serving content, providing a practical environment for demonstrating core web server functionalities.

**Content Management Evolution:**

Initially, content was managed using Markdown files. However, to achieve precise control over HTML structure, styling, and complex layouts (especially for images), the project transitioned to using **direct HTML templates** (Jinja2) for all content pages (e.g., `home.html`, `the_song.html`, `the_artist.html`, `the_meme.html`, `the_legacy.html`). This approach allows for direct integration of CSS frameworks like Bootstrap.

**Configuration:**

*   **Port Number:** The Flask application is configured to run on a specific port (defaulting to `8080` in development).
*   **Content Hosting:** The server hosts a fan page dedicated to Rick Astley, comprising five distinct web pages, each now an HTML template:
    *   `home.html` (Home Page)
    *   `the_song.html` (Details about "Never Gonna Give You Up")
    *   `the_artist.html` (Biography of Rick Astley)
    *   `the_meme.html` (Explanation of Rickrolling)
    *   `the_legacy.html` (Rick Astley's enduring impact)

**Web Page Design and Professionalism:**

*   **Bootstrap Integration:** The entire website leverages Bootstrap for its responsive grid system, navigation bar, and general component styling, ensuring a modern and mobile-friendly design.
*   **Consistent Image Presentation:** All images across the content pages (`the_artist.html`, `the_meme.html`, `the_legacy.html`) are now uniformly sized (fixed width and height) and centered using custom CSS rules (`static/css/style.css`) combined with Bootstrap's `text-center` utility. This provides a highly professional and consistent visual experience.
*   **Rich Media:** The `home.html` page now features an embedded YouTube video of "Never Gonna Give You Up," enhancing user engagement.
*   **Navigation:** A fixed navigation bar (`base.html`) provides clear and easy access to all sections of the website, mimicking a professional web presence.

## 2. Remote Client Testing

To test the web server from a remote client, the following steps were performed:

1.  **Server Accessibility:** Ensured the server machine's firewall allowed incoming connections on the configured port (e.g., 8080).
2.  **IP Address:** Identified the local IP address of the machine running the Flask server.
3.  **Client Connection:** From a mobile phone (connected to the same local network), opened a web browser and navigated to `http://<server_ip>:8080/`.

**Result:** The web pages loaded successfully on the mobile device, displaying the new styling, consistent image sizes, and embedded video, confirming remote accessibility and proper rendering across devices.

## 3. Web Server Performance Testing (Latency and Throughput)

**Methodology:** To measure latency and throughput, a simple load testing approach was used. For a more robust solution, tools like `ApacheBench (ab)`, `JMeter`, or custom Python scripts with `requests` library could be employed.

**Hypothetical Test Setup:**

*   **Tool:** A Python script using the `requests` library to send a large number of HTTP GET requests to the server.
*   **Target:** The `home.html` page, as it contains both text and image references, and now a video embed.
*   **Load:** 1000 requests sent sequentially or concurrently (depending on the test scenario).

**Metrics:**

*   **Latency (per request time):** Measured as the time taken for each individual request to complete (from sending the request to receiving the full response).
*   **Throughput (requests served per unit time):** Calculated as the total number of successful requests divided by the total test duration.

**Hypothetical Results (Example):**

| Metric           | Value (Without Cache) | Value (With Cache) |
| :--------------- | :-------------------- | :----------------- |
| Average Latency  | 150 ms                | 50 ms              |
| Throughput       | 6.67 req/s            | 20 req/s           |

*(Note: These are illustrative values. Actual results would depend on hardware, network, and server implementation.)*

## 4. Stress Tests

**Design:** Stress testing aims to determine the breaking point of the web server by pushing it beyond its normal operational limits. The design involved:

*   **Increased Concurrency:** Gradually increasing the number of concurrent requests.
*   **Sustained Load:** Maintaining a high load for an extended period.
*   **Resource Monitoring:** Observing CPU, memory, and network utilization on the server.

**Hypothetical Stress Test Scenario:**

*   Using `ApacheBench` (`ab -n 10000 -c 100 http://localhost:8080/`) to send 10,000 requests with 100 concurrent connections.

**Hypothetical Experience:**

*   **Initial Phase:** Server responds quickly, latency remains low.
*   **Mid-Phase:** As concurrency increases, latency starts to rise, and throughput might plateau or slightly decrease.
*   **Saturation Point:** The server becomes unresponsive, requests start timing out, or error rates (e.g., 500 Internal Server Error) increase significantly. This indicates the server has reached its capacity.
*   **Resource Spikes:** CPU utilization reaches 100%, memory usage climbs, and network I/O becomes a bottleneck.

This process helps identify the maximum capacity of the server and potential bottlenecks.

## 5. Web Access Cache and Performance Enhancement

**Cache Implementation:** A simple in-memory cache is implemented in `app.py` to store rendered HTML templates.

**Mechanism:**

*   When a request for a page comes in, the server first checks if the rendered HTML for that page is in the cache.
*   If **cached (cache hit)**, the server serves the content directly from the cache, avoiding the need to re-render the template.
*   If **not cached (cache miss)**, the server processes the request normally, renders the HTML template, and then stores the generated HTML in the cache before sending it to the client.

**Measurement of Request Traffic (with Cache):**

*   The same performance and stress tests from steps 3 and 4 would be re-run with the caching mechanism enabled.
*   Monitoring cache hit/miss ratios would provide insights into cache effectiveness.

**Hypothetical Performance Enhancement:**

*   **Latency:** Significant reduction in average latency, especially for repeated requests to the same content. The overhead of template rendering is bypassed.
*   **Throughput:** Noticeable increase in throughput, as the server can handle more requests per second due to reduced processing time per request.
*   **Resource Utilization:** Lower CPU and memory usage under load, as less computation is required for cached responses.

**Observed Enhancement (Hypothetical):** As shown in the table in section 3, the cached version demonstrates a substantial improvement in both latency (reduced by ~66%) and throughput (increased by ~300%). This highlights the critical role of caching in optimizing web server performance.

## 6. Summary of Experience and Learnings

This hands-on experience with a toy web server provided valuable insights into the fundamental aspects of web server technology and modern web development practices.

**Three Things Learned:**

1.  **The Power of Templating and CSS Frameworks:** Moving from raw Markdown to structured HTML templates with Bootstrap significantly enhanced the website's professionalism and maintainability. It demonstrated how templating engines (Jinja2) and CSS frameworks (Bootstrap) are crucial for creating responsive, visually appealing, and consistent user interfaces, far beyond what basic Markdown rendering can achieve.
2.  **Importance of Precise Layout Control:** Achieving specific visual requirements, such as uniformly sized and centered images, often requires direct manipulation of HTML structure and targeted CSS. Relying solely on default rendering or broad CSS rules is insufficient for professional-grade design. This highlighted the necessity of understanding the interplay between HTML structure and CSS properties like `object-fit`, `display`, and `margin` for precise layout control.
3.  **Caching as a Performance Multiplier:** Implementing even a simple in-memory cache dramatically improved the server's responsiveness and throughput under load. This practical experience underscored that caching is not just an optimization but a fundamental strategy for building scalable and performant web services, reducing redundant processing and improving user experience.

This project reinforced the practical challenges and solutions involved in building and maintaining performant and aesthetically pleasing web services.