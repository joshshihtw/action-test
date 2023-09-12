FROM python:3.8

# WORKDIR /usr/src/app

# # Bundle app source
# COPY . .

RUN mkdir /src
RUN pip3 install PyMysql
RUN pip3 install requests

COPY main.py /src

CMD [ "python3", "/src/main.py" ]
