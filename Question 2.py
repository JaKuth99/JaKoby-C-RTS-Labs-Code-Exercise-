test_string=input("Enter your string:")
overflow=int(input("Enter your desired overflow:"))
new_test_string=test_string
if len(test_string)< overflow:
 print("Your overflow is greater than the length of your string. Please run the program with a longer string or less overflow.")
else:
 moved_string=test_string[len(test_string)-overflow::]
 concat_string=moved_string+test_string
 result=concat_string[:len(test_string):]
 print(result)
