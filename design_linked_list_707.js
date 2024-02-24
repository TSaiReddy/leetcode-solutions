function Node(val) {
  this.val = val;
  this.next = null;
}

function MyLinkedList() {
  this.head = null;
  this.tail = null;
}

MyLinkedList.prototype.get = function (index) {
  if (!this.head) {
    return -1;
  } else {
    let current = this.head;
    let curIdx = 0;
    while (current) {
      if (index === curIdx) {
        return current.val;
      } else {
        curIdx++;
      }
      current = current.next;
    }
    return -1;
  }
};

MyLinkedList.prototype.addAtHead = function (val) {
  const newNode = new Node(val);

  if (!this.head) {
    this.head = newNode;
    this.tail = newNode;
  } else {
    let current = this.head;
    this.head = newNode;
    this.head.next = current;
  }
};

MyLinkedList.prototype.addAtTail = function (val) {
  const newNode = new Node(val);

  if (!this.head) {
    this.head = newNode;
    this.tail = newNode;
  } else {
    this.tail.next = newNode;
    this.tail = newNode;
  }
};

MyLinkedList.prototype.addAtIndex = function (index, val) {
  const newNode = new Node(val);

  if (index === 0) {
    const newNode = new Node(val);
    newNode.next = this.head;
    this.head = newNode;
    if (!this.tail) {
      this.tail = newNode;
    }
    return;
  }

  let curIdx = 0;
  let current = this.head;

  while (current) {
    if (curIdx === index - 1) {
      const prevNode = current.next;
      newNode.next = prevNode;
      current.next = newNode;
      if (!newNode.next) {
        this.tail = newNode;
      }
      return;
    }
    curIdx++;
    current = current.next;
  }
};

MyLinkedList.prototype.deleteAtIndex = function (index) {
  if (index === 0) {
    if (this.head) {
      this.head = this.head.next;
      if (!this.head) {
        this.tail = null;
      }
    }
    return;
  }

  let current = this.head;
  let curIdx = 0;

  while (current) {
    if (curIdx === index - 1) {
      if (current.next) {
        current.next = current.next.next;
        if (!current.next) {
          this.tail = current;
        }
      }
      return;
    }
    curIdx++;
    current = current.next;
  }
};

const obj = new MyLinkedList();
obj.addAtIndex(0, 10);
obj.addAtIndex(0, 20);
obj.addAtIndex(1, 30);

console.log(JSON.stringify(obj), "--------------");

obj.get(0);
console.log(obj, "get");
