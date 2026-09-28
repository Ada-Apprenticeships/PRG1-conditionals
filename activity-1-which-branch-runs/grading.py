def grade_for_score(score):
    if score >= 70:
        return "Distinction"
    elif score >= 60:
        return "Merit"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


print(grade_for_score(85))
print(grade_for_score(60))
print(grade_for_score(39))
print(grade_for_score(40))
