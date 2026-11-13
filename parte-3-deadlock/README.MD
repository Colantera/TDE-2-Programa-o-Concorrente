# Parte 3: Deadlock

Feito por Arthur Krauze

## Descrição do problema

O problema de deadlock consiste em basicamente um conjunto de processos que fica bloqueado permanentemente, porque cada thread tenta adquirir os recursos em uma ordem diferente. Com isso, uma acaba esperando pela outra, causando um travamento. 

O objetivo é reproduzir esse problema e depois apresentar uma solução para evitar que ele aconteça

## Versão reprodução (versão com trava)

Na primeira versão, foi criado duas threads, cada uma adquirindo um Lock diferente.

A primeira thread pega o LOCK_A, depois tenta pegar o LOCK_B. Já a segunda pega primeiro o LOCK_B e depois tenta pegar o LOCK_A.

Foi utilizado um pequeno intervalo de tempo entre a aquisição dos Locks para aumentar a possibilidade de as duas threads ficarem segurando um recurso enquanto aguardam o outro.

Com isso, cada thread fica esperando por um Lock que está sendo utilizado pela outra, causando um deadlock.

Para identificar o problema, utilizamos um tempo limite de espera (join com timeout). Se as duas threads continuarem em execução após esse período, o programa exibe a mensagem de deadlock detectado.

## Versão com solução

Na segunda versão, foi utilizada uma solução simples: padronizar a ordem de aquisição dos Locks.

Agora, as duas threads precisam pegar primeiro o LOCK_A e depois o LOCK_B.

Dessa forma, evitamos que uma thread fique segurando um recurso enquanto espera por outro em uma ordem contrária à da segunda thread.

Quando uma thread termina sua execução, ela libera os dois Locks, permitindo que a outra continue.

Com essa mudança, eliminamos a possibilidade de espera circular e evitamos o deadlock.

## Condições de Coffman

Existem quatro condições necessárias para acontecer um deadlock:

Exclusão mútua: cada Lock só pode ser utilizado por uma thread de cada vez.

Manter e esperar: uma thread mantém um Lock enquanto espera pelo outro.

Não preempção: uma thread não pode retirar um Lock que está sendo utilizado por outra.

Espera circular: uma thread espera por um recurso que está com outra, enquanto essa outra espera por um recurso da primeira.

Na versão com trava, as quatro condições estão presentes.

Na versão corrigida, foi eliminado a espera circular, pois todas as threads seguem uma ordem agora.


## Progresso e justiça

Na versão com trava, as duas threads ficam bloqueadas e não conseguem terminar suas execuções.

Na versão com solução, as threads conseguem adquirir os Locks, executar suas tarefas e liberar os recursos normalmente.

Porém, essa solução não garante totalmente a justiça entre as threads, pois uma delas pode precisar esperar mais tempo para conseguir utilizar os recursos.

## Protocolo utilizado

## Versão com trava:

-A primeira thread começa sua execução.

-Adquire o LOCK_A.

-A segunda thread começa sua execução.

-Adquire o LOCK_B.

-A primeira thread tenta adquirir o LOCK_B.

-A segunda thread tenta adquirir o LOCK_A.

-As duas ficam esperando uma pela outra, causando deadlock.

## Versão com solução:

-As duas threads começam sua execução.

-A primeira thread tenta adquirir o LOCK_A.

-A segunda thread também tenta adquirir o LOCK_A.

-Uma das threads consegue adquirir o Lock e depois pega o LOCK_B.

-Executa sua tarefa e libera os dois recursos.

-A outra thread consegue adquirir os Locks e finalizar sua execução.

-O programa termina sem deadlock.

## Como executar

O projeto foi desenvolvido em Python, utilizando a biblioteca threading e, na versão ingênua, também a biblioteca time.

É necessário ter o Python 3 instalado. Não é preciso instalar outras bibliotecas nem compilar o código.

Para executar, abra o terminal na pasta parte-3-deadlock.

Versão com trava:

python deadlock_reproducao.py

Versão comsolução:

python deadlock_solucao.py

## Resultados:

Versão com trava:

Durante a execução, cada thread adquire um Lock diferente e tenta adquirir o segundo. Como os recursos estão sendo utilizados uma pela outra, as duas ficam bloqueadas. Após o tempo limite, o programa identifica e exibe a mensagem de deadlock detectado.



Versão com solução:

Na segunda versão, as duas threads seguem a mesma ordem de aquisição dos Locks. Assim, conseguem executar suas tarefas, liberar os recursos e finalizar sem deadlock.



## Conclusão

Dado o exercício, concluimos que a utilização de recursos compartilhados pode causar deadlock entre threads, se ocorrer impasse entre eles.

Na primeira versão, as threads ficaram bloqueadas porque cada uma segurava um recurso que a outra precisava. Na segunda, foi definido a ordem de aquisição dos Locks, eliminando a espera circular, consequentemente chegando a solução

Assim, conseguimos compreender melhor o funcionamento de threads, dos Locks e das condições necessárias para que um deadlock aconteça ou que seja evitado.

## fontes: 

https://github.com/concu-unahur/python-filosofos-deadlock/blob/master/deadlock.py (somente deadlock)
https://www.geeksforgeeks.org/operating-systems/introduction-of-deadlock-in-operating-system/
https://pt.wikipedia.org/wiki/Deadlock
https://www.ece.villanova.edu/~rperry/os/ostep/Chapters/32-threads-bugs.pdf