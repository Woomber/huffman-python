from typing import Dict, Tuple, List
from huffman.tree import Tree
import huffman.tools as tools

def compress(string: str):

    frecuencias = {}

    for char in string:
        if char in frecuencias:
            frecuencias[char] = frecuencias[char] + 1
        else:
            frecuencias[char] = 1

    tree = Tree(frecuencias)
    codes = tree.to_code_dict()

    compressed = ''
    for char in string:
        compressed += codes[char]

    return compressed, codes


def encode_key(codes: Dict[str, str]):
    encoded = ''
    for char, code in codes.items():
        char_hex = hex(int(tools.str_to_bin(char),2))
        code_hex = hex(int(code,2))
        encoded += char_hex[2:] + '.' + code_hex[2:] + ':'
    return encoded[:-1]


def decode_key(code: str) -> Dict[str, str]:
    decoded = {}
    codes = code.split(':')
    for cd in codes:
        item = cd.split('.')
        char = chr(int(item[0], 16))
        code_b = bin(int(item[1], 16))[2:]
        decoded[char] = code_b
    return decoded


def decompress(binstring: str, codes: Dict[str, str]):
    fullstr = ''
    capture = ''
    matches = []
    for bit in binstring:
        capture += bit
        matches.clear()
        for char, code in codes.items():
            if capture == code[0:len(capture)]:
                matches.append(char)
        print(capture, matches)
        if len(matches) == 1:
            fullstr += matches[0]
            capture = ''
    return fullstr
