class RecurringServices(object):
    def __init__(self, qty, config, name, check=None):
        self.qty = qty
        self.config = config
        self.check = check
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}: qty={self.qty} config=${self.config} check={self.check}'

class MFA(RecurringServices):
    def __init__(self, qty, name="Duo", config=0, check=None):
        self.qty = qty
        self.name = name
        config = self.qty*33.75
        if config <= 405:
            self.config = 405
        else:
            self.config = config
        if check == None:
            self.check = 'No'
        else:
            self.check = check

    

_test = RecurringServices(3,5,"Duo", "Bill")
print(_test)
test = MFA(3)
print(test)
test2 = MFA(59, check="Bill")
print(test2)
test3 = MFA(100, check="Stan")
print(test3)