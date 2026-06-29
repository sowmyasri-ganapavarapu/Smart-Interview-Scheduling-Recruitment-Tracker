from database import connect
def schedule_interview():

    conn = connect()

    cursor = conn.cursor()

    print("\n===== Schedule Interview =====")

    candidate_id = input("Enter Candidate ID : ")

    interview_date = input("Enter Interview Date (YYYY-MM-DD): ")

    interview_time = input("Enter Interview Time (HH:MM:SS): ")

    interviewer = input("Enter Interviewer Name : ")

    mode = input("Enter Mode (Online/Offline): ")
    

    check_query = """
    SELECT *
    FROM interview
    WHERE interviewer=%s
    AND interview_date=%s
    AND interview_time=%s
    """

    check_values = (
        interviewer,
        interview_date,
        interview_time
    )

    cursor.execute(check_query, check_values)

    result = cursor.fetchone()

    if result:

        print("\n❌ Interviewer already has an interview.")

        conn.close()

        return
    query = """
    INSERT INTO interview
    (candidate_id,
     interview_date,
     interview_time,
     interviewer,
     mode)

    VALUES(%s,%s,%s,%s,%s)
    """

    values = (
        candidate_id,
        interview_date,
        interview_time,
        interviewer,
        mode
    )

    cursor.execute(query, values)

    conn.commit()

    print("\n✅ Interview Scheduled Successfully!")

    cursor.close()

    conn.close()