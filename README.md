# Seasons

A Python program that calculates the number of minutes a person has been alive based on their date of birth, then converts the result into English words.

## How It Works

The program:

1. Prompts the user to enter their date of birth in `YYYY-MM-DD` format.
2. Converts the input into a Python `date` object.
3. Calculates the number of days between the date of birth and today's date.
4. Converts the number of days into minutes.
5. Uses the `inflect` library to convert the number into English words.
6. Prints the result followed by `"minutes"`.

For example:

```text
Date of birth: 2000-01-01
ten million, ... minutes
```

## Requirements

* Python 3
* `inflect`

Install `inflect` with:

```bash
pip install inflect
```

## Running the Program

From the project directory:

```bash
python3 seasons.py
```

Enter your date of birth when prompted:

```text
Date of birth: YYYY-MM-DD
```

## Testing

The project includes `test_seasons.py`, which uses `pytest` to test the program's handling of invalid date formats.

Run the tests with:

```bash
python3 -m pytest
```

## Files

* `seasons.py` — Main program containing the date and minutes calculation.
* `test_seasons.py` — Automated tests for the program.

## Technologies

* **Python**
* `datetime`
* `sys`
* `inflect`
* `pytest`

## Project

This project was completed as part of:

**Harvard University's CS50's Introduction to Programming with Python (CS50P)**
