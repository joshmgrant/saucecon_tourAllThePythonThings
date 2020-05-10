class ItemCounter(object):

    def __init__(self, items=0):
        self.items  = items

    def add(self):
        self.items += 1

    def remove(self):
        self.items -= 1

    def total(self):
        return self.items

def test_default():
    counter = ItemCounter()
    assert counter.total() == 0

def test_add():
    counter = ItemCounter()
    counter.add()
    assert counter.total() == 1

def test_remove():
    counter = ItemCounter()
    counter.add()
    counter.add()
    counter.remove()
    assert counter.total() == 1