with open('test_input.txt', mode='r', encoding = 'utf-8') as f_int:
    test_content = [line.strip() for line in f_int.readlines()]

with open('final_input.txt', mode='r', encoding='utf-8') as f_inf:
    final_content = [line.strip() for line in f_inf.readlines()]

   
def calculatep1(input, monkey):
    assert isinstance(monkey, Monkey)
    assert isinstance(input, int)
    if monkey.operation_number == 'old':
        wl = input * input
    else:
        onumber = int(monkey.operation_number)
        match monkey.operation_symbol:
            case '*':
                wl = input * onumber
            case '+':
                wl = input + onumber
            case _:
                raise ValueError
    # divide wl by 3, and round down.
    wl3 = wl // 3
    # check if devisible
    if(wl3 % monkey.div_number == 0):
        throw_to = monkey.throw_true
    else:
        throw_to = monkey.throw_false

    monkey.inspecteditems += 1
    return throw_to, wl3

def calculatep2(input, monkey):
    if monkey.operation_number == 'old':
        wl = input * input
    else:
        onumber = int(monkey.operation_number)
        match monkey.operation_symbol:
            case '*':
                wl = input * onumber
            case '+':
                wl = input + onumber
            case _:
                raise ValueError
    # Guess: test data 96577 = 13*17*19*23
    #wl = wl % 96577

    #final data 2*3*5*7*11*13*17*19
    wl = wl % 9699690
    # check if devisible
    if(wl % monkey.div_number == 0):
        throw_to = monkey.throw_true
    else:
        throw_to = monkey.throw_false

    monkey.inspecteditems += 1
    return throw_to, wl

class Monkey:
    def __init__(self, osymbol, onumber, divnumber, nr_true, nr_false):
        self.operation_symbol = osymbol # operation to do before inspecting
        self.operation_number = onumber # number to use in operation while inspecting
        self.div_number = divnumber     # divisable by number test
        self.throw_true = nr_true       # throw to which monkey
        self.throw_false = nr_false     # throw to which monkey
        self.inspecteditems = 0         # total items inspected
 
    @classmethod
    def fromstrlist(cls, strlist):
        osymbol = strlist[2].split(' ')[-2]
        onr = strlist[2].split(' ')[-1]
        dnr = int(strlist[3][-2:])
        tt = int(strlist[4][-1])
        tf = int(strlist[5][-1])
        return cls(osymbol, onr, dnr, tt, tf)

    def __str__(self):
        return f'Operation: {self.operation_symbol} {self.operation_number}\nTest:      div by {self.div_number}\nIf True: throw to: {self.throw_true}\n else throw to:    {self.throw_false}'

class Items:
    def __init__(self):
        self.N = 4
        self.items = [[79,98]
                    ,[54,65,75,74]
                    ,[79,60,97]
                    ,[74]]
        
    def do_round_p1(self):
        for i in range(self.N):
            for value in self.items[i][:]:
                throw_to, new_value = calculatep1(value, monkeys[i])
                # add new element to row of items.
                self.items[throw_to].append(new_value)
                # remove item from current row.
                self.items[i].remove(value)
    
    def do_round_p2(self):
        for i in range(self.N):
            for value in self.items[i][:]:
                throw_to, new_value = calculatep2(value, monkeys[i])
                # add new element to row of items.
                self.items[throw_to].append(new_value)
                # remove item from current row.
                self.items[i].remove(value)

    def __str__(self):        
        return '\n'.join(f'Monkey {i}: {item_list}'for i, item_list in enumerate(self.items))


    


            

print('Part 1')
monkeys = [Monkey.fromstrlist(test_content[i:i+6]) for i in range(0,len(test_content),7)]
ims = Items()
for _ in range(20):
    ims.do_round_p1()
for monkey in monkeys:
    print(monkey.inspecteditems)

print('Part2')
#reread items
monkeys = [Monkey.fromstrlist(test_content[i:i+6]) for i in range(0,len(test_content),7)]
ims = Items()
for _ in range(10000):
    ims.do_round_p2()
for monkey in monkeys:
    print(monkey.inspecteditems)


print('\nFinal Data')

monkeys = [Monkey.fromstrlist(final_content[i:i+6]) for i in range(0,len(final_content),7)]
ims = Items()
ims.items = [[65, 78],[54, 78, 86, 79, 73, 64, 85, 88],[69, 97, 77, 88, 87],
[99],[60, 57, 52],[91, 82, 85, 73, 84, 53],[88, 74, 68, 56],
[54, 82, 72, 71, 53, 99, 67]]
ims.N = 8
for _ in range(20):
    ims.do_round_p1()

for monkey in monkeys:
    print(monkey.inspecteditems)

print('Part2')

monkeys = [Monkey.fromstrlist(final_content[i:i+6]) for i in range(0,len(final_content),7)]
ims = Items()
ims.items = [[65, 78],[54, 78, 86, 79, 73, 64, 85, 88],[69, 97, 77, 88, 87],
[99],[60, 57, 52],[91, 82, 85, 73, 84, 53],[88, 74, 68, 56],
[54, 82, 72, 71, 53, 99, 67]]
ims.N = 8
for _ in range(10000):
    ims.do_round_p2()

for monkey in monkeys:
    print(monkey.inspecteditems)
