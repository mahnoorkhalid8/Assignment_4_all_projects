import socket
import threading

HOST = "localhost"
PORT = 5555

def receive_data(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            if not data:
                break
            print("Opponent Y Position:", data)
            
        except Exception as e:
            print("Error receiving:", e)
            break    

# Game configuration
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        welcome = client_socket.recv(1024).decode()
        print(welcome)
        
        threading.Thread(target=receive_data, args=(client_socket,), daemon=True)
        
        while True:
            y_pos = input("Enter your Y position: ")
            client_socket.sendall(y_pos.encode())
            
    except Exception as e:
        print("Client error:", e)
        
    finally:
        client_socket.close()
        
if __name__ == "__main__":
    main()