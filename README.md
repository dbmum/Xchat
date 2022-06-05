# Overview

As a software engineer I am always trying to explore new things and learn how to put my ideas into action. I go into every project with the assumption that what I want to do is somehow possible, I just need to learn how.

I made a program that lets you send chat messages between two programs. The server starts listening on a port, and then the client connects to that same port, then they can send messages back and forth to each other.

I wrote this program to learn more about networking and how to send data between different programs. I wanted to practice this on a small scale to be able to apply it to larger programs.

[Software Demo Video](https://youtu.be/LCoVAuz5diY)

# Network Communication

I used a client/ server model of communication. I did this with a TCP connection to send strings from one program to another using port number 65432 .


# Development Environment

* Vs Code
* Python
* Sockets library

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Sockets documentation](https://docs.python.org/3/library/socket.html)
* [Real Python](https://realpython.com/python-sockets/)
* [Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1622s)


# Future Work

* Add threading to allow for a program to send multiple things seperately while always listening for recieving data.
* Include more server commands for the user to use.
* Integrate networking into a bigger application set as a way for programs to talk to each other.