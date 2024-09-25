function groupAnagrams(strs) {
  const result = new Map();
  for (const str of strs) {
    const abc = Array(26).fill(0);
    for (const s of str) {
      const idx = s.charCodeAt(0) - 97;
      abc[idx]++;
    }
    const key = abc.join(",");
    if (result.has(key)) result.get(key).push(str);
    else result.set(key, [str]);
  }

  return Array.from(result.values());
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
