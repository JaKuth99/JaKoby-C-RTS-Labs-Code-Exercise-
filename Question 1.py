test_array=[]
test_array_input= input("Enter integers separated by a space:")
test_array=test_array_input.split()
test=[]
try:
  for i in test_array:
    test.append(int(i))
  test_input=input("Enter your number:")
  try:
    test_input=float(test_input)
    below = 0
    above = 0
    for i in test:
      if i < test_input:
        below += 1
      elif i > test_input:
        above += 1
    print("above:{}, below:{}".format(above,below))
  except:
    print("Sorry, input is invalid. Please run the program again") 
except:
  print("There are non-integers in this array. Please restart and try again")
