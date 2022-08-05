import re

def arithmetic_arranger(problems_list, display=False):
  if len(problems_list) > 5: 
    return "Error: Too many problems."
  else:
    init_up = ''
    init_down = ''
    dash = ''
    init_answer = ''
    
    for prob in problems_list:
      if not ('+' in prob or '-' in prob): 
        return "Error: Operator must be '+' or '-'."
        
      elif not (re.findall("[^0-9+-]", prob) == [' ', ' ']):
        return "Error: Numbers must only contain digits."
        
      else:
        num1, num2 = re.findall("^([0-9]+)\s[+-]\s([0-9]+)", prob)[0]
        ops = re.findall("^[0-9]+\s([+-])\s[0-9]+", prob)[0]

        if ops == '+':
          answer = str(int(num1) + int(num2))
        else: 
          answer = str(int(num1) - int(num2))

        length1 = len(num1)
        length2 = len(num2)
        length_ans = len(answer)
        
        if length1 > 4 or length2 > 4:
          return "Error: Numbers cannot be more than four digits."

        if length1 == length2:
          init_up += ' ' * 2 + num1 + ' ' * 4
          init_down += ops + ' ' + num2 + ' ' * 4
          dash += '-' * (2 + length1) + ' ' * 4

          answer_space = abs(length_ans - (2 + length1))
          init_answer += ' ' * answer_space + answer + ' ' * 4

        elif length1 > length2:
          add_space = length1 - length2
          init_up += ' ' * 2 + num1 + ' ' * 4
          init_down += ops + ' ' * (add_space + 1) + num2 + ' ' * 4
          dash += '-' * (2 + length1) + ' ' * 4

          answer_space = abs(length_ans - (2 + length1))
          init_answer += ' ' * answer_space + answer + ' ' * 4

        else:
          add_space = length2 - length1
          init_up += ' ' * (2 + add_space) + num1 + ' ' * 4
          init_down += ops + ' ' + num2 + ' ' * 4
          dash += '-' * (2 + length2) + ' ' * 4

          answer_space = abs(length_ans - (2 + length2))
          init_answer += ' ' * answer_space + answer + ' ' * 4

    # delete excess spaces
    init_up = init_up[:-4]
    init_down = init_down[:-4]
    dash = dash[:-4]

    arranged_problems = init_up + '\n' + init_down + '\n' + dash

    if display == True:
      init_answer = init_answer[:-4]
      arranged_problems += '\n' + init_answer

    return arranged_problems
