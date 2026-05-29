"""
Battery monitoring module for system automation
Checks battery percentage, charger status, and sends alerts
"""

import psutil
import time
import threading
from datetime import datetime

# Global variables
BATTERY_ALERT_THRESHOLD = 20  # Alert when battery is below 20%
CHARGER_CHECK_INTERVAL = 5  # Check charger status every 5 seconds
BATTERY_CHECK_INTERVAL = 30  # Check battery every 30 seconds

class BatteryManager:
    """Manages battery monitoring and alerts"""
    
    def __init__(self):
        self.alert_triggered = False
    
    def get_battery_percentage(self):
        """Get current battery percentage"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                return battery.percent
            else:
                print("[ERROR] Battery information unavailable")
                return None
        except Exception as e:
            print(f"[ERROR] Getting battery percentage: {e}")
            return None
    
    def is_plugged_in(self):
        """Check if charger is plugged in"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                return battery.power_plugged
            else:
                print("[ERROR] Battery information unavailable")
                return None
        except Exception as e:
            print(f"[ERROR] Checking charger status: {e}")
            return None
    
    def battery_alert(self):
        """Continuously monitor battery and alert when low"""
        print("[INFO] Battery monitoring started...")
        while True:
            try:
                percentage = self.get_battery_percentage()
                plugged = self.is_plugged_in()
                
                if percentage is not None:
                    if percentage <= BATTERY_ALERT_THRESHOLD and not plugged:
                        if not self.alert_triggered:
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            print(f"[⚠️ ALERT] {timestamp} - LOW BATTERY: {percentage}%")
                            self.alert_triggered = True
                    else:
                        self.alert_triggered = False
                
                time.sleep(BATTERY_CHECK_INTERVAL)
            except Exception as e:
                print(f"[ERROR] Battery monitoring: {e}")
                time.sleep(BATTERY_CHECK_INTERVAL)


# Initialize battery manager
battery_manager = BatteryManager()


def check_plug1():
    """Check charger status periodically"""
    print("[INFO] Charger monitoring started...")
    while True:
        try:
            plugged = battery_manager.is_plugged_in()
            percentage = battery_manager.get_battery_percentage()
            
            if plugged:
                status_msg = f"🔌 Charger Connected - Battery: {percentage}%"
            else:
                status_msg = f"🔋 Charger Disconnected - Battery: {percentage}%"
            
            time.sleep(CHARGER_CHECK_INTERVAL)
        except Exception as e:
            print(f"[ERROR] Checking charger: {e}")
            time.sleep(CHARGER_CHECK_INTERVAL)


def battery_Alert():
    """Monitor battery and send alerts"""
    battery_manager.battery_alert()
