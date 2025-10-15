FROM python:3.11-slim

RUN pip install --no-cache-dir jupyterlab numpy pandas matplotlib

# Create a working directory
WORKDIR /home/jovyan
COPY . .

# Expose port Binder expects
EXPOSE 8888

# Run Jupyter when the container starts
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]