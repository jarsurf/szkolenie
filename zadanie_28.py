class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie= imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.worked_hours = 0

    def register_time(self , hours):
        self.worked_hours = hours


    def pay_salary(self):
          if self.worked_hours > 8:
           to_pay = 8 *self.worked_hours * (self.worked_hours - 8) * 2 * self.stawka

          else:
              to_pay = self.worked_hours * self.stawka
          self.worked_hours= 0
          return to_pay

czas = input("Podaj czas")
empl = Employee( "Jan", "Nowak", 100)
print(empl.pay_salary())


