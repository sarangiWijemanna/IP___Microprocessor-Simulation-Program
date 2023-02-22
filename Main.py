# import filehandle as filehandle
import os
from pickle import TRUE

# Import instructions
from instructions import dict

# Import decoder
import insdecoder

# Import processor
import Processor

# .....................................................................................................................
File_path = 'row0_input_chip.bin'  # Define the path of the Txt file
Binary_File = open(File_path)  # Open the defined file path

File_Name = os.path.basename(File_path)  # Get the name of the specified path
Name_Save_File = File_Name.split(".")[0]  # File Name separated by comma, Return the 1st`` item of the array
print(Name_Save_File)

PC = 0
Dict = {}
Memory = {}
Status = {}
Line_Number_Count = 0
opcode, operand, Instruct = "", "", ""
New_List = []

while True:
    try:
        line = next(Binary_File)
        # print(line)
        opcode = line[0:6]
        operand = line[6:35]
        # print(operand)

        # print(x)
        for key in dict:
            # print(key)
            if key == opcode:
                Instruct = dict[key]

        # print(decoder(Instruct))
        decodeInstruct = insdecoder.decoder(Instruct, operand, PC, Dict)
        PC += 1
        # New_List = New_List + [decodeInstruct]


    except StopIteration:
        break
Binary_File.close()

# ........................................................................................
# Create Instruction File
with open("Instruction File" + ".asm", 'w') as f:
    inst_str = ''
    for num, inst in Dict.items():
        for key in inst:
            x = str(inst[key])
            inst_str = inst_str + " " + x

        inst_str = str(num) + " " + inst_str
        f.write("%s\n" % inst_str)
        # print(num, inst_str)
        inst_str = ''

# ......................................................................................
PCx = 1
while TRUE:
    try:
        if PCx in Dict.keys():
            PCx, Memory = Processor.processor(Dict, PCx, Memory, Status)
            # print(PCx)
        else:
            break

    except StopIteration:
        break

# ......................................................................................
# Create Memory File
with open("Memory" + ".txt", 'w') as f:
    format_Dict = sorted({int(k): int(v) for k, v in Memory.items()}.items())

    f.write("{:<10} {:}".format('Register', 'Memory\n'))  # Print the names of the columns.

    # print each data item.
    for key, value in sorted(format_Dict):
        Memory = "{:<10} {:} ".format(key, value)  # Print the Register and Memory.
        # print(Memory)
        f.write("%s\n" % Memory)
