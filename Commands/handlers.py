"""
Command Handlers Module
Implements automation functions for various system commands
"""

import pyautogui
import webbrowser
import subprocess
import os
import platform
import requests
import time
from datetime import datetime

SYSTEM = platform.system()

class CommandHandler:
    """Handles various system automation commands"""
    
    @staticmethod
    def open_website(url):
        """Open a website in default browser"""
        try:
            if not url.startswith('http'):
                url = 'https://' + url
            webbrowser.open(url)
            print(f"[✅] Opening website: {url}")
            return True
        except Exception as e:
            print(f"[❌] Error opening website: {e}")
            return False
    
    @staticmethod
    def open_application(app_name):
        """Open an application"""
        try:
            if SYSTEM == 'Windows':
                os.startfile(app_name)
            elif SYSTEM == 'Darwin':
                subprocess.Popen(['open', '-a', app_name])
            elif SYSTEM == 'Linux':
                subprocess.Popen([app_name])
            print(f"[✅] Opening application: {app_name}")
            return True
        except Exception as e:
            print(f"[❌] Error opening application: {e}")
            return False
    
    @staticmethod
    def get_ip_address():
        """Get current IP address"""
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            ip = response.json()['ip']
            print(f"[✅] IP Address: {ip}")
            return ip
        except Exception as e:
            print(f"[❌] Error getting IP address: {e}")
            return None
    
    @staticmethod
    def play_pause_media():
        """Play or pause media"""
        try:
            pyautogui.press('playpause')
            print("[✅] Play/Pause executed")
            return True
        except Exception as e:
            print(f"[❌] Error: {e}")
            return False
    
    @staticmethod
    def next_video():
        """Skip to next video/track"""
        try:
            pyautogui.press('nexttrack')
            print("[✅] Next track executed")
            return True
        except Exception as e:
            print(f"[❌] Error: {e}")
            return False
    
    @staticmethod
    def previous_video():
        """Go to previous video/track"""
        try:
            pyautogui.press('prevtrack')
            print("[✅] Previous track executed")
            return True
        except Exception as e:
            print(f"[❌] Error: {e}")
            return False
    
    @staticmethod
    def open_new_tab():
        """Open new browser tab"""
        try:
            pyautogui.hotkey('ctrl', 't')
            print("[✅] New tab opened")
            return True
        except Exception as e:
            print(f"[❌] Error: {e}")
            return False
    
    @staticmethod
    def close_tab():
        """Close current tab"""
        try:
            pyautogui.hotkey('ctrl', 'w')
            print("[✅] Tab closed")
            return True
        except Exception as e:
            print(f"[❌] Error: {e}")
            return False
    
    @staticmethod
    def refresh_page():
        """Refresh current page"""
        try:
            pyautogui.press('f5')
            print("[✅] Page refreshed")
            return True
        except Exception as e:
            print(f"[❌] Error: {e}")
            return False
    
    @staticmethod
    def get_random_joke():
        """Get and display a random joke"""
        try:
            response = requests.get('https://official-joke-api.appspot.com/random_joke', timeout=5)
            joke = response.json()
            full_joke = f"{joke['setup']} ... {joke['punchline']}"
            print(f"[😄] {full_joke}")
            return full_joke
        except Exception as e:
            print(f"[❌] Error getting joke: {e}")
            return None
    
    @staticmethod
    def screenshot():
        """Take a screenshot"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            pyautogui.screenshot(filename)
            print(f"[✅] Screenshot saved: {filename}")
            return filename
        except Exception as e:
            print(f"[❌] Error taking screenshot: {e}")
            return None


handler = CommandHandler()
