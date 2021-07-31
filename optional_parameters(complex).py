def func(x=2):
    return x ** 2


def func1(word, freq=1, add=5):
    print(word * (freq + add))


call = func1('sai', 5)


class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):
        if showAll:
            print(
                f'This car is a {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.kms} kms.')
        else:
            print(f'This car is a {self.make} {self.model} from {self.year}.')


whip = car('Ford', 'Fusion', 2012)
whip.display(False)
