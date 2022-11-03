FROM python:latest
WORKDIR /workspace

COPY ./requirements.txt /workspace
RUN pip install -r requirements.txt
RUN apt install git -y && git clone https://github.com/RyuunosukeDS3/quando_lula_assume.git

CMD python /workspace/main.py