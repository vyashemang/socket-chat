import socket
from sys import argv
script, filename = argv


def Main():
    #selection of port "127.0.0.1:5555"
    host = "127.0.0.1"
    port = 5055

    file1 = open(filename, 'a')
    #setting up the port
    s = socket.socket()

    #starting the server
    s.bind((host, port))

    #how many clients to be connected
    s.listen(1)

    #accepting the connection
    c, add = s.accept()

    print "Connection Found: " + str(add)

    while True:
        data = c.recv(1024)

        file1.write("Client: " + str(data) + "\n")
        if not data:
            break
        print "Message found:" + "\n" + str(data)

        data = raw_input("Enter the message: ")

        print "Sending... " + "\n" + str(data)

        c.send(data)

        file1.write("Server: " + str(data) + "\n")

    file1.close()
    c.close()


if __name__ == "__main__":
    Main()
