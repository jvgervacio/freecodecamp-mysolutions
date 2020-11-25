def arithmetic_arranger(problems,show_answer = False):
    arranged_problems = ""
    arithmetic_line = [[],[],[],[]]
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        problem = problem.split(' ')
       
        n1 = problem[0]
        n2 = problem[2]
        op = problem[1]
         
        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not n1.isdigit() or not n2.isdigit():
            return "Error: Numbers must only contain digits."
            
        n = len(n1) if len(n1) > len(n2) else len(n2)
        
        arithmetic_line[0].append(f"{n1:>{n+2}}")
        arithmetic_line[1].append(f"{op:<2}{n2:>{n}}")
        arithmetic_line[2].append("-"*(n+2))

        answer = 0
        if op == '+':
            answer = int(n1) + int(n2)
        elif op == '-':
            answer = int(n1) - int(n2)
        else:
            return "Error: Operator must be '+' or '-'."
        arithmetic_line[3].append(f"{answer:{n+2}}")
        
    if not show_answer:
        del arithmetic_line[-1]
            
    for item in arithmetic_line:
        for i,sub in enumerate(item):
            arranged_problems = arranged_problems + sub + ('    ' if i < len(item)-1 else '')
        
        if arithmetic_line[-1] != item:
            arranged_problems = arranged_problems + '\n'
    
    return arranged_problems