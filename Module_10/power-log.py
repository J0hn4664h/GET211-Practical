import sqlite3

link = sqlite3.connect("power-log.db")
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

    remote.execute("INSERT INTO Power_log (voltage,current, power) VALUES(?, ?, ?)",(voltage, current, power))
    link.commit()
    print("Readings recorded. Power =",power,"W")

def viewReadings() :
    remote.execute("SELECT * FROM Power_log")
    rows = remote.fetchall()
    print("\n=====Power Recordings=====")
    for row in rows :
        print(row)

def updateReadings() :
    recordId = int(input("Input ID: "))
    newVoltage = float(input("Input voltage: "))
    newCurrent = float(input("input current: "))

    newPower = newVoltage * newCurrent
    remote.execute("""
     UPDATE Power_log SET voltage = ?, current = ?, voltage = ?
     WHERE id = ?""", (newVoltage, newCurrent, newPower, recordId))
    link.commit()
    print("Update Complete")

def deleteRecord() :
    idRecord = int(input("Input record id: "))
    remote.execute("DELETE FROM Power_log WHERE id = ?", (idRecord,))
    link.commit()
    print("Record ID",idRecord,"deleted.")

while True:
    print("\n1. Add readings")
    print("2. View readings")
    print("3. update readings")
    print("4. Delete readings")
    print("5. Exit")

    option = int(input("\nEnter option: "))
    if option == 1 :
        addReadings()
    elif option == 2 :
        viewReadings()
    elif option == 3 :
        updateReadings()
    elif option == 4 :
        deleteRecord()
    elif option == 5 :
        break
    else :
     print("\nInvalid option")

link.close()
