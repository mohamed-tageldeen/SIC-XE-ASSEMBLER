# SIC/XE ASSEMBLER

import os

# Identifying input and output files

# The input file in the same directory as the Python script
input_dir = "systems project\input_Files"

output_dir = "systems project\output_Files"
input_file = os.path.join(input_dir, "testLecture.txt")
output_pass1_file = os.path.join(output_dir, "output_pass1.txt")
symbTable_file = os.path.join(output_dir, "symbTable.txt")
intermediate_file = os.path.join(output_dir, "intermediate.txt")
output_pass2_file = os.path.join(output_dir, "output_pass2.txt")
htme_file =  os.path.join(output_dir, "htme.txt")

# Initialize location counter and list to track it
LOCCTR = 0
location_counter =[]


# Check if input file exists
if not os.path.exists(input_file):
 print(f"Error: Input file '{input_file}' does not exist!")
 exit(1)

# Create output directory if missing
os.makedirs(output_dir, exist_ok=True)  # No error if dir exists




# Part 1 : Input File Processing and Intermediate File generation
def intermediate_file_generation():
    
    # List of cleaned lines that will be stored in intermediate file
    cleaned_lines = []

    # Read and parse each line 
    with open(input_file, 'r') as infile:
        for line in infile:
            # Strip whitespaces, empty lines and full line comments 
            stripped_line = line.strip()
            

            if not stripped_line or stripped_line.startswith(';'):
                continue

            # Removing comments (inline comments)
            comment_position = stripped_line.find(';')
            if comment_position != -1:
                stripped_line = stripped_line[:comment_position].strip()
            
            # Remove number of lines
            parts = stripped_line.split()
            if not parts:
               continue

            if parts[0].isdigit():
                parts = parts[1:]
            
            # Construct the cleaned lines
            if parts:
             cleaned_line = ' '.join(parts)
             cleaned_lines.append(cleaned_line)
            
            # Write to intermediate file
            with open(intermediate_file, 'w') as outfile:
                for line in cleaned_lines:
                    outfile.write(line + '\n')
    
    print("input file processing completed")
    return True

# SIC/XE Instruction Set OPCODE TABLE

opcodeTable = {
    "ADD":    {"opcode": 0x18, "format": 3},
    "ADDF":   {"opcode": 0x58, "format": 3},
    "ADDR":   {"opcode": 0x90, "format": 2},
    "AND":    {"opcode": 0x40, "format": 3},
    "CLEAR":  {"opcode": 0xB4, "format": 2},
    "COMP":   {"opcode": 0x28, "format": 3},
    "COMPF":  {"opcode": 0x88, "format": 3},
    "COMPR":  {"opcode": 0xA0, "format": 2},
    "DIV":    {"opcode": 0x24, "format": 3},
    "DIVF":   {"opcode": 0x64, "format": 3},
    "DIVR":   {"opcode": 0x9C, "format": 2},
    "FIX":    {"opcode": 0xC4, "format": 1},
    "FLOAT":  {"opcode": 0xC0, "format": 1},
    "HIO":    {"opcode": 0xF4, "format": 1},
    "J":      {"opcode": 0x3C, "format": 3},
    "JEQ":    {"opcode": 0x30, "format": 3},
    "JGT":    {"opcode": 0x34, "format": 3},
    "JLT":    {"opcode": 0x38, "format": 3},
    "JSUB":   {"opcode": 0x48, "format": 3},
    "LDA":    {"opcode": 0x00, "format": 3},
    "LDB":    {"opcode": 0x68, "format": 3},
    "LDCH":   {"opcode": 0x50, "format": 3},
    "LDF":    {"opcode": 0x70, "format": 3},
    "LDL":    {"opcode": 0x08, "format": 3},
    "LDS":    {"opcode": 0x6C, "format": 3},
    "LDT":    {"opcode": 0x74, "format": 3},
    "LDX":    {"opcode": 0x04, "format": 3},
    "LPS":    {"opcode": 0xD0, "format": 3},
    "MUL":    {"opcode": 0x20, "format": 3},
    "MULF":   {"opcode": 0x60, "format": 3},
    "MULR":   {"opcode": 0x98, "format": 2},
    "NORM":   {"opcode": 0xC8, "format": 1},
    "OR":     {"opcode": 0x44, "format": 3},
    "RD":     {"opcode": 0xD8, "format": 3},
    "RMO":    {"opcode": 0xAC, "format": 2},
    "RSUB":   {"opcode": 0x4C, "format": 3},
    "SHIFTL": {"opcode": 0xA4, "format": 2},
    "SHIFTR": {"opcode": 0xA8, "format": 2},
    "SIO":    {"opcode": 0xF0, "format": 1},
    "SSK":    {"opcode": 0xEC, "format": 3},
    "STA":    {"opcode": 0x0C, "format": 3},
    "STB":    {"opcode": 0x78, "format": 3},
    "STCH":   {"opcode": 0x54, "format": 3},
    "STF":    {"opcode": 0x80, "format": 3},
    "STI":    {"opcode": 0xD4, "format": 3},
    "STL":    {"opcode": 0x14, "format": 3},
    "STS":    {"opcode": 0x7C, "format": 3},
    "STSW":   {"opcode": 0xE8, "format": 3},
    "STT":    {"opcode": 0x84, "format": 3},
    "STX":    {"opcode": 0x10, "format": 3},
    "SUB":    {"opcode": 0x1C, "format": 3},
    "SUBF":   {"opcode": 0x5C, "format": 3},
    "SUBR":   {"opcode": 0x94, "format": 2},
    "SVC":    {"opcode": 0xB0, "format": 2},
    "TD":     {"opcode": 0xE0, "format": 3},
    "TIO":    {"opcode": 0xF8, "format": 1},
    "TIX":    {"opcode": 0x2C, "format": 3},
    "TIXR":   {"opcode": 0xB8, "format": 2},
    "WD":     {"opcode": 0xDC, "format": 3}
}


# Check if mnemonic is valid
def mnemonic_validation (mnemonic):


      valid_mnemonics = set (opcodeTable.keys()) .union({"WORD", "RESW", "RESB", "BYTE", "START", "END", "BASE"} ) 

      if mnemonic.startswith('+'):
           F4_mnemonic=mnemonic.split('+') 
           if F4_mnemonic[1] not in valid_mnemonics:
            print (f'error: inavalid mnemonic "{mnemonic}"')
            exit(1)
           else:
            return

      if mnemonic.startswith('$'):
         F5_mnemonic=mnemonic.split('$')
         if F5_mnemonic[1] not in valid_mnemonics:
 
            print (f'error: inavalid mnemonic "{mnemonic}"')
            exit(1)
         else:
            return
           

      if mnemonic not in valid_mnemonics:
 
            print (f'error: inavalid mnemonic "{mnemonic}"')
            exit(1)
      else:
            return
      
 
# Check if reference is valid
def reference_validation (reference):
      if not (reference.startswith(('#','@')) or
       reference.endswith(',X') or 
       reference.isdigit() or
       isinstance(reference,str)):
              print (f'error: inavalid reference "{reference}"')
              exit(1)
      else:
       return   
                    
# Generate symbol table
def symbol_table(symb_table,mnemonic):
                
                if mnemonic == "START":
                 with open(symbTable_file, "w") as outfile:
                     outfile.write(f"Label\t\t\tLocCounter\n")
                     

                with open(symbTable_file, "a") as outfile:
                  for key, value in symb_table.items():
        
                   label = key
                   loc_counter = value

                   outfile.write(f"{label} \t\t\t {format(loc_counter,'04X')}\n") 
                   
                return
      


# Generate location counter
def loc_counter(label,mnemonic,reference):
                
                global LOCCTR 
                global location_counter    # variable stores Location counter
                format_value = 0  # variable that stores the format value for the mneomonic 
                symb_table = {} # dictionary for the symbol table (key: label , value: locCounter)


                # Handle START directive
                if mnemonic == "START":
                 with open(output_pass1_file, "w") as outfile:
                   outfile.write(f"LocCounter\tLabel\t\tMnemonic\tReference\n{format(LOCCTR, '04X')}\t\t{label}\t\t{mnemonic}\t\t{reference}\n")
                   location_counter.append(format(LOCCTR,'04X')) 
                   symbol_table(symb_table,"START")


                else: 
                 with open(output_pass1_file, "a") as outfile:
                 
                    outfile.write(f"{format(LOCCTR, '04X')}\t\t{label}\t\t{mnemonic}\t\t{reference}\n")
                    location_counter.append(format(LOCCTR,'04X'))

                    if label and label not in symb_table and mnemonic != "START":
                     symb_table[label] = LOCCTR
                     symbol_table(symb_table,'')

                    elif label and mnemonic != "START":
                     print(f"ERROR: Duplicate symbol found: {label}")
                     exit(1) 
                    
                    # Update location counter based on directive or instruction type
                    if mnemonic == "START":
                     startAddr = int(reference, 16)
                     LOCCTR = startAddr         
                    elif mnemonic == 'BASE':
                     LOCCTR += 0
                    elif mnemonic == 'RESW':
                     LOCCTR += 3 * int(reference)
                    elif mnemonic == 'RESB':
                     LOCCTR += int(reference)
                    elif mnemonic == 'WORD':
                     LOCCTR += 3
                    elif mnemonic == 'BYTE':
                     if reference.startswith("X'") and reference.endswith("'"):
                      LOCCTR += (len(reference) - 3) // 2  # Hex
                     elif reference.startswith("C'") and reference.endswith("'"):
                      LOCCTR += len(reference) - 3  # Chars

                    elif mnemonic.startswith('+'):
                     LOCCTR += 4 # Format 4
                    
                    elif mnemonic.startswith('$'):
                       LOCCTR+=4 # Special Format
                    
                
                    elif mnemonic in opcodeTable:
                     format_value = opcodeTable[mnemonic]["format"]
                   
   
                     if format_value == 3:
                      LOCCTR += 3 # Format 3
                     
                  
                     elif format_value == 2:
                      LOCCTR += 2 # Format 2
                      
                  
                     elif format_value == 1:
                      LOCCTR += 1 # Format 1
                      

                     elif mnemonic == "END":
                      LOCCTR += 0 # END directive
                          
                return

# Pass 1 of the assembler                       
def pass_1(intermediate_file):
    
    global location_counter
    location_counter = []
    instruction = [] # List of instructions 

# Read intermediate file
    with open(intermediate_file,'r') as infile:        
     
     readl = infile.readlines()
     for line in readl:
          
        # Clean and split into instruction components                                     
          instruction = line.strip().split()  

        # check if the instruction only contains mnemonic as "RSUB" 
          if len(instruction) == 1:
                mnemonic_validation(instruction[0])
                loc_counter('',instruction[0],'')
                
        # check if the instruction contains mnemonic and reference
          if len(instruction) == 2:
                mnemonic_validation(instruction[0])
                reference_validation(instruction[1])
                loc_counter('',instruction[0],instruction[1])
                
         # check if the instruction contains label, mnemonic and reference
          if len(instruction) == 3:
                mnemonic_validation(instruction[1])
                reference_validation(instruction[2])
                loc_counter(instruction[0],instruction[1],instruction[2])  
                

# Generate object code 
def object_code(pc,label, mnemonic, reference):
  
    operand = reference
    format_value = 0
    symbolTable_dict = {}
    global location_counter
    global base
    # Check if base is already defined; if not, initialize to 0
    try:   
     base
    except NameError:
     base = 0  

    # Read symbol table and Load symbol table into a dictionary
    with open(symbTable_file, 'r') as infile:
        next(infile)
        for line in infile:
            parts = line.strip().split()
            symb_label = parts[0]
            loccounter = parts[1]
            symbolTable_dict[symb_label] = loccounter

    # Register codes used in format 2 instructions
    registers = {"A": 0x0, "X": 0x1, "B": 0x4, "S": 0x5, "T": 0x6, "F": 0x7}
    # Flags used in format 3/4 instruction
    flags = {"n": 0, "i": 0, "x": 0, "b": 0, "p": 0, "e": 0}
    # New flag set used in special format ($)
    new_flags =  {"n": 0, "i": 0, "x": 0, "F4": 0, "F5": 0, "F6": 0}

    # Handle START directive
    if mnemonic == "START":
        with open(output_pass2_file, 'w') as outfile:
           outfile.write(f"label\t\tmnemonic\treference\tobject code\n")
           outfile.write(f'{label}\t\t{mnemonic}\t\t{reference}\t\t\n')
        return
    
    # Handle END directive
    if mnemonic == "END":
   
        with open(output_pass2_file, 'a') as outfile:
             outfile.write(f'{label}\t\t{mnemonic}\t\t{reference}\t\t\n')
        return
    
    # Handle RESW and RESB (no object code generated)
    if mnemonic in {"RESW","RESB"}:
        with open(output_pass2_file, 'a') as outfile:
           outfile.write(f'{label}\t\t{mnemonic}\t\t{reference}\t\t\n')
        return
    
    # Handle BASE directive (used for base-relative addressing)
    if mnemonic == "BASE":
      base = int(symbolTable_dict[reference], 16)
      
    
      with open(output_pass2_file, 'a') as outfile:
            outfile.write(f'{label}\t\t{mnemonic}\t\t{reference}\t\t\n')
      return
    
    # Handle WORD directive (3 bytes)
    elif mnemonic == "WORD":
        operand = int(reference,10)

        object_code = format(operand, '06X')

        with open(output_pass2_file,'a') as outfile:
            outfile.write(f'{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n')
        
    # Handle BYTE directive (character or hex constant)
    elif mnemonic == "BYTE":
        if reference.startswith("X'") and reference.endswith("'"):
            operand = ''.join(c for c in reference if c not in "'X")
            object_code = format(int(operand, 16), '02X')

        else:
            reference.startswith("C'") and reference.endswith("'")
            operand = reference[2:-1]
            # Convert each character to its ASCII value and format as hex
            object_code = ''.join(format(ord(c), '02X') for c in operand)

        with open(output_pass2_file,'a') as outfile:
            outfile.write(f'{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n')

    # Format 4 instruction
    elif mnemonic.startswith('+'):
        F4_mnemonic = mnemonic.split('+')
        format_value = opcodeTable[F4_mnemonic[1]]["format"]
        with open(output_pass2_file, 'a') as outfile:
            flags["e"] = 1
            flags["b"] = 0
            flags["p"] = 0

            opcode = opcodeTable[F4_mnemonic[1]]["opcode"]
            bin_opcode = bin(opcode >> 2)[2:].zfill(6)
            
            # Addressing modes
            if reference.startswith('@'):
                flags["n"] = 1
                flags["i"] = 0
                operand = reference[1:]
            elif reference.startswith('#'):
                flags["n"] = 0
                flags["i"] = 1
                operand = reference[1:]
            else:
                flags["n"] = 1
                flags["i"] = 1
                operand = reference

            if reference.endswith(',X'):
                flags["x"] = 1
                operand = reference.replace(',X', '')
            
            # Check whether the reference in numeric or label
            if operand.isdigit():
             address = int(operand)
            else:

             address = int(symbolTable_dict[operand], 16)

            address_hex = format(address, '05X')
            bin_flags = ''.join(str(v) for v in flags.values())
            opcode_flags_bin = bin_opcode + bin_flags
            opcode_flags_hex = f"{int(opcode_flags_bin, 2):03X}"
            object_code = opcode_flags_hex + address_hex

            outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n")

    # Special Format
    elif mnemonic.startswith('$'):
        F5_mnemonic = mnemonic.split('$')
        format_value = opcodeTable[F5_mnemonic[1]]["format"]
        with open(output_pass2_file, 'a') as outfile:
            opcode = opcodeTable[F5_mnemonic[1]]["opcode"]
            bin_opcode = bin(opcode >> 2)[2:].zfill(6)

            if reference.startswith('@'):
                new_flags["n"] = 1
                new_flags["i"] = 0
                operand = reference[1:]
            elif reference.startswith('#'):
                new_flags["n"] = 0
                new_flags["i"] = 1
                operand = reference[1:]
            else:
                new_flags["n"] = 1
                new_flags["i"] = 1
                operand = reference

            if reference.endswith(',X'):
                new_flags["x"] = 1
                operand = reference.replace(',X', '')
            
            if operand.isdigit():
             address = int(operand)
            else:

             address = int(symbolTable_dict[operand], 16)

             if address % 2 == 0:
                new_flags["F4"]=0
             else:
                new_flags["F4"]=1

             if address == 0:
                new_flags["F5"]=0
             else:
                new_flags["F5"]=1

             if address  == base:

                new_flags["F6"]=0
             else:
                new_flags["F6"]=1
            
            address_hex = format(address, '05X')
            bin_flags = ''.join(str(v) for v in new_flags.values())
            opcode_flags_bin = bin_opcode + bin_flags
            opcode_flags_hex = f"{int(opcode_flags_bin, 2):03X}"
            object_code = opcode_flags_hex + address_hex

            outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n")

    else:

        format_value = opcodeTable[mnemonic]["format"]
        with open(output_pass2_file, 'a') as outfile:
            # Format 1
            if format_value == 1:
                object_code = opcodeTable[mnemonic]["opcode"]
                outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{format(object_code,'02X')}\n")
                return
            
            # Format 2
            elif format_value == 2:
                regs = reference.split(',')
                opcode = opcodeTable[mnemonic]["opcode"]
                if len(regs) == 1:
                    r1 = registers[regs[0]]
                    r2 = 0x0
                    object_code = f"{opcode:02X}{r1:01X}{r2:01X}"
                    outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n")

                elif regs[0] and regs[1] in registers:
                    r1 = registers[regs[0]]
                    r2 = registers[regs[1]]
                    opcode = opcodeTable[mnemonic]["opcode"]
                    object_code = f"{opcode:02X}{r1:01X}{r2:01X}"
                    outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n")

            # Format 3
            elif format_value == 3 and mnemonic != "RSUB" :
                pc = int(pc, 16)
                opcode = opcodeTable[mnemonic]["opcode"]
                bin_opcode = bin(opcode >> 2)[2:].zfill(6)
                
                if reference.startswith('@'):
                    flags["n"] = 1
                    flags["i"] = 0
                    operand = reference[1:]
                elif reference.startswith('#'):
                   
                    flags["n"] = 0
                    flags["i"] = 1
                    operand = reference[1:]
                else:
                    flags["n"] = 1
                    flags["i"] = 1
                    operand = reference

                if reference.endswith(',X'):
                    flags["x"] = 1
                    operand = reference.replace(',X', '')

                if operand.isdigit():
                    displacement = int(operand,10)
                    flags["b"] = 0
                    flags["p"] = 0

                else:
                    if operand not in symbolTable_dict and mnemonic != "RSUB":
                        print(f"ERROR: Undefined symbol '{operand}' in reference.")
                        exit(1)

                    target_addr = int(symbolTable_dict[operand], 16)

                    disp = target_addr - pc
                    # PC relative
                    if -2048 <= disp <= 2047:
                        displacement = disp & 0xFFF
                        
                        flags["p"] = 1
                        flags["b"] = 0
                    # Base relative
                    else:
                       
                        displacement = target_addr - base
                        
                        if 0 <= displacement <= 4095:
                            flags["b"] = 1
                            flags["p"] = 0
                        else:
                            print(f"ERROR: Displacement out of range for both PC and BASE: {mnemonic} {operand}")
                            exit(1)

                displacement_hex = format(displacement, '03X')
                bin_flags = ''.join(str(v) for v in flags.values())
                opcode_flags_bin = bin_opcode + bin_flags
                opcode_flags_hex = f"{int(opcode_flags_bin, 2):03X}"
                object_code = opcode_flags_hex + displacement_hex

                outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n")

            # "RSUB" instruction
            elif mnemonic == "RSUB":
                flags["n"] = 1
                flags["i"] = 1
                flags["x"] = 0
                flags["b"] = 0
                flags["p"] = 0
                flags["e"] = 0
                displacement = 0000

                opcode = opcodeTable[mnemonic]["opcode"]
                bin_opcode = bin(opcode >> 2)[2:].zfill(6)

                displacement_hex = format(displacement, '03X')
                bin_flags = ''.join(str(v) for v in flags.values())
                opcode_flags_bin = bin_opcode + bin_flags
                opcode_flags_hex = f"{int(opcode_flags_bin, 2):03X}"
                object_code = opcode_flags_hex + displacement_hex
                
                outfile.write(f"{label}\t\t{mnemonic}\t\t{reference}\t\t{object_code}\n")
   
    return

# Generating HTME record
def htme():
    global location_counter
    H_record = ""

    T_record = [] # List to score Text records 
    M_record = [] # List to store Modification records
    E_record = "" # End record
    mnemonics = []
    references = []
    object_codes = []
    prog_name = None
    # Get starting address and program length 
    prog_starting_addr = int(location_counter[0],16)
    prog_length = int(location_counter[-1],16) - prog_starting_addr
   
   # Read from object file
    with open (output_pass2_file,'r') as infile :
        next(infile)
        readl = infile.readlines()

        # Extracting instruction components
        for line in readl:
         object_code = ''
         reference = ''
         instruction = line.split()

         if len(instruction) == 2:
          if instruction[0] in {"BASE","END"}:  
           mnemonic,reference = instruction
           mnemonics.append(mnemonic)
           references.append(reference)
           object_codes.append(object_code)
          else:
           mnemonic,object_code = instruction
           mnemonics.append(mnemonic)
           references.append(reference)
           object_codes.append(object_code)

         elif len(instruction) == 3:
          
          if instruction[1] in {"RESW","RESB"}:
           label,mnemonic,reference = instruction
           mnemonics.append(mnemonic)
           references.append(reference)
           object_codes.append(object_code)

          elif instruction[1] == "START":
           label,mnemonic,reference = instruction
           mnemonics.append(mnemonic)
           references.append(reference)
           object_codes.append(object_code)
           prog_name = label

          else:
           mnemonic,reference,object_code = instruction
           mnemonics.append(mnemonic)
           references.append(reference)
           object_codes.append(object_code)

         else:
             mnemonic= instruction[1]
             object_code = instruction[-1]
             mnemonics.append(mnemonic)
             references.append(reference)
             object_codes.append(object_code)

    T_record_content = None
    T_record_size = 0
    T_record_startAddr = 0
    T_max_limit = 30  # Maximum length of text records in Bytes
    record_obj_codes = ""
    splitted_reference= "" 
    M_record_content = None
    M_addr = 0

    # Creating Header record
    H_record = f"H^{prog_name}^{format(prog_starting_addr,'06X')}^{format(prog_length,'06X')}"

    for i in range (len(object_codes)):
       mnemonic = mnemonics[i]
       reference = references[i]
       object_code = object_codes[i]
       current_addr = int(location_counter[i],16)

       # Set starting address for T record
       if T_record_startAddr == 0 or record_obj_codes == "":
          T_record_startAddr = current_addr
          
       # Handle interruption or overflow of text record 
       if mnemonic in {"RESW","RESB","START","END"} or (T_record_size + len(object_code) // 2) > T_max_limit:
             
             if record_obj_codes:
              T_record_content = f"T^{format(T_record_startAddr,'06X')}^{format(T_record_size,'02x')}^{record_obj_codes}"
              T_record.append(T_record_content)
              record_obj_codes = object_code
              T_record_size = 0
              T_record_startAddr = 0   
       else:
             record_obj_codes += object_code
             T_record_size = (len(record_obj_codes)//2)

             # Generate M record if Format 4 
             if len(object_code) == 8 :  
                if reference.startswith('#'):
                   splitted_reference = reference[1:]
                if not(splitted_reference.isdigit()):
                 M_addr = current_addr + 1
                 M_record_content = f"M^{format(M_addr,'06X')}^05"
                 M_record.append(M_record_content)

       # Create E record
       if mnemonic == "END":
             if record_obj_codes:
              T_record_content = f"T^{format(T_record_startAddr,'06X')}^{format(T_record_size,'02x')},{record_obj_codes}"
              T_record.append(T_record_content)
              record_obj_codes = ""
              T_record_size = 0
              record_obj_codes = ""
              T_record_startAddr = 0

             E_record = f"E^{format(prog_starting_addr,'06X')}"

    # write HTME records in the file    
    with open (htme_file,'w') as outfile:
        outfile.write(H_record + "\n")
        for t in T_record:
            outfile.write(t + "\n")
        for m in M_record:
            outfile.write(m + "\n")
        outfile.write(E_record + "\n")

    print("HTME generation complete!")      
 
    return


# Pass 2 of the assembler
def pass_2():
    
    instruction = [] # List of instructions 

# open the intermediate file and read line by line 
    with open(intermediate_file,'r') as infile:        # label LDA 0003 # instruction = ["label","LDA","0003"]
     
     readl = infile.readlines()


     instructions = [line.strip().split() for line in readl]
    
    # Process each instruction 
    for i , instruction in enumerate(instructions):
 
        if i == len(instructions) - 1:
            loc = location_counter[i]  # use current
        else:
            loc = location_counter[i + 1]

        # Check instruction length
        if len(instruction) == 1:
            object_code(loc,'',instruction[0],'')
         
        if len(instruction) == 2:
            object_code(loc,'',instruction[0],instruction[1])

        if len(instruction) == 3:
            object_code(loc,instruction[0],instruction[1],instruction[2])
              


# ===== MAIN =====
if __name__ == "__main__":
    # Call the functions
    print(f'input file processing ....')
    if intermediate_file_generation():
     pass_1(intermediate_file)
     print(f'PASS 1 COMPLETED!!')
     pass_2()
     htme()
     print(f'PASS 2 COMPLETED!!')