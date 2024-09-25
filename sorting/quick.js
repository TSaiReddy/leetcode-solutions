function quickSort(arr) {
  if (arr.length <= 1) return arr;
  const pivot = arr.at(-1);
  let left = [];
  let right = [];

  for (let a = 0; a < arr.length - 1; a++) {
    const element = arr[a];

    if (element <= pivot) left.push(element);
    else right.push(element);
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

console.log(quickSort([-5, 3, 2, 1, -3, -3, 7, 2, 2]));
