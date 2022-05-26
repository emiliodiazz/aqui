class Bibliotecario:
    def __init__(self, rut, password, UserName, fullName,Email, rutAdministrador):
        self.id = rut
        self.password = password
        self.Username = UserName
        self.fullname = fullName
        self.Email = Email
        self.rutAdministrador = rutAdministrador


class Usuario:
    def __init__(self, rut, username, fullName, email):
        self.id = rut
        self.username = username
        self.fullName = fullName
        self.email = email


class Docentes(Usuario):
    def __init__(self, rut, username, fullName, email):
        super().__init__(rut, username, fullName, email)

class Alumnos(Usuario):
    def __init__(self, rut, username, fullName, email):
        super().__init__(rut, username, fullName, email)




class Libro:
    def __init__(self, isbn, title, state, reutrnDate, loanDate):
        self.id = isbn
        self.title = title
        self.state = state
        self.returnDate = reutrnDate
        self.loanDate = loanDate


class Deuda:
    def __init__(self, debtID, delayDays, debtMount):
        self.id = debtID
        self.delayDays = delayDays
        self.debtMount = debtMount


class Prestamo:
    def __init__(self, loanID, teacheID, studentID, librariaID, debtID):
        self.loanID = loanID
        self.teacherID = teacheID
        self.studentID = studentID
        self.librarianID = librariaID
        self.debtID = debtID
     
