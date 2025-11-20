from collections import deque

# similar approach to question no 909
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        # create a set of bank for Q(1) search
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        queue = deque([startGene])
        mutations = 0
        # BFS on the mutations existing in the bank
        while queue:
            lenq = len(queue)
            for _ in range(lenq):
                gene = queue.popleft()
                if gene == endGene:
                    return mutations
                # run for each mutation of the current gene
                for i in range(len(gene)):
                    for c in "ACGT":
                        mutated = gene[:i] + c + gene[i+1:]
                        if mutated in bankSet:
                            queue.append(mutated)
                            bankSet.remove(mutated)

            # Here it can be refer to as level, we are going +1 level each time we completely traverse all mutations of a give gene
            mutations += 1
        
        return -1