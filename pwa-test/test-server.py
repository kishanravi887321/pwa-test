#!/usr/bin/env python3
"""
Simple HTTPS server for testing PWA installation
Run with: python test-server.py
"""

import http.server
import ssl
import socketserver
import os

# Change to the directory containing the PWA files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8443
Handler = http.server.SimpleHTTPRequestHandler

print(f"PWA Test Server")
print(f"Serving at https://localhost:{PORT}")
print(f"")
print(f"🔗 Open in browser: https://localhost:{PORT}")
print(f"📱 For mobile testing: https://YOUR_LOCAL_IP:{PORT}")
print(f"")
print(f"To find your local IP:")
print(f"Windows: ipconfig")
print(f"Mac/Linux: ifconfig")
print(f"")
print(f"Press Ctrl+C to stop the server")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # Create self-signed certificate for HTTPS (for testing only)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    # Generate self-signed cert if it doesn't exist
    if not os.path.exists('server.pem'):
        import subprocess
        subprocess.run([
            'openssl', 'req', '-new', '-x509', '-keyout', 'server.pem', '-out', 'server.pem', 
            '-days', '365', '-nodes', '-subj', '/CN=localhost'
        ], check=False)
    
    try:
        context.load_cert_chain('server.pem')
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
    except FileNotFoundError:
        # Fallback to HTTP if SSL setup fails
        print("SSL setup failed, falling back to HTTP...")
        PORT = 8080
        print(f"🔗 Open in browser: http://localhost:{PORT}")
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()