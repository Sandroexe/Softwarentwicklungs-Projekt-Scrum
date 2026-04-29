import tkinter as tk
from connection.server import get_ip_address, start_server
from gui.game import show_game_window


def show_server_window():
    """Display server window with IP address and start button."""
    window = tk.Tk()
    window.title("CHESS - Host Game")
    window.geometry("400x250")
    window.resizable(False, False)
    window.configure(bg="#f0f0f0")
    
    # Title
    title = tk.Label(
        window,
        text="Host Game",
        font=("Arial", 28, "bold"),
        bg="#f0f0f0",
        fg="#333333"
    )
    title.pack(pady=20)
    
    # Info text
    info_label = tk.Label(
        window,
        text="Your IP Address:",
        font=("Arial", 12),
        bg="#f0f0f0",
        fg="#666666"
    )
    info_label.pack(pady=10)
    
    # Get and display IP address
    ip_address = get_ip_address()
    ip_display = tk.Label(
        window,
        text=ip_address,
        font=("Arial", 20, "bold"),
        bg="#e8f5e9",
        fg="#2e7d32",
        pady=10
    )
    ip_display.pack(fill=tk.X, padx=20, pady=10)
    
    # Start button
    button_start = tk.Button(
        window,
        text="Start Server",
        command=lambda: [window.destroy(), start_server(), show_game_window("server")],
        font=("Arial", 14, "bold"),
        bg="#4CAF50",
        fg="white",
        height=2,
        border=0,
        cursor="hand2",
        activebackground="#45a049"
    )
    button_start.pack(fill=tk.X, padx=20, pady=20)
    
    window.mainloop()
