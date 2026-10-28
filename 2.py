class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library: {self.street}, {self.city}, {self.zip_code}; "
            f"open: {self.open_hours}; phone: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}; "
            f"hire date: {self.hire_date}; birth date: {self.birth_date}; "
            f"address: {self.street}, {self.city}, {self.zip_code}; "
            f"phone: {self.phone}"
        )


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book by {self.author_name} {self.author_surname}; "
            f"publication date: {self.publication_date}; "
            f"pages: {self.number_of_pages}; {self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = "\n".join(f"  - {book}" for book in self.books)
        return (
            f"Order date: {self.order_date}\n"
            f"Employee: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Books:\n{books_description}"
        )


biblioteka1 = Library(
    "Warsaw", "Marszalkowska 1", "00-001", "9:00-17:00", "22 123 45 67"
)
biblioteka2 = Library(
    "Krakow", "Dluga 10", "31-147", "10:00-18:00", "12 987 65 43"
)

pracownik1 = Employee(
    "Anna",
    "Kowalska",
    "2018-04-02",
    "1985-06-15",
    "Warsaw",
    "Nowa 5",
    "00-002",
    "501 111 222",
)
pracownik2 = Employee(
    "Piotr",
    "Nowak",
    "2020-09-01",
    "1990-02-20",
    "Krakow",
    "Kwiatowa 8",
    "31-148",
    "502 222 333",
)
pracownik3 = Employee(
    "Maria",
    "Wisniewska",
    "2016-01-11",
    "1980-11-03",
    "Warsaw",
    "Lesna 12",
    "00-003",
    "503 333 444",
)

student1 = Student("Jan", "Zielinski")
student2 = Student("Oliwia", "Wojcik")
student3 = Student("Tomasz", "Kaminski")

ksiazka1 = Book(biblioteka1, "1925-04-10", "F. Scott", "Fitzgerald", 180)
ksiazka2 = Book(biblioteka1, "1960-07-11", "Harper", "Lee", 281)
ksiazka3 = Book(biblioteka2, "1949-06-08", "George", "Orwell", 328)
ksiazka4 = Book(biblioteka2, "1932-08-18", "Aldous", "Huxley", 268)
ksiazka5 = Book(biblioteka1, "1813-01-28", "Jane", "Austen", 432)

order1 = Order(pracownik1, student1, [ksiazka1, ksiazka2], "2026-10-20")
order2 = Order(
    pracownik2,
    student2,
    [ksiazka3, ksiazka4, ksiazka5],
    "2026-10-21",
)

print(order1)
print(order2)
