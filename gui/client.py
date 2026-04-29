import tkinter as tk
import socket
from gui.game import show_game_window


def show_client_window():
    """Display client window with IP address input field."""
    window = tk.Tk()
    window.title("CHESS - Join Game")
    window.geometry("400x280")
    window.resizable(False, False)
    window.configure(bg="#f0f0f0")
    
    # Title
    title = tk.Label(
        window,
        text="Join Game",
        font=("Arial", 28, "bold"),
        bg="#f0f0f0",
        fg="#333333"
    )
    title.pack(pady=20)
    
    # Info text
    info_label = tk.Label(
        window,
        text="Enter Server IP Address:",
        font=("Arial", 12),
        bg="#f0f0f0",
        fg="#666666"
    )
    info_label.pack(pady=10)
    
    # Input field
    ip_input = tk.Entry(
        window,
        font=("Arial", 14),
        width=20,
        border=2
    )
    ip_input.pack(pady=10)
    ip_input.focus()
    
    def connect():
        ip_address = ip_input.get().strip()
        if ip_address:
            window.destroy()
            connect_to_server_with_ip(ip_address)
        else:
            error_label.config(text="Please enter an IP address!")
    
    # Error label
    error_label = tk.Label(
        window,
        text="",
        font=("Arial", 10),
        bg="#f0f0f0",
        fg="#d32f2f"
    )
    error_label.pack(pady=5)
    
    # Connect button
    button_connect = tk.Button(
        window,
        text="Connect",
        command=connect,
        font=("Arial", 14, "bold"),
        bg="#2196F3",
        fg="white",
        height=2,
        border=0,
        cursor="hand2",
        activebackground="#0b7dda"
    )
    button_connect.pack(fill=tk.X, padx=20, pady=20)
    
    # Allow pressing Enter to connect
    ip_input.bind("<Return>", lambda event: connect())
    
    window.mainloop()


def connect_to_server_with_ip(ip_address):
    """Connect to server with provided IP address."""
    try:
        port = 65432
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print(f"Attempting to connect to {ip_address}...")
            sock.connect((ip_address, port))
            
            # Receive message from server
            data = sock.recv(1024)
            print(f"Response: {data.decode('utf-8')}")
            
            # Show game window after successful connection
            show_game_window("client")
    except Exception as e:
        # Show error window
        error_window = tk.Tk()
        error_window.title("Connection Error")
        error_window.geometry("300x150")
        error_window.configure(bg="#f0f0f0")
        
        error_label = tk.Label(
            error_window,
            text=f"Connection failed:\n{str(e)}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#d32f2f"
        )
        error_label.pack(pady=20)
        
        close_button = tk.Button(
            error_window,
            text="Close",
            command=error_window.destroy,
            font=("Arial", 12),
            bg="#f44336",
            fg="white"
        )
        close_button.pack()
        
        error_window.mainloop()
