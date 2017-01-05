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

'''Run this code in maya to start the commandPorts
'''

import maya.cmds as cmds
import time

command_ports = { 37001: 'mel', 37002: 'python' }
delay = 1

for port, source in command_ports.iteritems():
    port_name = ':' + str(port)
    try:
        cmds.commandPort(name=port_name, close=True)
        print 'Shutting down previous commandPort on {}'.format(port)
        time.sleep(delay)
    except RuntimeError as e:
        cmds.warning("Counldn't close port {} ({})".format(port, str(e)))

    cmds.commandPort(name=port_name, sourceType=source, echoOutput=True)
    print 'Started listening for {} on port {}'.format(source, port)
