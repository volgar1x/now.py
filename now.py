#!/usr/bin/env python3
from datetime import datetime, timedelta
from sys import argv, stdout

ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

now = datetime.now()

for i in range(1, len(argv), 3):
    op = ops[argv[i]]
    num = int(argv[i+1], base=10)
    resolution = argv[i+2]

    d = timedelta(**{resolution: num})
    now = op(now, d)
    
stdout.write(str(int(now.timestamp())))
