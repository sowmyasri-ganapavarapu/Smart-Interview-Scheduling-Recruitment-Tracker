from database import connect

def login():

    conn = connect()

    cursor = conn.cursor()

    username = input("Enter Username : ")

    password = input("Enter Password : ")

    query = "SELECT * FROM users WHERE username=%s AND password=%s"

    values = (username, password)

    cursor.execute(query, values)

    result = cursor.fetchone()

    if result:

        print("\n✅ Login Successful")

        return True

    else:

        print("\n❌ Invalid Username or Password")

        return False 