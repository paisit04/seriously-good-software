class Container:
    def __init__(self):
        self.g = {0:self}
        self.n = 1
        self.x = 0.0
    
    def get_amount(self):
        return self.x

    def add_water(self, x):
        y = x / self.n
        for i in range(self.n):
            self.g[i].x = self.g[i].x + y

    def connect_to(self, c):
        z = (self.x * self.n + c.x * c.n) / (self.n + c.n)

        for i in range(self.n): # for each container g[i] in first group
            for j in range(c.n): # for each container c.g[j] in second group
                self.g[i].g[self.n+j] = c.g[j]; # add second to group of first 
                c.g[j].g[c.n+i] = self.g[i]; # add first to group of second

        self.n += c.n

        for i in range(self.n):
            self.g[i].n = self.n
            self.g[i].x = z

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
