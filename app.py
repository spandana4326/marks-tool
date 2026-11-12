"""Marks Tool - print a short report for a list of marks."""
from stats import average, highest
from stats import average, highest, lowest, pass_count

MARKS = [72, 65, 88, 91, 54]


def main():
    settings = load_env()
    pass_mark = int(settings["PASS_MARK"])    
    print(settings["APP_NAME"])
    print("Count :", len(MARKS))
    print("Average:", average(MARKS))
    print("Highest:", highest(MARKS))
    print("Passed:", pass_count(MARKS, pass_mark), "of", len(MARKS))

if __name__ == "__main__":
    main()


