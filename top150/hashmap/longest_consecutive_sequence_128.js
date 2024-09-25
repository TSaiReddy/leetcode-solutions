function longestConsecutive(nums) {
  const set = new Set(nums);
  let longConSeq = 0;

  for (const num of nums) {
    if (set.has(num - 1)) continue;
    let count = 1;
    let nextNum = num + 1;
    while (set.has(nextNum)) {
      count++;
      nextNum++;
    }
    longConSeq = Math.max(longConSeq, count);
  }
  return longConSeq;
}

console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));
