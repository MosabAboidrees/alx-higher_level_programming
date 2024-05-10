#!/usr/bin/python3
for i in range(25, -1, -1):
    a = i + ord('A')
    if i % 2 == 1:
        a += 32
    print("{:a}".format(a), end="")
