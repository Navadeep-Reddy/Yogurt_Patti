import csv

def user_check(username, password):
        with open("Data/users.csv", "r") as f:
            reader = csv.reader(f)

            for line in reader:
                  if line[0] == username and line[1] == password:
                        print("yes")
                        return True
                  
            return False
        
