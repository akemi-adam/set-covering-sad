# set-covering-sad
Atividade avaliativa da primeira unidade da disciplina de Sistema de Apoio a Decisão (SAD) do curso de Bachalerado em Sistemas de Informação (BSI) da UFRN.

## Contexto

O trabalho tem como escopo resolver o problema de Set Covering (Cobertura de conjuntos, ou SCP) no contexto de testes de coberturas, nas linguagens Python e Minizinc, e produzir um artigo com isso.

SCP é um problema NP-Difícil que se baseia em representar um conjunto U original a partir do menor número de sub conjuntos S possível.

Dessa forma, o problema de teste de cobertura x requisitos de software foi representado com o SCP. Aqui, é preciso encontrar o menor número possível de testes que cubram todos os requisitos do sistema.

## Solução Python

O código em Python utiliza a meta-heurística Tabu Search com algoritmo guloso para responder o problema de SCP de forma aproximada, buscando estar o mais próximo do ótimo global.

O código pode ser executado com:

```python
python3 ./main.py
```

## Solução MiniZinc

Ao executar o código em Python, um arquivo `.dzn` é criado. Você deve instalar o MiniZinc e abrir esse arquivo e o arquivo `minizinc_solution.mzn` para poder executar a solução MiniZinc.

O MiniZinc é um software que oferece uma linguagem onde você pode definir dados e restrições para aplicar um solver em uma função objetivo. Nesse caso, o objetivo é minimizar o número de testes de forma que todos os requisitos estejam representados.