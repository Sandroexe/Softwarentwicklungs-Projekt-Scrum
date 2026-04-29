# main.py

print("Starting Chess application...")

from gui.menu import show_menu
from gui.server import show_server_window
from gui.client import show_client_window

# Display menu and get user selection
mode = show_menu()

# Start the selected mode window
if mode == "server":
    print("→ Opening Server window...")
    show_server_window()
elif mode == "client":
    print("→ Opening Client window...")
    show_client_window()
else:
    print("No selection made!")

