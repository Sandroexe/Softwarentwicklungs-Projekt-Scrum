# main.py

print("Starting Chess application...")

from gui.menu import show_menu
from connection.server import start_server
from connection.client import connect_to_server

# Display menu and get user selection
mode = show_menu()

# Start the selected mode
if mode == "server":
    print("→ Starting SERVER...")
    start_server()
elif mode == "client":
    print("→ Starting CLIENT...")
    connect_to_server()
else:
    print("No selection made!")

