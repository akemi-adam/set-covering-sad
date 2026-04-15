from random import choice, randint, sample
from typing import Dict

class GenerateSet:
    '''
    Gera um conjunto de requisitos U e relaciona com conjuntos de requisitos S
    '''
    
    def __init__(self, requirements: list, tests: list) -> None:
        self.requirements = requirements
        self.requirements_length = len(requirements)
        self.tests = tests
        
    def _make_requirements(self):
        '''
        Retorna uma lista que relaciona testes com requisitos.
        '''
        requirements_by_tests: Dict[str, set] = {}
        for test in self.tests:
            i: int = randint(1, self.requirements_length)
            requirements_by_tests[test] = set(sample(self.requirements, i))
        return requirements_by_tests
            
    def safe_exec(self):
        '''
        Retorna uma lista que relaciona testes com requisitos. Garante que todos os requisitos estarão dispersos entre os testes.
        '''
        requirements_by_tests: Dict[str, set] = self._make_requirements()
        for requirement in self.requirements:
            for test in requirements_by_tests:
                if requirement in requirements_by_tests[test]: break
            else:
                test: str = choice(list(requirements_by_tests))
                requirements_by_tests[test].add(requirement)
        return requirements_by_tests
    
    def unsafe_exec(self) -> Dict[str, set]:
        '''
        Retorna uma lista que relaciona testes com requisitos. Não garante que todos os requisitos estão dispersos entre os testes.
        '''
        return self._make_requirements()
        