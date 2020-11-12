"""
Herramientas adicionales
Yael Chavoya
"""


def str_to_bin(string: str) -> str:
    """
    Convierte una cadena de texto en su representación binaria

    :param string: La cadena de texto a convertir
    :return: La representación en binario de la cadena de texto
    """
    return ''.join(format(ord(x), 'b') for x in string)
