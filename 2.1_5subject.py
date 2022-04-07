print("Enter the marks of five subjects::")

subject_1 = float (input ("Subject 1: "))
subject_2 = float (input ("Subject 2: "))
subject_3 = float (input ("Subject 3: "))
subject_4 = float (input ("Subject 4: "))
subject_5 = float (input ("Subject 5: "))


total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total / 500.0) * 100
if percentage >= 60:
    division = 'First'
elif percentage >= 45:
    division = 'Second'
elif percentage >= 33:
    division = 'Third'
else:
    division = 'Failed'

print ("The Total marks is: ", total)
print ("The Percentage is: =", percentage, "%")
print ("The Division is:   ", division)