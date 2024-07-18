class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.hash = new Map();
  }

  get(key) {
    if (!this.hash.has(key)) {
      return -1;
    }
    const value = this.hash.get(key);

    this.hash.delete(key);
    this.hash.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.hash.has(key)) {
      this.hash.delete(key);
    } else if (this.hash.size >= this.capacity) {
      const leastRecentlyUsedKey = this.hash.keys().next().value;
      this.hash.delete(leastRecentlyUsedKey);
    }
    this.hash.set(key, value);
  }
}

var obj = new LRUCache(2);
console.log(obj.put(1, 0)); // cache is {1=1}
console.log(obj.put(2, 2)); // cache is {1=1, 2=2}
console.log(obj.get(1)); // return 1
console.log(obj.put(3, 3)); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
console.log(obj.get(2)); // returns -1 (not found)
console.log(obj.put(4, 4)); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
console.log(obj.get(1)); // return -1 (not found)
console.log(obj.get(3)); // return 3
console.log(obj.get(4)); // return 4
