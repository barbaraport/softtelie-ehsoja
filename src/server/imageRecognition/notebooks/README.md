:warning: Utilize a versão <b>3.10</b> do Python :warning:

1. Crie um ambiente virtual dentro de <i>notebooks</i> (o nome pode ser qualquer um, mas o adicione ao <i>gitignore</i> caso não escolha <i>modelTraining</i>):
```python -m venv modelTraining```
2. Ative o ambiente virtual: ```.\modelTraining\Scripts\activate```
3. Atualize o <i>pip</i> do ambiente virtual: ```python -m pip install --upgrade pip```
4. Instale o <i>jupyter notebook</i> no ambiente virtual: ```pip install notebook```
5. Inicialize o notebook: ```jupyter notebook```
6. Execute-o completamente e somente após o seu término abra o TensorBoard
7. Para inicializar o TensorBoard, digite no terminal: ```tensorboard --logdir=.```
