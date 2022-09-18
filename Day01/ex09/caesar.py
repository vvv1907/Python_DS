#!/usr/local/bin/python3

import sys

def caesar(code, phrase, n):
    if code == 'decode':
        n *= -1
    new_phrase = ''
    alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(phrase)):
        if phrase[i] in alphabet1:
            m = alphabet1.find(phrase[i])
            new_phrase += alphabet1[(n + m) % len(alphabet1)]
        elif phrase[i] in alphabet2:
            m = alphabet2.find(phrase[i])
            new_phrase += alphabet2[(n + m) % len(alphabet2)]
        else:
            new_phrase += phrase[i]

    print(new_phrase)

if __name__ == '__main__':
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        raise Exception('Error: wrong arguments number')
    if not sys.argv[2].isascii():
        raise Exception('Error: wrong symbol in string')
    try:
        n_shift = int(sys.argv[3])
    except ValueError:
        raise Exception('Error: shift is not integer')
    caesar(sys.argv[1], sys.argv[2], n_shift)
