# Bot para atualização de status do concurso público

Aqui, o arquivo `main.py ` é o script principal. Ao rodar, ele verifica a data da sua 
última execução no arquivo `last_novelty`, obtém o conteúdo da página 
`https://conhecimento.fgv.br/concursos/bbts23`, cria uma lista com as `divs` de html 
que se iniciam com uma data válida no formato `%d/%m/%Y`, e à partir dele cria uma 
lista de tuplas de dois elementos (data da div, conteúdo da div) para os quais a data 
é igual ou mais recente que a data da última execução (obtida do arquivo 
`last_novelty`). Por fim, ele checa se há novidades e envia uma mensagem pelo Telegram.

## Módulos: 

Em datatools, há três módulos, cada um com uma função: 

- `extracao`: Contém uma função `novidade()`, que simplesmente pega a última linha de 
uma string (no caso, o conteúdo em texto das `div`s de interesse);

- `validata`: contém uma função `validar_data()`, que checa se uma string é um formato 
de data válido;

- `message`: contém uma função `send()` que envia uma mensagem para um usuário 
Telegram via bot.

## Como é executado: 

O programa procura, dentro da pasta scraping, por dois arquivos. Por questão de 
privacidade, os arquivos costam em `.gitignore`. São eles:

- `scraping/.chat_id`: contém o chat id de um usuário do Telegram;
- `scraping/.bot_token`: contém do token do bot que irá mandar a mensagem pelo Telegram.

O script `scraping/main.py` pode ser executado regularmente, por exemplo, por um cron 
job.
