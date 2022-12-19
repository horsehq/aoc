with open('test_input.txt', mode='r', encoding = 'utf-8') as f_int:
    test_content = [line.strip() for line in f_int.readlines()]

with open('final_input.txt', mode='r', encoding='utf-8') as f_inf:
    final_content = [line.strip() for line in f_inf.readlines()]
    
class ClockCircuit:
    def __init__(self, content):
        self.cycles = [1]
        self.memory = 1
        self.readcontent(content)

    def readcontent(self, content):
        for line in content:
            self.process_instruction(line)       

    def process_instruction(self, instruction):
        if instruction.startswith('noop'):
            self.addlength()
        elif instruction.startswith('addx'):
            _, value = instruction.split(' ')
            self.addvalue(int(value))

    def addlength(self):
        # extend the list with the known value
        self.cycles.append(self.memory)

    def addvalue(self, value):
        # extend the list twice and set add value to the memory value
        self.addlength()
        self.addlength()
        self.memory += value

    def cal40(self):
        return sum(i * self.cycles[i] for i in range(20, len(self.cycles), 40))

    def drawline(self, line, N):
        drawing = ['.' for i in range(N)]
        for i in range(0, N):
            cur_value = self.cycles[i + 1 + line * N]
            # current value must be equal to i or only 1 difference.
            if abs(cur_value - i) <= 1:
                drawing[i] = '#'
        return ''.join(drawing)
    
    def createdrawing(self, N):
        return '\n'.join([self.drawline(i, N) for i in range(0, len(self.cycles)//N)])


print('Part 1')
print('Test input')
ct = ClockCircuit(test_content)
print(f'Sum of signal strengths: {ct.cal40()}')
print(ct.createdrawing(40))

print('Final input')
cf = ClockCircuit(final_content)
print(f'Sum of signal strengths: {cf.cal40()}')   
print(cf.createdrawing(40))
