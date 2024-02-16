function returnToBoundaryCount(nums) {
  let returnedToBoundry = 0;
  let count = 0;
  for (const num of nums) {
    count += num;
    if (count === 0) {
      returnedToBoundry++;
    }
  }
  return returnedToBoundry;
}

console.log(returnToBoundaryCount([2, 3, -5])); //1
console.log(returnToBoundaryCount([3, 2, -3, -4])); //0
console.log(returnToBoundaryCount([-10, 10, 8])); //1
console.log(returnToBoundaryCount([1])); //0
console.log(returnToBoundaryCount([-7, 10])); //0
