class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.size < 5:
            new_node = ListNode(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.size += 1

    def traverse(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

class TreeNode:
    def __init__(self, apartment):
        self.apartment = apartment
        self.left = None
        self.right = None
        self.left_list = LinkedList()
        self.right_list = LinkedList()

    def add_apartment(self,data,side):
        if side == "left":
            self.left_list.add(data)
        elif side == "right":
            self.right_list.add(data)
        else:
            print("Invalid side. Please choose 'left' or 'right'.")

root = TreeNode("Deccan Enclave")

import csv
with open('apartment.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for line in csv_reader:
        if line[0] == '1':
            root.add_apartment(line, "left")
        elif line[0] == '2':
            root.add_apartment(line, "right")
        else:
            pass

def blockwiselist(block):
    if block == 1:
        return root.left_list.traverse()
    elif block == 2:
        return root.right_list.traverse()
    else:
        return "Block number does not exist"

block = int(input("Enter block number: "))
b=blockwiselist(block)
print(b)
    

def details(block,house):
    if block==1:
        if house in range(1,6):
            apartments=root.left_list.traverse()
            res=[line for line in apartments if line[1]==str(house)]
            return res
        else:
            return "House does not exist"

    elif block==2:
        if house in range(1,6):
            apartments = root.right_list.traverse()
            res=[line for line in apartments if line[1]==str(house)]
            return res
        else:
            return "House does not exist"
            
    else:
        return "Block does not exist"

block = int(input("Enter block number: "))
house = int(input("Enter house number: "))
d=details(block,house)
print(d)


def house_availability(bhk):
    res=[]
    for block in [1,2]:
        apartments = root.left_list.traverse() if block==1 else root.right_list.traverse()
        for apartment in apartments:
            if apartment[2]==str(bhk) and apartment[3]=='vacant':
                res.append(apartment)
    if len(res)>0:
        return res
    else:
        "No vacant houses found for the given BHK value"
             
    if not res:
        return "No vacant houses found for the given BHK value"
    
bhk=int(input("Enter BHK(2/3):"))
house=house_availability(bhk)
print(house)


def maintenance(block,house):    
    if block == 1:
        apartments = root.left_list.traverse()
    elif block == 2:
        apartments = root.right_list.traverse()
    else:
        return "Block does not exist"

    res = [line for line in apartments if line[1] == str(house)]
    if not res:
        return "Block number or house number does not exist"

    return [[line[0], line[1], line[6]] for line in res]

block=int(input("Enter block number:"))
house=int(input("Enter house number:"))
m=maintenance(block,house)
print(m)

def updation(block,house,occ):
    l=[]
    flag=False
    with open("apartment.csv","r") as file:
        csv_reader=csv.reader(file)
        header=next(csv_reader)
        for i in csv_reader:
            l.append(i)
    for j in l:
        if j[0]==str(block) and j[1]==str(house):
            j[3]=str(occ)
            flag=True
            break
    with open("apartment.csv","w+",newline='') as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(header)
        for i in range(len(l)):
            csv_writer.writerow(l[i])

    if flag:
        return "Updation successful"
    else:
        return "Updation unsuccessful"

block=int(input("Enter block number:"))
house=int(input("Enter house number:"))
occ=input("Enter occupancy status(occupied/vacant):")
u=updation(block,house,occ)
print(u) 
