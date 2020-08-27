import json

with open(r"C:\Users\ManoKutty\PycharmProjects\APITesting\JSON\Book.json") as f:
    lo = json.load(f)
    for k in lo:
        print(k)
print(lo)
