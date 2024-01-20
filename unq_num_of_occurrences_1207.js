function uniqueOccurrences(arr) {
  const occurrences = {};
  for (const item of arr) {
    occurrences[item] = (occurrences[item] || 0) + 1;
  }
  const array = Object.values(occurrences);
  const removeDupArr = [...new Set(array)];
  if (String(array) === String(removeDupArr)) {
    return true;
  } else {
    return false;
  }
}

console.log(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]));
