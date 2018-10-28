import socket


def Main():
    #selection of port "127.0.0.1:5555"
    host = "127.0.0.1"
    port = 5055

    #setting up the port
    s = socket.socket()

    #connecting with server with address of "127.0.0.1:5555"
    s.connect((host, port))

    #enterting the message that is to be sent
    msg = raw_input("Enter the message: ")

    #loop
    while msg != 'bye':

        #send the message to server
        s.send(msg)

        #receiving the message
        data = s.recv(1024)
        print "Message found: " + str(data)

        #sending the reply
        msg = raw_input("Enter the message: ")

    s.close()


if __name__ == '__main__':
    Main()
