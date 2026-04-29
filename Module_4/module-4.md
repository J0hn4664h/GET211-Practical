# Module 4

## cgpa.py

```python
gradePoints = [3, 4, 5, 3, 4, 5]
creditUnits = [1, 2, 3, 2, 2, 2]
total_points = 0
total_units = 0

for points in range(len(gradePoints)):
    total_points += gradePoints[points] * creditUnits[points]
    total_units += creditUnits[units]

cgpa = total_points/total_units

print(f"CGPA = {cgpa:.2f}")
```
## traffic.py

```python
colour = input("Input colour: ").strip().lower()

if colour == "red":
   print("STOP")
elif colour == "yellow":
    print("READY")
elif colour == "green":
    print("GO")
else:
    print("Invalid input");
```
