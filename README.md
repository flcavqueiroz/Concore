# Concore | API
## API para gerenciar Empresas e Funcionários

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Rode o servidor local do Django

```
cd concore
python3 -m venv .env
source .venv/bin/activate (windows: .env\Scripts\activate.bat)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
* Crie o usuário admin

```
python manage.py createsuperuser
```

