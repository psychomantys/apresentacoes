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

Como parte interessante, JS tem uma lista de palavras reservadas que não tem funcionalidade atual(a não ser por algumas implementações não-padrão, como const), mas que são reservadas, para uso futuro.

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
|:---------------:|:----------------:|:---------------:|:---------------:|
|implements|let| private|public|interface|
|package|protected|static|yield|


## Variáveis

### Nomes das variáveis

Os nomes das variáveis de JavaScript, obedecem as seguintes regras:

* Devem começar com letras
* Podem começar também com $ ou _
* Os caracteres subsequentes devem ser letras, números ou _
* Existe distinção entre maiúsculas e minúsculas


### Endereço

JS suporta duas variáveis com nomes iguais em um conceito chamado "Anonymous Closures":

```JavaScript
(function () {
var a=myapp.load();
}());


(function () {
var a=myapp2.init();
}());
```

#### Apelidos

JS suporta apelidos, sendo através deles que para objetos são passados por padrão para funções, e tipo primitivos não, por exemplo:

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

Em JS, existem apenas os seguintes tipos:
* String
* Number
* Boolean
* Array
* Object
* Null
* Undefined

## O conceito de vinculação

Em JS, a vinculação das variáveis foi feito em tempo de projeto da linguagem, porque ela tem muitos poucos tipos e não tem sobrecarga de operadores.

Como não existe sobrecarga de operadores, mas JS pode aceitar diferentes tipos em operadores, essa a decisão de que operação realizar é normalmente feita em tempo de execução, se resumindo a se converte tudo para string e concatena, ou se soma dois números.

### Vinculação quanto a atributos a variáveis

JS tem uma vinculação dinâmica de atributos a variáveis. Durante a execução, essa atribuição pode mudar, como por exemplo:

```JavaScript
var a=1;
var a="42!!!"
```

### Vinculação quanto a tipos

JS usa a vinculação dinâmica de tipos. Como todas as variáveis são declaradas com a palavra reservada **var**, essas variáveis são por padrão do tipo **Undefined**, mas quando você associa um valor, a variavel se torna do tipo daquele valor.



* Verificações de tipos 189
* Tipificação forte 189
* Compatibilidade de tipos 191
* Escopo 193
* Escopo e tempo de vida 200
* Ambientes de referenciamento 201
* Constantes Nomeadas 203
* Inicialização de Variáveis 204

<!---Cap 06-->

Tipos de dados
=====================================================================

* Tipos de dados primitivos 213
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

