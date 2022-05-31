# READING FILE DATA

Este projecto foi criado como solução a extração de dados em arquivos e execução dos mesmos na base de dados.

Para esse exemplo foi utilizado como base de dados o **mysql**, escolha pessoal.

## Rodar o projecto

Para rodar o projecto precisas ter o ``docker`` e o ``docker-compose`` instalados na tua maquina, em seguida rodar
o seguinte comando.

Caso estiver a usar ubuntu, como é o meu caso, usa o seguinte comando

```bash
sudo docker-compose up --build
```

Caso estiver a usar o windows pode remover o prefixo sudo.

Esse comando já vai criar um banco de dados com o nome ``recicla``, e vai executar um dump com duas tabelas como exemplo,
de uma base de dados existente para o projecto.

### Assistir um video demostrando como a aplicação funciona.

O video está no root do projecto com o nome ``overview.mkv``

### Credenciais da base de dados

```bash
HOST=db
DB_NAME=recicla
DB_USER=root
DB_PASSWORD=12345
```

### Respostas da requisição

Caso a base de dados informada não existir a aplicação retorna a seguinte resposta:

```json
{
  "error": {
    "status": 404, // Status da requisição
    "msg": "Table not exists", // Informação da inexistência da tabela
    "unlink": "Remove extracted content to local file" // Informação da remoção dos dados no arquivo local
  }
}
```

Caso inserir os dados com sucesso, retorna a seguinte resposta

```json
{
  "success": {
    "status": 200, // Status da requisição
    "affected_rows": 0, // Quantas linhas foram inseridas na base de dados
    "total_records_from_file": 6, // Quantas linhas de dados tem o arquivo, excepto o header
    "unlink": "Remove extracted content to local file", // Informação da remoção dos dados no arquivo local
    "data": [...] // Os dados que foram inseridos
  }
}
```

E no terminal apresenta a normalização do dados em uma tabela., exemplo

```bash
reading | comprador       descricao                   preco_unitario    quantidade  endereco       fornecedor
reading | --------------  ------------------------  ----------------  ------------  -------------  ----------------------
reading | João Silva      R$10 off R$20 of food                   10             2  987 Fake St    Bob's Pizza
reading | Amy Pond        R$30 of awesome for R$10                10             5  456 Unreal Rd  Tom's Awesome Shop
reading | Marty McFly     R$20 Sneakers for R$5                    5             1  123 Fake St    Sneaker Store Emporium
reading | Snake Plissken  R$20 Sneakers for R$5                    5             4  123 Fake St    Sneaker Store Emporium
```

## Funcionalidades

- [x] Aceitar (via formulário) o upload de arquivos text, com dados separados por TAB. A primeira linha do arquivo tem o nome das colunas.
- [x] Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional.
- [x] Exibir todos os registros importados, bem como a receita bruta total dos registros contidos no arquivo enviado após o upload + parser.
- [x] A aplicação deve ser escrita obrigatoriamente em: Python 3.7+ utilizando qualquer framework de preferência.
- [x] Executar via Docker ou Docker Compose.
- [x] Utilizar apenas linguagens e bibliotecas livres ou gratuitas.
- [x] Ter testes automatizados.
- [x] Ter uma boa aparência e ser fácil de usar.