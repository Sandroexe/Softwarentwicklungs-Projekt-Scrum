# schach.py

print("starte schach.py...")

from connection.server import start_server
from connection.client import connect_to_server

modus = input("Server oder Client? (server/client): ").strip().lower()

if modus == "server":
    start_server()
elif modus == "client":
    connect_to_server()
else:
    print("Ungültige Eingabe!")

