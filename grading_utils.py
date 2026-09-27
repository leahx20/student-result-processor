
def validate_mark(mark):
    return 0 <= mark <= 100


def get_grade_description(average):
    if average >= 70:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"
