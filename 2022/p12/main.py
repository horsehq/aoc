with open('test_input.txt', mode='r', encoding = 'utf-8') as f_int:
    test_content = [line.strip() for line in f_int.readlines()]

with open('final_input.txt', mode='r', encoding='utf-8') as f_inf:
    final_content = [line.strip() for line in f_inf.readlines()]

class Node:
    def __init__(self, char):
        self.char = ord(char)
        self.value = 9999999999
        self.finished = False

    def can_move_to(self, other):
        assert isinstance(other, Node)
        if other.char - 1 <= self.char:
            return True
        else:
            return False
    
class Grid:
    def __init__(self, content):
        self.width = len(content[0])
        self.height = len(content)
        self.nodes = [[Node(char) for char in content[j]] for j in range(self.height)]
    
    def get_node(self, rownr, colnr):
        return self.nodes[rownr][colnr]

    def get_neighbours(self, rownr, colnr):
        neighbours = []
        if colnr == 0:
            neighbours.append(self.nodes[rownr][colnr+1])
        elif colnr == self.width - 1:
            neighbours.append(self.nodes[rownr][colnr-1])
        else:
            neighbours.extend([self.nodes[rownr][colnr-1],self.nodes[rownr][colnr+1]])
        if rownr == 0:
            neighbours.append(self.nodes[rownr+1][colnr])
        elif rownr == self.height - 1:
            neighbours.append(self.nodes[rownr-1][colnr])
        else:
            neighbours.extend([self.nodes[rownr-1][colnr],self.nodes[rownr+1][colnr]])            
        return neighbours

    def process_node(self, rownr, colnr):
        node = self.nodes[rownr][colnr]
        assert node.finished == False

        neighbours = self.get_neighbours(rownr,colnr)
        for neighbour in neighbours:
            if neighbour.finished == False and node.can_move_to(neighbour):
                # it possible to go from node to neighbour. 
                if neighbour.value > node.value + 1:
                    # neighbour can be reached trhough this node. 
                    neighbour.value = node.value + 1

        # Node is finished processing.
        node.finished = True

    def get_row_values(self, i):
        return [node.value for node in self.nodes[i]]
    
    def smallest_node(self):
        #smallestvalue = min(min(node.value for node in self.nodes[j] if node.finished == False) for j in range(self.height))
        frow = None
        fcol = None
        smallestvalue = 99999999999
        for rownr in range(self.height):
            for colnr in range(self.width):
                node = self.nodes[rownr][colnr]
                if node.value < smallestvalue and node.finished == False:
                    frow = rownr
                    fcol = colnr
                    smallestvalue = node.value
        return frow, fcol

    def solve(self, lastrownr, lastcolnr):
        while True:
            rownr, colnr = self.smallest_node()
            if rownr == lastrownr and colnr == lastcolnr:
                # destination is reached. 
                break
            self.process_node(rownr, colnr)

    # printing functions
    def str_row_chars(self, i):
        return ''.join([node.char for node in self.nodes[i]])
    def str_chars(self):
        return '\n'.join([self.str_row_chars(i) for i in range(self.height)])

    def str_row_values(self, i):
        return ''.join([f'[{str(node.value)}]' for node in self.nodes[i]]) 
    def str_values(self):
        return '\n'.join([self.str_row_values(i) for i in range(self.height)])

    def str_row_finished(self, i):
        return ''.join([str(node.finished) for node in self.nodes[i]]) 
    def str_finished(self):
        return '\n'.join([self.str_row_finished(i) for i in range(self.height)])





g1 = Grid(test_content)
g1.nodes[0][0].value = 0
g1.solve(2,5)
print(g1.nodes[2][5].value)

g2 = Grid(final_content)
g2.nodes[20][0].value = 0
g2.solve(20,132)
#print(g2.str_values())
print(g2.nodes[20][132].value)

