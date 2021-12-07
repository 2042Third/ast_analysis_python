import ast

def simpe_eval(a):
  a = ast.parse(a)
  print(ast.dump(a,indent=2))
  
if __name__ == "__main__":
  simpe_eval(input("Enter regular expression: "))
