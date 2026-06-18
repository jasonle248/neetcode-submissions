class Solution:
  
    def checkInclusion(self, t: str, s: str) -> bool:
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
          
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

           
            while right - left >= len(t):
               
                if valid == len(need):
                    return True
                d = s[left]
                left += 1
              
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

      
        return False