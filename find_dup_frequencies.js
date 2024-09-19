function findDuplicateFrequencies(arr) {
  const freqs = {};

  for (const a of arr) {
    freqs[a] = (freqs[a] || 0) + 1;
  }

  let maxFreq = 0;

  for (const freq in freqs) {
    if (freqs[freq] > maxFreq) maxFreq = freqs[freq];
  }

  return maxFreq;
}

const arr = ["apple", "banana", "apple", "orange", "banana", "apple"];
const duplicateFrequencies = findDuplicateFrequencies(arr);
console.log(duplicateFrequencies);
