import random
import socket
import time

HOST = 'telegraf'  # The server's hostname or IP address
PORT = 10000  # The port used by the server

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        with open('/data/ratings.csv') as file:
            # Skip header
            file.readline()

            line = file.readline().strip().split(',')

            while line and len(line) > 1:
                line_protocol = f'ratings,userId={str(line[0])},movieId={str(line[1])} rating={float(line[2])} ' \
                                f'{line[3].strip()}000000000\n'
                print(line_protocol.strip())
                s.send(line_protocol.encode('utf-8'))
                sleep = random.randint(50, 100) / 5000
                time.sleep(sleep)
                line = file.readline().strip().split(',')

except ConnectionRefusedError:
    print("Connection to Telegraf failed. Ensure Telegraf is running and accessible.")
except Exception as e:
    print(f"An error occurred: {e}")