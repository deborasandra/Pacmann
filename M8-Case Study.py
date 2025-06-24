# untuk membuat table
from tabulate import tabulate

# square root, untuk menghitung euclidean distance
from math import sqrt

data = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

class Member:
    def __init__ (self,username,monthly_income,monthly_expense):
        self.username = username
        self.monthly_income = monthly_income
        self.monthly_expense = monthly_expense
    
    def show_all_tier(self):
        rows = [
            ["Platinum", "15%", "Benefit Gold + Silver + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"],
        ]
        headers = ["Membership", "Discount", "Another Benefit"]
        print(tabulate(rows,headers))

    def show_requirements(self):
        rows = [
            ["Platinum",8,15],
            ["Gold",6,10],
            ["Silver",5,7]
        ]
        headers = ["Membership", "Monthly Expense (JT)", "Monthly Income (JT)"]
        print(tabulate(rows,headers))
    
    def predict_member(self):
        platinum = [8,15]
        gold = [6,10]
        silver = [5,7]

        platinum_distance = sqrt(((self.monthly_expense-platinum[0])**2)+((self.monthly_income-platinum[1])**2))
        gold_distance = sqrt(((self.monthly_expense-gold[0])**2)+((self.monthly_income-gold[1])**2))
        silver_distance = sqrt(((self.monthly_expense-silver[0])**2)+((self.monthly_income-silver[1])**2))

        if platinum_distance < gold_distance and platinum_distance < silver_distance:
            print(f"Hasil Prediksi untuk user {self.username} adalah Platinum")
        elif gold_distance < platinum_distance and gold_distance < silver_distance:
            print(f"Hasil Prediksi untuk user {self.username} adalah Gold")
        elif silver_distance < platinum_distance and silver_distance < gold_distance:
            print(f"Hasil Prediksi untuk user {self.username} adalah Silver")

user_1 = Member("Cahya",10,7)
user_1.show_all_tier()
print()
user_1.show_requirements()
print()
user_1.predict_member()
        