/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
function characterReplacement(s, k) {
  const count = {};
  let result = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    count[s[right]] = count[s[right]] + 1 || 1;

    while (right - left + 1 - Math.max(...Object.values(count)) > k) {
      count[s[left]]--;
      left++;
    }
    result = Math.max(result, right - left + 1);
  }

  return result;
}

// Other Solution
// function characterReplacement(s, k) {
//   const count = {};
//   let result = 0;
//   let left = 0;
//   let maxFreq = 0;

//   for (let right = 0; right < s.length; right++) {
//     count[s[right]] = count[s[right]] + 1 || 1;

//     maxFreq = Math.max(maxFreq, count[s[right]]);

//     while (right - left + 1 - maxFreq > k) {
//       count[s[left]]--;
//       left++;
//     }
//     result = Math.max(result, right - left + 1);
//   }

//   return result;
// }

// console.log(characterReplacement("ABAB", 2));
console.log(characterReplacement("AABABBA", 1));
