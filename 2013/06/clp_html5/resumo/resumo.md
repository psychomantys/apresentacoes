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

Existe até uma palavra reservada para "alocar" uma variável, mas não existe nada similar para liberar a memoria daquela variável.

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

Por essas e outras características, **JS** pode declarar variáveis com escopo dinâmico.

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

O tipo Number suporta tanto os números inteiros quanto os números de ponto flutuante.

Ele é a implementação do padrão IEEE 754 de números de precisão de ponto flutuante de 64 bit. Todos os limites desse padrão valem para Number.

## Boolean

O tipo booleano tradicional, que pode apenas assumir 2 valores.

## String

Temos que as cadeias de caracteres são um tipo diferente de todos os outros e elas podem ser de tamanho dinâmico, e o seu tamanho máximo em **JS** não é especificado, dependendo exclusivamente da implementação da linguagem.

## Array


* Se usam colchetes para referenciar os itens
* Qualquer tipo é permitido ser subscrito
* Não se verificam os indexes do Array, se retorna undefined caso não tenha aquele elemento
* A alocação de memoria ocorre de forma dinâmica a partir do momento que você passa a referenciar uma célula que não existe
* A quantidade de itens permitido depende da implementação, ou seja, teoricamente ilimitada
* Os indexes podem ser de qualquer tipo
* São usados tanto matrizes dinâmicas no monte quanto dinâmicas na pilhas
* São oferecidas algumas operações dentro do espaço de nomes Array, como por exemplo concatenação


## Object

Um tipo primitivo da linguagem que representa todos os objetos em geral. O que diferencia entre um objeto e outro é exclusivamente o seu conteúdo, ou seja, em **JS** você não pode criar outros tipos por nome de tipo, mas apenas que se diferencie pelo conteúdo.

Se usa referencias amplamente qualificadas para acessar os membros dos Objeto.


<!---Cap 07-->

# Expressões e instruções de atribuição

Não existe sobrecarga de operadores que seja definido pelo usuário.

## Conversões de tipo

Como o tipo de "**Number**" representa tanto os números decimais quanto os de ponto flutuante, não existe problemas de precisão com operações com números, e normalmente todos os outros tipos são convertidos para string para resolver os outros operadores.

Isso causa uma perda segurança, mas aumenta a escritabilidade da linguagem, porque torna mais fácil de usar os tipos.


## Expressões, relacionais e booleanas

JavaScript usa os mesmo operadores da família "C/C++", com a adição de alguns operadores a mais, em especial **===** e **!==**, que são operadores que fazem também a checagem de tipo.

## Instruções de atribuição

É usado o operador "**=**" para fazer atribuições, como na família "C/C++".

Também é permitido a atribuição para alvos múltiplos e condicionais, na forma:

```JavaScript
x=y=42;
x=true?10:0;
```

Grande parte da sintaxe de operações de JS vem diretamente de "**C/C++**", que por sua vez herdou de outras linguagens.

## Atribuições de modo misto

É permitido as atribuições de modo misto, como existem poucos tipos, normalmente elas são fáceis de implementar e existem conversões de tipos implícitas para a todos os tipo, então a escritabilidade é muito beneficiada.

<!---Cap 08-->

# Estruturas de controle no nível de instrução


Em JavaScript, a sintaxe das instruções de controle são herdadas do "C/C++".

O mais notável da sintaxe, é o break que não funciona como normalmente o break funciona. O break ele tem a função da estrutura de outras linguagens chamada "goto". Apesar de facilitar a escrita dos programas, dificulta a legibilidade um pouco por 2 fatores, porque o comportamento é diferente do esperado, e porque estruturas "goto" normalmente tende a deixar o código mais difícil de ler e manter.


Como JS é uma linguagem multi-paradigma, ela também suporta um certo nível de programação funcional para iterar entre os elementos de suas estruturas também, o que torna muito mais fácil de escrever os programas, e no caso de JS, torna também muito fácil de se ler o programa. Um exemplo pode ser:

```JavaScript

function logArrayElements(element, index, array) {
console.log("a[" + index + "] = " + element);
}

[2, 5, 9].forEach(logArrayElements);
// Ou...
var arr=[2, 5, 9];
for (var i = 0; i < arr.length; i++){
console.log("arr["+i+"] = "+arr[i]);
}
```

<!---Cap 09-->

# Subprogramas

## Fundamentos de subprogramas em JavaScript

Como o paradigma funcional é suportado, a criação e manipulação de funções é uma tarefa feita de forma fácil, manipular funções é simples.

Existe muitos mecanismos para manipular e sobrescrever as funções, manipular e usar argumentos e outras características de chamadas de função.

Como JS usa também JSON para declarar objetos, manipular métodos também se torna uma tarefa mais fácil. Usar JSON é melhor também na hora de manipular os parâmetros que são passados, porque ao invés de manipular os métodos de forma nativa com as funções, você pode tratar os parâmetros como uma estrutura como qualquer outro, se tornando mais fácil de escrever e mais seguro também.


Como funções podem ser atribuídas a variáveis de forma quase transparente, chamar indiretamente uma função pode se tornar fácil tanto quanto ao invés de atribuir a variavel, você usa a sintaxe para chamar funções.


Não existem sobrecarga de operadores, mas a diferenciação de tipos dos parâmetros, pode ser usada para gerar comportamentos diferentes para tipos diferentes de argumentos. JS também utiliza "Duck Language" para fazer as funções genéricas, ou seja, contanto que a função tenha os mesmo métodos que essa função precise, ou seja existam aqueles métodos no objetos, a função ainda vai funcionar.


<!--- Cap 12-->

# Suporte a programação orientada a objetos

Existe o suporte a orientação a objetos baseado em protótipos em **JS**, que é implementado pelo tipo "Object".

Uma das vantagens que facilita a escrita, segurança e legibilidade também é o fato do **JS** suportar JSON para criar objetos.


<!--- http://www.w3schools.com/html/html5_intro.asphttp://www.w3schools.com/js/ -->





