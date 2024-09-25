function canConstruct(ransomNote, magazine) {
  const hash = {};

  for (const m of magazine) {
    hash[m] = (hash[m] || 0) + 1;
  }

  for (const r of ransomNote) {
    if (!hash[r]) return false;
    else hash[r] -= 1;
  }
  return true;
}

console.log(canConstruct("a", "b"));
