function merge(left, right) {
  const arr = [];
  let leftIdx = 0;
  let rightIdx = 0;

  while (leftIdx < left.length && rightIdx < right.length) {
    if (left[leftIdx] < right[rightIdx]) {
      arr.push(left[leftIdx]);
      leftIdx++;
    } else {
      arr.push(right[rightIdx]);
      rightIdx++;
    }
  }

  while (leftIdx < left.length) {
    arr.push(left[leftIdx]);
    leftIdx++;
  }
  while (rightIdx < right.length) {
    arr.push(right[rightIdx]);
    rightIdx++;
  }

  return arr;
}

function divide(arr) {
  const arrLen = arr.length;
  if (arrLen <= 1) return arr;

  const mid = Math.floor(arrLen / 2);

  let left = divide(arr.slice(0, mid));
  let right = divide(arr.slice(mid));

  return merge(left, right);
}

console.log(divide([-5, 3, 2, 1, -3, -2, 7, 2, 2]));
