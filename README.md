simples-nacional - API desenvolvida para entregar a automação do site Simples Nacional.
=====================================================


Iniciando o projeto:
------------------
Executando diretamente no Docker.
```bash
 docker-compose up -d
```

Variáveis de ambiente:
-----------------------
        - SIMPLES_URL: "url do site"
        - CONTAINER_SELENIUM: "http://127.0.0.1:4444/wd/hub"
        - DOCKER_EXECUTION: 1
        - CAPTCHA_USER: "usercliente" caso não possuir token
        - CAPTCHA_PASS: "senhacliente" caso não possuir toke
        - CAPTCHA_TOKEN: "TOKEN" Se tiver token igonar pass e user acima.
        - PYTHONDONTWRITEBYTECODE: 1
        - APP_ENV:"prod"
          Enviromment type (dev, prod, test)

Instalar 
---------
```bash
pip install pipenv 
```
---------
```bash
pipenv install 
```

Iniciar seriviço:
```bash
   uvicorn asgi:app
``` 

Iniciar seriviço com mais workers, em caso de muita demanda. **Obs:** No Docker deve ser visto a config:
```bash 
   uvicorn asgi:app --workers 4 
``` 

Swagger API:
--------------
http://localhost:8000/docs


ReDoc API:
--------------
http://localhost:8000/redoc

Utilizando via REST:
--------------------

- Criar chave: POST http://localhost:8000/api/simples-nc/opcoes/criar-chave-acesso
```json
{
    "cnpj":"xxxxxxxxxxxxxx",
    "cpf": "xxxxxxxxxxx",
    "recibo_irpf": "xxxxxxxxxxxx",
    "data_recibo": "2021"
}
```
Retorno
```json
{
    "dados": {
        "cnpj": "xxxxxxxxxxxxxx",
        "cpf": "xxxxxxxxxxx",
        "titulo_eleitoral": null,
        "data_nascimento": null,
        "recibo_irpf": "xxxxxxxxxxxx",
        "data_recibo": "2021"
    },
    "status": true,
    "chave": "xxxxxxxxxxxx",
    "msg": null
}
```

- Enquadrar: POST http://localhost:8000/api/simples-nc/opcoes/enquadrar
```json
{
    "cnpj":"xxxxxxxxxxxxxx",
    "cpf": "xxxxxxxxxxx",
    "chave": "xxxxxxxxxxxx",
    "data_cnpj": "ddmmyyyy"
}
```
Retorno
```json
{
    "dados": {
        "cnpj": "xxxxxxxxxxxxxx",
        "cpf": "xxxxxxxxxxx",
        "chave": "xxxxxxxxxxxx",
        "data_cnpj": "ddmmyyyy"
    },
    "status": true,
    "data_resultado": "dd/mm/yyyy",
    "msg": null
}
```