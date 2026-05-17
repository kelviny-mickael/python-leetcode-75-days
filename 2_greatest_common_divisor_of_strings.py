"""
Para duas strings s a e b t, dizemos que "t a divide s b" se e somente se 
s = t + t + t + ... + t + ta tfor concatenada com ela mesma uma ou mais vezes.

Dadas duas strings str1 e str2, retorne a maior string x 
tal que x divide ambas str1 e str2 .

Exemplo 1:

Entrada: str1 = "ABCABC", str2 = "ABC"

Saída: "ABC"

Exemplo 2:

Entrada: str1 = "ABABAB", str2 = "ABAB"

Saída: "AB"

Exemplo 3:

Entrada: str1 = "LEET", str2 = "CODE"

Saída: ""

Exemplo 4:

Entrada: str1 = "AAAAAB", str2 = "AAA"

Saída: " "

Restrições:

1 <= str1.length, str2.length <= 1000
str1e str2são compostas por letras maiúsculas do alfabeto inglês.
"""

class Solution(object):
    
    def gcdOfStrings(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.result = ''
        
        for ind, value in enumerate(str1):
            print(ind, value)
        
inst = Solution()

print(inst.gcdOfStrings('ABCABC', 'ABC'))