import math

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    bc = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))

if __name__ == '__main__':
    main()
# # This code calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem.