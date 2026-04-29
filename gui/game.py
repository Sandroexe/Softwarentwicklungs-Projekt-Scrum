import tkinter as tk
from tkinter import font as tkFont


def show_game_window(mode):
    """Display main game window for chess game."""
    window = tk.Tk()
    window.title("CHESS - Game")
    window.geometry("900x700")
    window.resizable(False, False)
    window.configure(bg="#2c2c2c")
    
    # ============ TOP STATUS BAR ============
    status_frame = tk.Frame(window, bg="#1a1a1a", height=50)
    status_frame.pack(fill=tk.X, padx=0, pady=0)
    
    # Mode label
    mode_label = tk.Label(
        status_frame,
        text=f"Mode: {mode.upper()}",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="#4CAF50" if mode == "server" else "#2196F3"
    )
    mode_label.pack(side=tk.LEFT, padx=15, pady=10)
    
    # Connection status
    connection_label = tk.Label(
        status_frame,
        text="● Connection: Waiting...",
        font=("Arial", 11, "bold"),
        bg="#1a1a1a",
        fg="#FFC107"
    )
    connection_label.pack(side=tk.RIGHT, padx=15, pady=10)
    
    # ============ MAIN CONTENT ============
    content_frame = tk.Frame(window, bg="#2c2c2c")
    content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # LEFT SIDE - CHESS BOARD
    board_frame = tk.Frame(content_frame, bg="#2c2c2c")
    board_frame.pack(side=tk.LEFT, padx=10)
    
    # Board title
    board_title = tk.Label(
        board_frame,
        text="Chess Board",
        font=("Arial", 14, "bold"),
        bg="#2c2c2c",
        fg="white"
    )
    board_title.pack(pady=10)
    
    # Chess board
    canvas = tk.Canvas(
        board_frame,
        width=480,
        height=480,
        bg="#333333",
        highlightthickness=2,
        highlightbackground="#555555"
    )
    canvas.pack()
    
    # Draw chess board
    square_size = 60
    colors = ["#f0d9b5", "#b58863"]
    
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
            
            # Add coordinates
            if col == 0:
                canvas.create_text(5, y1 + 5, text=str(8 - row), fill="#666", font=("Arial", 8, "bold"), anchor="nw")
            if row == 7:
                canvas.create_text(x1 + square_size - 5, y1 + square_size - 5, text=chr(97 + col), fill="#666", font=("Arial", 8, "bold"), anchor="se")
    
    # Add chess pieces (simple representation)
    pieces = {
        "white": ["♔", "♕", "♖", "♗", "♘", "♙"],
        "black": ["♚", "♛", "♜", "♝", "♞", "♟"]
    }
    
    # Draw starting position for white
    for i in range(8):
        canvas.create_text(i * square_size + 30, 7 * square_size + 30, text="♙", font=("Arial", 28), fill="white")
    
    # Draw starting position for black
    for i in range(8):
        canvas.create_text(i * square_size + 30, square_size + 30, text="♟", font=("Arial", 28), fill="black")
    
    # RIGHT SIDE - INFO PANEL
    info_frame = tk.Frame(content_frame, bg="#1a1a1a", width=350)
    info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
    
    # ---- Player Info ----
    players_label = tk.Label(
        info_frame,
        text="Players",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="white"
    )
    players_label.pack(pady=10)
    
    player_frame = tk.Frame(info_frame, bg="#2c2c2c")
    player_frame.pack(fill=tk.X, padx=10, pady=5)
    
    # White player
    white_frame = tk.Frame(player_frame, bg="#f0d9b5", height=40)
    white_frame.pack(fill=tk.X, pady=5)
    white_label = tk.Label(
        white_frame,
        text="White (You)" if mode == "server" else "White",
        font=("Arial", 11, "bold"),
        bg="#f0d9b5",
        fg="#333"
    )
    white_label.pack(pady=5)
    
    # Black player
    black_frame = tk.Frame(player_frame, bg="#333333", height=40)
    black_frame.pack(fill=tk.X, pady=5)
    black_label = tk.Label(
        black_frame,
        text="Black" if mode == "server" else "Black (Opponent)",
        font=("Arial", 11, "bold"),
        bg="#333333",
        fg="#f0d9b5"
    )
    black_label.pack(pady=5)
    
    # ---- Game Status ----
    status_title = tk.Label(
        info_frame,
        text="Game Status",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="white"
    )
    status_title.pack(pady=(20, 10))
    
    status_text = tk.Label(
        info_frame,
        text="Waiting for opponent...",
        font=("Arial", 10),
        bg="#1a1a1a",
        fg="#FFC107",
        wraplength=320,
        justify=tk.LEFT
    )
    status_text.pack(padx=10, pady=5)
    
    # ---- Move History ----
    history_label = tk.Label(
        info_frame,
        text="Move History",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="white"
    )
    history_label.pack(pady=(20, 10))
    
    history_frame = tk.Frame(info_frame, bg="#2c2c2c", height=150)
    history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    history_text = tk.Text(
        history_frame,
        font=("Courier", 9),
        bg="#333333",
        fg="#ffffff",
        height=10,
        width=30,
        state=tk.DISABLED,
        relief=tk.FLAT,
        border=1
    )
    history_text.pack(fill=tk.BOTH, expand=True)
    
    # ---- Buttons ----
    button_frame = tk.Frame(info_frame, bg="#1a1a1a")
    button_frame.pack(fill=tk.X, padx=10, pady=10)
    
    resign_button = tk.Button(
        button_frame,
        text="Resign",
        font=("Arial", 10, "bold"),
        bg="#f44336",
        fg="white",
        cursor="hand2"
    )
    resign_button.pack(fill=tk.X, pady=5)
    
    draw_button = tk.Button(
        button_frame,
        text="Offer Draw",
        font=("Arial", 10, "bold"),
        bg="#FF9800",
        fg="white",
        cursor="hand2"
    )
    draw_button.pack(fill=tk.X, pady=5)
    
    # ============ FOOTER ============
    footer_frame = tk.Frame(window, bg="#1a1a1a", height=30)
    footer_frame.pack(fill=tk.X, padx=0, pady=0)
    
    footer_label = tk.Label(
        footer_frame,
        text="Chess Game v1.0 | Ready to play",
        font=("Arial", 9),
        bg="#1a1a1a",
        fg="#999999"
    )
    footer_label.pack(pady=5)
    
    window.mainloop()


if __name__ == "__main__":
    # Test the game window directly
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "server"
    show_game_window(mode)
