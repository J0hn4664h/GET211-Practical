name = input("Name: ")
subjects = []
scores = []
total = int(input("Input number of subjects: "))
for i in range(total):
    subject = input("Input subject: ")
    score = float(input(f"Input score: "))
    subjects.append(subject)
    scores.append(score)
print("Name:",name)
for i in range(total):
    if scores[i] >= 70 :
        grade = "A"
    elif scores[i] >= 60 :
        grade = "B"
    elif scores[i] >= 50 :
        grade = "C"
    elif scores[i] >= 45 :
        grade = "D"
    elif scores[i] >= 40 :
        grade = "E"
    else :
        grade = "F"
    if scores[i] >= 40 :
        status = "Pass"
    else :
        status = "Fail"
    print("Subject:",subjects[i],"Score:",scores[i],"Grade:",grade,"Status:",status)
