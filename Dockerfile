FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a working directory
WORKDIR /home/jovyan
COPY . .

# Expose port Binder expects
EXPOSE 8888

# Run Jupyter when the container starts
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]