class Solution:
    def isValid(self, s: str) -> bool:

        my_dict = {"}": "{", "]": "[", ")": "("}
        my_list = {"{", "[", "("}

        #init stack to store half the string s
        stack = []

        try:
            #store half the string s in stack
            for char in s:
                if char in my_dict:
                    if (my_dict.get(char)!=stack.pop()):
                        return False
                elif char in my_list:
                    stack.append(char)
                else:
                    return False
        except Exception as e:
            print(e, " exception caught")
            return False

            
        if (stack != []):
            return False

        return True

        