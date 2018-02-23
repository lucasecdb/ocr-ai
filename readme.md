# OCR - Projeto de IA 1 2017.2

Analisador de caracteres opticos (impressos).

## Instalar

* Python 3
* Pip
* VirtualEnv

Pra começar, é bom criar um ambiente virtual, pra as dependências desse projeto
não misturarem com a da maquina toda.

```bash
virtualenv -p python3 env
```

O comando acima cria um ambiente virtual numa pasta 'env', no mesmo diretório do projeto.
Ai, em seguida, é so ativar o ambiente e instalar as dependências.

```bash
source env/bin/activate
pip install -r requirements.txt
```

Baixa os dados que a gente vai usar como o conjunto de treinamento e de testes executando o script.

```bash
./download_data.sh
```

E pronto.
