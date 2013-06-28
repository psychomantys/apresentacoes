# Tópicos de CLP para **HTML5**

<!---Cap 05-->

# Nomes, Vinculações, Verificações de Tipos e Escopos

Com relação aos nomes em JavaScript(**JS**), temos que:

* Podemos ter nomes com qualquer tamanho em JS
* Ignora espaços em branco adicionais entre palavras
* Faz diferenciação entre maiúsculas e minúsculas
* As palavras especiais são reservadas

## Palavras reservada

A lista de palavras reservadas de JS:

|||||
|:---------------:|:----------------:|:---------------:|:---------------:|
|break|do|instanceof|typeof|
|case|else|new|var|
|catch|finally|return|void|
|continue|for|switch|while|
|debugger|function|this|with|
|default|if|throw|delete|
|in|try|

Como parte interessante, **JS** tem uma lista de palavras reservadas que não tem funcionalidade atual(a não ser por algumas implementações não padrão, como *const*), mas que são reservadas, para uso futuro.

Essa lista é:

|||||
|:---------------:|:----------------:|:---------------:|:---------------:|
|class|enum|extends|super|
|const|export|import||

Vale a pena mencionar também que existe uma modo restrito, que pode ser ativado assim:

```JavaScript
"use strict";
var v = "Hi!  I'm a strict mode script!";
```

ou:

```JavaScript
function strict(){
  // Function-level strict mode syntax
  'use strict';
  function nested() { return "And so am I!"; }
  return "Hi!  I'm a strict mode function!  " + nested();
}
function notStrict() { return "I'm not strict."; }

```

O Objetivo do modo restrito é fazer um ambiente mais restrito da linguagem, convertendo erros que normalmente o JS deixaria passar em erro fatais, além de ter mais a portabilidade em foco nesse modo.

No modo restrito, as seguintes palavras também são reservadas:

||||||
|:----------:|:-----------:|:----------:|:----------:|:----------:|
|implements|let| private|public|interface|
|package|protected|static|yield|

Existem mais algumas palavras, mas essas são as principais do padrão mais novo, o **ECMAScript 5**.

## Variáveis

### Nomes das variáveis

Os nomes das variáveis de **JavaScript**, obedecem as seguintes regras:

* Devem começar com letras
* Podem começar também com $ ou _
* Os caracteres subsequentes devem ser letras, números ou _
* Existe distinção entre maiúsculas e minúsculas


### Endereço

**JS** suporta duas variáveis com nomes iguais em um conceito chamado "Anonymous Closures":

```JavaScript
(function () {
var a=myapp.load();
}());


(function () {
var a=myapp2.init();
}());
```

#### Apelidos

**JS** suporta apelidos, sendo através deles que para objetos são passados por padrão para funções, e tipo primitivos não, por exemplo:

```JavaScript
function change_a(a){
a.a=1;
};

var x={a:4};
console.log(x); // 4
change_a(x);
console.log(x); // 1
```

Existem também outras formas para explicitamente dizer que parâmetros são também apelidos para tipos básicos.

### Tipos

Em **JS**, existem apenas os seguintes tipos:

* String
* Number
* Boolean
* Array
* Object
* Null
* Undefined

## O conceito de vinculação

Em **JS**, a vinculação das variáveis foi feito em tempo de projeto da linguagem, porque ela tem muitos poucos tipos e não tem sobrecarga de operadores.

Como não existe sobrecarga de operadores, mas **JS** pode aceitar diferentes tipos em operadores, essa a decisão de que operação realizar é normalmente feita em tempo de execução, se resumindo a se converte tudo para *string* e concatena, ou se soma dois números.

### Vinculação quanto a atributos a variáveis

**JS** tem uma vinculação dinâmica de atributos a variáveis. Durante a execução, essa atribuição pode mudar, como por exemplo:

```JavaScript
var a=1;
var a="42!!!"
```

### Vinculação quanto a tipos

**JS** usa a vinculação dinâmica de tipos. Como todas as variáveis são declaradas com a palavra reservada **var**, essas variáveis são por padrão do tipo **Undefined**, mas quando você associa um valor, a variável se torna do tipo daquele valor.

Também se pode criar variáveis sem a palavra chave **var**, apenas atribuindo um valor para uma variável não declarada antes.

## Vinculação de Armazenamento e Tempo de vida

### Variáveis estáticas

JS não tem faz uso de variáveis estáticas, apesar de existirem formas que simulem bem.

### Variáveis dinâmicas na pilha

JS existe as variáveis dinâmicas em pilha, mas em alguns casos elas podem se comportar de forma diferente



### Variáveis dinâmicas no monte Explicitas

Existe até uma palavra reservada para "alocar" uma variavel, mas não existe nada similar para liberar a memoria daquela variável.

Então, não existe variáveis dinâmicas no monte explicitas em JS.

### Variáveis dinâmicas no monte Implícitas

JS faz uso intensivo de Variáveis dinâmicas no monte Implícitas.

Como quando você usa "Anonymous Closures", que permite que endereços e
 nomes de variáveis existam apenas naquele contexto, com por exemplo:

```JavaScript
var uniqueID = (function() {
  var id = 0;
  return function() { return id++; };
})();
```

O nome de "id" não vai existir fora desse contexto, mas o tempo de vida ainda continua valendo porque não chegou a *desalocação* de "id".



## Verificação de Tipos

Como existem poucos tipos básicos e devido a sua vinculação dinâmica de tipos, **JavaScript** tem poucas possibilidades para verificação de tipo, e costuma ser bem generosa nas variedades de conversões entre tipos, além de avaliar os tipos em tempo de execução.

Em operações numéricas, por exemplo, string são avaliadas como operadores se seu conteúdo for uma cadeia de caracteres que represente números, como por exemplo:

```JavaScript
var a=1*"5";
```

Mas devido a essa quantidade de conversões e possibilidades, pode ficar menos segura a linguagem, pode gerar ambiguidades e quebra de ortogonalidade, como no caso:

```JavaScript
var a="4"+2;
```

## Tipificação forte

Devido a sua tolerante política de conversões entre tipo, e ao tipo Object ser bem genérico, JavaScript é considerado uma linguagem fracamente tipificada.

## Compatibilidade de tipos

JS usa compatibilidade de tipos por nome.

## Escopo

JavaScript tem variáveis globais, que podem ser criadas a qualquer momento a não ser que você esteja dentro de um "Anonymous Closures".

Não se pode também aninhar sub-programas dentro de outras definições de subprogramas, mas sempre se pode criar variáveis globais ou redefinir variáveis globais.

Com "Anonymous Closures", também temos a possibilidade de criar o conceito de módulos que tem nomes e endereços de memoria auto-contidos.

Por essas e outras caracteristicas, **JS** pode declarar variáveis com escopo dinâmico.

## Constantes Numeradas

**JS** não tem suporte a constantes nomeadas.

Apesar do padrão **ECMAScript 5** reservar para o futuro a palavra **const**, o comportamento dessa palavra ainda não esta definido.

No máximo, existem muitas implementações que tem seu próprio **const** implementado, que faz normalmente a mesma coisa.

## Inicialização de Variáveis

Como em **JS** temos que a vinculação ao armazenamento de forma dinâmica, a inicialização de variáveis também são dinâmicas, com exceção a algumas variáveis que são inicializadas no inicio do programa, que fazem parte do padrão como biblioteca para fornecer funcionalidades, como por exemplo o objeto **Math**.

Como podemos declarar uma variável sem inicializar ela, por padrão essa variável não será vazia(Ou seja, do tipo **Null** com o único valor que uma variável desse tipo pode ter, que é "**null**"), mas sim será do tipo **Undefined** e conterá o único valor que uma variável desse tipo pode ter, que é "**undefined**"








<!---Cap 06-->

# Tipos de dados

## Number

O tipo Number suporta tanto os numeros inteiros quanto os numeros de ponto flutuante.

Ele é a implementação do padrão IEEE 754 de números de precisão de ponto flutuante de 64 bit. Todos os limites desse padrão valem para Number.

## Boolean

O tipo booleano tradicional, que pode apenas assumir 2 valores.

## String

Temos que as cadeias de caracteres são um tipo diferente de todos os outros e elas podem ser de tamanho dinamico, e o seu tamanho maximo em **JS** não é especificado, dependendo exclusivamente da implementação da linguagem.

## Array

* Qualquer tipo é permitido ser subscrito
* Não se verificam os indexes do Array, se retorna undefined caso não tenha aquele elemento










* Object
* Null
* Undefined


## Tipos de dados primitivos 213



* Tipos Cadeia de Caracteres 216
* Tipos Ordinais definidos pelo usuário 221
* Tipos de Matriz 225
* Matrizes Associativas 237
* Tipos Registro 238
* Tipos União 243
* Tipos de conjunto 248
* Tipos ponteiro

<!---Cap 07-->

Expressões e instruções de atribuição
=====================================================================

* Expressões aritméticas 269
* Operadores Sobrecarregados 276
* Conversões de tipo 278
* Expressões, relacionais e booleanas 281
* Avaliação curto-circuito 283
* instruções de atribuição 284
* Atribuições de modo misto

<!---Cap 08-->

Estruturas de controle no nível de instrução
=====================================================================

* Instruções compostas 295
* Instruções de seleção 296
* instruções iterativas 306
* Desvio Incondicional 318
* Comandos Protegidos 320

<!---Cap 09-->

Subprogramas
=====================================================================

* Fundamentals of Subprograms 388
* Design Issues for Subprograms 396
* Local Referencing Environments 397
* Parameter-Passing Methods 399
* Parameters That Are Subprograms 417
* Calling Subprograms Indirectly 419
* Overloaded Subprograms 421
* Generic Subprograms 422
* Design Issues for Functions 428
* User-Defined Overloaded Operators 430
* Closures 430
* Coroutines 432

<!---Cap 12-->

Suporte a programação orientada a objetos 523
=====================================================================


<!---
http://www.w3schools.com/html/html5_intro.asp
http://www.w3schools.com/js/
-->


