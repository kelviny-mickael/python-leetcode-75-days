"""
1768. Mesclar strings alternadamente

Você recebe duas strings, ` word1a` e `b` word2. 
Combine as strings adicionando letras em ordem alternada, começando com `a` word1. 
Se uma string for mais longa que a outra, anexe as letras adicionais ao final da string resultante.
Retorne a string mesclada.

Exemplo 1:
Entrada: palavra1 = "abc", palavra2 = "pqr"
 Saída: "apbqcr"
 Explicação:  A string resultante será mesclada da seguinte forma: 
palavra1: abc 
palavra2: pqr 
mesclada: apbqcr

Exemplo 2:

Entrada: palavra1 = "ab", palavra2 = "pqrs"
 Saída: "apbqrs"
 Explicação:  Observe que, como a palavra2 é mais longa, "rs" é adicionado ao final. 
palavra1: ab 
palavra2: pqrs 
mescladas: apbqrs

Exemplo 3:

Entrada: palavra1 = "abcd", palavra2 = "pq"
 Saída: "apbqcd"
 Explicação:  Observe que, como a palavra1 é mais longa, "cd" é adicionado ao final. 
palavra1: abcd 
palavra2: pq 
mescladas: apbqcd

Restrições:

1 <= word1.length, word2.length <= 100
word1 e word2 são compostas por letras minúsculas do alfabeto inglês.
"""


class Solution():
    
    def mergeAlternately(self, str1, str2, merge_str = ''):
        self.str1 = str1
        self.str2 = str2
        self.merge_str = merge_str
        
        if len(self.str1) == len(self.str2):
            for each_word in range(len(self.str1)):
                
                self.merge_str += self.str1[each_word] + self.str2[each_word]

        elif len(self.str1) > len(self.str2) or len(self.str2) > len(self.str1):
            len_geral = 0
            last_chars = ''

            if len(self.str1) >= len(self.str2):
                len_geral = len(self.str1) - len(self.str2)
                last_chars = self.str1[-len_geral:]
            
                for each_word in range(len(self.str1) - len_geral):
                    self.merge_str += self.str1[each_word] + self.str2[each_word]
            
                self.merge_str += last_chars
            else:
                len_geral = len(self.str2) - len(self.str1)
                last_chars = self.str2[-len_geral:]
            
                for each_word in range(len(self.str2) - len_geral):
                    self.merge_str += self.str1[each_word] + self.str2[each_word]
                
                self.merge_str += last_chars
            
        return self.merge_str
    
merge_str = Solution()

result_merge_str = merge_str.mergeAlternately('ab', 'pqrs')

print(result_merge_str)