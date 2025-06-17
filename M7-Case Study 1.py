from tabulate import tabulate
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}
class User:
    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan
    
    def check_plan(self, username):
        for key, value in data.items():
            if key == self.username:
                print(f"Username : {self.username}")
                print(value[0])
                print(f'{value[1]} bulan')
                print()

                try:
                    if value[0] == "Basic Plan":
                        headers = ["Basic Plan","Services"]
                        rows = [
                            [True, "Bisa Stream"],
                            [True, "Bisa Download"],
                            [True, "Kualitas SD"],
                            [False, "Kualitas HD"],
                            [False, "Kualitas UHD"],
                            [1, "Number of Devices"],
                            ["3rd party Movie only","Jenis Konten"],
                            [120_000, "Harga"]
                        ]
                        print(f"{value[0]} PacFlix Benefit List")
                        print()
                        print(tabulate(rows, headers))

                    elif value[0] == "Standard Plan":
                        headers = ["Standard Plan","Services"]
                        rows = [
                            [True, "Bisa Stream"],
                            [True, "Bisa Download"],
                            [True, "Kualitas SD"],
                            [True, "Kualitas HD"],
                            [False, "Kualitas UHD"],
                            [2, "Number of Devices"],
                            ["Basic Plan + Sports (F1, Football, Basketball)","Jenis Konten"],
                            [160_000, "Harga"]
                        ]
                        print(f"{value[0]} PacFlix Benefit List")
                        print()
                        print(tabulate(rows, headers))

                    elif value[0] == "Premium Plan":
                        headers = ["Premium Plan","Services"]
                        rows = [
                            [True, "Bisa Stream"],
                            [True, "Bisa Download"],
                            [True, "Kualitas SD"],
                            [True, "Kualitas HD"],
                            [True, "Kualitas UHD"],
                            [4, "Number of Devices"],
                            ["Basic Plan + Standard Plan + PacFlix Original Series or Movies","Jenis Konten"],
                            [200_000, "Harga"]
                        ]
                        print(f"{value[0]} PacFlix Benefit List")
                        print()
                        print(tabulate(rows, headers))
                    
                    else:
                        raise Exception("Plan didn't exist")
                except:
                    print("Plan didn't exist")
    
    def upgrade_plan(self, current_plan, new_plan):
        if new_plan != self.current_plan:
            if self.duration_plan > 12:
                if new_plan == "Basic Plan":
                    print("Tidak bisa downgrade")
                elif new_plan == "Standard Plan":
                    total = 160_000 - (160_000 * 0.05)
                    print()
                    print(f"Total biaya upgrade plan dari {self.current_plan} ke {new_plan} adalah Rp {total:,}")
                elif new_plan == "Premium Plan":
                    total = 200_000 - (200_000 * 0.05)
                    print()
                    print(f"Total biaya upgrade plan dari {self.current_plan} ke {new_plan} adalah Rp {total:,}")
                else:
                    print("Plan didn't exist")
            else:
                if new_plan == "Basic Plan":
                    total = 120_000
                    print()
                    print(f"Total biaya {new_plan} adalah Rp {total:,}")
                elif new_plan == "Standard Plan":
                    total = 160_000
                    print()
                    print(f"Total biaya {new_plan} adalah Rp {total:,}")
                elif new_plan == "Premium Plan":
                    total = 200_000
                    print()
                    print(f"Total biaya {new_plan} adalah Rp {total:,}")
                else:
                    print("Plan didn't exist")
        else:
            if new_plan == "Basic Plan":
                total = 120_000
                print()
                print(f"Total biaya {new_plan} adalah Rp {total:,}")
            elif new_plan == "Standard Plan":
                total = 160_000
                print()
                print(f"Total biaya {new_plan} adalah Rp {total:,}")
            elif new_plan == "Premium Plan":
                total = 200_000
                print()
                print(f"Total biaya {new_plan} adalah Rp {total:,}")
            else:
                print("Plan didn't exist")
            
def check_all_plan():
    print("PacFlix Plan List")
        
    headers = ["Basic Plan","Standard Plan","Premium Plan","Service"]
    rows = [
        [True, True, True, "Bisa Stream"],
        [True, True, True, "Bisa Download"],
        [True, True, True, "Kualitas SD"],
        [False, True, True, "Kualitas HD"],
        [False, False, True, "Kualitas UHD"],
        [1, 2,4, "Number of Devices"],
        ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
        [120000, 160000, 200000, "Harga"]
        ]
    print()
    print(tabulate(rows, headers))

#Check semua plan dari platform
check_all_plan()
print()

#Check plan yang sedang aktif digunakan
user1 = User("Shandy",12,"Basic Plan")
user2 = User("Cahya",24,"Standard Plan")
user2.check_plan(user2.username)

#Upgrade plan
user2.upgrade_plan(user2.current_plan,"Premium Plan")

class NewUser:
    check_list = []
    
    def __init__(self, username):
        self.username = username
    
    # method to dictionary to list to easier use
    def convert_data_to_list(self, data):
        for data in data.values():
            for val in data:
                self.check_list.append(val)
        return self.check_list
        
    # method to pick plan 
    def pick_plan(self, new_plan, referral_code):
        if referral_code in self.check_list:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * 0.04)
                print()
                print(f"Total biaya {new_plan} adalah Rp {total:,}")
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * 0.04)
                print()
                print(f"Total biaya {new_plan} adalah Rp {total:,}")
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * 0.04)
                print()
                print(f"Total biaya {new_plan} adalah Rp {total:,}")
            else:
                print("Plan doesn't exist")
        else:
            raise Exception("Referral Code doesn't exist")

faizal = NewUser("faizal_icikiwir")
faizal.convert_data_to_list(data)
faizal.pick_plan("Basic Plan", "shandy-2134")