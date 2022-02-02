
class Empolyee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname} @Coderashlaan.com"

    def explane(self):
        return f"This is Empolyee {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is Delated"
        return f"{self.fname}.{self.lname}@Coderarshlaan.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.lname = names.split(".")[0]
        self.fname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skilf = Empolyee("Skill", "F")
# print(skilf.email)
o = "This is Tatti"
print(dir(o))
# print(id("This is STR"))

import inspect
print(inspect.getmembers(skilf))