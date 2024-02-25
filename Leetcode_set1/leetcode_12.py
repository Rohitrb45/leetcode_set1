class Solution:
    def intToRoman(self, num: int) -> str:
        nu = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000]
        i=12
        roman=""
        sym = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"]
        
    
        while(num!=0):
            div = num // nu[i]
            num %= nu[i]
            while div:
              print(sym[i], end = "")
              roman+=sym[i]
              div -= 1
            i -= 1
            
        return roman