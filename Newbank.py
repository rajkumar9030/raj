class Newbank:
    amount_bal = 1000000
    withdraw_count = 0

    def viewoptions(self):
        print("1. Deposit\n2. Withdraw\n3. Balance enquiry\n0. Exit")

    def validate(self, count):
        pin_no = int(input("Enter PIN number: "))
        count = count+1

        if pin_no == 1234:
            count = 0
            self.viewoptions()
            while True:
                choice = int(input("Enter the option: "))
                if choice == 1:
                    amount_deposit = int(input("Enter deposit amount: "))
                    if amount_deposit < 100:
                        print("Enter only amount more than 100")
                    elif amount_deposit % 100 != 0:
                        print("Only multiples of 100")
                    elif amount_deposit > 50000:
                        print("Deposit only available upto 50k")
                    else:
                        self.amount_bal+=amount_deposit
                        print("Deposit successful")

                if choice == 2:
                    if self.withdraw_count >= 3:
                        print("Withdrawal limit reached for today.")
                        break

                    amount_withdraw = int(input("Enter withdraw amount: "))
                    if amount_withdraw < 100:
                        print("Enter only amount more than 100")
                    elif amount_withdraw % 100 != 0:
                        print("Only multiples of 100")
                    elif amount_withdraw > self.amount_bal:
                        print("Balance not available")
                    elif self.amount_bal <= 500:
                        print("Withdraw not possible")
                    elif amount_withdraw > 20000:
                        print("Limit exceeded Only 20k possible")
                    else:
                        self.amount_bal -= amount_withdraw
                        self.withdraw_count += 1

                if choice == 3:
                    print(f"Your current balance is: {self.amount_bal}")

                if choice == 0:
                    print("Exiting")
                    break

        else:
            if count < 3:
                print("Incorrect PIN  try again.")
                self.validate(count)
            else:
                print("Card blocked")


obj = Newbank()
obj.validate(0)
