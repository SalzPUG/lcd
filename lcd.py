#!/usr/bin/env python
# -*- coding: utf-8 -*-

numbers = [
    (" _ ", "| |", "|_|"),
    ("   ", "  |", "  |"),
    (" _ ", " _|", "|_ "),
    (" _ ", " _|", " _|"),
    ("   ", "|_|", "  |"),
    (" _ ", "|_ ", " _|"),
    (" _ ", "|_ ", "|_|"),
    (" _ ", "  |", "  |"),
    (" _ ", "|_|", "|_|"),
    (" _ ", "|_|", " _|")
]

def lcd(number):
    output = ["", "", ""]
    
    for i in range(3):
        for c in str(number):
            output[i] += numbers[int(c)][i]
    return "\n".join(output)

if __name__ == "__main__":
    import nose
    nose.main()
