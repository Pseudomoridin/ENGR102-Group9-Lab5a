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
if smoker == "Y":
  smoker = True
else:
  smoker = False
cholesterol = int(input("Enter your total cholesterol (mg/dL): "))
hdl = int(input("Enter your HDL cholesterol (mg/dL): "))
bp = int(input("Enter your systolic BP (mmHg): "))
medicated = str(input("Are you taking blood pressure medication (Y/N)? "))
if medicated == "Y":
  medicated = True
else:
  medicated = False

if gender == "M":
  reference = r[0]
else:
  reference = r[1]

reference[1] = reference[1][agegroup]
reference[2] = reference[2][agegroup]

if medicated:
  reference[4] = reference[4][0]
else:
  reference[4] = reference[4][1]

############################################
############ The Actual Program ############
############################################
score = 0
# Age
if age < 35:
  score += reference[0][0]
elif age < 40:
  score += reference[0][1]
elif age < 45:
  score += reference[0][2]
elif age < 50:
  score += reference[0][3]
elif age < 55:
  score += reference[0][4]
elif age < 60:
  score += reference[0][5]
elif age < 65:
  score += reference[0][6]
elif age < 70:
  score += reference[0][7]
elif age < 75:
  score += reference[0][8]
else:
  score += reference[0][9]

# Cholesterol
if cholesterol < 160:
  score += reference[1][0]
elif cholesterol < 200:
  score += reference[1][1]
elif cholesterol < 240:
  score += reference[1][2]
elif cholesterol < 280:
  score += reference[1][3]
else:
  score += reference[1][4]

# Smoking
if smoker:
  score += reference[2][1]

# HDL
if hdl > 60:
  score += reference[3][0]
elif hdl > 50:
  score += reference[3][1]
elif hdl > 40:
  score += reference[3][2]
else: 
  score += reference[3][3]

# Blood Pressure
if bp < 120:
  score += reference[4][0]
elif bp < 130:
  score += reference[4][1]
elif bp < 140:
  score += reference[4][2]
elif bp < 160:
  score += reference[4][3]
else:
  score += reference[4][4]

# Percent calculation
for key in reference[5].keys():
  if score < key:
    print("Your 10-year risk of a heart attack is {}%".format(reference[5][key]))
    break