class Student: # Основний (батьківський класс)

    def __init__(self, name: str, surname: str, course: int, marks: list) -> None: # Ініціалізація класу

        self.name = name # Додаємо параметри, задані в завданні
        self.surname = surname
        self.course = course
        self.marks = marks

    def about(self) -> None:  # Метод about

        mark = ""

        for i in self.marks:
            mark += f"{i}/" # Додаємо бали в 1 рядок
        
        mark = mark[:-1] # обрізаємо останній символ
        # вивожимо загальну інформацію
        print(f"Студент: {self.name} {self.surname}.\nКурс: {self.course}.\nOцінки: {mark} балів.")

    def next_year(self) -> None:  # Метод next_year

        number = 0

        for i in self.marks:
            if i >= 60: # Перевіряємо кожну оцінку чи вона більша за 60 балів
                number += 1 
        
        if number == len(self.marks): # Перевіряємо чи усі оцінки більші за 60 балів
            self.course += 1 # Якщо так, то змінюємо значення курсу на +1
            print(f"Студент перейшов на {self.course} курс.") # Та виводимо що змінили знечення курсу

        else: # Якщо ні то виводимо задане повідомлення
            print("Cтудент відрахований та може поновитись тільки на контракт.")


class BudgetStud(Student):  # Похідкний класс BudgetStud

    def __init__(self, name: str, surname: str, course: int, marks: list, stipend: bool = False) -> None:
        
        # Ініціалізуємо параметри із класу Student
        super().__init__(name, surname, course, marks)
        self.stipend = stipend #  ініціалізуємо додатковий параметр притаманний лише для цього классу
    
    def about(self) -> None: # Метод about з доповненями для классу

        mark = ""

        for i in self.marks:
            mark += f"{i}/"

        mark = mark[:-1]

        if self.stipend == True: # Повідомлення про неявність стипендії
            budget_info = "Стипендія: присутня."

        else:  # негативне повідомлення про неявність стипендії
            budget_info = "Стипендія: відсутня."

        print(f"Студент: {self.name} {self.surname}.\nКурс: {self.course}.\nOцінки: {mark} балів.\n{budget_info}.")

    def next_year(self) -> int:  # Замінений метод next_year

        number = 0
        stepend = 0
        stepend1 = 0
        stepend2 = 0
        stepend3 = 0 # зманні дле перевірки рівня стипендії

        for i in self.marks:
            if i >= 60:
                number += 1
                if i >= 70:
                    stepend += 1
                    if i >= 80:
                        stepend1 += 1
                        if i >= 90:
                            stepend2 += 1
                            if i == 100:
                                stepend3 += 1
        # проходимось по усім можливим рівянми та записуємо результати у змінній

        # У оерненому порядку перевіряємо на рівень стипендії
        if stepend3 == len(self.marks):
            self.stipend = True
            result = 1300
            print(f"Студент перейшов на {self.course} курс.")
            print(f"Степендія студента: {result}грн.")

        elif stepend2 == len(self.marks):
            self.stipend = True
            result = 1200
            print(f"Студент перейшов на {self.course} курс.")
            print(f"Степендія студента: {result}грн.")

        elif stepend1 == len(self.marks):
            self.stipend = True
            result = 1100
            print(f"Студент перейшов на {self.course} курс.")
            print(f"Степендія студента: {result}грн.")
        
        elif stepend == len(self.marks):
            self.stipend = True
            result = 1000
            print(f"Студент перейшов на {self.course} курс.")
            print(f"Степендія студента: {result}грн.")
            

        elif number == len(self.marks):
            # Рівень коли усі бали більше за 60 та менші за 70
            self.course += 1
            self.stipend = False
            result = 0
            print(f"Степендія студента: {result}грн.")
            print(f"Студент перейшов на {self.course} курс.")

        else:
            # Рівень коли усі бали менші за 70
            result = 0
            print("Cтудент відрахований та може поновитись тільки на контракт.")

        # Повертаємо стипендію для поліморфічної функції
        return result


class ContractorStud(Student):  # Похідкний класс ContractorStud

    def __init__(self, name: str, surname: str, course: int, marks: list, contract_paid: bool = False) -> None:

        # Ініціалізуємо параметри із класу Student
        super().__init__(name, surname, course, marks)
        # ініціалізуємо додатковий параметр притаманний лише для цього классу
        self.contract_paid = contract_paid
    
    def about(self) -> None:  # Змінена функція about

        mark = ""
        for i in self.marks:
            mark += f"{i}/"

        mark = mark[:-1]

        if self.contract_paid == True: # Перевіряємо наявність оплати
            conrractor_info = "За навчання по контракту оплачено."

        else:
            conrractor_info = "Неоплачено за навчання по контракту."
        
        print(f"Студент: {self.name} {self.surname}.\nКурс: {self.course}.\nOцінки: {mark} балів.\n{conrractor_info}.")

    def next_year(self) -> int:  # змінена функція next_year

        result = 10000 # задаємо значення вартості контрактного навчання

        if self.contract_paid == True: # Перевіряємо чи навчання оплачене

            number = 0

            for i in self.marks:
                if i >= 60: #Перевіряємо на мінмальні бали
                    number += 1

            if number == len(self.marks):
                # якщо мінімальні бали набрані переводимо на наступний курс
                self.course += 1
                print(f"Студент перейшов на {self.course} курс.")

            else:
                # Якщо бали не набрані виводимо відповідне повідомлення
                print("Студент не перейшов на настуаний курс через низькі бали.")

        else:
            # Якщо навчання не оплачене виводимо відповідне повідомлення
            print("Студент не перейшов на наступний курс через те, щo не оплатив контрактне навчання.")
        
        # Повертаємо вартість навчання
        return result


if __name__ == "__main__":
    # основне тіло програми

    def polymorphic_function(student: object) -> None:
        # Поліморфічна функція
        #student.about()
        if isinstance(student, BudgetStud) == True:
            # Перевіряємо чи об'єкт є екземпляром класу BudgetStud
            result = student.next_year()
            print(f"\nСтепендія студента становить {result} гривень")

        if isinstance(student, ContractorStud) == True:
            # Перевіряємо чи об'єкт є екземпляром класу ContractorStud
            result = student.next_year()
            print(f"\nВартість навчання студента становить {result} гривень")
    
    # Видоми усі можливі варіанти усіх класів
    print("\nСтудент класу 'Student'")
    student = Student("Andriy", "Kindrat", 2, [68, 73, 81])
    print("метод 'about':")
    student.about()
    print("метод 'next_year':")
    student.next_year()
    print("\nСтудент класу 'ContractorStud'")
    contrstud = ContractorStud("Vlad", "Melnuk", 3, [61, 72, 60], False)
    print("метод 'about':")
    contrstud.about()
    print("метод 'next_year':")
    contrstud.next_year()
    print("\nСтудент класу 'BudgetStud'")
    bugstud = BudgetStud("Oleg", "Biluy", 1, [81, 92, 83], False)
    print("метод 'about':")
    bugstud.about()
    print("метод 'next_year':")
    bugstud.next_year()

    print("\nПоліморфічна функція: ")
    print("1. Для об'єкта класу 'ContractorStud':")
    polymorphic_function(contrstud)  # викликаємо поліморфічну функцію
    print("2. Для об'єкта класу 'BudgetStud':")
    polymorphic_function(bugstud)
