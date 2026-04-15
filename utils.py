import os

def print_dict(d, indent=0):
    '''
    Printa um dicionário e suas chaves de forma mais legível e identada no dispositivo de saída.
    '''
    for key, value in d.items():
        prefix = "  " * indent
        if isinstance(value, dict):
            print(f"{prefix}{key}:")
            print_dict(value, indent + 1)
        elif isinstance(value, list):
            print(f"{prefix}{key}:")
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    print(f"{prefix}  -")
                    print_dict(item, indent + 2)
                else:
                    print(f"{prefix}  - {item}")
        else:
            print(f"{prefix}{key}: {value}")
            
            
def generate_dzn(coverage) -> str:
    '''
    Converte um dicionário de cobertura (estrutura que relaciona testes com requisitos) e cria a solução do SCP como um arquivo que pode ser aberto no MiniZinc.
    '''
    tests: list = list(coverage.keys())
    requirements: list = sorted(set().union(*coverage.values()))
    n_tests: int = len(tests)
    n_req: int = len(requirements)
    matrix: list[list] = []
    for t in tests:
        row: list = []
        for r in requirements:
            row.append("true" if r in coverage[t] else "false")
        matrix.append(", ".join(row))
    matrix_str: str = ",\n".join(matrix)
    dzn = f"""
n_tests = {n_tests};
n_req = {n_req};

covers = array2d(1..{n_tests}, 1..{n_req},
[
{matrix_str}
]);
"""
    i: int = 0
    filename: str = ''
    while True:
        filename = os.path.join('.', f"ex{i}.dzn")
        if not os.path.exists(filename):
            break
        i += 1

    with open(filename, "w") as f:
        f.write(dzn.strip())
    
    return filename