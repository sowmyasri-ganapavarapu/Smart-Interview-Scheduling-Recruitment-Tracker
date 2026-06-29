from login import login
from candidate import register_candidate,view_candidates
from interview import schedule_interview
from status import update_status, view_status

print("========================================")
print(" Smart Interview Recruitment Tracker ")
print("========================================")

if login():

    while True:

        print("\n========== MENU ==========")
        print("1. Candidate Registration")
        print("2. View Candidate Details")
        print("3. Schedule Interview") 
        print("4. Update Status")
        print("5. View Status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_candidate()

        elif choice == "2":
            view_candidates()
        elif choice == "3":
            schedule_interview()
        elif choice == "4":
            update_status()
        elif choice == "5":
            view_status()
        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")
else:
    print("Access Denied!")
