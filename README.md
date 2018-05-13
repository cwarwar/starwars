# Star wars planets

Api em python + mongoDB com intuito de gerenciar os planetas do universo de star wars 

## Pré requisitos
Python 3  + pipenv (Opcional, caso não possua as dependências) + mongodb
O host do mongo está para localhost sem senha

## Rodando o projeto
python ./sw.py ou pipenv run ./sw.py


## Rodando os testes
Os testes ficam no diretório _tests na raiz do projeto, dentro do diretório execute o comando python "nomedoteste.py"


### Requests
O projeto rodará no seguinte endereço:
http://127.0.0.1:5002


/planets/getById/5af73ae1d6611a1e3c401a85D [GET]

/planets/getByName/teste7 [GET]

/planets/remove/5aeed967d6611a04e8371bfc [GET]

/planets/getAll/0/7 [GET]

/planets/store [POST]
Body
name: xxxx
weather: xxxx
terrain: xxx