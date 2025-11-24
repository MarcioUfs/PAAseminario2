# **Branch and Bound aplicado ao Problema da Mochila 0-1**

## *Projeto e Análise de Algoritmos – UFS*

---

# **1. Introdução**

O **problema da Mochila 0-1** (0-1 Knapsack) é um dos problemas clássicos em otimização combinatória e aparece com frequência em situações reais envolvendo seleção de recursos, alocação de itens, planejamento logístico e maximização de lucro. Sua formulação consiste em selecionar um conjunto de itens, cada um com valor e peso, de forma a **maximizar o valor total sem ultrapassar a capacidade** da mochila.

Apesar de simples de formular, o problema é **NP-Completo**, o que significa que não há algoritmo conhecido que o resolva eficientemente para todos os casos em tempo polinomial. Por isso, diversas técnicas são utilizadas para melhorar sua resolução prática, entre elas **Programação Dinâmica**, **algoritmos gulosos**, **métodos heurísticos** e, especialmente, o **Branch and Bound**, foco deste texto.

O **Branch and Bound** é uma técnica de busca sistemática baseada em árvore, que utiliza limites superiores (“bounds”) para eliminar partes inteiras da busca que não podem gerar soluções melhores do que as já conhecidas. Ele não transforma o problema em polinomial, mas **reduz drasticamente o número de nós explorados em muitos casos reais**, tornando-se uma abordagem altamente eficaz.

---

#  **2. Explicação da Técnica Branch and Bound**

###  **2.1 Estrutura geral da técnica**

O Branch and Bound funciona explorando uma **árvore de decisão**, onde cada nível representa uma escolha:

* **Incluir o item** no subconjunto;
* **Não incluir o item**.

Cada nó dessa árvore representa um estado parcial da solução. Para cada nó, são armazenadas informações essenciais:

* **level**: índice do item atual;
* **value**: valor acumulado até aquele ponto;
* **weight**: peso acumulado;
* **bound**: uma estimativa otimista (limite superior) do máximo valor possível a partir daquele nó.

A estratégia principal consiste em **expandir apenas os nós que ainda podem levar a uma solução melhor**, descartando (“podando”) os demais.

---

### **2.2 Uso de Bound Fracionário (limite superior)**

O coração do Branch and Bound está no cálculo do **bound**, que representa o maior valor possível que um caminho pode atingir — mesmo que usando soluções fracionárias.

Esse bound é calculado através da **mochila fracionária**, resolvida por um algoritmo guloso:

1. Ordena-se os itens pela razão **valor/peso**;
2. Insere-se itens inteiros enquanto couberem;
3. Quando não couber mais, insere-se **uma fração do próximo item**.

Essa solução não é válida para o problema 0-1, mas fornece um **limite superior realista e rápido**.
Se o bound de um nó é menor ou igual ao melhor valor já encontrado, ele é **descartado imediatamente**.

Isso evita explorar combinações inteiras que **não têm potencial** para superar a solução ótima parcial.

---

### **2.3 Expansão dos nós**

Para cada nó extraído da **priority queue** (fila de prioridade baseada no maior bound):

* Gera-se o **nó da esquerda** (item incluído);
* Gera-se o **nó da direita** (item excluído);
* Ambos são avaliados com o bound;
* Apenas aqueles com bound promissor são inseridos de volta na fila.

O uso de fila de prioridade transforma o Branch and Bound em uma **busca best-first**, sempre expandindo primeiro o nó com maior potencial estimado de valor.

---

### **2.4 Complexidade**

Embora o Branch and Bound seja eficiente na prática, a complexidade no pior caso ainda é:

> **O(2ⁿ)**

Isso ocorre quando o bound não consegue podar quase nada — ou seja, quando praticamente todas as combinações precisam ser exploradas.

Na prática, entretanto, com itens bem ordenados e um bound ajustado, o número real de nós visitados é muito inferior.

---

# **3. Usos Práticos do Branch and Bound com Mochila 0-1**

O algoritmo é amplamente utilizado em contextos onde decisões binárias precisam ser otimizadas sob restrições. Alguns exemplos:

---

### **3.1 Logística e Transporte**

* Escolha de cargas que devem ser transportadas em veículos limitados.
* Decidir quais produtos enviar para maximizar o lucro.

---

### **3.2 Planejamento de Recursos**

* Seleção de máquinas, ferramentas ou equipamentos com custos e benefícios.
* Útil em indústrias que precisam aproveitar ao máximo um orçamento limitado.

---

### **3.3 Finanças e Investimentos**

* Escolha de carteiras de investimento quando existe limitação de capital.
* Útil quando não é possível fracionar ativos (como imóveis).

---

### **3.4 Computação e Sistemas**

* Seleção de tarefas com diferentes custos computacionais.
* Decisões de alocação de memória.
* Organização de cargas de trabalho em clusters.

---

# **4. Conclusão**

O Branch and Bound é uma abordagem poderosa para resolver o problema da Mochila 0-1 de forma exata, explorando a árvore de estados de maneira inteligente e evitando soluções inviáveis. Ele se destaca por:

* Utilizar limites superiores para **podar** grande parte da árvore.
* Usar a solução fracionária como bound, garantindo eficiência prática.
* Priorizar nós promissores, acelerando a busca pelo ótimo.

Embora tenha custo exponencial no pior caso, é extremamente eficaz em muitas instâncias reais, sendo uma das técnicas fundamentais no estudo de **projeto e análise de algoritmos**.
