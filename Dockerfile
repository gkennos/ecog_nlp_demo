FROM python:3.11-slim

RUN pip install --no-cache-dir jupyterlab numpy pandas matplotlib

# Create a working directory
WORKDIR /home/jovyan
COPY . .

# Default command when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]