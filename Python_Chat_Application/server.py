import socket

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to localhost and port
server.bind(("localhost", 5050))

# Listen for incoming connections
server.listen(1)

print("====================================")
print(" Server is running...")
print(" Waiting for client connection...")
print("====================================")

# Accept client connection
client_socket, client_address = server.accept()

print(f"Connected to {client_address}")

while True:

    # Receive message from client
    message = client_socket.recv(1024).decode()

    if message.lower() == "exit":
        print("Client ended the chat.")
        break

    print(f"\nClient: {message}")

    # Send reply
    reply = input("Server: ")

    client_socket.send(reply.encode())

    if reply.lower() == "exit":
        break

client_socket.close()
server.close()

print("\nServer Closed.")