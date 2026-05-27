"""
Para duas strings s a e b t, dizemos que "t a divide s b" se e somente se 
s = t + t + t + ... + t + ta t for concatenada com ela mesma uma ou mais vezes.

Dadas duas strings str1 e str2, retorne a maior string x 
tal que x divide ambas str1 e str2.

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
str1 e str2 são compostas por letras maiúsculas do alfabeto inglês.
"""

class Solution(object):
    
    def calc_mdc(self, num_a, num_b, mdc_both = 0):
        self.num_a = num_a
        self.num_b = num_b
        self.mdc_both = mdc_both
    
        while num_b != 0:

            try:
                self.num_a, self.num_b = self.num_b, self.num_a % self.num_b
                self.mdc_both = self.num_a
            except ZeroDivisionError:
                break
        
        return self.mdc_both
    
    def gcdOfStrings(self, str1, str2, result_mdc = ''):
        
        self.str1 = str1
        self.str2 = str2
        self.result_mdc = result_mdc
        
        if (self.str1 + self.str2) == (self.str2 + self.str1):
            self.result_mdc = self.calc_mdc(len(self.str1), len(self.str2))
            return self.str1[:self.result_mdc]
        else:
            return ''
        
inst = Solution()

print(inst.gcdOfStrings('ABCABC', 'ABC'))
print(inst.gcdOfStrings('ABABAB', 'ABAB'))
print(inst.gcdOfStrings('LEET', 'CODE'))
print(inst.gcdOfStrings('AAAAAB', 'AAA'))
print(inst.gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXX'))