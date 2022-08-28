from python:3.10
copy src/ /src
workdir src
copy 'requirements.txt' 'requirements.txt'
run ["pip","install", "-r", "requirements.txt"]
cmd ["python", "main.py"]
