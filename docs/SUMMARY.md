# Web Server Experience Summary

This project involved setting up a Flask web server to host a five-page website about Rick Astley's "Never Gonna Give You Up." The pages were created from Markdown files and included images. The project also involved performance testing, stress testing, and implementing a cache.

## Three Things I Learned

1.  **The Power of Caching:** The performance tests demonstrated the significant impact of caching on web server performance. With a simple in-memory cache, the average latency for page loads was nearly halved, and the throughput (requests per second) was significantly increased. This highlights the importance of caching for any web application that serves dynamic content.

2.  **The Importance of Stress Testing:** The stress test, which was designed to saturate the server, revealed a limitation not in the web server software itself, but in the operating system's networking stack. The "Can't assign requested address" error indicates that the client (the performance test script) was trying to open new connections faster than the OS could provide new ports. This is a valuable lesson in understanding that performance bottlenecks can come from unexpected places, and that stress testing is crucial for identifying them.

3.  **The Simplicity of Flask:** Flask is a lightweight and easy-to-use web framework. It was simple to set up a basic web server, and the integration with the Markdown library was straightforward. The framework's flexibility allowed for easy extension, such as adding the caching mechanism.
