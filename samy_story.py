class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = max(0, min(100, health_rate))  

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} slept for {hours} hours and feels {self.mood}.")

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50
        print(f"{self.name} ate {meals} meals and has health rate {self.health_rate}%.")

    def buy(self, items):
        self.money -= items * 10  
        print(f"{self.name} bought {items} items. Money left: {self.money} L.E")


class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = max(0, min(100, fuel_rate)) 
        self.velocity = max(0, min(200, velocity))  

    def run(self, velocity, distance):
        if self.fuel_rate <= 0:
            print("Car has no fuel! Cannot start.")
            return
        
        self.velocity = max(0, min(200, velocity))  
        self.fuel_rate -= (distance / 10) * 10 
        self.fuel_rate = max(0, self.fuel_rate)  

        print(f"{self.name} is running at {self.velocity} km/h. Fuel left: {self.fuel_rate}%")

        if self.fuel_rate == 0:
            print(f"{self.name} stopped due to empty fuel before reaching destination.")

    def stop(self):
        self.velocity = 0
        print(f"{self.name} has stopped.")


class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} worked for {hours} hours and feels {self.mood}.")

    def drive(self):
        print(f"{self.name} is driving to work...")
        self.car.run(velocity=60, distance=self.distance_to_work)  

    def refuel(self, gas_amount=100):
        self.car.fuel_rate = min(100, self.car.fuel_rate + gas_amount)
        print(f"{self.name} refueled the car. Fuel rate: {self.car.fuel_rate}%")


class Office:
    employees_num = 0  
    def __init__(self, name):
        self.name = name
        self.employees = []  
    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1
        print(f"{employee.name} has been hired at {self.name}.")

    def fire(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                Office.employees_num -= 1
                print(f"Employee {employee.name} has been fired.")
                return
        print("Employee not found.")

    def get_all_employees(self):
        return [emp.name for emp in self.employees]

    def get_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        return None

    def check_lateness(self, emp_id, move_hour):
        employee = self.get_employee(emp_id)
        if employee:
            arrival_time = move_hour + (employee.distance_to_work / 60)  
            if arrival_time > 9:
                print(f"{employee.name} is late! Salary deducted.")
                self.deduct(emp_id, 10)
            else:
                print(f"{employee.name} arrived on time! Salary rewarded.")
                self.reward(emp_id, 10)

    def deduct(self, emp_id, amount):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary -= amount
            print(f"{employee.name}'s salary deducted by {amount}. New salary: {employee.salary}")

    def reward(self, emp_id, amount):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary += amount
            print(f"{employee.name} received a reward of {amount}. New salary: {employee.salary}")

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num

samys_car = Car(name="Fiat 128", fuel_rate=100, velocity=60)

samy = Employee(
    name="Samy",
    money=1000,
    mood="Neutral",
    health_rate=90,
    emp_id=1,
    car=samys_car,
    email="samy@iti.com",
    salary=5000,
    distance_to_work=20
)

iti_office = Office(name="ITI Smart Village")

iti_office.hire(samy)

samy.drive()

iti_office.check_lateness(emp_id=1, move_hour=8.5)

print("Employees in ITI:", iti_office.get_all_employees())
