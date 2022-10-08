import sqlite3

db = sqlite3.connect("AppointmentTable2.db")

c = db.cursor()

def main():
    keepGoing = True
    while keepGoing:
        choice = menu()
        if choice == "5":
            keepGoing = False
            print("Bye-Bye! Thank you for visiting us, you have always been our favorite patient")
        elif choice == "1":
            viewHours()
        elif choice == "2":
            shedapp()
        elif choice == "3":
            reschedapp()
        elif choice == "4":
            canapp()
        elif choice == "6":
            default()
    c.close()

def menu():
    print(""" --- Sohma General Hospital ---
Welcome to Sohma General Hospital
We are glad you chose us to provide you with expert care
What would you like to do today?

1) View Hours of Hospital and Provider time
2) Schedule a new Appointment
3) Reschedule an Existing Appointment
4) Cancel an Existing Appointment
5) Exit
""")
    choice = input("What is your selection: ")
    return choice

def default():
    c.execute("DROP TABLE IF EXISTS appoints")
    sql ="""
    CREATE TABLE appoints (
    id  INTEGER Primary key,
    Doctor varchar(50),
    Specialty varchar(50),
    Center VARCHAR(50),
    Scheduled VARCHAR(50)
    )"""
    c.execute(sql)

    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",
            ('Dr.Joy' , 'Dermatology', 'Center for Dermarology', 'No Appointment Set'))
    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",
            ('Dr.Smith' , 'Cardiology', 'Center for Cardiac Care','No Appointment Set'))
    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",
            ('Dr.Adams' , 'Pediatrics', 'Center for Family Medicine','No Appointment Set'))
    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",
            ('Dr.Williams' , 'Gynecology','Center for OB/GYN','No Appointment Set'))
    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",
            ('Dr.Davis' , 'Orthopedics', 'Center for Orthapedic Care','No Appointment Set'))
    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",
            ('Dr.Miller' , 'General Surgery','Center for General Surgery','No Appointment Set'))

    db.commit()

def viewHours():
    choice = c.execute("SELECT * FROM appoints")
    for record in choice:
        (id, Doctor, Specialty, Center, Scheduled) = record
        print("Doctor Name:",format(Doctor))
        print("Area of Specialty:",format(Specialty))
        print("Location: ",format(Center))
        print("Scheduled Appointment on File: ",format(Scheduled))
        print()

def shedapp():
    print("Please choose which Doctor, Specialty, Center, and time you want your appointment")
    doctor = input("Doctor: ")
    specialty = input("Specialty: ")
    center = input("Center: ")
    time = input("Time: ")

    c.execute("INSERT INTO appoints VALUES (null, ?, ?, ?, ?)",(doctor, specialty, center, time))
    db.commit()

def reschedapp():
    grid = getRecordID()
    if grid == 0:
        print("Not a valid input, please try again")
    else:
        choice = c.execute("SELECT * FROM appoints WHERE id = ?",(grid,))
        for row in choice:
            (id, Doctor, Specialty, Center, Scheduled) = row
        DiffDoc = input("Doctor: ({}) ".format(Doctor))
        if DiffDoc =="":
            DiffDoc = Doctor
        Diffspec = input("Specialty: ({}) ".format(Specialty))
        if Diffspec =="":
            Diffspec = Specialty
        Diffcent = input("Center: ({})".format(Center))
        if Diffcent =="":
            Diffcent = Center
        Diffshed = input("Scheduled: ({})".format(Scheduled))
        if Diffshed =="":
            Diffshed = Scheduled
    c.execute("""UPDATE appoints
        SET
        Doctor = ?,
        Specialty = ?,
        Center = ?,
        Scheduled = ?
        WHERE id = ?""",
        (DiffDoc,Diffspec, Diffcent,Diffshed, grid ))

    db.commit()

def canapp():
    grid = getRecordID()
    if grid == 0:
        print("Not a valid input, please try again")
    else:
        choice = c.execute("SELECT * FROM appoints WHERE id = ?",(grid,))
        for row in choice:
            (id, Doctor, Specialty, Center, Scheduled) = row
            print("Doctor: ({}) ".format(Doctor))
            print("Specialty: ({}) ".format(Specialty))
            print("Center: ({}) ".format(Center))
            print("Scheduled: ({})".format(Scheduled))
        confirm = input("Are you sure you want to reschedule this appointment, It may not become available again")
        confirm = confirm.upper()
        if confirm == "YES":
            c.execute("DELETE FROM appoints WHERE id = ?",(grid,))
            print("Appointment cancelled, we are sad to see you go")
            db.commit


def getRecordID():
    choice = c.execute("SELECT id, scheduled FROM appoints")

    print()
  #create empty list of current IDs
    legalIDs = []
    for row in choice:
        (id, scheduled) = row
        print("Your appointment {}: {}".format(id, scheduled))

    #add current ID to list of legal IDs
    legalIDs.append(id)

    print()
    returnVal = input("Which user #? (or 0 to cancel) ")

  #be sure it's really a digit
    if not returnVal.isdigit():
        print("ID must be a digit")
        returnVal = 0

  #ensure returnVal is one of the legal IDs
    if int(returnVal) not in legalIDs:
        returnVal = 0

    return returnVal



if __name__ == "__main__":
    main()

