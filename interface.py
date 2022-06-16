import tkinter as tk
import main

root = tk.Tk()  # Begin GUI
root.wm_title("Twitch Account Creator")
root.geometry("500x450")
root.configure(bg='#7c8491')
email = ""
username = ""

def start():
    global email
    global username

    try:
        email = emailInput.get()
        main.username = accountInput.get()
        main.email = email
        username = accountInput.get()
        main.username = username
        main.numberOfAccounts = int(numberAccountsInput.get())
        validityCheck1 = main.email.index('@')
        validityCheck2 = main.email.index('.')
        print("Success! Starting program.")
        print("\n\tEmail: " + main.email +
              "\n\tUsername: " + main.username +
              "\nCreating " + str(main.numberOfAccounts) + " accounts.")
        root.destroy()
        for x in range(main.numberOfAccounts):
            main.email = email
            main.username = username
            main.registerAccount(main.generateLogin())

    except ValueError:
        print("Please fill out all fields properly.")


info1 = tk.Label(root, text="Twitch Account Creator Tool", font=("Arial", 16), bg='#7c8491')
info2 = tk.Label(root, text="xlpvyxj.xyz", font=("Arial", 8), bg='#7c8491')

emailLabel = tk.Label(root, text="Email:", font=("Arial", 16), bg='#7c8491')
emailInput = tk.Entry(root, width=25, font=("Arial", 12), bg='#868f9e')

accountLabel = tk.Label(root, text="Name of account:", font=("Arial", 16), bg='#7c8491')
accountLabelInstructions = tk.Label(root, text="This will be the base name of the account.\nNumbers will be included at the end.", font=("Arial", 8), bg='#7c8491')
accountInput = tk.Entry(root, width=25, font=("Arial", 12), bg='#868f9e')

numberAccounts = tk.Label(root, text="Number of accounts to generate:", font=("Arial", 16), bg='#7c8491')
numberAccountsInput = tk.Entry(root, width=3, font=("Arial", 24), bg='#868f9e')

startButton = tk.Button(root, text="Start", width=25, height=2, font=("Arial", 16), bg='#595f69', command=lambda: start())
info1.pack(pady=(10, 0))
info2.pack(pady=(0, 15))
emailLabel.pack()
emailInput.pack(pady=(0, 30))
accountLabel.pack()
accountLabelInstructions.pack()
accountInput.pack(pady=(0, 30))
numberAccounts.pack()
numberAccountsInput.pack()
startButton.pack(pady=30)
root.mainloop()  # End GUI


