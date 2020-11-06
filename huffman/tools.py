def str_to_bin(string: str) -> str:
    return ''.join(format(ord(x), 'b') for x in string)
