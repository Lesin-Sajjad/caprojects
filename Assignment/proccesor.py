import math
file_path = 'machine code.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read all lines and store them in a list, removing newline characters
    assemblylines = [line.strip() for line in file.readlines()]



class SimpleComputer:
    def __init__(self):
        # Initialize registers
        self.AC = "0000000000000000000000000000000000000000"
        self.PC = 8
        self.MAR = 0
        self.IBR = "00000000000000000000"
        self.MBR = "0000000000000000000000000000000000000000"
        self.address = "000000000000"
        self.HALT = False
        self.LHI = True
        self.memory = assemblylines
        self.opcodes = {
            "HALT": "00000000",  # 0
            "LOAD_M": "00000001",  # 1
            "ADD_M": "00000101",  # 5
            "SUB_M": "00000110",  # 6
            "JMP_M_0:19": "00001101",  # 13
            "JMP+_M_0:19": "00001111",  # 15
            "STORE_M_8:19": "00010010",  # 18
            "STORE_M_28:39": "00010011",  # 19
            "RSH": "00010101",  # 21
            "STORE_M": "00100001",  # 33
            "NOP": "00100010",  # 34
            "SQUARE": "00100011",  # 35
            "SQUAREROOT": "00100100",  # 36
        }

    def fetch(self):
        self.MAR = self.PC
        self.MBR = self.memory[self.MAR]
        self.PC += 1
        self.LHI = True


    def binary_add(self, binary_a, binary_b):
        # Implement your binary addition logic here
        # This is just a placeholder, you need to replace it
        result = bin(int(binary_a, 2) + int(binary_b, 2))[2:].zfill(40)
        return "00" + result[2:]

    def binary_subtract(self, binary_a, binary_b):
        # Implement your binary subtraction logic here
        # This is just a placeholder, you need to replace it
        result = bin(int(binary_a, 2) - int(binary_b, 2))[2:].zfill(40)
        return "00" + result[2:]

    def load_m(self):
        # Extract the memory address from the current instruction
        address = int(self.address, 2)

        # Load the value from memory into the accumulator
        self.AC = self.memory[address]

    def jmp_m_0_19(self):
        # Extract the memory address from the current instruction
        address = int(self.address, 2)

        # Set the program counter (PC) to the specified memory address
        self.PC = address

    def jmp_plus_m_0_19(self):
        # Extract the memory address from the current instruction
        address = int(self.address, 2)

        # Check if the sign bit of the accumulator is positive
        if self.AC[0] == '0':
            # If positive, set the program counter (PC) to the specified memory address
            self.PC = address
    
    def store_m_8_19(self):
        # Extract the memory address from the current instruction
        address = int(self.address, 2)

        # Store the value in the accumulator into the specified memory address
        self.memory[address] = self.AC

    def store_m_28_39(self):
        # Extract the memory address from the current instruction
        address = int(self.address, 2)

        # Store the value in the accumulator into the specified memory address
        self.memory[address] = self.AC

    def store_m(self):
        # Extract the memory address from the current instruction
        address = int(self.address, 2)

        # Store the value in the accumulator into the specified memory address
        self.memory[address] = self.AC

    def decode_execute(self):

        if self.LHI == True:
            opcode = self.MBR[:8]
            self.address = self.MBR[8:20]
            self.IBR = self.MBR[20:]
            self.LHI = False
        else:
            opcode = self.IBR[0:8]
            self.address = self.IBR[8:20]


        if opcode == self.opcodes["HALT"]:
            self.HALT = True

        elif opcode == self.opcodes["LOAD_M"]:
            # Implement the LOAD_M operation
            self.load_m()

        elif opcode == self.opcodes["ADD_M"]:
            operand = self.address
            self.AC = self.binary_add(self.AC, operand)
            # Implement the ADD_M operation

        elif opcode == self.opcodes["SUB_M"]:
            # Implement the SUB_M operation
            operand = self.address
            self.AC = self.binary_subtract(self.AC, operand)

        elif opcode == self.opcodes["JMP_M_0:19"]:
            # Implement the JMP_M_0:19 operation
            self.jmp_m_0_19()

        elif opcode == self.opcodes["JMP+_M_0:19"]:
            # Implement the JMP+_M_0:19 operation
            self.jmp_plus_m_0_19()

        elif opcode == self.opcodes["STORE_M_8:19"]:
            # Implement the STORE_M_8:19 operation
            self.store_m_8_19()

        elif opcode == self.opcodes["STORE_M_28:39"]:
            # Implement the STORE_M_28:39 operation
            self.store_m_28_39()

        elif opcode == self.opcodes["RSH"]:
            # Implement the RSH operation
            self.AC = int (self.AC,2)
            self.AC=self.AC>>1
            self.AC=bin(self.AC)
            self.AC="00"+ (self.AC[2:])

        elif opcode == self.opcodes["STORE_M"]:
            # Implement the STORE_M operation
            self.store_m()

        elif opcode == self.opcodes["NOP"]:
            # Implement the NOP operation
            pass

        elif opcode == self.opcodes["SQUARE"]:
            # Implement the SQUARE operation
            #self.AC = bin(int(self.AC, 2) ** 2)[2:].zfill(40)[-40:]
            self.AC=format(int(self.AC, 2) ** 2, "040b")

        elif opcode == self.opcodes["SQUAREROOT"]:
            # Implement the SQUAREROOT operation
            root = math.sqrt(int(self.AC, 2))
            # Convert the result back to binary format and zero-pad to 40 bits
            #self.AC = bin(int(root))[2:].zfill(40)[-40:]
            #root=int(self.AC, 2) ** 0.5
            self.AC=format(int(root), "040b")


        print(f"AC: {self.AC} | PC: {self.PC} | MAR: {self.MAR} | MBR: {self.MBR}")

        

    def run(self):
        while not self.HALT:
            self.fetch()
            self.decode_execute()
            self.decode_execute()

            
    

# Create an instance of the SimpleComputer and run the simulation
computer = SimpleComputer()
computer.run()
print(f"standard deviation={computer.memory[5]}")