import socket
import threading
import json


class NetworkManager:
    """Manages a persistent TCP connection between two chess clients.

    Protocol: newline-delimited JSON messages.
    Example message: {"from": [6, 4], "to": [4, 4]}
    """

    def __init__(self):
        self.conn = None
        self.move_callback = None
        self.connected = False
        self.connected_callback = None  # called (with no args) once connection is established

    def set_move_callback(self, cb):
        """Register a function to call when a move is received: cb(from_pos, to_pos)."""
        self.move_callback = cb

    def set_connected_callback(self, cb):
        """Register a function to call once the connection is established."""
        self.connected_callback = cb

    def start_server(self, port=65432):
        """Bind, listen, and block until one client connects.
        
        Call this in a background thread so it does not block the GUI.
        """
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(('0.0.0.0', port))
        srv.listen(1)
        print(f"[Server] Waiting for connection on port {port}...")

        try:
            self.conn, addr = srv.accept()
            srv.close()
            self.connected = True
            print(f"[Server] Client connected: {addr[0]}")
            if self.connected_callback:
                self.connected_callback()
            threading.Thread(target=self._recv_loop, daemon=True).start()
        except Exception as e:
            print(f"[Server] Error accepting connection: {e}")

    def connect_to_server(self, ip, port=65432):
        """Connect to the server at the given IP.
        
        Call this in a background thread so it does not block the GUI.
        """
        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"[Client] Connecting to {ip}:{port}...")
            self.conn.connect((ip, port))
            self.connected = True
            print(f"[Client] Connected to {ip}")
            if self.connected_callback:
                self.connected_callback()
            threading.Thread(target=self._recv_loop, daemon=True).start()
        except Exception as e:
            print(f"[Client] Connection failed: {e}")
            raise

    def send_move(self, from_pos, to_pos):
        """Send a move to the opponent.

        Args:
            from_pos: [row, col] of the piece being moved.
            to_pos:   [row, col] of the destination square.
        """
        if not self.conn:
            print("[Network] Cannot send move: not connected.")
            return
        try:
            msg = json.dumps({"from": from_pos, "to": to_pos}) + "\n"
            self.conn.sendall(msg.encode('utf-8'))
        except Exception as e:
            print(f"[Network] Send error: {e}")

    def _recv_loop(self):
        """Background thread: continuously reads incoming moves."""
        buf = ""
        while True:
            try:
                data = self.conn.recv(4096).decode('utf-8')
                if not data:
                    print("[Network] Connection closed by peer.")
                    self.connected = False
                    break
                buf += data
                # Process all complete newline-delimited messages in the buffer.
                while "\n" in buf:
                    line, buf = buf.split("\n", 1)
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        msg = json.loads(line)
                        if self.move_callback:
                            self.move_callback(msg["from"], msg["to"])
                    except json.JSONDecodeError as e:
                        print(f"[Network] Bad message: {line!r} — {e}")
            except Exception as e:
                print(f"[Network] Receive error: {e}")
                self.connected = False
                break
