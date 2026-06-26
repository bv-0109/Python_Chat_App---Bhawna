import socket

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("localhost", 5050))

print("====================================")
print(" Connected to Server Successfully!")
print(" Type 'exit' to end the chat.")
print("====================================")

while True:

    # Send message to server
    message = input("Client: ")

    client.send(message.encode())

    if message.lower() == "exit":
        break

    # Receive reply from server
    reply = client.recv(1024).decode()

    if reply.lower() == "exit":
        print("Server ended the chat.")
        break

    print(f"Server: {reply}")

client.close()

print("\nClient Closed.")