function maxFrequencyElements(nums) {
  const frequencyMap = new Map();

  let maxFrequency = 0;
  let totalSum = 0;

  for (const num of nums) {
    const frequency = (frequencyMap.get(num) || 0) + 1;
    frequencyMap.set(num, frequency);

    if (frequency > maxFrequency) {
      maxFrequency = frequency;
      totalSum = frequency;
    } else if (frequency === maxFrequency) {
      totalSum += frequency;
    }
  }

  return totalSum;
}

console.log(maxFrequencyElements([1, 2, 3, 4, 5]));
