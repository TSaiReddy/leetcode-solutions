function isAnagram(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const counter1 = {};
  const counter2 = {};

  for (const c1 of s) {
    counter1[c1] = (counter1[c1] || 0) + 1;
  }

  for (const c2 of t) {
    counter2[c2] = (counter2[c2] || 0) + 1;
  }

  for (const c3 in counter1) {
    if (counter1[c3] !== counter2[c3]) {
      return false;
    }
  }

  return true;
}

isAnagram("anagram", "nagaram");
