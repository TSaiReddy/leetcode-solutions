// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

function getDecimalValue(head) {
  let decimalValue = 0;
  while (head) {
    decimalValue = decimalValue * 2 + head.val;
    head = head.next;
  }
  return decimalValue;
}

const head = new ListNode(1);
head.next = new ListNode(0);
head.next.next = new ListNode(1);

// Print linked list details
const result = getDecimalValue(head);
console.log("Linked List Details:", result);
