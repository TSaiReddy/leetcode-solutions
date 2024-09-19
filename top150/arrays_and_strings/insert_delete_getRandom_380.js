class RandomizedSet {
  constructor() {
    this.hash = new Map();
    this.arr = [];
  }

  insert(val) {
    if (this.hash.has(val)) return false;

    this.hash.set(val, this.arr.length);
    this.arr.push(val);
    return true;
  }
  remove(val) {
    if (!this.hash.has(val)) return false;

    const idx = this.hash.get(val);

    // Move the last element to the index of the element to be removed
    const lastElement = this.arr[this.arr.length - 1];
    this.arr[idx] = lastElement;
    this.hash.set(lastElement, idx);

    // Remove the last element
    this.arr.pop();
    this.hash.delete(val);
    return true;
  }
  getRandom() {
    return this.arr[Math.floor(Math.random() * this.arr.length)];
  }
}

const obj = new RandomizedSet();
console.log(obj.insert(2), "in");
console.log(obj.insert(3), "in");
console.log(obj.insert(2), "in");
console.log(obj.remove(2), "re");
console.log(obj.insert(8), "in");
console.log(obj.insert(4), "in");
console.log(obj.insert(5), "in");
console.log(obj.getRandom(), "get");
