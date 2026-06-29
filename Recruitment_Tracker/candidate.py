from database import connect

def register_candidate():
    conn = connect()
    cursor = conn.cursor()

    print("\n===== Candidate Registration =====")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    qualification = input("Enter Qualification: ")
    skills = input("Enter Skills: ")
    experience = input("Enter Experience: ")
    position = input("Enter Position Applied: ")

    query = """
    INSERT INTO candidate
    (name, email, phone, qualification, skills, experience, position)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        email,
        phone,
        qualification,
        skills,
        experience,
        position
    )

    cursor.execute(query, values)
    conn.commit()

    print("\n✅ Candidate Registered Successfully!")

    cursor.close()
    conn.close()

def view_candidates():

    conn = connect()

    cursor = conn.cursor()

    query = "SELECT * FROM candidate"

    cursor.execute(query)

    candidates = cursor.fetchall()

    print("\n========== Candidate Details ==========\n")

    if len(candidates) == 0:

        print("No Candidates Found")

    else:

        for candidate in candidates:

            print("------------------------------------------")
            print("Candidate ID :", candidate[0])
            print("Name         :", candidate[1])
            print("Email        :", candidate[2])
            print("Phone        :", candidate[3])
            print("Qualification:", candidate[4])
            print("Skills       :", candidate[5])
            print("Experience   :", candidate[6])
            print("Position     :", candidate[7])

    cursor.close()

    conn.close()