# Use a Python base image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3-pip \
    git \
    openssh-client \
    && apt-get clean
RUN sudo apt-get install poppler-utils
RUN pip install -U jupyterlab pandas matplotlib
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Copy the rest of the application code
COPY Datasplit .
COPY ResNet_50_Transfer_learning.ipynb .


# Expose the port the app runs on
EXPOSE 8888
EXPOSE 8501

# Start the application
# CMD ["streamlit", "run", "app.py"]
ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root","--no-browser"]