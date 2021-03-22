class DataBase1:
    def __init__(self, filename):
        self.filename1 = filename
        self.students = None
        self.students1 = None
        self.file1 = None
        self.file3 = None
        self.file4 = None
        self.stu = None
        self.load()

    def load(self):
        self.file1 = open(self.filename1, "r")
        self.students = {}

        for line in self.file1:
            admission, snamee, fnamee, dobe, classe, mobile, tot, paid, bal = line.strip().split(";")
            self.students[admission] = (snamee, fnamee, dobe, classe, mobile, tot, paid, bal)
        self.file1.close()

    def get_user1(self, admission):
        if admission not in self.students:
            return True
        else:
            return -False

    def add_stu(self, snamee, fnamee, dobe, classe, admission, mobile):
        if admission.strip() not in self.students:
            tot = str(db3.gettotal(classe))
            self.students[admission.strip()] = (
                snamee.strip(), fnamee.strip(), dobe.strip(), classe.strip(), mobile.strip(), tot.strip(), "0",
                tot.strip())
            self.savestu()
            return 1
        else:
            return -1

    def savestu(self):
        with open(self.filename1, "w") as f:
            for user in self.students:
                f.write(user + ";" + self.students[user][0] + ";" + self.students[user][1] + ";" + self.students[user][
                    2] + ";" + self.students[user][3] + ";" + self.students[user][4] + ";" + self.students[user][
                            5] + ";" + self.students[user][6] + ";" + self.students[user][7] + "\n")

    def add_payment(self, adm, amt):
        self.file1 = open(self.filename1, "r")

        for line in self.file1:
            admission, snamee, fnamee, dobe, classe, mobile, tot, paid, bal = line.strip().split(";")
            if adm == admission:
                bal1 = str(float(bal) - float(amt))
                paid = str(float(paid) + float(amt))
                self.students[admission.strip()] = (
                    snamee.strip(), fnamee.strip(), dobe.strip(), classe.strip(), mobile.strip(), tot.strip(),
                    paid.strip(), bal1.strip())
                self.savestu()
                self.file1.close()
                return 1
            else:
                continue

    def get_bal(self, adm):
        self.file3 = open(self.filename1, "r")

        for line in self.file3:
            admission, snamee, fnamee, dobe, classe, mobile, tot, paid, bal = line.strip().split(";")
            if adm == admission:
                self.stu = (snamee, fnamee, classe, tot, paid, bal)
            else:
                continue
        self.file3.close()
        return self.stu

    def class1tab(self, val):

        self.file1 = open(self.filename1, "r")
        self.students1 = {}

        for line in self.file1:
            admission, snamee, fnamee, dobe, classe, mobile, tot, paid, bal = line.strip().split(";")
            if val == classe:
                self.students1[admission] = (snamee, fnamee, dobe, classe, mobile, tot, paid, bal)
        self.file1.close()
        return self.students1

    def getdetails(self, adm):
        self.file1 = open(self.filename1, "r")

        for line in self.file1:
            admission, snamee, fnamee, dobe, classe, mobile, tot, paid, bal = line.strip().split(";")
            if adm == admission:
                self.stu = (snamee, fnamee, classe, dobe, mobile, bal)
            else:
                continue
        self.file1.close()
        return self.stu

    def editstudent(self, adm, sname3, fname3, dobe3, clas3, mob3, bal3):

        self.file4 = open(self.filename1, "r")

        for line in self.file4:
            admission, snamee, fnamee, dobe, classe, mobile, tot, paid, bal = line.strip().split(";")
            if adm == admission:
                if sname3 == "":
                    sname3 = snamee
                if fname3 == "":
                    fname3 = fnamee
                if dobe3 == "":
                    dobe3 = dobe
                if clas3 == "":
                    clas3 = classe
                if mob3 == "":
                    mob3 = mobile
                if bal3 == "":
                    bal3 = bal
                self.students[admission] = (sname3, fname3, dobe3, clas3, mob3, tot, paid, bal3)
        self.update()
        self.file4.close()

    def update(self):
        with open(self.filename1, "w") as f:
            for user in self.students:
                f.write(user + ";" + self.students[user][0] + ";" + self.students[user][1] + ";" + self.students[user][
                    2] + ";" + self.students[user][3] + ";" + self.students[user][4] + ";" + self.students[user][
                            5] + ";" + self.students[user][6] + ";" + self.students[user][7] + "\n")


class DataBase2:
    def __init__(self, filename):
        self.filename2 = filename
        self.fee = None
        self.file2 = None
        self.load()

    def load(self):
        self.file2 = open(self.filename2, "r")
        self.fee = {}

        for line in self.file2:
            clas, tfee, afee, efee, oth, tot = line.strip().split(";")
            self.fee[clas] = (tfee, afee, efee, oth, tot)
        self.file2.close()

    def add_fees(self, clas, tfee, afee, efee, oth):
        tot = str(float(tfee) + float(afee) + float(efee) + float(oth))
        if clas.strip() not in self.fee:
            self.fee[clas.strip()] = (tfee.strip(), afee.strip(), efee.strip(), oth.strip(), tot.strip())
            self.savefee()
            return 1
        else:
            return -1

    def savefee(self):
        with open(self.filename2, "w") as f:
            for abc in self.fee:
                f.write(abc + ";" + self.fee[abc][0] + ";" + self.fee[abc][1] + ";" + self.fee[abc][2] + ";" +
                        self.fee[abc][3] + ";" + self.fee[abc][4] + "\n")

    def gettotal(self, classe):

        self.file2 = open(self.filename2, "r")

        for line in self.file2:
            clas, tfee, afee, efee, oth, tot = line.strip().split(";")
            if classe == clas:
                return tot
            else:
                continue

        self.file2.close()


db3 = DataBase2("fees.txt")
