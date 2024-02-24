function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

function reverseList(head) {
  let prev = null;
  let current = head;

  while (current) {
    const temp = current.next;
    current.next = prev;
    prev = current;
    current = temp;
  }
  return prev;
}

const node = new ListNode(1);
node.next = new ListNode(2);
node.next.next = new ListNode(3);
node.next.next.next = new ListNode(4);
node.next.next.next.next = new ListNode(5);
console.log(reverseList(node));
