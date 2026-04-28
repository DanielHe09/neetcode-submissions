class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #use hashmap to store number of occurences of each letter in each string
        #ex. {"s":2, "a":1}
        #compare the two hashmaps
        
        s_map = {}
        for char in s:#o(n)
            if (char in s_map):
                s_map[char] = s_map[char]+1
            else:
                s_map[char]=1

        t_map={}
        for char in t:#o(m)
            if (char in t_map):
                t_map[char] = t_map[char]+1
            else:
                t_map[char]=1

        if (s_map==t_map):
            return True
        else:
            return False