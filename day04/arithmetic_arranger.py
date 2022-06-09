def findlarger(a,b):
  if len(a) > len(b):
    return (len(a), 0)
  elif len(a) == len(b):
    return (len(a), 0)
  else:
    return (len(b), 2)
 

def arithmetic_arranger(problems, show_ans=False):
  upper_values = ''
  middle_values = ''
  dashes = ''
  ans = ''
  
  if len(problems) > 5:
    return "Error: Too many problems."
  for pr in problems:
    temp = pr.split()
    if temp[1] not in ('+','-'):
      return "Error: Operator must be '+' or '-'."
    if not (temp[0].isdigit() and temp[2].isdigit()):
      return "Error: Numbers must only contain digits."
    if len(temp[0]) > 4 or len(temp[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    larger_one = findlarger(temp[0], temp[2])
    dashes += f"{'-'*(larger_one[0]+2)}    "
    if temp[1] == '+':
      a = int(temp[0]) + int(temp[2])
    else:
      a = int(temp[0]) - int(temp[2])

    ans += f"{str(a).rjust(larger_one[0]+2)}    "
    
    if larger_one[1] == 0:
      upper_values += f"{temp[0].rjust(len(temp[0])+2)}    "
      middle_values += f"{temp[1]} {temp[2].rjust(len(temp[0]))}    "
      
    else:
      upper_values += f"{temp[0].rjust(len(temp[2])+2)}    "
      middle_values += f"{temp[1]} {temp[2].rjust(len(temp[2]))}    "

  if show_ans:
    return upper_values.rstrip() + '\n' + middle_values.rstrip() + '\n'+ dashes.rstrip() + '\n' + ans.rstrip()
    
  return upper_values.rstrip() + '\n' + middle_values.rstrip() + '\n' + dashes.rstrip()