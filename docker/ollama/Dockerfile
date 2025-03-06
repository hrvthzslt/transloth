FROM ollama/ollama:0.5.12

WORKDIR /root/ollama

COPY ./Modelfile.base Modelfile.base
RUN ollama serve & sleep 5 && ollama create basemodel -f Modelfile.base

COPY ./Modelfile.trans Modelfile.trans
RUN ollama serve & sleep 5 && ollama create trans -f Modelfile.trans
