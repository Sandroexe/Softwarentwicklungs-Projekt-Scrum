import tkinter as tk


def show_menu():
    """Display selection GUI and return 'server' or 'client'."""
    selection = None
    
    def choose_server():
        nonlocal selection
        selection = "server"
        window.destroy()
    
    def choose_client():
        nonlocal selection
        selection = "client"
        window.destroy()
    
    # Create window
    window = tk.Tk()
    window.title("CHESS - Mode Selection")
    window.geometry("300x200")
    window.resizable(False, False)
    
    # Title
    title = tk.Label(window, text="CHESS", font=("Arial", 24, "bold"))
    title.pack(pady=20)
    
    # Subtitle
    subtitle = tk.Label(window, text="Select your mode", font=("Arial", 12))
    subtitle.pack(pady=10)
    
    # Button frame
    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)
    
    # Server button
    button_server = tk.Button(
        button_frame,
        text="🖥️ Server",
        command=choose_server,
        width=15,
        height=2,
        font=("Arial", 11),
        bg="#4CAF50",
        fg="white"
    )
    button_server.pack(pady=10)
    
    # Client button
    button_client = tk.Button(
        button_frame,
        text="👤 Client",
        command=choose_client,
        width=15,
        height=2,
        font=("Arial", 11),
        bg="#2196F3",
        fg="white"
    )
    button_client.pack(pady=10)
    
    # Display window
    window.mainloop()
    
    return selection

