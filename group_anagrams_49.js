/**
 * @param {string[]} strs
 * @return {string[][]}
 */
function groupAnagrams(strs) {
  const result = new Map();

  for (const str of strs) {
    const arr = Array(26).fill(0);
    for (const char of str) {
      const val = char.charCodeAt(0) - 97;
      arr[val]++;
    }
    const key = arr.join(",");

    if (result.has(key)) {
      result.get(key).push(str);
    } else {
      result.set(key, [str]);
    }
  }
  return Array.from(result.values());
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
