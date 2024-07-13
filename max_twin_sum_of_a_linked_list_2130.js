function pairSum(head) {
  let slow = head;
  let fast = head;

  const stack = [];

  while (fast && fast.next) {
    stack.push(slow.val);
    slow = slow.next;
    fast = fast.next.next;
  }

  let maxTwinSum = 0;

  while (slow) {
    maxTwinSum = Math.max(maxTwinSum, stack.pop() + slow.val);
    slow = slow.next;
  }

  return maxTwinSum;
}
