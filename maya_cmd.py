#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (c) 2017 John Barbero Unenge

This code is licensed under MIT (below)

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import logging

logging.basicConfig()
logger = logging.getLogger(__file__)

def send_command(port, file_name=None):
    address = ('127.0.0.1', port)

    if file_name:
        with open(file_name) as f:
            command = f.read()
    else:
        command = sys.stdin.read()

    if len(command) >= 4096:
        msg = ('Command might be too big to send ({}). Maya specifies a default'
               ' buffer size of 4096 for commands, although while testing'
               ' larger commands have seemed to work.'
               .format(len(command)))
        logger.warning(msg)

    try:
        import socket
        client = socket.socket()
        client.connect(address)
        client.send(command)
        client.recv(1024)
    finally:
        client.close()

def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Path to the file to send')
    parser.add_argument('-p', '--port',
                        help='Listening port for maya commandPort')
    args = parser.parse_args()

    if not args.port:
        raise Exception('Unable to run without a port!')

    try:
        port = int(args.port)
        send_command(port, args.file)
    except ValueError as e:
        logger.critical('Unable to parse --port as an integer: "{}"'.format(e))

if __name__ == '__main__':
    main()
