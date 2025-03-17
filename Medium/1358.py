class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    a = 0
    cnt = {c: 0 for c in 'abc'}

    lptr = 0
    for c in s:
      cnt[c] += 1
      while min(cnt.values()) > 0:
        cnt[s[lptr]] -= 1
        lptr += 1
    
      a += lptr

    return a
