FROM python:3.7.14

COPY install_deps.py /app/script.py
WORKDIR /app
run echo $(python -V)
cmd ["python", "script.py"]
