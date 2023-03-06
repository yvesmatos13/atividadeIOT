FROM registry.redhat.io/rhel9/python-39@sha256:ca20140a54051a5063b42a1a55fdca4261a07eca0aa470239b8a7b1fad51bee8

EXPOSE 443

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
