class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        fizz = 0
        buzz = 0
        for i in range(1, n + 1):
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                ans.append("FizzBuzz")
                fizz = 0
                buzz = 0
            elif fizz == 3:
                ans.append("Fizz")
                fizz = 0
            elif buzz == 5:
                ans.append("Buzz")
                buzz = 0
            else:
                ans.append(str(i))
        return ans
    
        # for i in range(1, n + 1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         ans.append('FizzBuzz')
        #     elif i % 3 == 0:
        #         ans.append("Fizz")
        #     elif i % 5 == 0:
        #         ans.append("Buzz")
        #     else:
        #         ans.append(str(i))
        # return ans
        
        # for i in range(1, n + 1):
        #     a = ""
        #     if i % 3 == 0:
        #         a += "Fizz"
        #     if i % 5 == 0:
        #         a += "Buzz"
        #     if a == "":
        #         ans.append(str(i))
        #     else:
        #         ans.append(a)
        # return ans
        