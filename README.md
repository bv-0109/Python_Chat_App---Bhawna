# Python Chat Application using Socket Programming

## Project Description

This mini project demonstrates a simple client-server chat application using Python Socket Programming. The application establishes communication between a server and a client, allowing them to exchange messages through a TCP connection.

The project is developed as part of a Python Networking/Socket Programming practical assignment.

---

## Objectives

- Create a server that listens for incoming client connections.
- Create a client that connects to the server.
- Exchange messages between the client and server.
- Support two-way communication.
- Display all sent and received messages.
- Demonstrate socket programming concepts using Python.

---

## Technologies Used

- Python 3.x
- Socket Programming (Built-in socket module)

---

## Project Structure

```
Python_Chat_Application/
│
├── server.py
├── client.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Requirements

No external libraries are required.

The project uses Python's built-in **socket** module.

---

## How to Run

### Step 1

Open two terminal windows.

### Step 2

Run the server:

```bash
python server.py
```

### Step 3

Open another terminal and run the client:

```bash
python client.py
```

### Step 4

Start exchanging messages between the client and the server.

Type **exit** from either side to end the chat.

---

## Features

- Establishes connection between server and client.
- Supports two-way communication.
- Sends messages from client to server.
- Sends replies from server to client.
- Displays sent and received messages.
- Closes the connection safely using the **exit** command.

---

## Socket Methods Used

- socket.socket()
- bind()
- listen()
- accept()
- connect()
- send()
- recv()
- close()

---

## Expected Output

Running the application will:

- Start the server and wait for a client connection.
- Connect the client successfully.
- Allow users to exchange messages.
- Display sent and received messages in both terminals.
- Close the connection when the user enters **exit**.

---

## Applications

- Chat Applications
- Client-Server Communication
- Networking Fundamentals
- Remote Communication Systems
- Multiplayer Games
- Messaging Applications

---

## Advantages

- Simple and easy to understand.
- Demonstrates TCP socket programming.
- Supports interactive communication.
- Uses only Python's built-in libraries.
- Can be extended into a real-time chat application.

---
