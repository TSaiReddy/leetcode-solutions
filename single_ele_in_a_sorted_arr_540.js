function singleNonDuplicate(arr) {
  for (let index = 0; index < arr.length; index += 2) {
    const element1 = arr[index];
    const element2 = arr[index + 1];
    if (element1 !== element2) {
      return element1;
    }
  }
}
