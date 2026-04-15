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
