class Assembler:
    def __init__(self):
        self.instruc = { #defining opcodes and instruction in a dictionary
            "HALT": "00000000", #0
            "LOAD_M": "00000001",#1
            "ADD_M": "00000101",#5
            "SUB_M": "00000110",#6
            "JMP_M_0:19": "00001101",#13
            "JMP+_M_0:19": "00001111",#15
            "STORE_M_8:19": "00010010",#18
            "STORE_M_28:39": "00010011",#19
            "RSH": "00010101",#21
            "STORE_M": "00100001",#33
            "NOP": "00100010",#34
            "SQUARE":"00100011",#35
            "SQUAREROOT":"00100100"#36
            
        }
        self.assemble()
        
    def assemble(self):
        fileI = open('Assembly code.txt', 'r')                      #opens the "Assembly code.txt" file in read mode
        fileO = open('machine code.txt', 'w')                       #opens the "Machine code.txt" file in write mode
        for l in fileI:                                             #iterates through each line in the fileI
            instruc=list(l.strip().split()) #splits each line into a list of words, removes any space from each word
            # print(instruc[0])
            word=instruc[0]
            binary_code = ""
            if (self.instruc.get(word)!=None):                      #checks if the word key present in the instruc
                for inst in instruc:                                # iterates through each word in the instruc
                    opcode = self.instruc.get(inst)                 #assigns binary machine code for the inst variableto the opcode variable.
                    if opcode!=None:                                #checks whether instruc or no
                        if opcode in {"00100010","00100011","00100100","00010101"}: #NOP Square squareroot rsh
                            binary_code+=opcode
                            binary_code+=format(0,"012b")
                        else:
                            binary_code += opcode                       #instruc so adds opcode
                    else:
                        binary_code += format(int(inst), "012b")    #no so makes it 12 bit long binary no
            else:
                binary_code += format(int(word) if int(word) >= 0 else (int(word) & 0b111111111111), "040b")

            while(len(binary_code)!=40):                            #converts whole code into 40 bit length
                binary_code+= "0"
            print(binary_code, file=fileO)
assembler = Assembler()
file = open("machine code.txt", "r") 
print (file.read())
