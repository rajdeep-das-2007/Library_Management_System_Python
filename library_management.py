import os
import mysql.connector as sc
import datetime as dt

# Function to Delete/truncate data from Library
def truncate_data():
    os.system('cls')
    print('************************************************************')
    print('*                Truncate Library Data                     *')
    print('************************************************************')
    print('* 1. Delete all Books                                      *')
    print('* 2. Delete all Members                                    *')
    print('* 3. Delete all Registers (Issued Books)                   *')
    print('* 4. Delete ALL (Books, Members, Registers)                *')
    print('* 0. Cancel                                                *')
    print('************************************************************')
    try:
        choice = int(input(' Enter Option :- '))
        if choice == 0:
            print("Cancelled.")
            return
        con = sc.connect(host='localhost', user='root', password='12345678', database='library')
        cur = con.cursor()
        if choice == 1:
            cur.execute("TRUNCATE TABLE book")
            con.commit()
            print("All books deleted.")
        elif choice == 2:
            cur.execute("TRUNCATE TABLE member")
            con.commit()
            print("All members deleted.")
        elif choice == 3:
            cur.execute("TRUNCATE TABLE register")
            con.commit()
            print("All register records deleted.")
        elif choice == 4:
            cur.execute("TRUNCATE TABLE register")
            cur.execute("TRUNCATE TABLE book")
            cur.execute("TRUNCATE TABLE member")
            con.commit()
            print("All data deleted from library.")
        else:
            print("Invalid option.")
        con.close()
    except Exception as e:
        print("Error during truncation:", e)
    input("Press any key to continue...")

#Function to check availibity of a Book no.
def checkbook(bno):
    try:
        con = sc.connect(host='localhost', user='root', password='12345678', database='library')
        cur = con.cursor()
        cur.execute("Select count(*) from book where bno=%s", (bno,))
        data = cur.fetchall()
        d = data[0][0]
        con.close()
        return d
    except Exception:
        return 0

#Function to check availibity of a Member no..
def checkmember(idd):
    try:
        con = sc.connect(host='localhost', user='root', password='12345678', database='library')
        cur = con.cursor()
        cur.execute("Select count(*) from member where id=%s", (idd,))
        data = cur.fetchall()
        d = data[0][0]
        con.close()
        return d
    except Exception:
        return 0

#Function to check availibity of a issue no.
def checkissue(iss):
    try:
        con = sc.connect(host='localhost', user='root', password='12345678', database='library')
        cur = con.cursor()
        cur.execute("Select count(*) from register where is_no=%s", (iss,))
        data = cur.fetchall()
        d = data[0][0]
        con.close()
        return d
    except Exception:
        return 0

#Function to check book with member.
def checki_book_member(iss):
    try:
        con = sc.connect(host='localhost', user='root', password='12345678', database='library')
        cur = con.cursor()
        cur.execute("Select count(*) from register where id=%s", (iss,))
        data = cur.fetchall()
        d = data[0][0]
        con.close()
        return d
    except Exception:
        return 0

#Function to check availibity of a issue no.
def checkqty(bno):
    try:
        con = sc.connect(host='localhost', user='root', password='12345678', database='library')
        cur = con.cursor()
        cur.execute("Select copy from book where bno=%s", (bno,))
        data = cur.fetchone()
        d = data[0] if data else 0
        con.close()
        return d
    except Exception:
        return 0

# Function to Register a Book
def book():
    os.system('cls')
    ch = 'y'
    while ch.lower() == 'y':
        con = sc.connect(host='localhost', database='library', user='root', password='12345678')
        cur = con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*              Library Management System                   *')
            print('************************************************************')

            bno = int(input(" Enter Book No. \t\t\t: "))
            bno = int("102" + str(bno))
            while checkbook(bno):
                print(" Entered Book No. already Exists ")
                bno = int(input(" Enter Book No. \t\t\t: "))
                bno = int("102" + str(bno))

            bname = input(" Enter Book Name \t\t\t: ")
            author = input(" Enter Author Name \t\t\t: ")
            price = float(input(" Enter Book Price \t\t\t: "))
            qty = int(input(" Enter Quantity \t\t\t: "))

            cur.execute("""
                INSERT INTO book (bno, bname, author, price, copy)
                VALUES (%s, %s, %s, %s, %s)
            """, (bno, bname, author, price, qty))
            con.commit()

            print('************************************************************')
            print("\t\tBook Successfully Registered")
            print('************************************************************')
            ch = input("Do you want to register another book? (y/n): ")
            con.close()

        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during registering book.")
            print('************************************************************')
            ch = input("Do you want to try with another data? (y/n): ")

# Function to Register a Member
def member():
    os.system('cls')
    ch = 'y'
    while ch.lower() == 'y':
        con = sc.connect(host='localhost', database='library', user='root', password='12345678')
        cur = con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*              Library Management System                   *')
            print('************************************************************')

            mno = int(input(" Enter Member No. \t\t\t: "))
            mno = int("101" + str(mno))
            while checkmember(mno):
                print(" Entered Member No. already Exists ")
                mno = int(input(" Enter Member No. \t\t\t: "))
                mno = int("101" + str(mno))

            name = input(" Enter Member Name \t\t\t: ")
            mob = input(" Enter Mobile No. \t\t\t: ")

            df = dt.date.today()
            jdate = df.strftime("%Y-%m-%d")

            cur.execute("""
                INSERT INTO member (id, name, join_date, mob)
                VALUES (%s, %s, %s, %s)
            """, (mno, name, jdate, mob))
            con.commit()

            print('************************************************************')
            print("\t\tMember Registered Successfully")
            print('************************************************************')
            ch = input("Do you want to register another member? (y/n): ")
            con.close()

        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during Member Registration.")
            print('************************************************************')
            ch = input("Do you want to try with another data? (y/n): ")

# Function to Issue a Book
def register():
    os.system('cls')
    ch = 'y'
    while ch.lower() == 'y':
        con = sc.connect(host='localhost', database='library', user='root', password='12345678')
        cur = con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*              Library Management System                   *')
            print('************************************************************')

            ino = int(input(" Enter Issue No. \t\t\t: "))
            ino = int("103" + str(ino))
            while checkissue(ino):
                print(" Entered Issue No. already Exists ")
                ino = int(input(" Enter Issue No. \t\t\t: "))
                ino = int("103" + str(ino))

            bno = int(input(" Enter Book no. \t\t\t: "))
            bno = int("102" + str(bno))
            while checkbook(bno) == 0 or checkqty(bno) == 0:
                print(" Entered Book No. not available or out of stock ")
                bno = int(input(" Enter Book no. \t\t\t: "))
                bno = int("102" + str(bno))

            mno = int(input(" Enter Member No. \t\t\t: "))
            mno = int("101" + str(mno))
            while checkmember(mno) == 0:
                print(" Entered Member does not Exist ")
                mno = int(input(" Enter Member No. \t\t\t: "))
                mno = int("101" + str(mno))

            df = dt.date.today()
            idate = df.strftime("%Y-%m-%d")

            dew = input(" Enter Due date (yyyy-mm-dd) \t: ")

            cur.execute("""
                INSERT INTO register (is_no, bno, id, issue_date, dew_date)
                VALUES (%s, %s, %s, %s, %s)
            """, (ino, bno, mno, idate, dew))
            con.commit()

            cur.execute("UPDATE book SET copy = copy - 1 WHERE bno = %s", (bno,))
            con.commit()

            print('************************************************************')
            print("\t\tBook Issued Successfully")
            print('************************************************************')
            ch = input("Do you want to issue more books? (y/n): ")
            con.close()

        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during Issuing Book.")
            print('************************************************************')
            ch = input("Do you want to try with another data? (y/n): ")

# Function to View Member Details
def view():
    ch = 'y'
    while ch.lower() == 'y':
        try:
            con = sc.connect(
                host='localhost',
                database='library',
                user='root',
                password='12345678'
            )
            cur = con.cursor()
            os.system('cls')

            print('************************************************************')
            print('*              Library Management System                   *')
            print('************************************************************')

            mno = int(input(" Enter Member No. \t\t\t: "))
            mno = int("101" + str(mno))

            while checkmember(mno) == 0:
                print(" Entered Member Not Exists ")
                mno = int(input(" Enter Member No. \t\t\t: "))
                mno = int("101" + str(mno))

            cur.execute("""
                SELECT name, bname, issue_date, dew_date, return_date, mob
                FROM book b, register r, member m
                WHERE b.bno = r.bno AND m.id = r.id AND m.id = %s
            """, (mno,))
            data = cur.fetchone()

            os.system('cls')
            print('************************************************************')
            print('*                    Member Details                        *')
            print('************************************************************')
            print(' Member No.   :', mno)

            if data:
                print(' Member Name  :', data[0])
                print(' Book Name    :', data[1])
                print(' Issue Date   :', data[2])
                print(' Due Date     :', data[3])
                print(' Return Date  :', data[4])
                print(' Mobile       :', data[5])
            else:
                print(' No records found for this member.')

            print('************************************************************')
            ch = input("Do you want to view another record? (y/n): ")
            con.close()

        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during viewing.")
            print('************************************************************')
            ch = input("Do you want to try with another data? (y/n): ")

# Function to view list of Books present in library
def list_all_book():
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        try:
            con = sc.connect(host='localhost', database='library', user='root', password='12345678')
            cur = con.cursor()
            os.system('cls')
            print('************************************************************')
            print('* Library Management System *')
            print('************************************************************')
            cur.execute("SELECT bno, bname, copy FROM book")
            data = cur.fetchall()
            os.system('cls')
            print('************************************************************')
            print('* List of Books *')
            print('************************************************************')
            print("{:<10} {:<40} {:<5}".format("Book No.", "Book Name", "Qty"))
            print('-' * 60)
            for row in data:
                print("{:<10} {:<40} {:<5}".format(row[0], row[1], row[2]))
            print('************************************************************')
            ch = input("Press any key to Continue...")
            con.close()
        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during Viewing.")
            print('************************************************************')
            ch = input("\tDo you want to try with another data?(y/n)")
def list_all_members():
    try:
        con = sc.connect(
            host='localhost',
            database='library',
            user='root',
            password='12345678'
        )
        cur = con.cursor()
        os.system('cls')

        print('************************************************************')
        print('*              Library Management System                   *')
        print('************************************************************')

        cur.execute("SELECT id, name, mob FROM member")
        data = cur.fetchall()

        os.system('cls')
        print('************************************************************')
        print('*                    List of Members                       *')
        print('************************************************************')
        print(f"{'Member No.':<15}{'Member Name':<25}{'Mobile'}")
        print('------------------------------------------------------------')

        for row in data:
            print(f"{row[0]:<15}{row[1]:<25}{row[2]}")

        print('************************************************************')
        input("Press any key to Continue...")
        con.close()

    except Exception:
        print('************************************************************')
        print("\t\tError!!!... during Viewing.")
        print('************************************************************')


# Function to view list of Books issued with member name
def list_all():
    ch = 'y'
    while ch.lower() == 'y':
        try:
            con = sc.connect(
                host='localhost',
                database='library',
                user='root',
                password='12345678'
            )
            cur = con.cursor()
            os.system('cls')

            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')

            cur.execute("""
                SELECT is_no, name, bname, dew_date
                FROM book b, register r, member m
                WHERE b.bno = r.bno AND m.id = r.id
            """)
            data = cur.fetchall()
            os.system('cls')

            print('************************************************************')
            print('*                 List of Books Issued                    *')
            print('************************************************************')
            print(f'{"Issue No.":<12}{"Member Name":<20}{"Book Name":<30}{"Due Date":<15}')
            print('-' * 80)

            for row in data:
                print(f'{str(row[0]):<12}{str(row[1]):<20}{str(row[2]):<30}{str(row[3]):<15}')

            print('************************************************************')
            ch = input("Press any key to Continue...")

            con.close()
        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during Viewing.")
            print('************************************************************')
            ch = input("\tDo you want to try with another data? (y/n): ")

# Function to Extend due Date or Cancel Membership
def extend():
    ch = 'y'
    while ch.lower() == 'y':
        try:
            con = sc.connect(
                host='localhost',
                database='library',
                user='root',
                password='12345678'
            )
            cur = con.cursor()
            os.system('cls')

            print('************************************************************')
            print('*                Library Management System                 *')
            print('************************************************************')
            print('*                                                          *')
            print('*  1. Extend Due Date                                      *')
            print('*  2. Cancel Membership                                    *')
            print('*                                                          *')
            print('************************************************************')

            opt = int(input(' Enter Option :- '))
            print('************************************************************')

            if opt == 1:
                os.system('cls')
                list_all()
                print("\n")
                ino = int(input(" Enter Issue No. \t\t\t: "))
                ino = int("103" + str(ino))

                while checkissue(ino) == 0:
                    print(" Entered Issue No. does not exist ")
                    ino = int(input(" Enter Issue No. \t\t\t: "))
                    ino = int("103" + str(ino))

                print('************************************************************')
                dew = input("\t\tEnter new Due Date (YYYY-MM-DD): ")
                cur.execute("UPDATE register SET dew_date = %s WHERE is_no = %s", (dew, ino))
                con.commit()
                print('************************************************************')
                print("\t\tDue Date Successfully Extended")
                print('************************************************************')

            elif opt == 2:
                list_all_members()
                print("\n")
                mno = int(input(" Enter Member No. \t\t\t: "))
                mno = int("101" + str(mno))

                while checkmember(mno) == 0:
                    print(" Entered Member does not exist ")
                    mno = int(input(" Enter Member No. \t\t\t: "))
                    mno = int("101" + str(mno))

                while checki_book_member(mno):
                    print('************************************************************')
                    print("\tBooks pending = ", checki_book_member(mno))
                    print("\tPlease return all books first.")
                    print('************************************************************')
                    input("Press any key to return books...")
                    ret_book()

                cur.execute("DELETE FROM member WHERE id = %s", (mno,))
                con.commit()
                print('************************************************************')
                print("\t\tMembership Successfully Cancelled")
                print('************************************************************')

            ch = input("\tDo you want to update anything else? (y/n): ")
            con.close()

        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during updating.")
            print('************************************************************')
            ch = input("\tDo you want to try with another data? (y/n): ")

# Function to Return a Book
def ret_book():
    ch = 'y'
    while ch.lower() == 'y':
        try:
            con = sc.connect(
                host='localhost',
                database='library',
                user='root',
                password='12345678'
            )
            cur = con.cursor()
            os.system('cls')

            list_all()
            ino = int(input(" Enter Issue No. \t\t\t: "))
            ino = int("103" + str(ino))

            while checkissue(ino) == 0:
                print(" Entered Issue No. does not exist ")
                ino = int(input(" Enter Issue No. \t\t\t: "))
                ino = int("103" + str(ino))

            cur.execute(
                "UPDATE book SET copy = copy + 1 WHERE bno IN (SELECT bno FROM register WHERE is_no = %s)",
                (ino,)
            )
            con.commit()

            cur.execute("DELETE FROM register WHERE is_no = %s", (ino,))
            con.commit()

            print('************************************************************')
            print('*                  Book Returned Successfully              *')
            print('************************************************************')

            ch = input(" Do you want to return another book? (y/n): ")
            con.close()

        except Exception:
            print('************************************************************')
            print("\t\tError!!!... during returning book.")
            print('************************************************************')
            ch = input(" Do you want to try with another data? (y/n): ")

#Main
if __name__ == "__main__":
    ch = 1
    while ch != 0:
        os.system('cls')
        print('************************************************************')
        print('* Library Management System *')
        print('************************************************************')
        print('* *')
        print('* 1. Book Entry *')
        print('* 2. Register Member *')
        print('* 3. Issue Book *')
        print('* 4. View Member issued Books *')
        print('* 5. View All Books *')
        print('* 6. View All Members *')
        print('* 7. View All issued Books *')
        print('* 8. Update details *')
        print('* 9. Return Book *')
        print('* 0. Exit *')
        print('* *')
        print('************************************************************')
        ch = int(input(' Enter Option :- '))
        if ch == 1:
            book()
        elif ch == 2:
            member()
        elif ch == 3:
            register()
        elif ch == 4:
            view()
        elif ch == 5:
            list_all_book()
        elif ch == 6:
            list_all_members()
        elif ch == 7:
            list_all()
        elif ch == 8:
            extend()
        elif ch == 9:
            ret_book()
        elif ch == 0:
            print("\n\nThanks For Visiting")
        elif ch== 100:
            truncate_data()
