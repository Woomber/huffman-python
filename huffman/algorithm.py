"""
Algoritmo de Huffman
Yael Chavoya

Este es el archivo principal para comprimir y descomprimir un texto mediante el Algoritmo de compresión de Huffman
"""
from typing import Dict, Tuple
from huffman.tree import Tree
import huffman.tools as tools
import re


def compress(string: str) -> Tuple[str, Dict[str, str]]:
    """
    Comprime una cadena de texto con el algoritmo de Huffman, generando códigos específicos basados en la frecuencia
    de los caracteres.

    :param string: La cadena a comprimir
    :return: Una cadena con el texto encriptado en binario y el diccionario usado para encriptarlo
    """
    frecuencias = {}

    # Llenar un diccionario con el carácter como clave y la frecuencia como valor
    for char in string:
        if char in frecuencias:
            frecuencias[char] = frecuencias[char] + 1
        else:
            frecuencias[char] = 1

    # Apoyarse de la clase Tree (tree.py) para generar un árbol binario, dejando los caracteres más frecuentes más
    # cerca de la raíz
    tree = Tree(frecuencias)
    # Asignar los códigos a cada carácter basándose en su posición en el árbol
    codes = tree.to_code_dict()

    # Para cada carácter, insertar su código en la cadena resultante
    compressed = ''
    for char in string:
        compressed += codes[char]

    return compressed, codes


def encode_key(codes: Dict[str, str]) -> str:
    """
    Convierte el diccionario con los códigos de cada carácter en una cadena de texto, para poder almacenar la
    información usada para comprimir un texto

    :param codes: El diccionario de códigos en formato "carácter": "código"
    :return: Una cadena con información de los códigos de cada carácter
    """
    encoded = ''
    for char, code in codes.items():
        # Para cada carácter, convertir el carácter a hexadecimal Unicode y juntarlo con su código
        char_hex = hex(int(tools.str_to_bin(char), 2))
        encoded += char_hex[2:] + '.' + code + ':'
    return encoded[:-1]


def decode_key(code: str) -> Dict[str, str]:
    """
    Convierte una cadena de texto con la información usada para comprimir un texto en un diccionario con los códigos
    de cada carácter en una cadena de texto

    :param code: La cadena de texto con la información
    :return: Un diccionario de códigos en formato "carácter": "código"
    """
    decoded = {}
    codes = code.split(':')
    for cd in codes:
        try:
            # Convertir el Unicode hexadecimal a un carácter y asignarle su código en el diccionario
            item = cd.split('.')
            char = chr(int(item[0], 16))
            decoded[char] = item[1]
        except Exception:
            raise ValueError('Formato de código no reconocido')
    return decoded


def decompress(binstring: str, codes: Dict[str, str]) -> str:
    """
    Convierte una representación binaria comprimida en una cadena legible usando un diccionario de códigos

    :param binstring: La representación binaria de la cadena
    :param codes: El diccionario de códigos en formato "carácter": "código"
    :return: La cadena restaurada
    """
    full_str = ''
    capture = ''
    matches = []

    # Verificar que la cadena contenga solamente unos y ceros
    if not re.search('^[01]+$', binstring):
        raise ValueError('La cadena proporcionada no es una representación binaria')
    
    for bit in binstring:
        # Para cada bit, ir agregándolo a una cadena de captura y buscar esa captura en el diccionario hasta que sólo
        # haya una coincidencia, entonces cambiar la cadena capturada hasta el momento por su carácter
        capture += bit

        # Agregar a matches todos los códigos que empiecen por lo que va en capture
        matches.clear()
        for char, code in codes.items():
            if capture == code[0:len(capture)]:
                matches.append(char)

        # Si sólo hay una coincidencia, es el carácter que coincide
        if len(matches) == 1:
            full_str += matches[0]
            capture = ''

    return full_str
