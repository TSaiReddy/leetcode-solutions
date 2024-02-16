function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

function deleteDuplicates(head) {
  let prevVal = null;
  let current = head;

  while (current) {
    if (prevVal && prevVal.val === current.val) {
      prevVal.next = current.next;
    } else {
      prevVal = current;
    }
    current = current.next;
  }
  return head;
}

const node = new ListNode(1);
node.next = new ListNode(1);
node.next.next = new ListNode(2);

deleteDuplicates(node);
