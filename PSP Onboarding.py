area = 0
R = 0.0821
M = 1
temp = 273
pressure = 17.01 * 1.44
c= 0.62
densityOxygen = 24.3
densityHydrogen = 1.53
CpHydrogen = 14.25
CpOxygen = 0.916
CvHydrogen = CpHydrogen - R
CvOxygen = CpOxygen - R
Cv = 0
Cp = 0
chosenGas = 0
import math 

print(" ******READ ME******")
print("This program will calculate orfice area for a flame ignitor that uses Gaseous Oxygen and Hydrogen as the Oxidizer and Fuel.")
print("The suggested mDot is 0.0605 g/s and the suggested OF ratio. However, the program will work with other values as well. \n \n")


mDotTotal = float(input("At what combined mDot do you want to calculate area for? (g/s) "))
OFRatio = int(input("At what O/F do you want to calculate area for? "))

mDotTotal = mDotTotal / 1000
mDotOx = (mDotTotal * OFRatio)/(1 + OFRatio)

mDotFuel = (mDotTotal - mDotOx)

chosenGas = input("Calculate for Oxygen or Hydrogen? (O or H) ")
if chosenGas == "O":
    Cp = CpOxygen
    Cv = CvOxygen
    density = densityOxygen
    mDotUsed = mDotOx
elif chosenGas == "H":
    Cp = CpHydrogen
    Cv = CvHydrogen
    density = densityHydrogen
    mDotUsed = mDotFuel
    
gamma = Cp /Cv

termOne = (gamma*density*pressure)

termTwo = 2/(gamma + 1)

termThree = (gamma + 1) / (gamma - 1)


area = mDotUsed / (c * (math.sqrt(termOne * (termTwo ** termThree))))
area *= 1000000
print (str(area) + " mm^2")
