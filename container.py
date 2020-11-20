class Container:
    def __init__(self):
        self.group = set()
        self.group.add(self)
        self.amount = 0.0
    
    def get_amount(self):
        return self.amount

    def add_water(self, amount):
        amount_per_container = amount * 1.0 / len(self.group)
        for c in self.group:
            c.amount = c.amount + amount_per_container

    def connect_to(self, other):
        diff = self.group.difference(other.group)
        if len(diff) == 0:
            return

        size1 = len(self.group)
        size2 = len(other.group)
        tot1 = self.amount * size1
        tot2 = other.amount * size2
        new_amount = (tot1 + tot2) / (size1 + size2)

        self.group.update(other.group)

        for c in other.group:
            c.group = self.group

        for c in self.group:
            c.amount = new_amount

if __name__ == "__main__":
    a = Container()
    b = Container()
    c = Container()
    d = Container()

    a.add_water(12);
    d.add_water(8);
    print("{} {} {} {}".format(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount()))

    a.connect_to(b);
    print("{} {} {} {}".format(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount()))
    
    b.connect_to(c);
    print("{} {} {} {}".format(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount()))
    
    b.connect_to(d);
    print("{} {} {} {}".format(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount()))

    print("Done...")
