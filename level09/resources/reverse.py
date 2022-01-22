#!/usr/bin/python3

import sys

token = sys.stdin.buffer.read()

print(''.join([chr((b - i) % 255) for i, b in enumerate(token.strip())]))
