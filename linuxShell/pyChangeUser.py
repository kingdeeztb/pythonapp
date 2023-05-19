#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess

sudo_password = 'sns123.00'
command = '-i -u gbasedbt \n id'
command = command.split()

cmd1 = subprocess.Popen(['echo', sudo_password], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(['sudo', '-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)


output = cmd2.stdout.read()

print (output)