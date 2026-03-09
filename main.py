# Ini program utama yang menjalankan menu atm

from bank_account import BankAccount

account = BankAccount("Ela", 1000) #nama pemilik #saldo 

# membuat program terus berjalan
while True:

    print("\n===== MENU ATM =====")
    print("1. Deposit") #menambah uang
    print("2. Withdraw") #mengambil uang
    print("3. Check Balance") #meihat saldo
    print("4. Exit") #keluar dari progam

    choice = input("Pilih menu: ")

    if choice == "1":

        amount = int(input("Masukkan jumlah deposit: "))
        account.deposit(amount)

    elif choice == "2":

        amount = int(input("Masukkan jumlah withdraw: "))
        account.withdraw(amount)

    elif choice == "3":

        account.check_balance()

    elif choice == "4":

        print("Program selesai")
        break