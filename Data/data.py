"""
Command Phrases and Mappings
Maps voice commands to handler functions
"""

from Commands.handlers import handler

command_phrases = {
    # Media Control
    "play pause": handler.play_pause_media,
    "play": handler.play_pause_media,
    "pause": handler.play_pause_media,
    "next video": handler.next_video,
    "next track": handler.next_video,
    "skip": handler.next_video,
    "previous video": handler.previous_video,
    "previous track": handler.previous_video,
    
    # Browser Control
    "open new tab": handler.open_new_tab,
    "new tab": handler.open_new_tab,
    "close tab": handler.close_tab,
    "refresh": handler.refresh_page,
    "refresh page": handler.refresh_page,
    
    # Website Opening
    "open google": lambda: handler.open_website("https://www.google.com"),
    "google": lambda: handler.open_website("https://www.google.com"),
    "open youtube": lambda: handler.open_website("https://www.youtube.com"),
    "youtube": lambda: handler.open_website("https://www.youtube.com"),
    "open github": lambda: handler.open_website("https://www.github.com"),
    
    # System
    "get my ip": handler.get_ip_address,
    "ip address": handler.get_ip_address,
    "screenshot": handler.screenshot,
    "tell me a joke": handler.get_random_joke,
    "joke": handler.get_random_joke,
}


def get_command_phrases():
    """Return all command phrases"""
    return command_phrases


def list_all_commands():
    """List all available commands"""
    print("\n[📋] Available Commands:")
    print("-" * 50)
    for i, command in enumerate(command_phrases.keys(), 1):
        print(f"{i}. {command}")
    print("-" * 50)
    print(f"Total: {len(command_phrases)} commands\n")
