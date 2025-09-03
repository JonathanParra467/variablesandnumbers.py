"""
Create a Python program that converts kilograms to pounds.
 Use at least four different samples to convert.
 A sample of the math is provided below; do not use the same example in your program.
"""

#this gives the pounds a value
conversian_factor = 2.204

# this give the kilograms a value
kilograms_1 = 1
kilograms_2 = 2
kilograms_3 = 3
kilograms_4 = 4
#This allows the code to make a multiplicaition awnser to the conversion factor
pounds_1 = kilograms_1 * conversian_factor
pounds_2 = kilograms_2 * conversian_factor
pounds_3 = kilograms_3 * conversian_factor
pounds_4 = kilograms_4 * conversian_factor

#This help define and write 
print(f"{kilograms_1} kilograms is equal to {pounds_1:.2f} pounds.")
print(f"{kilograms_2} kilograms is equal to {pounds_2:.2f} pounds.")
print(f"{kilograms_3} kilograms is equal to {pounds_3:.2f} pounds.")
print(f"{kilograms_4} kilograms is equal to {pounds_4:.2f} pounds.")