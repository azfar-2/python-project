import os

def assistance():
    print("How can I help you?")
    print("1. Open Calendar")
    print("2. Open Chrome")
    print("3. Open File Explorer")
    print("4. Open Command Prompt")
    print("5. Open Control Panel")
    print("6. Open Task Manager")
    print("7. Open System Settings")
    print("0. Exit")
    ch = input("Enter your choice: ").strip()
    return ch

def open_calendar():
    print("Opening calendar...")
    os.system("start outlookcal:")

def open_chrome():
    print("Opening Chrome...")
    os.system("start chrome")

def open_file_explorer():
    print("Opening File Explorer...")
    os.system("start explorer")

def open_command_prompt():
    print("Opening Command Prompt...")
    os.system("start cmd")

def open_control_panel():
    print("Opening Control Panel...")
    os.system("start control")

def open_task_manager():
    print("Opening Task Manager...")
    os.system("start taskmgr")

def open_system_settings():
    print("Opening System Settings...")
    os.system("start ms-settings:")

while True:
    choice = assistance()

    if choice == "1":
        open_calendar()
    elif choice == "2":
        open_chrome()
    elif choice == "3":
        open_file_explorer()
    elif choice == "4":
        open_command_prompt()
    elif choice == "5":
        open_control_panel()
    elif choice == "6":
        open_task_manager()
    elif choice == "7":
        open_system_settings()
    elif choice == "0":
        print("Thank you for using the assistant. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
