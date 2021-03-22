from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from database import DataBase
from database1 import DataBase1
from database1 import DataBase2


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    current = ""

    def submit(self):
        if self.namee.text != "" and self.email.text != "":
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "getready"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class GetReady(Screen):

    @staticmethod
    def fee():
        sm.current = "fees"

    @staticmethod
    def student():
        sm.current = "main"


class FeeStructure(Screen):
    clas = ObjectProperty(None)
    afee = ObjectProperty(None)
    tfee = ObjectProperty(None)
    efee = ObjectProperty(None)
    oth = ObjectProperty(None)

    def feed(self):
        if self.clas.text != "" and self.afee.text != "" and self.tfee.text != "" and self.efee.text != "" and self.oth.text != "":
            db2.add_fees(self.clas.text, self.afee.text, self.tfee.text, self.efee.text, self.oth.text)
            self.reset()

    @staticmethod
    def ret():
        sm.current = "getready"

    def reset(self):
        self.clas.text = ""
        self.afee.text = ""
        self.tfee.text = ""
        self.efee.text = ""
        self.oth.text = ""


class MainWindow(Screen):
    current = ""

    @staticmethod
    def newstudent():
        sm.current = "newstu"

    @staticmethod
    def editstu():
        sm.current = "edit"

    @staticmethod
    def print():
        sm.current = "dis"

    @staticmethod
    def payfee():
        sm.current = "pay"

    @staticmethod
    def logout():
        sm.current = "login"


class NewStudent(Screen):
    snamee = ObjectProperty(None)
    fnamee = ObjectProperty(None)
    dobe = ObjectProperty(None)
    classe = ObjectProperty(None)
    admission = ObjectProperty(None)
    mobile = ObjectProperty(None)
    current = ""

    def submit(self):
        if self.snamee.text != "" and self.fnamee.text != "" and self.dobe.text != "" and self.classe.text != "" and self.admission.text != "" and self.mobile.text != "":
            if db1.get_user1(self.admission.text):
                db1.add_stu(self.snamee.text, self.fnamee.text, self.dobe.text, self.classe.text, self.admission.text,
                            self.mobile.text)

                self.reset()
            else:
                invalidadm()
        else:
            invalidForm()

    def back(self):
        self.reset()
        sm.current = "main"

    def reset(self):
        self.snamee.text = ""
        self.fnamee.text = ""
        self.dobe.text = ""
        self.classe.text = ""
        self.admission.text = ""
        self.mobile.text = ""


class Display(Screen):
    current = ""
    s = ObjectProperty(None)

    @staticmethod
    def spinner_clicked(val):
        s = db1.class1tab(val)
        data_table = MDDataTable(column_data=[("admission", dp(18)), ("student name", dp(22)), ("father name", dp(20)),
                                              ("date of birth", dp(20)), ("class", dp(10)), ("mobile", dp(20)),
                                              ("total fee", dp(15)), ("paid", dp(15)), ("balance", dp(15))],
                                 row_data=[
                                     (a, s[a][0], s[a][1], s[a][2], s[a][3], s[a][4], s[a][5], s[a][6], s[a][7])
                                     for a in s])
        pop = Popup(title='Invalid Login',
                    content=data_table,
                    size_hint=(None, None), size=(800, 400))
        pop.open()

    @staticmethod
    def back1():
        sm.current = "main"


class Payment(Screen):
    sname1 = ObjectProperty(None)
    fname1 = ObjectProperty(None)
    clas1 = ObjectProperty(None)
    amt = ObjectProperty(None)
    adm = ObjectProperty(None)

    def getbal(self):
        s = {}
        if self.adm.text != "":
            s = db1.get_bal(self.adm.text)
        self.ids.sname2.text = s[0]
        self.ids.fname1.text = s[1]
        self.ids.clas1.text = s[2]
        self.ids.tot.text = s[3]
        self.ids.paid.text = s[4]
        self.ids.balance.text = s[5]

    @staticmethod
    def back():
        sm.current = "main"

    def submit(self):
        db1.add_payment(self.adm.text, self.amt.text)
        self.reset()

    def reset(self):
        self.sname2.text = ""
        self.fname1.text = ""
        self.clas1.text = ""
        self.amt.text = ""
        self.tot.text = ""
        self.paid.text = ""
        self.balance.text = ""
        self.adm.text = ""


class EditStudent(Screen):
    sname3 = ObjectProperty(None)
    fname3 = ObjectProperty(None)
    clas3 = ObjectProperty(None)
    dobe3 = ObjectProperty(None)
    mob3 = ObjectProperty(None)
    adm = ObjectProperty(None)
    bal3 = ObjectProperty(None)

    @staticmethod
    def back():
        sm.current = "main"

    def getdet(self):
        s = {}
        if self.adm.text != "":
            s = db1.getdetails(self.adm.text)
        self.ids.sname3.text = s[0]
        self.ids.fname3.text = s[1]
        self.ids.clas3.text = s[2]
        self.ids.dobe3.text = s[3]
        self.ids.mob3.text = s[4]
        self.ids.bal3.text = s[5]

    def submit(self):
        if self.sname3.text != "" or self.fname3.text != "" or self.dobe3.text != "" or self.clas3.text != "" or self.mob3.text != "" or self.bal3.text != "":
            db1.editstudent(self.adm.text, self.sname3.text, self.fname3.text, self.dobe3.text, self.clas3.text, self.mob3.text, self.bal3.text)

            self.reset()

    def reset(self):
        self.sname3.text = ""
        self.fname3.text = ""
        self.clas3.text = ""
        self.dobe3.text = ""
        self.mob3.text = ""
        self.bal3.text = ""


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidadm():
    pop = Popup(title='Invalid admission',
                content=Label(text='admission number already exists'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


def invalidClass():
    pop = Popup(title='Invalid class',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")
db1 = DataBase1("table.txt")
db2 = DataBase2("fees.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"),
           NewStudent(name="newstu"), Display(name="dis"), GetReady(name="getready"), FeeStructure(name="fees"),
           Payment(name="pay"), EditStudent(name="edit")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(MDApp):

    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
