#!/usr/bin/env python

if __name__ == "__main__":
    import sys
    # Inputs exit with "enter" + "ctrl+Z" + "enter"
    def reverse():
        input1=sys.stdin.read()
        result =""
        for i in range(1,len(input1)+1):
            result+=input1[-i]
        print(result)

    reverse()
