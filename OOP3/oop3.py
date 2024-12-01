class Operations:
    def __init__(self, name, a, b):
        self.a = a
        self.b = b
        self.name = name

    def name(self):
        pass

    def znak(self):
        print('OPERATIONS')

    def estimate(self):
        pass

class XOR(Operations):
    def __init__(self, a, b):
        self.name = "XOR"
        self.a = a
        self.b = b

    def name(self):
        return self.name

    def znak(self):
        return "^"

    def estimate(self):
        return self.a ^ self.b

class AND(Operations):
    def __init__(self, a, b):
        self.name = "AND"
        self.a = a
        self.b = b

    def name(self):
        return self.name

    def znak(self):
        return "&"

    def estimate(self):
        return self.a & self.b

class OR(Operations):
    def __init__(self, a, b):
        self.name = "OR"
        self.a = a
        self.b = b

    def name(self):
        return self.name

    def znak(self):
        return "||"

    def estimate(self):
        return self.a | self.b

class SHEFFER(Operations):
    def __init__(self, a, b):
        self.name = "SHEFFER"
        self.a = a
        self.b = b

    def name(self):
        return self.name

    def znak(self):
        return "|"

    def estimate(self):
        return int( not (self.a & self.b))

class Unknow(Operations):
    def __init__(self):
        super().__init__(name='Unknow', a=1, b=1)

num1=int(input('Enter the first argument (0 or 1): '))
num2=int(input('Enter the second argument (0 or 1): '))
print()
Operation = [XOR, AND, OR, SHEFFER]

for opr in Operation:
    obct = opr(num1, num2)
    print(f'{obct.name}: {num1} {obct.znak()} {num2} = {obct.estimate()}')

print()
o = Unknow()
print(o)
print(o.znak())
