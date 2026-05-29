"""
Voice Recognition Module
Converts speech to text using Google Speech Recognition
"""

import speech_recognition as sr
from datetime import datetime
import threading
import time

class VoiceRecognizer:
    """Handles voice input and speech-to-text conversion"""
    
    def __init__(self, language='en-US'):
        """
        Initialize voice recognizer
        Args:
            language: Language code (default: 'en-US')
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        self.is_listening = False
        self.last_command = None
        
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[INFO] Voice Recognizer initialized")
        except Exception as e:
            print(f"[WARNING] Could not initialize audio: {e}")
    
    def listen_once(self, timeout=10):
        """Listen for a single command"""
        try:
            print("[🎤] Listening...")
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=15)
            
            print("[⏳] Processing speech...")
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"[✅] Recognized: {text}")
            self.last_command = text
            return text
        
        except sr.UnknownValueError:
            print("[❌] Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"[❌] API Error: {e}")
            return None
        except sr.WaitTimeoutError:
            print("[❌] No speech detected, timeout")
            return None
        except Exception as e:
            print(f"[❌] Error: {e}")
            return None


void_recognizer = VoiceRecognizer()


def get_voice_input(timeout=10):
    """Get single voice input"""
    return void_recognizer.listen_once(timeout=timeout)
