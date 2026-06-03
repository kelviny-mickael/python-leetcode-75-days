"""
Há n crianças com doces. Você recebe um vetor de inteiros candies, onde cada elemento candies[i] representa a quantidade 
de doces que a criança tem, e um inteiro, que indica a quantidade de doces extras que você possui. i^th extraCandies

Retorna um array booleano result de comprimento n, onde result[i] é verdadeiro true se, 
depois de dar todos os doces à criança , ela terá o maior número de doces entre todas as 
crianças, ou falso caso contrário .i^th extraCandies false.

Observe que várias crianças podem ter a maior quantidade de doces.

Exemplo 1:

Entrada: doces = [2,3,5,1,3], docesExtras = 3
 Saída: [verdadeiro,verdadeiro,verdadeiro,falso,verdadeiro] 
 Explicação: Se você der todos os doces extras para: 
- Criança 1, ela terá 2 + 3 = 5 doces, que é o maior número entre as crianças. 
- Criança 2, ela terá 3 + 3 = 6 doces, que é o maior número entre as crianças. 
- Criança 3, ela terá 5 + 3 = 8 doces, que é o maior número entre as crianças. 
- Criança 4, ela terá 1 + 3 = 4 doces, que não é o maior número entre as crianças. 
- Criança 5, ela terá 3 + 3 = 6 doces, que é o maior número entre as crianças.
Exemplo 2:

Entrada: doces = [4,2,1,1,2], docesextras = 1
 Saída: [verdadeiro,falso,falso,falso,falso] 
 Explicação: Há apenas 1 doce extra. 
A criança 1 sempre terá o maior número de doces, mesmo que outra criança receba o doce extra.
Exemplo 3:

Entrada: doces = [12,1,12], docesExtras = 10
 Saída: [verdadeiro,falso,verdadeiro]
 

Restrições:

n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
"""

class Solution(object):
    
    def kidsWithCandies(self, candies, extraCandies):
        sum_cand_extra = []
        val_max_cand = max(candies)
        result = []
        
        for ind, cands_each_kid in enumerate(candies):
            sum_cand_extra.append(candies[ind] + extraCandies)

            if sum_cand_extra[ind] >= val_max_cand:
                result.append(True)
            else:
                result.append(False)
    
        return result
        
instance = Solution()

print(instance.kidsWithCandies([2,3,5,1,3], 3))
print(instance.kidsWithCandies([4, 2, 1, 1, 2], 1))