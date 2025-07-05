import os
import time
from flask import Flask, render_template, abort
from waitress import serve
import socket
import platform
import subprocess
import re

app = Flask(__name__)

cache = {}
CACHE_TIMEOUT = 300  # 5 minutes

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/<page_name>')
def page(page_name):
    template_name = f'{page_name}.html'

    if template_name in cache and time.time() - cache[template_name]['timestamp'] < CACHE_TIMEOUT:
        return cache[template_name]['content']

    try:
        template_path = os.path.join(app.template_folder, template_name)
        if not os.path.exists(template_path):
            abort(404)

        rendered_content = render_template(template_name)
        
        cache[template_name] = {
            'content': rendered_content,
            'timestamp': time.time()
        }
        
        return cache[template_name]['content']

    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error rendering template {template_name}: {e}")
        abort(500) # Internal Server Error

def get_network_info():
    ip_address = "Unknown"
    network_interface = "Unknown"
    try:
        system = platform.system()
        if system == "Windows":
            result = subprocess.run(["ipconfig"], capture_output=True, text=True, check=True)
            match = re.search(r'IPv4 Address[^\n]*: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', result.stdout)
            if match:
                ip_address = match.group(1)
            match_interface = re.search(r'Ethernet adapter ([^:]+):|Wireless LAN adapter ([^:]+):', result.stdout)
            if match_interface:
                network_interface = match_interface.group(1) or match_interface.group(2)
        elif system == "Darwin" or system == "Linux": # macOS or Linux
            result = subprocess.run(["ifconfig"], capture_output=True, text=True, check=True)
            # Try to find an active non-loopback interface
            match = re.search(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?broadcast.*?inet6.*?\n\s*ether.*?\n\s*media.*?\n\s*status: active', result.stdout, re.DOTALL)
            if not match:
                match = re.search(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?netmask.*?broadcast', result.stdout)
            if match:
                ip_address = match.group(1)
                # Attempt to find the interface name associated with this IP
                interface_match = re.search(r'^(\w+):.*?inet {}.*?'.format(re.escape(ip_address)), result.stdout, re.MULTILINE | re.DOTALL)
                if interface_match:
                    network_interface = interface_match.group(1)
            else:
                # Fallback for Linux if ifconfig is not detailed enough or different format
                result = subprocess.run(["ip", "addr", "show"], capture_output=True, text=True, check=True)
                match = re.search(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/\d+.*?scope global.*?\s*valid_lft.*?\s*preferred_lft.*?\s*([a-zA-Z0-9]+)', result.stdout, re.DOTALL)
                if match:
                    ip_address = match.group(1)
                    network_interface = match.group(2)

    except Exception as e:
        print(f"Could not determine network info: {e}")
    return network_interface, ip_address

if __name__ == '__main__':
    network_interface, ip_address = get_network_info()
    port = 8080
    print(f"\n--- Web Server Deployment Information ---")
    print(f"Network Interface: {network_interface}")
    print(f"Your Local IP Address: {ip_address}")
    print(f"Web Server URL (for other devices on your network): http://{ip_address}:{port}/")
    print(f"-----------------------------------------")
    print(f"Serving Flask app on http://0.0.0.0:{port}")
    serve(app, host='0.0.0.0', port=port)