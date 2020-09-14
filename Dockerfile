FROM debian:jessie
RUN apt-get update && apt-get install -y \
    sudo \
    packaging-dev \
    pkg-config \
    libglib2.0-dev \
    giflib-dbg \
    check \
    build-essential \
    python-dev \
    automake  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN git clone --recursive https://github.com/leomrtns/tauari.git && \
    cd tauari && \
    pip install -r requirements.txt && \ 
    pip install . 
