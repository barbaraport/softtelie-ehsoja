Crie um ambiente virtual dentro de notebooks

python -m venv modelTraining

Ative o ambiente virtual
.\modelTraining\Scripts\activate

Atualize o pip do ambiente virtual
python -m pip install --upgrade pip

Instale ipykernel
pip install ipykernel

Crie o usuário modelTraining para o kernel do notebook
python -m ipykernel install --user --name=modelTraining

Instale o jupyter notebook no ambiente virtual
pip install notebook

Inicialize o notebook
jupyter notebook

tensorboard --logdir=.