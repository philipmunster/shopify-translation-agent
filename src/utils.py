import os

def send_mac_notification(title, message, sound="Hero"):
    os.system(f"""
        osascript -e 'display notification "{message}" with title "{title}" sound name "{sound}"'
    """)