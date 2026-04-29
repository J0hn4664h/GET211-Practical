## srs.txt

```txt
TITLE: Student Result Processing System

1. OBJECTIVE
To develop a program that processes student scores and determines grade and pass/fail status.

2. INPUTS
- Student name
- Subjects
- Scores

3. PROCESS
- Store subjects and scores
- Compute grade based on score
- Determine pass/fail status

4. OUTPUTS
- Student name
- Subject, score, grade, status

5. ASSUMPTIONS
- Scores are numeric
- Pass mark is 40
```

---

## scores.py

```python
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
```
