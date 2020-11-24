class Container { 
  constructor() {
    this.group = new Set();
    this.group.add(this);
    this.amount = 0.0;
  }

  get_amount() { 
    return this.amount; 
  }

  add_water(amount) {
    let amount_per_container = amount * 1.0 / this.group.size;
    for (let item of this.group) {
      item.amount = item.amount + amount_per_container;
    }
  }

  connect_to(other) {
    let diff = new Set([...this.group].filter(x => !other.group.has(x)));
    if (diff.size == 0) {
      return;
    }

    let size1 = this.group.size;
    let size2 = other.group.size;
    let tot1 = this.amount * size1;
    let tot2 = other.amount * size2;
    let new_amount = (tot1 + tot2) / (size1 + size2);

    for (let item of other.group) {
      this.group.add(item);
    }

    for (let item of other.group) {
      item.group = this.group;
    }

    for (let item of this.group) {
      item.amount = new_amount;
    }
  }
}

let a = new Container();
let b = new Container();
let c = new Container();
let d = new Container();

a.add_water(12);
d.add_water(8);
console.log(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount());

a.connect_to(b);
console.log(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount());

b.connect_to(c);
console.log(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount());

b.connect_to(d);
console.log(a.get_amount(), b.get_amount(), c.get_amount(), d.get_amount());

console.log("Done...");
