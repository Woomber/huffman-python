from typing import List, Dict

class Node:
    def __init__(self, char: str or None = None, count: int = 0):
        self.char: str or None = char
        self.count: int = count
        self.children: List[Node] = []

class Tree:
    def __init__(self, freq_dict:  Dict[str, int] or None = None):
        self.root = None

        if not freq_dict:
            return
        
        sortedlist = sorted(freq_dict.items(), key=lambda x: x[1])
        tree_list = []
        for item in sortedlist:
            tree_list.append(Node(item[0], item[1]))
        
        while tree_list:
            item1 = tree_list.pop(0)
            item2 = tree_list.pop(0)

            combined = Node(count=item1.count + item2.count)
            combined.children = [item1, item2]

            if not tree_list:
                self.root = combined
            else:
                tree_list.append(combined)

            tree_list.sort(key=lambda x: x.count)
    
    def __str__(self):
        string = ''
        for item in self.order_bfs():
            num_children = len(item.children)
            if num_children > 0:
                string += f'Nodo {item.char} ({item.count}) children {num_children}\n'
                for child in item.children:
                    string += f'-- child: {child.char} ({child.count})\n'
        return string

    def order_bfs(self) -> List[Node]:
        pending: List[Node] = [self.root]
        nodelist: List[Node] = []

        while pending:
            curr = pending.pop(0)
            nodelist.append(curr)

            for child in curr.children:
                pending.append(child)
        
        return nodelist

    def _assign_code_char(self, code_dict, node, code):
        if node.char:
            code_dict[node.char] = code
        
        if len(node.children) == 2:
            self._assign_code_char(code_dict, node.children[0], code + '0')
            self._assign_code_char(code_dict, node.children[1], code + '1')

    def to_code_dict(self) -> Dict[str, str]:
        code_dict = {}
        self._assign_code_char(code_dict, self.root, '')

        return code_dict
