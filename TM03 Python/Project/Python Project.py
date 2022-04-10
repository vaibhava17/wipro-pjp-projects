
class Employee:
    Empid : int
    Ename : str
    Sal : int
    Deptno : int

    def __init__(self) -> None:
        choice = 0
        while choice != 4:
            print("\n1. Add_emp\n2. Display_emp\n3. Separate_data\n4. Exit")
            try:
                choice = int(input("\nEnter your choice:  "))
            except ValueError:
                print(f"Please try again with correct option, enter 1, 2, 3, 4...")
            if choice == 1:
                self.Add_Emp()
            elif choice == 2:
                self.Display_Emp()
            elif choice == 3:
                self.Separate_data()
            elif choice == 4:
                print("...EXITING...")

    def Add_Emp(self):
        try:
            employeeData = input("Enter the input data in the format: EmpId, EmpName, Salary, Deptno *comma separted: ").split(", ")
            self.Empid = employeeData[0]
            self.Ename = employeeData[1]
            self.Sal = employeeData[2]
            self.Deptno = employeeData[3]
        except IndexError:
            print("Please enter the data again with ', 'between each value!")
            return

        try:
            with open("emp.txt", "r") as f:
                employees = f.read().split("\n")
        except FileNotFoundError:
            employees = []


        if len(str(self.Empid)) < 3:
            print(f"\n****EmpId too short!****\nPlease try again!\n")
            return

        if self.Deptno not in ["10", "20", "30"]:
            print(f"\n****Deptno is incorrect!****\nPlease try again!\n")
            return

        try:
            if int(self.Sal) < 3000:
                print(f"\n****Salary is incorrect!****\nPlease try again!\n")
                return

        except ValueError:
            print("\n****Please enter the salary in integers.****\n")
            return

        existingEmpId = [i.split()[0] for i in employees if i != ""]
        if str(self.Empid) in existingEmpId:
            print(f"\n****EmpId already exist!\nPlease try again!****\n")
            return
 
        with open("emp.txt", "a+") as f:
            f.write("\n" + self.Empid+ " "+self.Ename.upper()+ " "+self.Sal+ " "+ self.Deptno)
            print(f"Employedd added with empId:{self.Empid}\nEname: {self.Ename.upper()}\nSalary : {self.Sal}\nDeptno : {self.Deptno}")
        
    def Display_Emp(self):
        print("\nEmployee Data is : ")
        with open("emp.txt", "r") as f:
            employees = f.read().split("\n")
        if len(employees) != 1:
            for i in employees:
                print(i)
            print()
        else:
            print("There no data available, please add data to continue!")

    def Separate_data(self):
        with open("emp.txt", "r") as f:
            employees = f.read().split("\n")

        dept_10, dept_20, dept_30 = "", "", ""

        for employe in employees:
            if employe == "":
                continue
            if employe.split()[-1] == "10":
                dept_10 += employe + "\n"
            elif employe.split()[-1] == "20":
                dept_20 += employe + "\n"
            else:
                dept_30 += employe + "\n"
    
        with open("Emp_10.txt", "w") as f:    
            f.write(dept_10)
        with open("Emp_20.txt", "w") as f:    
            f.write(dept_20)
        with open("Emp_30.txt", "w") as f:    
            f.write(dept_30)

        print("Successfully separated files into three files!")


def main():
    employe = Employee()

if __name__ == "__main__":
    main()