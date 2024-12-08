function increasingTriplet(nums) {
  let num1 = Infinate;
  let num2 = Infinity;

  for (const num of nums) {
    if (num < num1) num1 = num;
    else if (num < num2) num2 = num;
    else return true;
  }
  return false;
}

// console.log(increasingTriplet([1, 2, 3, 4, 5]));
// console.log(increasingTriplet([1, 2, 3, 4, 5].reverse()));
console.log(increasingTriplet([1, 2, 1, 3]));
