FROM jupyter/minimal-notebook:python-3.11
USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends git build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt


WORKDIR /home/jovyan
COPY . .
EXPOSE 8888

# Start JupyterLab in Binder-friendly way
CMD ["start-notebook.sh", "--LabApp.token=''", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
