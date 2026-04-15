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

    def initial_solution(self) -> set:
        '''
        Gera uma primeira solução com um algoritmo guloso. 
        '''
        uncovered: set = set(self.requirements)
        solution: set = set()
        while uncovered:
            best_test = max(
                self.tests,
                key=lambda t: len(self.coverage[t] & uncovered)
            )
            solution.add(best_test)
            uncovered -= self.coverage[best_test]
        return solution

    def get_neighbors(self, solution) -> list:
        '''
        Gera vizinhos de uma solução
        '''
        neighbors = []
        for test in self.tests:
            new_solution = solution.copy()
            if test in new_solution:
                new_solution.remove(test)
                move = ("remove", test)
            else:
                new_solution.add(test)
                move = ("add", test)
            neighbors.append((new_solution, move))
        return neighbors

    def exec(self) -> set:
        '''
        Algoritmo do Tabu Search. Percorre um número X de interações, pegando os vizinhos e ordenando eles com base no seu custo.
        
        Depois, percorre cada vizinho. Se o movimento não estiver na lista tabu ou seu custo for menor que o da melhor solução atual, promove ele a candidato atual e proibe o movimento.
        '''
        current: set = self.initial_solution()
        best: set = current.copy()
        tabu_list: list = []
        for _ in range(self.max_iter):
            neighbors = self.get_neighbors(current)
            neighbors.sort(key=lambda neighbor: self.cost(neighbor[0]))
            for candidate, move in neighbors:
                if move not in tabu_list or self.cost(candidate) < self.cost(best):
                    current = candidate
                    tabu_list.append(move)
                    if len(tabu_list) > self.max_movs_size:
                        tabu_list.pop(0)
                    break
            if self.cost(current) < self.cost(best):
                best = current.copy()
        return best