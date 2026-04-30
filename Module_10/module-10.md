# Module 10

```python
import sqlite3

link = sqlite3.connect("power_log.db")
remote = link.cursor()

remote.execute("""
CREATE TABLE IF NOT EXISTS Power_log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    voltage REAL,
    current REAL,
    power REAL
)"""
 )
link.commit()

def addReadings() :
    voltage = float(input("Input Voltage: "))
    current = float(input("Input Current: "))

    power = voltage * current

    remote.execute("INSERT INTO Power_log (voltage,current, power) VALUES(?, ?,?)",(voltage, current, power))
    link.commit()
    print("Readings recorded. Power =",power,"W")

def viewReadings() :
    remote.execute("SELECT * FROM Power_log")
    rows = remote.fetchall()
    print("\n=====Power Recordings=====")
    for row in rows :
        print(row)

def deleteRecord() :
    idRecord = int(input("Input record id: "))
    remote.execute("DELETE FROM Power_log WHERE id = ?", (idRecord,))
    link.commit()
    print("Record ID",idRecord,"deleted.")

while True:
    print("\n1. Add readings")
    print("2. View readings")
    print("3. Delete readings")
    print("4. Exit")

    option = int(input("Enter option: "))
    if option == 1 :
        addReadings()
    elif option == 2 :
        viewReadings()
    elif option == 3 :
        deleteRecord()
    elif option == 4 :
        break;
    else :
     print("Invalid option")

link.close()
```
