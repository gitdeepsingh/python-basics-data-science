
# ------------ASSIGNMENT 2-----------------
# ANSWER 1

#%%
'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''

# grade = 'A' # as maximum marks are not mentioned in the question, default grade is A
# try:
#     inputMarks = int(input('Please enter marks: '))
#     if (inputMarks < 0):
#       print('Minimum Marks obtained can be 0!!')
#     else:
#       if(inputMarks < 25):
#           grade = 'F'
#       if(25 <= inputMarks < 45):
#           grade = 'E'
#       elif(45<= inputMarks < 50):
#           grade = 'D'
#       elif(50 <= inputMarks < 60):
#           grade = 'C'
#       elif(60 <= inputMarks < 80):
#           grade = 'B'
#       print(f'Yoour Grade is {grade}')
# except ValueError: # catch non-numeric inputs appropriately
#     print('Invalid marks input. Please re-try!')



    

# %%
# ANSWER 3
def doWhile():
  num = 0
  numList = list([])
  while(len(numList) < 20 and num % 5 != 0 and num % 7 != 0 and num % 11 != 0):
      num += 1
  numList.append(num)
  print(numList)
        
doWhile()