import random

class UUID():
    def __init__(self):
        # lower case alphabets
        self.lower_alphabets = []
        for i in range(97, 123):
            self.lower_alphabets.append(i)
        self.lower_alphabets = tuple(self.lower_alphabets)

        # numbers
        self.numbers = []
        for i in range(48, 58):
            self.numbers.append(i)
        self.numbers = tuple(self.numbers)

        # hexadecimal
        self.hexadecimal = tuple(self.lower_alphabets + self.numbers)


    def generate_uuid(self):
        # UUID(8-4-4-4-12) -> xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        self.uuid = ""
        for _ in range(8):
            self.uuid += chr(random.choice(self.hexadecimal))
        self.uuid += "-"
        for _ in range(3):
            for _ in range(4):
                self.uuid += chr(random.choice(self.hexadecimal))
            self.uuid += "-"
        for _ in range(12):
            self.uuid += chr(random.choice(self.hexadecimal))
        return self.uuid
            

if __name__ == "__main__":
    uuid = UUID()
    while True:
        input("Generate UUID?")
        print(uuid.generate_uuid())
        print()
    
