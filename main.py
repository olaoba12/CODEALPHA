"""
PC Voice Automation AI - Main Entry Point
Automated PC control through voice and text commands
"""

import threading
import time
import sys
from fuzzywuzzy import fuzz
from Voice.speech_recognition import get_voice_input
from Battery.Battery import check_plug1, battery_Alert
from Data.data import command_phrases, list_all_commands

SIMILARITY_THRESHOLD = 85

class AutoBrain:
    """Main automation brain for command processing"""
    
    def __init__(self, use_voice=False):
        self.use_voice = use_voice
        self.running = True
    
    def process_command(self, cmd):
        """Process voice/text command and execute matching function"""
        if not cmd or not cmd.strip():
            return False
        
        best_match = None
        best_score = 0
        
        for phrase, func in command_phrases.items():
            similarity = fuzz.ratio(cmd.lower(), phrase.lower())
            if similarity > best_score:
                best_score = similarity
                best_match = (phrase, func)
        
        if best_score >= SIMILARITY_THRESHOLD and best_match:
            phrase, func = best_match
            print(f"\n[⚡] Matched: '{phrase}' ({best_score}%)")
            try:
                func()
                print(f"[✅] Command executed successfully\n")
                return True
            except Exception as e:
                print(f"[❌] Error executing command: {e}\n")
                return False
        else:
            print(f"[❌] Command not recognized (Best match: {best_score}%)\n")
            return False
    
    def run_text_mode(self):
        """Run in text input mode"""
        print("\n" + "="*60)
        print("⌨️  TEXT MODE")
        print("="*60)
        print("[INFO] Enter commands (type 'help' for list, 'exit' to quit)\n")
        
        time.sleep(2)
        
        while self.running:
            try:
                cmd = input("🔷 Enter command: ").strip()
                
                if not cmd:
                    continue
                
                if cmd.lower() in ['help', 'commands', 'list']:
                    list_all_commands()
                    continue
                elif cmd.lower() in ['exit', 'quit', 'stop']:
                    print("\n[INFO] Exiting...")
                    self.running = False
                    break
                
                self.process_command(cmd)
                
            except KeyboardInterrupt:
                print("\n[INFO] Interrupted by user")
                self.running = False
                break
            except Exception as e:
                print(f"[ERROR] {e}")


def main():
    """Main entry point"""
    
    print("\n" + "="*60)
    print("    🤖 PC VOICE AUTOMATION AI 🤖")
    print("="*60)
    print("\nChoose input mode:")
    print("1. Voice Input (🎤)")
    print("2. Text Input (⌨️)")
    print("-" * 60)
    
    try:
        choice = input("Select mode (1 or 2): ").strip()
        
        if choice == "1":
            use_voice = True
        elif choice == "2":
            use_voice = False
        else:
            print("[❌] Invalid choice. Using text mode.")
            use_voice = False
        
        brain = AutoBrain(use_voice=use_voice)
        
        threads = []
        
        main_thread = threading.Thread(target=brain.run_text_mode, name="TextInput")
        charger_thread = threading.Thread(target=check_plug1, name="ChargerMonitor")
        battery_thread = threading.Thread(target=battery_Alert, name="BatteryAlert")
        
        charger_thread.daemon = True
        battery_thread.daemon = True
        
        threads = [main_thread, charger_thread, battery_thread]
        
        for thread in threads:
            thread.start()
        
        print("\n[✅] All systems initialized\n")
        
        main_thread.join()
        
        brain.running = False
        time.sleep(1)
        print("\n[✅] Application closed\n")
        
    except KeyboardInterrupt:
        print("\n[INFO] Application interrupted")
    except Exception as e:
        print(f"\n[ERROR] Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
        sys.exit(1)
