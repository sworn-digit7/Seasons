from datetime import date
import sys
import inflect


def main():
    dob = input("Date of birth: ")
    minutes(dob)


def minutes(x):
    
    try:
        x = x.split("-")

        today = date.today()
        date1 = date(int(x[0]), int(x[1]), int(x[2]))

        difference = today - date1

        mins = int((difference.days) * 24 * 60)

        p = inflect.engine()
        print(p.number_to_words(mins))

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()