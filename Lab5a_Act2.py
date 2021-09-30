# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 5A Activity 2
# Date:         September 29, 2021

from reference import reference as r

############################################
## Getting input and condensing reference ##
############################################
gender = str(input("Enter your sex (M/F): "))
age = int(input("Enter your age (years): "))
# Splitting age into groups
if age < 40:
  agegroup = 0
elif age < 50:
  agegroup = 1
elif age < 60:
  agegroup = 2
elif age < 70:
  agegroup = 3
else:
  agegroup = 4

smoker = str(input("Do you smoke cigarettes (Y/N)? "))
if smoker in ["Y","y"]:
  smoker = True
else:
  smoker = False
cholesterol = int(input("Enter your total cholesterol (mg/dL): "))
hdl = int(input("Enter your HDL cholesterol (mg/dL): "))
bp = int(input("Enter your systolic BP (mmHg): "))
medicated = str(input("Are you taking blood pressure medication (Y/N)? "))
if medicated in ["Y","y"]:
  medicated = True
else:
  medicated = False

if gender in ["M","m"]:
  reference = r[0]
else:
  reference = r[1]

reference[0][1] = reference[0][1][agegroup]
reference[0][2] = reference[0][2][agegroup]

if medicated:
  reference[0][4] = reference[0][4][0]
else:
  reference[0][4] = reference[0][4][1]

############################################
############ The Actual Program ############
############################################
score = 0
# Age
if age < 35:
  score += reference[0][0][0]
elif age < 40:
  score += reference[0][0][1]
elif age < 45:
  score += reference[0][0][2]
elif age < 50:
  score += reference[0][0][3]
elif age < 55:
  score += reference[0][0][4]
elif age < 60:
  score += reference[0][0][5]
elif age < 65:
  score += reference[0][0][6]
elif age < 70:
  score += reference[0][0][7]
elif age < 75:
  score += reference[0][0][8]
else:
  score += reference[0][0][9]
#print(score)

# Cholesterol
if cholesterol < 160:
  score += reference[0][1][0]
elif cholesterol < 200:
  score += reference[0][1][1]
elif cholesterol < 240:
  score += reference[0][1][2]
elif cholesterol < 280:
  score += reference[0][1][3]
else:
  score += reference[0][1][4]
#print(score)

# Smoking
if smoker:
  score += reference[0][2][1]
#print(score)

# HDL
if hdl >= 60:
  score += reference[0][3][0]
elif hdl >= 50:
  score += reference[0][3][1]
elif hdl >= 40:
  score += reference[0][3][2]
else: 
  score += reference[0][3][3]
#print(score)

# Blood Pressure
if bp < 120:
  score += reference[0][4][0]
elif bp < 130:
  score += reference[0][4][1]
elif bp < 140:
  score += reference[0][4][2]
elif bp < 160:
  score += reference[0][4][3]
else:
  score += reference[0][4][4]
#print(score)

key_list = list(reference[0][5].keys())
key_list.sort()
#print(key_list)
#print(score)
# Percent calculation
for x in range(len(key_list)):
  if score <= key_list[x]:
    print("Your 10-year risk of a heart attack is {}%".format(reference[0][5][key_list[x]]))
    break