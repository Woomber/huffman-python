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


def _dict_to_tree(freq_dict: Dict[str, int]) -> Node:
    sortedlist = sorted(freq_dict.items(), key=lambda x: x[1])
    tree_list = []
    for item in sortedlist:
        tree_list.append(Node(item[0], item[1]))

    root = None
    
    while tree_list:
        item1 = tree_list.pop(0)
        item2 = tree_list.pop(0)

        combined = Node(count=item1.count + item2.count)
        combined.children = [item1, item2]

        if not tree_list:
            root = combined
        else:
            tree_list.append(combined)

        tree_list.sort(key=lambda x: x.count)

    return root


def _print_tree(root):
    for item in _bfs(root):
        print(f'Nodo {item.char} ({item.count}) children {len(item.children)}')
        for child in item.children:
            print(f'-- child: {child.char} ({child.count})')


def _assign_code_char(code_dict, node, code):

    if node.char:
        code_dict[node.char] = code
    
    if len(node.children) == 2:
        _assign_code_char(code_dict, node.children[0], code + '0')
        _assign_code_char(code_dict, node.children[1], code + '1')


def _assign_codes(root):
    code_dict = {}
    _assign_code_char(code_dict, root, '')

    return code_dict


def regular_binary(string: str):
    return ''.join(format(ord(x), 'b') for x in string)

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

    return compressed
