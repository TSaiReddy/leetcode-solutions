function guessNumber(n) {
  let low = 0;
  let high = n;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const val = guess(mid);

    if (val === 0) {
      return mid;
    }
    if (val === -1) {
      low--;
      high = mid;
    }
    if (val === 1) {
      low = mid + 1;
    }
  }
}

console.log(guessNumber(10));

function guess(num) {
  if (num > 6) {
    return -1;
  }
  if (num < 6) {
    return 1;
  }
  if (num === 6) {
    return 0;
  }
}
