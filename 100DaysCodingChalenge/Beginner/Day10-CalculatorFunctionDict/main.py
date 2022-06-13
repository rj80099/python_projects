#calculator 
from art import logo
#add
def add(n1,n2):
  """Takes two number as and return the addition of them"""
  return (n1+n2)
#subtract
def sub(n1,n2):
  """Takes two number as and return the subtration of them"""
  return (n1-n2)

#multiply
def mul(n1,n2):
  """Takes two number as and return the multiplication of them"""
  return (n1*n2)

#divide
def div(n1,n2):
  """Takes two number as and return the division of them"""
  return (n1/n2)


operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}


def calculator():
  print(logo)
  num1=float(input("what is the first number? "))
  for symbol in operations:
    print(symbol)
  should_continue=True
  while should_continue:
    operation_symbol=input("Pick an operation from above :")

    if operation_symbol not in operations:
      print("Invalid operation please type again")
    else:
      num2=float(input("what's the next number? "))
      function =operations[operation_symbol]
      answer=function(num1,num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      if input("Do you want to continue, Type 'y' or 'n' :") =='y':
        num1=answer
      else:
        should_contiue=False
        calculator()
calculator()
