def Add(a, b):
    return a + b
  
# Function to subtract two numbers 
def Subtract(a, b):
    return a - b
  
# Function to multiply two numbers
def Multiply(a, b):
    return a * b
  
# Function to divide two numbers
def Divide(a, b):
    return a / b

# Function to power two numbers
def Power(a, b):
    return a ** b

# Function to remaind two numbers
def Remainder(a, b):
    return a % b


while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  # take input from the user
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if choice in ('+', '-', '*', '/', '^', '%', '#', '$'):
      if choice == '#':
          print("Done. Terminating")
          break
      a = input('Enter first number: ')
      print(str(a))
      if a.endswith('$'): continue
      b = input('Enter second number: ')
      print(str(b))
      if b.endswith('#'):
        print("Done. Terminating")
        break
      if b.endswith('$'): continue

      
      


      
  if choice == '+':
      print(float(a), "+" ,float(b), "=", Add(float(a), float(b)))
  elif choice == '-':
      print(a, "-", b, "=", Subtract(a, b))
  elif choice == '*':
      print(float(a), "*",float(b), "=", Multiply(float(a), float(b)))
  elif choice == '/':
      if int(b) != 0:
          print(float(a), "/", float(b), "=", Divide(float(a), float(b)))
          break
      else:
          print("float division by zero")
          print(float(a), "/", float(b), "=", "None")
  elif choice == '^':
      print(float(a), "**",float(b), "=", Power(float(a), float(b)))
  elif choice == '%':
      print(float(a), "%",float(b), "=", Remainder(float(a), float(b)))
      break
