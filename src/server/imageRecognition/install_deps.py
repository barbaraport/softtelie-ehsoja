import os
try:
  os.system('''
  pip install mrcnn \
  pip install tensorflow==1.13.1 \
  pip install keras==2.2.5 \
  pip install h5py==2.10.0 \
  pip install matplotlib \
  pip install imgaug
  ''')
except:
  print('Deu ruim na instalação das deps')
  exit(1)

print('Deu bom na instalação das deps')