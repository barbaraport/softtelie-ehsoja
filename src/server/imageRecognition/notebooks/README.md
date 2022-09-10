Utilize a versão 3.10 do Python

Crie um ambiente virtual dentro de notebooks (o nome pode ser qualquer um, mas o adicione ao gitignore caso não escolha modelTraining)
python -m venv modelTraining

Ative o ambiente virtual
.\modelTraining\Scripts\activate

Atualize o pip do ambiente virtual
python -m pip install --upgrade pip

Instale o jupyter notebook no ambiente virtual
pip install notebook

Inicialize o notebook
jupyter notebook

tensorboard --logdir=.
