#!/usr/bin/env python
"""
Launcher for Smart Lost and Found System Django Web Application
Internship Project: Novalis Infotech | Pavithran V (420423104056)
"""

import sys
import os
import subprocess
import webbrowser
import time

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("=" * 60)
    print("   SMART LOST AND FOUND SYSTEM - DJANGO FULL STACK")
    print("   Internship Project: Novalis Infotech | Pavithran V")
    print("=" * 60)
    print("\nStarting Django Development Server on http://127.0.0.1:8000/ ...")
    print("Press Ctrl+C to stop the server.\n")

    # Open browser after a brief delay
    def open_browser():
        time.sleep(1.5)
        webbrowser.open("http://127.0.0.1:8000/")

    import threading
    threading.Thread(target=open_browser, daemon=True).start()

    try:
        subprocess.run([sys.executable, "manage.py", "runserver", "127.0.0.1:8000"])
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    main()
