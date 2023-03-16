def run(program):
    var_dict = {'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}
    
    jump_dict = {}
    output_list = []

    instruction_count = 0

    for ins in program:
        jump_dict[ins[:-1]] = instruction_count
        instruction_count += 1

    instructions = 0

    while instructions<=len(program)-1:
        instruction = program[instructions].split()
        instructions += 1

        if(instruction[0]=="PRINT"): 
            if instruction[1].isdigit(): output_list.append(int(instruction[1]))
            else: output_list.append(var_dict[instruction[1]])
        elif(instruction[0]=="MOV"): 
            if instruction[2].isdigit(): var_dict[instruction[1]] = int(instruction[2])
            else: var_dict[instruction[1]] = var_dict[instruction[2]]
        elif(instruction[0]=="ADD"): 
            if instruction[2].isdigit(): var_dict[instruction[1]] += int(instruction[2]) 
            else: var_dict[instruction[1]] += var_dict[instruction[2]] 
        elif(instruction[0]=="SUB"): 
            if instruction[2].isdigit(): var_dict[instruction[1]] -= int(instruction[2])
            else: var_dict[instruction[1]] -= var_dict[instruction[2]]
        elif(instruction[0]=="MUL"): 
            if instruction[2].isdigit(): var_dict[instruction[1]] *= int(instruction[2])
            else: var_dict[instruction[1]] *= var_dict[(instruction[2])]
        elif(instruction[0]=="JUMP"): instructions = jump_dict[instruction[1]]
        elif(instruction[0]=="END"): break
        elif(instruction[0]=="IF"):
            condition_result = bool()
            
            if(instruction[2]=="=="): 
                if instruction[3].isdigit(): condition_result = var_dict[instruction[1]]==int(instruction[3])
                else: condition_result = var_dict[instruction[1]]==var_dict[instruction[3]]
            elif(instruction[2]=="!="): 
                if instruction[3].isdigit(): condition_result = var_dict[instruction[1]]!=int(instruction[3])
                else: condition_result = var_dict[instruction[1]]!=var_dict[instruction[3]]
            elif(instruction[2]=="<"): 
                if instruction[3].isdigit(): condition_result = var_dict[instruction[1]]<int(instruction[3])
                else: condition_result = var_dict[instruction[1]]<var_dict[instruction[3]]
            elif(instruction[2]=="<="): 
                if instruction[3].isdigit(): condition_result = var_dict[instruction[1]]<=int(instruction[3])
                else: condition_result = var_dict[instruction[1]]<=var_dict[instruction[3]]
            elif(instruction[2]==">"): 
                if instruction[3].isdigit(): condition_result = var_dict[instruction[1]]>int(instruction[3])
                else: condition_result = var_dict[instruction[1]]>var_dict[instruction[3]]
            else: 
                if instruction[3].isdigit(): condition_result = var_dict[instruction[1]]>=int(instruction[3])
                else: condition_result = var_dict[instruction[1]]>=var_dict[instruction[3]]

            if condition_result: instructions = jump_dict[instruction[5]]
        else: jump_dict[instruction[0][:-1]] = instructions-1

    return output_list

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)