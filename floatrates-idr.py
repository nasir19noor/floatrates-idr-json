import requests

response = requests.get("http://www.floatrates.com/daily/idr.json")
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.0535758529016e-5,"date":"Thu, 21 Oct 2021 23:55:01 GMT","inverseRate":14177.206297266},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.0612532342641e-5,"date":"Thu, 21 Oct 2021 23:55:01 GMT","inverseRate":16498.238257841}}

for data in json_data.values():
    print(data["code"])
    print(data["name"])
    print(data["inverseRate"])