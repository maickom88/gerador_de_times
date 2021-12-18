# Caupe API 🧑‍💻
### Executar em ambiente de desenvolvimento

<img align="center" alt="Rafa-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"> Python
 - Version 3.8
 

#### Baixando as dependencias
- Abra o terminal e digite `pip install -r requirements.txt`
- Certifique-se que todas as dependencias foram instaladas corretamente
- Certifique-se que tenha o `.env`


### Migrations
As migrations são gerados e executadas pelo _alembic_
- Antes de realizar qualquer operação com o alembic, certifique-se que: 
    - Todos os arquivos de modelo foram importados no arquivo `alembic/env.py`;
    - Adicionar a string de conexão correta no arquivo `alembic/env.py`;
- Para gerar uma nova migration execute o comando: `alembic revision --autogenerate -m "v[NRO_VERSAO]"` 
- Para atualizar rodar as migrations e atualizar com a última versão execute o comando `alembic upgrade head`
- Para fazer um downgrade execute o comando `alembic downgread [revision]` 
  