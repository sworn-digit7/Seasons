from datetime import date
import sys

def main():
    dob = input("Date of birth: ")
    minutes(dob)


def minutes(x):
    
    x = x.split("-")

    today = date.today()
    date1 = date(int(x[0]), int(x[1]), int(x[2]))

    difference = today - date1

    min = difference.days

    print(min * 60)


if __name__ == "__main__":
    main()