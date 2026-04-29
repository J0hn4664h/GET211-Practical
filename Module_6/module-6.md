## data.csv

```csv
voltage,current
10,2
12,3
9,1
15,5
11,4
```
---

## analysis.py

```python
import csv

voltages = []
currents = []

with open("data.csv", "r") as a:
    content = csv.DictReader(a)
    for row in content:
        voltages.append(float(row["voltage"]))
        currents.append(float(row["current"])

avg_vol = sum(voltages)/len(voltages)
max_vol = max(voltages)
min_vol = min(voltages

print("Voltages => Avg:",avg_vol,"Max:",max_vol,"Min:",min_vol)

avg_cur = sum(currents)/len(currents)
max_cur = max(currents)
min_cur = min(currents)

print("Currents => Avg:",avg_cur,"Max:",max_cur,"Min:",min_cur)
```
