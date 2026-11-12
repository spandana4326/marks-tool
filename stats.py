def average(marks):
    return sum(marks) / len(marks)


def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def pass_count(marks, pass_mark):
    return sum(1 for mark in marks if mark >= pass_mark)
