from database import connect

def update_status():

    conn = connect()
    cursor = conn.cursor()

    print("\n===== Update Candidate Status =====")

    candidate_id = input("Enter Candidate ID: ")
    status = input("Enter Status: ")
    remarks = input("Enter Remarks: ")

    # Check if status already exists
    cursor.execute(
        "SELECT * FROM recruitment_status WHERE candidate_id=%s",
        (candidate_id,)
    )

    result = cursor.fetchone()

    if result:

        query = """
        UPDATE recruitment_status
        SET status=%s, remarks=%s
        WHERE candidate_id=%s
        """

        values = (status, remarks, candidate_id)

    else:

        query = """
        INSERT INTO recruitment_status
        (candidate_id, status, remarks)
        VALUES (%s, %s, %s)
        """

        values = (candidate_id, status, remarks)

    cursor.execute(query, values)
    conn.commit()

    print("\n✅ Status Updated Successfully!")

    cursor.close()
    conn.close()

def view_status():

    conn = connect()
    cursor = conn.cursor()

    candidate_id = input("Enter Candidate ID: ")

    cursor.execute(
        "SELECT * FROM recruitment_status WHERE candidate_id=%s",
        (candidate_id,)
    )

    result = cursor.fetchone()

    if result:

        print("\n===== Candidate Status =====")
        print("Candidate ID :", result[0])
        print("Status       :", result[1])
        print("Remarks      :", result[2])

    else:

        print("No status found!")

    cursor.close()
    conn.close()