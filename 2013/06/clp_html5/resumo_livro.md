
Resumo do livro do Sebesta sobre linguagens de programação. Feito em forma de perguntas, alguns coisas ainda podem não estar terminadas, e nem todos os capítulos estão ai, mas o que está e bastante útil ;).

# Capitulo 7

## **O que são expressões aritméticas em linguagens de programação?**

Expressões aritméticas consistem em operadores, parêntesis e chamadas de função, que tem como objetivo computar uma expressão matemática.

## **Qual a função da precedência e da associatividade de operadores?**

Ditar a ordem na qual os operadores serão avaliados.

## **O que é precedência de um operador?**

Define a ordem na qual diferentes operadores com leveis de precedência diferentes serão avaliados.

## **O que é associatividade de um operador?**

Define a ordem no qual operadores adjacentes(separados por um único operando) com a mesma precedência serão avaliados.

## **O que é a associatividade da esquerda para a direita?**

Dado:
```
a-b+c;
```
**b+c** será resolvido primeiro.

## **O que é a associatividade da direita para a esquerda?**

Dado:
```
a-b+c;
```
a-b será resolvido primeiro.

## **O que é efeito colateral de uma função?**

Ocorre quando uma função muda um de seus parâmetros ou uma variável global(variáveis estáticas são globais).

## **Quais são as duas possíveis soluções para os efeitos colaterais de funções?**

Primeiro, desabilitar a avaliação de funções em expressões.

Segundo, garantir a ordem de avaliação das funções.

## **Quando um programa tem a propriedade de transparência referencial?**

Quando qualquer 2 expressões no programa tem o mesmo valor pode ser substituída por outra em qualquer canto do programa, sem afetar as ações do programa.

## **Quais são as vantagens da  transparência referencial para o programa?**

A semântica do programa é muito mais simples de entender, aumentando a legibilidade.

## **O que é a sobrecarga de operadores?**

É quando um operador pode ser usado para fazer operações em mais de um tipo.

## **Qual seria as desvantagens da sobrecarga de operadores?**

Sobrecarga de operadores pode gerar diminuição da legibilidade, principalmente se for usado o mesmo operador para 2 operações completamente diferentes.

Sobrecarga de operadores pode gerar perda de segurança, quando o programador confundir os operandos ou operadores e usar a expressão com outro sentido.

## **Qual seria as vantagens da sobrecarga de operadores?**

Aumento da escritabilidade, porque o programador vai ter mais poder expressivo por causa que pode ter mais operadores disponíveis.

Sobrecarga de operadores pode gerar aumento da legibilidade, quando bem utilizado é mais fácil associar um operador a uma função especifica do que uma função, por exemplo.

## **O que é coerção?**

É uma conversão implícita de tipo que é feita pelo compilador.

## **Quais são os 2 tipos de conversões?**

Conversão por estreitamento e por alargamento.

## **O que é a conversão por estreitamento?**

É converter um valor para um tipo que não pode nem mesmo armazenar aproximações do tipo original.

## **O que é a conversão por alargamento?**

Converte um valor para um tipo que pode pelo menos armazenar aproximações de todos os valores do tipo original.

Normalmente, existe perda de precisão.

## **O que são expressões de modo misto?**

São expressões que aceitam operandos de tipos diferentes, através de coerções implícitas.

## **O que é o *overflow?* **

É o erro quando o resultado de uma operação não pode ser representado na célula de memoria que ele esta armazenado, se ele for muito grande.

## **O que é o *underflow?* **

É o erro quando o resultado de uma operação não pode ser representado na célula de memoria que ele esta armazenado, se ele for muito pequeno.

## **O que são expressões relacionais?**

São operações que são comparados os 2 operandos e o resultado é um booleano, a não ser quando a linguagem não tem booleano como tipo nativo.

## **O que são expressões booleanas?**

São expressões que aceitam como operandos variáveis ou constantes booleanas, expressões booleanas ou operadores booleanos. O resultado é um booleano, a não ser quando a linguagem não tem booleano como tipo nativo.

## **O que a avaliação em curto-circuito?**

É quando o resultado de uma expressão é determinado ser avaliado toda a expressão.

## **O que é uma atribuição composta?**

É uma atribuição da seguinte forma, como exemplo:

a+=10;

que é equivalente:

a=a+10;

# Capitulo 8

## **O que são instruções de controle?**

São mecanismos linguísticos da linguagem para decidir entre fluxos de execução diferentes, ou  repetir um conjunto de instruções.

## **Segundo Bohm e Jacopini, qual são as únicas duas instruções de controle básicas necessárias?**

Uma para escolher entre 2 fluxos de execução, e outra para iterações controladas por expressões lógicas.

## **Porque não se é usado somente as 2 instruções básicas na maioria das linguagens?**

Para que a escritabilidade e a legibilidade não sejam prejudicadas.

## **O que é uma estrutura de controle?**

É a instrução de controle e as instruções que essa instrução de controle controla.

## **O que são instruções de seleção?**

São instruções que permitem escolher entre 2 ou mais caminhos de execução no programa.

## **O que são instruções de seleção de 2 caminhos?**

É uma instrução na seguinte forma:
```
if expressão_de_controle
then clausula
else clausula
```
Com as seguintes considerações:

* Qual é a forma e o tipo da **expressão_de_controle**?
* Como o ***then*** e o ***else*** são especificados?
* Como ficam os seletores aninhados?

# Parou 350.....


# Capitulo 9

## **Quais são as características gerais dos subprogramas?**

* Cada subprograma tem apenas um único ponto de entrada
* O programa chamador é suspendido durante a execução do subprograma, so existindo 1 subprograma em execução ao mesmo tempo
* O controle de execução sempre retorna ao chamador quando termina a execução do subprograma

A exceções são corrotinas e unidade de execução concorrentes.

## **Qual é a definição de um subprograma?**

Define a interface e as ações que o subprograma abstrai.

## **O que é a chamada de um subprograma?**

É uma requisição explicita para que um subprograma seja executado.

## **Quando um subprograma esta ativo?**

Quando um subprograma é chamado, e ele começou a executar mas ainda não completou a sua execução, esse subprograma é considerado ativo.

## **O que é o cabeçalho de um subprograma?**

Cabeçalho de um subprograma especifica que a próxima unidade sintática é a definição de um subprograma.

Se a definição do subprograma não for anônima, ele também prove o nome do subprograma.

## **O que é o perfil de parâmetros de um subprograma?**

É o numero, a ordem e tipos de seus parâmetros formais.

## **O que é o protocolo de um subprograma?**

É o perfil de parâmetros e, se for uma função, o seu tipo de retorno.

## **O que são os parâmetros formais de um subprograma?**

São os parâmetros em um cabeçalho de um subprograma.

## **O que são os parâmetros posicionais do subprograma?**

É a forma de passar parâmetros para um subprograma através da posição que cada parâmetro é passado. Ou seja, o primeiro parâmetro atual é associado ao primeiro parâmetro formal, e assim por diante.

## **O que são os parâmetros por palavra-chave no subprograma?**

É a forma de passar parâmetros associando um nome ao parâmetro.

## **Qual a diferencia entre funções e procedimentos?**

Funções retornam valores e procedimentos não.

## **O que é a sobrecarga de subprograma?**

É um subprograma pode ter o mesmo nome de outro em um mesmo ambiente de referenciamento. O que muda entre os subprogramas é o seu protocolo.

## **O que é um subprograma genérico?**

É um subprograma que a computação dele pode ser feita em dados de diferentes tipos em diferentes chamadas do subprograma.

## **Qual as vantagens e desvantagens de um subprograma ter variáveis locais na pilha?**

Existem varias vantagens, mas a principal é a flexibilidade que prove ao subprograma.

Outra vantagem é a economia de espaço, porque o espaço para criar variáveis é compartilhado entre os subprogramas ativos e os inativos.

Como desvantagem podemos citar que existe uma perda de desempenho porque toda vez que o subprograma é chamado, tem um tempo para reservar e inicializar, se preciso, aquelas variáveis.

## **O que são nested subprogramas?**

São subprogramas que podem ser referenciados somente em alguns contextos, escondendo eles do escopo global.

## **Quais sãos os modelos semânticos de passagem de parâmetros?**

* **Modo de entrada:** O subprograma pode receber dados do parâmetro correspondente.
* **Modo de saída:** O subprograma pode transmitir dados do parâmetro correspondente.
* **Modo de entrada-saída:** O subprograma pode fazer os 2 anteriores no parâmetro correspondente.


## **Quais são os 2 modelos conceituais de passagem de parâmetros?**

* O valor atual é copiado(para o chamador, para o chamado ou para ambos)
* Ou o caminho de acesso é transmitido, para o acesso direto.

## **Quais são os modelos de implementação da passagem de parâmetros?**

* **Passagem por valor:** O valor do parâmetro atual é usado para inicializar o parâmetro formal correspondente. O parâmetro formal age como uma variável local normal do subprograma.
* **Passagem por resultado:** Implementa um modo de saída. Quando o subprograma inicia, o parâmetro formal correspondente atua como uma variável local normal, mas quando o subprograma termina sua execução, o valor dessa variável é copiado para o parâmetro atual correspondente.
* **Passagem por valor-resultado:** Implementa o modo de entrada-saída. No começo do subprograma faz o modelo de por valor, e no final só subprograma faz o que o modelo por resultado faz.
* **Passagem por referencia:** Também é uma implementação do modelo de entrada-saída. Só que ao invés de copiar no final como o valor-resultado faz, ele transmite o caminho de acesso ao dado(usualmente o endereço), e altera diretamente durante a execução do subprograma.
* **Passagem por nome**: Implementa o modelo de entrada-saida. Ele literalmente substitui a ocorrência de uma variável com um determinado nome por outra do parâmetro no subprograma.

## **Quais sãs as desvantagens e vantagens dos modelos de implementação da passagem de parâmetros?**

??????

## **O que é checagem de tipos de parâmetros em subprogramas?**

É a checagem se os tipos dos parâmetros formais de um subprograma são iguais aos tipos dos parâmetros atuais quando um subprograma é chamado.

## **Qual as vantagens e desvantagens da checagem de tipos de parâmetros em subprogramas?**

?????? desnecessário agora, responder depois

## **O que é um closure?**

É um subprograma e o ambiente de referencia que ele esta definido. O ambiente de referencia é requerido se esse subprograma for chamado em qualquer parte do programa.

## **O que é uma co-rotina?**

É um tipo especial de subprograma que tem diversos pontos de entrada para execução, que são controlados pela própria co-rotina.

A co-rotina continua a sua execução do ponto depois em que ela foi suspensa.



