#Things to Fix:
#T_t should be chamber?
#Double check Should specific heat ratio of O and H be the same? Check with Connor
#Recalculate Density for both since Our Pressure is now 200 PSI, should the temp for that be ambient or chamber??
#https://www.omnicalculator.com/physics/gas-density

import math

# Constants and given values
C = 0.62  # Coefficient

PO = 18.104  # Density of Oxygen (kg/m^3 or other consistent unit)
PH = 1.1315  # Density of Hydrogen (kg/m^3 or other consistent unit)
T_t = 1818.97  # Temperature in Kelvin

# Specific Heat Ratios
yO = 1.4  # Specific Heat Ratio of Oxygen
yH = 1.4  # Specific Heat Ratio of Hydrogen


# Mass flow rates for Oxygen and Hydrogen (example values, replace with actual values)
q_m_tot = 0.003
print(f"Mass flow rate total: {q_m_tot}")
q_m_H2 = .001
q_m_O2 = .002
# Solving for cross-sectional area A for oxygen and hydrogen

#Lets iterate
target_O2_A = 8.107*(10**-7)#Unit is m^2 #Using .04 inch diameter
target_H2_A = 0.00000153279012 #Using .055 inch diameter

solved_O2_p1 = ((q_m_O2/(C*target_O2_A))**2)/(yO*PO*((2 / (yO + 1)) ** ((yO + 1) / (yO - 1))))
print("Solved O2 in PASCALS")
print(solved_O2_p1)

solved_H2_p1 = ((q_m_H2/(C*target_H2_A))**2)/(yH*PH*((2 / (yH + 1)) ** ((yH + 1) / (yH - 1))))
print("Solved H2 in PASCALS")
print(solved_H2_p1)


