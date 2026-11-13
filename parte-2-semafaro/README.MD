# Parte 2: Threads e Semáforos

Feito Por: Pedro Henrique J Colantonio

## Descrição do problema

O desafio envolve 8 threads tentando atualizar o mesmo contador simultaneamente.
Como cada uma precisa fazer 200.000 incrementos, o resultado final deveria ser exatamente 1.600.000.
O problema é que sem um mecanismo de sincronização, essas threads acabam acessando a variável ao mesmo tempo. 
Nisso, uma lê o valor antes que a outra termine de atualizar, o que faz com que várias somas se percam no meio do caminho e o total dê errado.
O objetivo é demonstrar esse problema e depois corrigi-lo utilizando um semáforo.

## Versão sem sincronização

Na primeira versão, criamos 8 threads que tentam aumentar o mesmo contador sem nenhum controle.
Cada thread lê o valor atual do contador, soma 1 e salva o novo valor.
Utilizamos `time.sleep(0)` entre a leitura e a atualização para permitir que outras threads executem nesse intervalo.
Com isso, algumas threads acabam lendo o mesmo valor e sobrescrevendo as alterações umas das outras. Esse problema é chamado de **condição de corrida**.

## Versão com semáforo

Na segunda versão, utilizamos `threading.Semaphore(1)` para controlar o acesso ao contador.
O semáforo foi criado com apenas uma permissão, permitindo que somente uma thread por vez altere o contador.
Antes de acessar o contador, a thread utiliza `acquire()` para adquirir a permissão. Depois de realizar o incremento, utiliza `release()` para liberar a permissão.
Também utilizamos `try` e `finally` para garantir que o semáforo seja liberado mesmo se acontecer algum erro.
Dessa forma, evitamos que duas threads alterem o contador ao mesmo tempo, garantindo o resultado esperado.

## Progresso e justiça

Na versão sem sincronização, todas as threads conseguem executar, mas alguns incrementos são perdidos.
Na versão com semáforo, as threads precisam esperar sua vez para acessar o contador.
Porém, o `threading.Semaphore` do Python não garante que as threads sejam atendidas na ordem em que chegaram. Isso significa que uma thread pode esperar mais tempo que outra.

## Desempenho e throughput

O throughput representa a quantidade de operações realizadas em determinado tempo.
Nos testes, a versão sem semáforo terminou mais rápido, mas apresentou resultados incorretos.
Já a versão com semáforo demorou mais, pois as threads precisaram esperar para acessar o contador.
O tempo médio da versão sem sincronização foi de aproximadamente **5,48 segundos**, enquanto a versão com semáforo teve média de **7,94 segundos**.
Além disso, utilizamos `time.sleep(0)` nas duas versões, o que influencia o tempo de execução. Por isso, essa comparação não mede diretamente a quantidade de incrementos corretos por segundo.

## Visibilidade e ordenação

A visibilidade está relacionada à forma como uma alteração feita por uma thread pode ser observada pelas outras. A ordenação está relacionada à sequência em que as operações acontecem.
Na versão sem sincronização, uma thread pode ler um valor e depois sobrescrever uma atualização feita por outra.
Na versão com semáforo, a aquisição e a liberação coordenam o acesso ao contador, evitando que outra thread entre na seção crítica antes da primeira terminar.
O Python também possui o GIL no CPython tradicional, mas ele não substitui o semáforo e não impede todas as condições de corrida.

## Protocolo utilizado

**Versão sem sincronização:**

1. O programa cria 8 threads.
2. Cada thread começa a incrementar o contador.
3. A thread lê o valor atual.
4. O `time.sleep(0)` permite que outra thread execute.
5. A thread soma 1 ao valor que leu.
6. Alguns incrementos acabam sendo perdidos.
7. O programa mostra o resultado e o tempo de execução.

**Versão com semáforo:**

1. O programa cria 8 threads.
2. Cada thread tenta adquirir o semáforo.
3. Se o semáforo estiver ocupado, a thread espera.
4. Quando consegue a permissão, lê e aumenta o contador.
5. Libera o semáforo para outra thread.
6. O processo continua até todas terminarem.
7. O programa mostra o resultado e o tempo de execução.

## Como executar

O projeto foi desenvolvido em Python, utilizando as bibliotecas `threading` e `time`.
É necessário ter o Python 3 instalado. Não é preciso instalar outras bibliotecas nem compilar o código.
Para executar, abra o terminal na pasta do projeto e de **cd "parte 2 semafaro"**.

**Versão sem sincronização:**

```bash
python contador_sem_sincronizacao.py
```

**Versão com semáforo:**

```bash
python contador_com_semaforo.py
```

Cada programa realiza 3 execuções e mostra o valor esperado, o valor obtido e o tempo gasto.

## Resultados

**Versão sem sincronização:**

(logs/Sem-Semafaro.png)

Na primeira versão, nenhuma das execuções chegou ao valor esperado. Isso aconteceu porque várias threads acessaram o contador sem sincronização, fazendo com que incrementos fossem perdidos.

**Versão com semáforo:**

(logs/Com-Semafaro.png)

Na segunda versão, todas as execuções chegaram ao valor esperado de 1.600.000. Isso mostra que o semáforo conseguiu controlar o acesso ao contador e evitar a perda de incrementos.

## Conclusão

Com a atividade, conseguimos observar como várias threads acessando a mesma variável podem causar uma condição de corrida.
Na primeira versão, os incrementos foram perdidos porque não existia nenhum controle de acesso ao contador.
Na segunda versão, utilizamos um semáforo binário para permitir que apenas uma thread por vez modificasse o valor.
Assim, conseguimos entender melhor o funcionamento das threads, dos semáforos e a importância da sincronização, mesmo que ela aumente o tempo de execução.
