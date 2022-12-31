# initialising the class
class Employee:
    # Adding employee details
    def add(self):
        name = input("Enter the name of the Employee:")
        age = int(input("Enter the Age of the Employee:"))
        salary = int(input("Enter the Salary of the Employee:"))
        Id = input("Enter the Id of the Employee:")
        with open("Employees.txt","a") as e:
            e.write(f"\n Name:{name} \n Age:{age} \n Salary:{salary}\n Id:{Id} \n")
    # Reading Employee Details
    def read(self):
        with open("Employees.txt","r") as r:
            print("The Employee Details Are As Follows:\n")
            print(r.read())

# Main Working
# chosing what to do
print("******Welcome to the Employee Server******")
def chose():
    opt = int(input("Enter 1 for adding, 2 for fetching the details, 3 to exit:"))
    work(opt)
# working
def work(op):
    if op==1:
        e = Employee()
        e.add()
        chose()
    elif op==2:
        e = Employee()
        e.read()
        chose()
    else:
        print("******Thanks for using our Server******")
        exit()
# Starting
chose()



