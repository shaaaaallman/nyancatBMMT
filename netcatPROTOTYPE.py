import socket

def nc_client(host, port):
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect(( host, port ))
    comms(client)
    #client.send(DATA.encode())
    #response = client.recv(4096)
    
def comms(client):
    while 1:
        # wait for data
        recv_len = 1
        response = ''

        while recv_len:
            data = client.recv(4096)
            recv_len = len(data)
            response += str(data).format('utf8')
            if recv_len < 4096:
                break
        print(response)

        # wait for more input until there is no more data
        buffer = input(">")
        buffer += '\n'

        client.send(buffer.encode())

host = input("IP:")
port = int(input("PORT:"))


nc_client(host, port)
