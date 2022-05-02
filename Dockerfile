FROM python:2.7-slim
WORKDIR /webserver2
ADD . /webserver2
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install requests
RUN pip install psutil
CMD ["python", "webserver2.py"]
