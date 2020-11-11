from typing import Dict, Tuple, List
from huffman.tree import Tree
import huffman.tools as tools
import re


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
        encoded += char_hex[2:] + '.' + code + ':'
    return encoded[:-1]


def decode_key(code: str) -> Dict[str, str]:
    decoded = {}
    codes = code.split(':')
    for cd in codes:
        try:
            item = cd.split('.')
            char = chr(int(item[0], 16))
            code_b = item[1]
            decoded[char] = code_b
        except:
            raise ValueError('Código no reconocido')
    return decoded


def decompress(binstring: str, codes: Dict[str, str]):
    fullstr = ''
    capture = ''
    matches = []

    if not re.search('^[01]+$', binstring):
        raise ValueError('No es cadena binaria')
    
    for bit in binstring:
        capture += bit
        matches.clear()
        for char, code in codes.items():
            if capture == code[0:len(capture)]:
                matches.append(char)
        if len(matches) == 1:
            fullstr += matches[0]
            capture = ''
    return fullstr
