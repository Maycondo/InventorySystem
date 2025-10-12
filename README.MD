
# Inventory-Syste

O __Inventory-System__ tem como objetivo principal servir de projeto acadêmico para consolidar conhecimentos em __banco de dados (SQL)__, criando familiaridade com a linguagem e, principalmente, com sua sintaxe.

O projeto consiste em um __CRUD__ (Create, Read, Update, Delete) para cadastrar, alterar e excluir produtos, utilizando a linguagem __Python__ com __Programação Orientada a Objetos (POO)__ integrada ao SQL.

## Python 🐍</>

Escolhi utilizar __Python__ porque ainda não tenho familiaridade em conectar a linguagem a bancos de dados relacionais, como o __SQL__, que organiza os dados em estruturas de tabelas.

O desenvolvimento do projeto segue o paradigma da __Programação Orientada a Objetos (POO)__, aplicando uma classe chamada __Inventory__ para criar o modelo base do sistema.
Dentro dela, há o método de inicialização responsável por conectar o programa ao banco de dados, recebendo atributos de instância como host, user, password, entre outros.

O método __create_table__ verifica se a tabela já foi criada; caso contrário, ele a cria para inserir os dados necessários, como id, name, price e quantity.

O método __create_item__ é responsável por inserir um novo produto diretamente no banco de dados __SQL__. Esse método recebe atributos como item_name, price e quantity.

## 🙌 Agradecimentos

Todos os métodos adicionados ao projeto utilizam o comando __WITH__ e instruções __SQL__. Como se trata de um projeto simples, sua construção tem o intuito puramente acadêmico e de aprendizado.


## 🤝Contribuição

Contribuições são bem-vindas! Sinta-se à vontade.