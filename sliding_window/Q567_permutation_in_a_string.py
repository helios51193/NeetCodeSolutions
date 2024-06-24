from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        window = len(s1)
        freq_window = Counter(s2[:window])
        s1_dict = Counter(s1)

        # if both are of same length
        if s1_dict == freq_window:
            return True
        
        for i in range(window, len(s2)):
            start_ch = s2[i-window]
            end_ch =s2[i]
            if freq_window[start_ch] == 1:
                del freq_window[start_ch]
            else:
                freq_window[start_ch] -=1
            
            freq_window[end_ch] = freq_window.get(end_ch,0) + 1

            if freq_window == s1_dict:
                return True
        
        return False
        