#!/usr/bin/env python3
i = 1
while i <= 100:
    if i < 10:
        if i == 7:
            i += 1
        else:
            print(i)
            i += 1
    elif i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        i += 1
    else:
        print(i)
        i += 1

