#! /usr/bin/python3.6

import socket
import codecs

IP = '192.168.0.22'
Puerto = 9999
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect((IP, Puerto))
data = codecs.decode("0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedfa2dfa2","hex")
Socket.send(data)
data = codecs.decode("00000025d0f281e28aef8bfe92f7d5ef94b6d1b4c09ff194ec98c7a6c5b1d8b7d9fbc1afdab6daa7da","hex")
Socket.send(data)
Socket.close()
