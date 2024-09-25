function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const hash = {};

  for (const char of s) {
    hash[char] = (hash[char] || 0) + 1;
  }

  for (const char of t) {
    if (!hash[char]) return false;
    else hash[char] -= 1;
  }

  return true;
}

console.log(isAnagram("anagram", "nagaram"));
