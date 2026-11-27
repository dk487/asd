#!/usr/bin/env python3

# https://eolymp.com/problems/6126

queue = []
while True:
    try:
        cmd, arg = input(), None
    except EOFError:
        break
    if ' ' in cmd:
        cmd, arg = cmd.split(' ')
    match cmd:
        case 'push':
            queue.append(arg)       
            print('ok')
        case 'pop':
            print(queue.pop(0) if len(queue) else 'error')
        case 'front':
            print(queue[0] if len(queue) else 'error')
        case 'size':
            print(len(queue))
        case 'clear':
            queue = []
            print('ok')
        case 'exit':
            print('bye')
            break
