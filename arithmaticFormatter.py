def arithmetic_arranger(problems, show_answers=False):
    #print(len(problems))

    #error handling 1
    if(len(problems)>5):
        return "Error: Too many problems."

    line1,line2,line3,line4=[],[],[],[]

    # extracting numbers and operators
    for problemSet in problems:
        #print(problemSet)
        problemOperands=problemSet.split(" ")

        #error 2 handling, not a digit
        try:
            int(problemOperands[0])
            int(problemOperands[2])
        except:
            return "Error: Numbers must only contain digits."
            
        #error 3 handling, greater than 4 digits
        if(int(problemOperands[0])>9999 or int(problemOperands[2])>9999):
            return "Error: Numbers cannot be more than four digits."

        #error 4 handling, operater aside from + and -
        if(not(problemOperands[1]=="+" or problemOperands[1]=="-")):
            return "Error: Operator must be '+' or '-'."

        num1,num2=problemOperands[0],problemOperands[2]

        if(len(num1)>len(num2)):
            additionalSpaces=len(num1)-len(num2)
            for i in range(len(num1)-len(num2)):
                num2=" "+num2
        else:
            for i in range(len(num2)-len(num1)):
                num1=" "+num1

        num1="  "+num1
        num2=problemOperands[1]+" "+num2
       # print(num1+'\n'+num2)

        dashes=""
        for i in range(len(num1)):
            dashes="-"+dashes

        if(problemOperands[1]=="+"):
            answer=str(int(problemOperands[0])+int(problemOperands[2]))
        else:
            answer=str(int(problemOperands[0])-int(problemOperands[2]))
    
        for i in range(len(dashes)-len(answer)):
                answer=" "+answer
        
       # print(num1+'\n'+num2+'\n'+ dashes + '\n'+answer)

        
        line1.insert(0,num1)

        
        line2.insert(0,num2)

        
        line3.insert(0,dashes)
        
        
        line4.insert(0,answer)

    outputLine1=""
    for i in line1:
        outputLine1=i+"    "+outputLine1
    outputLine1=outputLine1[:len(outputLine1)-4]

    outputLine2=""
    for i in line2:
        outputLine2=i+"    "+outputLine2
    outputLine2=outputLine2[:len(outputLine2)-4]

    outputLine3=""
    for i in line3:
        outputLine3=i+"    "+outputLine3
    outputLine3=outputLine3[:len(outputLine3)-4]

    #print(outputLine1)
    #print(outputLine2)
    #print(outputLine3)

    if(show_answers==False):
        return outputLine1+'\n'+outputLine2+'\n'+outputLine3

    else:
        outputLine4=""
        for i in line4:
            outputLine4=i+"    "+outputLine4
        outputLine4=outputLine4[:len(outputLine4)-4]
    
        return outputLine1+'\n'+outputLine2+'\n'+outputLine3+'\n'+outputLine4


    return problems

print(f'\n{arithmetic_arranger(["9999 + 9999", "3801 - 2", "45 + 43", "123 + 49","123 + 49"])}')