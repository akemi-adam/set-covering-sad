from typing import Dict

class SolveSCP:
    '''
    Resolução do problema de set covering para testes de cobertura utilizando tabu search.
    '''
    def __init__(self, coverage: Dict[str, set], max_movs_size=5, max_iter=100):
        self.coverage = coverage
        self.tests = list(coverage.keys())
        self.requirements = set().union(*coverage.values())
        self.max_movs_size = max_movs_size
        self.max_iter = max_iter

    def cost(self, solution: set) -> int:
        '''
        Função de custo para uma solução. Aplica uma penalidade para o número de requisitos não cobertos
        '''
        covered: set = set()
        for t in solution:
            covered |= self.coverage[t]
        not_covered: set = self.requirements - covered
        return len(solution) + len(self.requirements) * len(not_covered)

