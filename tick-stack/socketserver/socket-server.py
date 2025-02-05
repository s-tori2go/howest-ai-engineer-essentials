import random
import socket
import time

HOST = 'telegraf'  # The server's hostname or IP address
PORT = 10000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with open('/socketserver/data/ratings.csv') as file:
        # Skip header
        line = file.readline()

        line = file.readline().split(',')

        while line:
            line_protocol = f'ratings,userId={str(line[0])},movieId={str(line[1])} rating={float(line[2])} ' \
                            f'{line[3].strip()}000000000\n'
            print(line_protocol.strip())
            s.send(line_protocol.encode('utf-8'))
            sleep = random.randint(50, 100) / 5000
            time.sleep(sleep)
            line = file.readline().split(',')