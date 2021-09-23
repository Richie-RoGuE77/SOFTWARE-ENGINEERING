class content(object):
    def __init__(self):
        self.name = 'Before calling'
        self.contentcoupling = self.contentcoupling()
    def display(self):
        self.contentcoupling.display()
    class contentcoupling():
        def display(self):
            self.name = 'After calling'
            print(self.name)


obj1 = content()
obj1.display()


"""In this example the content class has a variable name which 
initially stores some data but after the inner class contentcoupling 
access it, that data is replaced by some other data.."""
