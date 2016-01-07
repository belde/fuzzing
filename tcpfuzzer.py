
import random
import string
import sys
import argparse
import socket
import os

def custom_string(buffer):
    if args.multiply:
        pattern = buffer
        for i in range(args.multiply-1):
            buffer+=pattern
    try:
        sock.send(buffer)
    except:
        print "[*] Failed to send string"

def random_buffer(rand_length):
    rand_buffer= ''
    rand_sequence= ''

    if args.lowercase:
        rand_sequence = ''.join((rand_sequence, string.lowercase))
    if args.uppercase:
        rand_sequence = ''.join((rand_sequence, string.uppercase))
    if args.numbers:
        rand_sequence = ''.join((rand_sequence, string.digits))
    if args.punctuation:
        rand_sequence = ''.join((rand_sequence, string.punctuation))
    if args.whitespace:
        rand_sequence = ''.join((rand_sequence, string.whitespace))
    if args.printable:
        rand_sequence = ''.join((rand_sequence, string.printable))

    if args.lowercase or args.uppercase or args.numbers or args.punctuation or args.whitespace or args.printable:
        for i in range(rand_length):
            rand_buffer+=random.choice(rand_sequence)
    else:
        rand_buffer = os.urandom(rand_length)

    try:
        sock.send(rand_buffer)
    except:
        print "[*] Failed to send random buffer"

#TODO let the user specify bytes and add pattern options
#TODO pattern functions
#TODO a function that takes input from a file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target_ip")
    parser.add_argument("port", type=int)
    parser.add_argument("-s","--string", type=str, help="send the target a string from the command line")
    parser.add_argument("-x","--multiply", type=int, help="specify the number of times a custom string should be multiplied (for use with the -s option)")
    parser.add_argument("-r","--random", type=int, help="send a buffer of a specified length with random data")
    parser.add_argument("-l","--lowercase", help="FLAG: include lowercase letters in --random and --pattern",action="store_true")
    parser.add_argument("-u","--uppercase", help="FLAG: include uppercase letters in --random and --pattern",action="store_true")
    parser.add_argument("-n","--numbers", help="FLAG: include numbers in --random and --pattern",action="store_true")
    parser.add_argument("-p","--punctuation", help="FLAG: include punctuation in --random and --pattern",action="store_true")
    parser.add_argument("-w","--whitespace", help="FLAG: include whitespace characters in --random and --pattern",action="store_true")
    parser.add_argument("-a","--printable", help="FLAG: include all printable characters in --random and --pattern",action="store_true")
    args = parser.parse_args()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.target_ip,args.port))
    except:
        print "[*] Failed to connect to " + target_ip


    if args.string:
        custom_string(args.string)
    elif args.random:
        random_buffer(args.random)

