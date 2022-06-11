class Rel_Check:

    def __init__(self, name=None,birthday=None,status=None):
        self.peeps = {'EZRA':'30th July','EDITH':'6th June','MY FATHER':'2nd May','SIR DANJUMA': '29th January 1995',
                      'ALPHA': '1999-12-19', 'EMMA':'15th january 2000', 'AUNTY ROSE':'22nd September', 'UNCLE DOUGLAS':'10th October',
                      'AUNTY BLESSING': '19th March', 'FAVOUR':'7th October', 'HAVILLAH': '27th MAY','HEBRON':'6th June','JERRY':'17th June',
                      'RACHEAL':'19th July', 'PATIENCE AKYENGO':'8th July', 'AUNTY DORATHY':'7th JUNE'}
        self.name = name
        self.birthday = birthday
        self.status = status

#input a name i have saved in my dict and it tells the person's birthday
    def Notification(self):
        user_input = input('Whoose birthday do you want to check: ').upper()
        for peep in self.peeps.keys():
            if user_input in self.peeps.keys():
                return f"{user_input}'s birthday is {self.peeps[user_input.upper()]}"
            else:
                return f'No one is saved as {user_input}'


        def add_one(self, x,y):
            import  datetime
            today = datetime.date.today()
            x = self.peeps.keys()
            y = self.peeps.values()

#save a dict:value and key that is not in the dict
    def reload_dict(self):
        new_dict = {}
        if self.add_one():
            new_dict = self.peeps
        return

    '''def save_new_person(self):
        self.peeps = self.peeps
        with open("dict.txt", 'w') as f:
            f.write(str(self.peeps))'''

#rel1 = Rel_Check('Sir Danjuma')
#print(rel1.Notification())



#rel3 = Rel_Check()
#print(rel3.reload_dict())
#print(rel3.Notification())

rel2 = Rel_Check()
print(rel2.Notification())

