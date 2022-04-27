class Rel_Check:

    def __init__(self, name=None,birthday=None,status=None):
        self.peeps = {'Sir Danjuma': '29th January 1995', 'Alpha': '19th December 1999', 'emma':'15th january 2000'}
        self.name = name
        self.birthday = birthday
        self.status = status

    def Notification(self):
        user_input = input('Whoose birthday do you want to check: ')
        for peep in self.peeps.keys():
            if user_input in self.peeps.keys():
                return self.peeps[user_input]
            else:
                return 'Invalid Rel'


    def add_one(self):
        new_name = str(input('Enter your name: '))
        birthday = str(input('Enter a birthdate and year in string format: '))
        self.peeps[new_name] = birthday


    def reload_dict(self):
        new_dict = {}
        if self.add_one():
            new_dict = self.peeps
        return True

    '''def save_new_person(self):
        self.peeps = self.peeps
        with open("dict.txt", 'w') as f:
            f.write(str(self.peeps))'''






#rel1 = Rel_Check('Sir Danjuma')
#print(rel1.Notification())



rel3 = Rel_Check()
print(rel3.reload_dict())
print(rel3.Notification())

rel2 = Rel_Check('Alpha')
print(rel2.Notification())

