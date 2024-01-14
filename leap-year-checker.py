
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else: 
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

print("Welcome to my leap year checker!")
year = int(input("Enter the year you want to check: "))
is_leap_year(year)