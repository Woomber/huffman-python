from typing import Dict, Tuple, List

class Node:
    def __init__(self, char=None, count=0):
        self.char: str or None = char
        self.count: int = count
        self.children: List[Node] = []


def _bfs(root: Node):
    pending = [root]
    nodelist = []

    while pending:
        curr = pending.pop(0)
        nodelist.append(curr)

        for child in curr.children:
            pending.append(child)
    
    return nodelist


def _dict_to_tree(dict: Dict[str, int]) -> Node:
    sortedlist = sorted(dict.items(), key=lambda x: x[1])
    treelist = []
    for item in sortedlist:
        treelist.append(Node(item[0], item[1]))

    root = None
    
    while treelist:
        item1 = treelist.pop(0)
        item2 = treelist.pop(0)

        combined = Node(count=item1.count + item2.count)
        combined.children = [item1, item2]

        if not treelist:
            root = combined
        else:
            treelist.append(combined)

        treelist.sort(key=lambda x: x.count)

    return root

def _print_tree(root):
    for item in _bfs(root):
        print(f'Nodo {item.char} ({item.count}) children {len(item.children)}')
        for child in item.children:
            print(f'-- child: {child.char} ({child.count})')


def _assign_code_char(dict, node, code):

    if node.char:
        dict[node.char] = code
    
    if len(node.children) == 2:
        _assign_code_char(dict, node.children[0], code + '0')
        _assign_code_char(dict, node.children[1], code + '1')


def _assign_codes(root):
    code_dict = {}
    _assign_code_char(code_dict, root, '')

    return code_dict


def compress(string: str):

    frecuencias = {}

    for char in string:
        if char in frecuencias:
            frecuencias[char] = frecuencias[char] + 1
        else:
            frecuencias[char] = 1

    print(frecuencias)
    tree = _dict_to_tree(frecuencias)
    codes = _assign_codes(tree)

    compressed = ''
    for char in string:
        compressed = compressed + codes[char]

    print(compressed)

    compressed_binary = int(compressed, 2)

    print(compressed_binary)

    return (compressed, bytearray(compressed_binary))


compress('anita lava la tina')