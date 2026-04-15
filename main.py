from generate import GenerateSet
from tabu_search import SolveSCP
from utils import print_dict, generate_dzn

if __name__ == '__main__':
    requirements = [f"RF{i}" for i in range(1, 11)]
    tests = [f"T{i}" for i in range(1, 8)]

    gen = GenerateSet(requirements, tests)
    coverage = gen.safe_exec()

    tabu = SolveSCP(coverage, 5, 100)
    solution = tabu.exec()

    print("Requisitos: ", requirements)
    print("Testes: ", tests)
    print("Cobertura: ")
    print_dict(coverage)
    print("Solução encontrada:", solution)
    minizinc_filename: str = generate_dzn(coverage)
    print(f'Arquivo {minizinc_filename} criado!')