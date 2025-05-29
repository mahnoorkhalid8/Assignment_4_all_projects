import socket
import threading

# Server configuration 
HOST = "localhost"
PORT = 5555

clients = []
positions = {}

def handle_client(client_socket, client_address, player_id):
    print(f"Player {player_id} connected: {client_address}")
    
    # Sending a welcome message to the client
    client_socket.sendall(f"Welcome Player {player_id + 1}".encode())
    
    try: 
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            # Update the player's position
            positions[player_id] = data
            
            # If both players have sent data, exchange it
            if len(positions) == 2:
                other_player_id = 1 - player_id
                other_position = positions[other_player_id]
                client_socket.sendall(other_position.encode())
            
    except Exception as e:
        print(f"Error with player {player_id + 1}: {e}")
        
    finally:
        client_socket.close()
        print(f"Player {player_id + 1} disconnected")
        
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    print("Server started, waiting for players...")
    
    player_id = 0
    while player_id < 2:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, player_id))
        thread.start()
        player_id += 1
            
if __name__ == "__main__":
    start_server()