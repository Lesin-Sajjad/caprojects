"""MACHINE CODES FOR ALL 3 PROGRAMS"""
machine_code_prog1={4194320: '10001100100010000000000000000000',
                    4194324: '10001100100010010000000000000100',
                    4194328: '10001100100010100000000000001000',
                    4194332: '10001100100010110000000000001100',
                    4194336: '10001100101011000000000000000000',
                    4194340: '10001100101011010000000000000100',
                    4194344: '10001100101011100000000000001000',
                    4194348: '10001100101011110000000000001100',
                    4194352: '01110001000011001000000000000010',
                    4194356: '01110001001011101000100000000010',
                    4194360: '00000010001100001000000000100000',
                    4194364: '01110001000011011001000000000010',
                    4194368: '01110001001011111001100000000010',
                    4194372: '00000010011100101001000000100000',
                    4194376: '01110001010011001010000000000010',
                    4194380: '01110001011011101010100000000010',
                    4194384: '00000010101101001010000000100000',
                    4194388: '01110001010011011011000000000010',
                    4194392: '01110001011011111011100000000010',
                    4194396: '00000010111101101011000000100000',
                    4194400: '00111100000000010001000000000001',
                    4194404: '10101100001100000000000000100000',
                    4194408: '00111100000000010001000000000001',
                    4194412: '10101100001100100000000000100100',
                    4194416: '00111100000000010001000000000001',
                    4194420: '10101100001101000000000000101000',
                    4194424: '00111100000000010001000000000001'}
machine_code_prog2= {4194320:'00000001001010100110000000100000',
                     4194324:'00000000000010100100100000100000',
                     4194328:'00000000000011000101000000100000',
                     4194332:'00100001011010110000000000000001',
                     4194336:'00010101011010001111111111111011'}
machine_code_prog3= {
    4194328: '00100000000010010000000000000000',
    4194332: '00010001001010000000000000000110',
    4194336: '10001101010011000000000000000000',
    4194340: '10101101011011000000000000000000',
    4194344: '00100001001010010000000000000001',
    4194348: '00100001010010100000000000000100',
    4194352: '00100001011010110000000000000100',
    4194356: '00001000000100000000000000000111'}

"""DATA MEMORY FOR ALL 3 PROGRAMS"""
mem1={268500992:1,
      268500996:2,
      268501000:3,
      268501004:4,
      268501008:5,
      268501012:6,
      268501016:7,
      268501020:8,
      268501024:0,
      268501028:0,
      268501032:0,
      268501036:0}
mem2={268500992:0,
      268500996:0,
      268501000:0,
      268501004:0,
      268501008:0,
      268501012:0,
      268501016:0,
      268501020:0,
      268501024:0,
      268501028:0,
      268501032:0,
      268501036:0}
mem3={268500992:1,
      268500996:2,
      268501000:3,
      268501004:4,
      268501008:5,
      268501012:0,
      268501016:0,
      268501020:0,
      268501024:0,
      268501028:0,
      268501032:5}

"""CONTROL SIGNALS AND OTHER UTILITIES"""
RegDst=0
ALUSrc=0
MemReg=0
RegWr=0
MemRd=0
MemWr=0
Branch=0
ALUOp=00
Jump=0

reg=[0]*32
PC=0
clk_cycles=0

def bin_to_int(bins):   
    #Converts a binary string to a signed integer
    if bins[0] == '1': #-ve
        bins = ''.join('1' if b == '0' else '0' for b in bins)
        return -1 * (int(bins, 2) + 1)
    else:  #+ve
        return int(bins, 2)
"""ALL PROCESSOR FUNCTIONS BELOW"""

#release of control signals
def control(opcode):
    global RegDst, Branch, MemReg, MemRd, ALUOp, MemWr, ALUSrc, RegWr, Jump
    if opcode == '000000':  # R type
        RegDst = 1
        Branch = 0
        MemRd = 0
        MemReg = 0
        ALUOp = 10
        MemWr = 0
        ALUSrc = 0
        RegWr = 1
        Jump = 0
    elif opcode == '000010':  # j types
        RegDst = 0
        Branch = 0
        MemRd = 0
        MemReg = 0
        ALUOp = 00
        MemWr = 0
        ALUSrc = 0
        RegWr = 0
        Jump = 1
    elif opcode == '001000':  # addi
        RegDst = 0
        Branch = 0
        MemRd = 0
        MemReg = 0
        ALUOp = 00
        MemWr = 0
        ALUSrc = 1
        RegWr = 1
        Jump = 0
    elif opcode == '000100':  # beq
        RegDst = 0
        Branch = 1
        MemRd = 0
        MemReg = 0
        ALUOp = 1
        MemWr = 0
        ALUSrc = 0
        RegWr = 0
        Jump = 0
    elif opcode == '000101':  # bne
        RegDst = 0
        Branch = 1
        MemRd = 0
        MemReg = 0
        ALUOp = 3
        MemWr = 0
        ALUSrc = 0
        RegWr = 0
        Jump = 0
    elif opcode == '100011':  # lw
        RegDst = 0
        Branch = 0
        MemRd = 1
        MemReg = 1
        ALUOp = 00
        MemWr = 0
        ALUSrc = 1
        RegWr = 1
        Jump = 0
    elif opcode == '101011':  # sw
        RegDst = 0
        Branch = 0
        MemRd = 0
        MemReg = 0
        ALUOp = 00
        MemWr = 1
        ALUSrc = 1
        RegWr = 0
        Jump = 0
    elif opcode == '011100':  # mul
        RegDst = 1
        Branch = 0
        MemRd = 0
        MemReg = 0
        ALUOp = 2
        MemWr = 0
        ALUSrc = 0
        RegWr = 1
        Jump = 0
    else:
        RegDst = 0
        Branch = 0
        MemRd = 0
        MemReg = 0
        ALUOp = 00
        MemWr = 0
        ALUSrc = 0
        RegWr = 0
        Jump = 0
#tells ALU what operation to take
def ALUControlUnit(ALUOp,funct):
    if(ALUOp==00): #lw,sw,addi
        return "010"
    elif(ALUOp==1):#beq
        return "0111"
    elif(ALUOp==3): #bne
        return '101'
    elif(ALUOp==10):#R types
        if(funct=='100000'):#add
            return '010'
        elif(funct== '100010'):#sub
            return '011'
        elif(funct== '101010'):#slt
            return '100'
        elif(funct== '100001'):#addu
            return '010'
    elif(ALUOp==2):
        return '111'
#instruction fetch phase
def fetch(machine_code):
    global PC
    global clk_cycles
    clk_cycles+=1
    instruct= machine_code[PC]
    PC+=4
    return instruct
#decode phase
def decode(instruct): 
    global clk_cycles
    opcode, rs, rt, rd, shamt, funct, target, imm = "", "", "", "", "", "", "", "" 
    opcode = instruct[0:6]
    control(opcode)
    clk_cycles += 1
    if opcode == '000000':  # R types
        rs = instruct[6:11]
        rt = instruct[11:16]
        rd = instruct[16:21]
        shamt = instruct[21:26]
        funct = instruct[26:32]
        return opcode, rs, rt, rd, shamt, funct, target, imm
    elif opcode == '011100':  # mul
        rs = instruct[6:11]
        rt = instruct[11:16]
        rd = instruct[16:21]
        shamt = instruct[21:26]
        funct = instruct[26:32]
        return opcode, rs, rt, rd, shamt, funct, target, imm
    elif opcode == '000010':  # J types
        target = instruct[6:32] + '00'
        return opcode, rs, rt, rd, shamt, funct, target, imm
    else:  # I types
        rs = instruct[6:11]
        rt = instruct[11:16]
        imm = instruct[16:32]
        return opcode, rs, rt, rd, shamt, funct, target, imm
#execute phase
def execute(rs,rt,imm,funct,target):
    global clk_cycles,PC,ALUSrc,ALUOp,Branch,Jump,RegDst,reg
    clk_cycles==1
    ALUOut=0
    ALUcontrol=ALUControlUnit(ALUOp,funct)
    if(Jump==1):#j types
        PC=int(target,2)
        return 0
    if(rs!=''):
        ALU_in1=reg[int(rs,2)]# inp 1
    if(ALUSrc==0):#inp 2
        if(rt!=''):
            ALU_in2=reg[int(rt,2)]
    else:
            ALU_in2=bin_to_int(imm)
    if(ALUcontrol=="010"):#add
        ALUOut=ALU_in1+ALU_in2
    elif(ALUcontrol=="011"):#sub
        ALUOut=ALU_in1-ALU_in2
    elif(ALUcontrol=='111'):#mul
        ALUOut=ALU_in1*ALU_in2
    
    elif(ALUcontrol=="100"):#slt
        if(ALU_in1<ALU_in2):
            ALUOut=1
        else:
            ALUOut=0
    elif(ALUcontrol=='101'):#bne
        if(ALU_in1!=ALU_in2):
            PC=PC+4*bin_to_int(imm)
    elif(ALUcontrol=='0111'):#beq
       
        if(ALU_in1==ALU_in2):
            PC=PC+4*bin_to_int(imm)
    return ALUOut
    
#memory access phase
def memory(ALUOut,w,n):
    global clk_cycles,MemRd,MemWr,MemReg,mem1,mem2,mem3
    if(n==1):
        clk_cycles+=1
        if(MemRd==1): 
            return mem1[ALUOut]
        elif(MemWr==1): 
            mem1[ALUOut]=reg[int(w,2)]
        if(MemReg==0): 
            return ALUOut
        elif(MemReg==1):
            return mem1[ALUOut]
    elif(n==2):
        clk_cycles+=1
        if(MemRd==1): 
            return mem2[ALUOut]
        elif(MemWr==1): 
            mem2[ALUOut]=reg[int(w,2)]
        if(MemReg==0): 
            return ALUOut
        elif(MemReg==1):
            return mem2[ALUOut]
    elif(n==3):
        clk_cycles+=1
        if(MemRd==1): 
            return mem3[ALUOut]
        elif(MemWr==1): 
            mem3[ALUOut]=reg[int(w,2)]
        if(MemReg==0): 
            return ALUOut
        elif(MemReg==1):
            return mem3[ALUOut]    
#writeback to register phase
def writeback(rt,rd,data):
    global clk_cycles,RegWr,RegDst,reg
    clk_cycles+=1
    if(RegWr==1):
        if(RegDst==1):# R types
            reg[int(rd,2)]=data
        else:# I types
            reg[int(rt,2)]=data

#DRIVER CODE

#taking choice of program from the user
choice= int(input("Enter choice from Matrix Multiplication :1 , Fibbonacci :2 , Array Copying :3 ::  "))

if choice==1:#Matrix Multiplication
    n=1 #control for which memory dictionary to access
    l=list(map(int,input('Enter 8 elements , 4 per matrix with spaces : ').split())) #taking input from user
    for i in range(8): #storing in the required registers $t0-$t7
        mem1[268500992+ 4*i]= l[i]
    PC=4194320
    reg[4]=268500992 #address of first matrix $a0
    reg[5]=268501008 #address of second matrix $a1
    while(1): #processor running all phases through PC
        instruct=fetch(machine_code_prog1)
        opcode,rs,rt,rd,shamt,funct,target,imm=decode(instruct)
        ALUOut=execute(rs,rt,imm,funct,target)
        data=memory(ALUOut,rt,n)
        writeback(rt,rd,data)
        if(PC>4194424): #break condition
            break
    #Printing output matrix stored in the predecided registers.
    print(reg[16]) #$s0
    print(reg[18]) #$s2
    print(reg[20]) #$s4
    print(reg[22]) #$s6

elif choice==2:#Fibonacci
    n=2
    num= int(input("Enter which digit fibbonacci: "))
    PC=4194320
    reg[8]=num #n-th digit of fibbonacci needed
    reg[9]=0 #a-> first elem will also have answer
    reg[10]=1 #b-> second element
    reg[11]=0 #counter

    while(1):
        instruct=fetch(machine_code_prog2)
        opcode,rs,rt,rd,shamt,funct,target,imm=decode(instruct)
        ALUOut=execute(rs,rt,imm,funct,target)
        data=memory(ALUOut,rt,n)
        writeback(rt,rd,data)
        if(PC>4194336):
            break
    print(reg[9])

elif choice==3:#copying arrays
    n=3
    PC=4194328
    reg[10]=268500992
    reg[11]=268501012
    reg[8]=5
    while(1):
        instruct=fetch(machine_code_prog3)
        opcode,rs,rt,rd,shamt,funct,target,imm=decode(instruct)
        ALUOut=execute(rs,rt,imm,funct,target)
        data=memory(ALUOut,rt,n)
        writeback(rt,rd,data)

        if(PC>4194356):
            break
    for i in range(5):
        print(mem3[268501012+ 4*i])



    