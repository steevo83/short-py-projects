class EasyDict():
    def __init__(self, dictionary={}):
        self.__dict__.update(dictionary)

    def __getitem__(self, key):
        return self.__dict__[key]

person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})