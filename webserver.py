from flask import Flask, request
import requests

app = Flask(__name__)

ipAdd1 = "10.0.1.30:8080"
ipAdd2 = "10.0.1.20:8080"

weightedroundRobin ="0"

@app.route('/')
def func1():
    response = loadBalancer()
    return str(response.content)
def loadBalancer():
    global weightedroundRobin
    ipAddressWebServer = ""
    if weightedroundRobin == "0":
        loadWebServer1 =float(requests.get("http://" + ipAdd1 + "/load").content)
        loadWebServer2 =float(requests.get("http://" + ipAdd2 + "/load").content)
        if loadWebServer1 > loadWebServer2:
            ipAddressWebServer = str(loadWebServer2)
        else:
            ipAddressWebServer = str(loadWebServer1)
    response = requests.get("http://" + ipAddressWebServer + "/load")
    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
