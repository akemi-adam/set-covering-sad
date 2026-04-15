int: n_tests;
int: n_req;

set of int: TESTS = 1..n_tests;
set of int: REQS = 1..n_req;

array[TESTS, REQS] of bool: covers;

% Representa cada teste, se foi escolhido ou não
array[TESTS] of var bool: x;

% Define a condição: percorre os requisitos de forma que pelo menos um teste cubra cada requisito
constraint
    forall(r in REQS)(
        sum(t in TESTS)(bool2int(covers[t,r] /\ x[t])) >= 1
    );

% Resolve o problema com base na restrição buscando minimizar o número de testes
solve minimize sum(t in TESTS)(bool2int(x[t]));