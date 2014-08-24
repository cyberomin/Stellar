import requests
import json

class Stellar:

    url = "https://test.stellar.org:9002"

    def make_payment(self):
        data = {
                "method": "submit",
                "params": [
                    {
                        "secret": "sfwtwgV3zHekZMm6F2cNPzEGzogQqPMEZcdVftKnrstngZvotYr",
                        "tx_json": {
                            "TransactionType": "Payment",
                            "Account": "gM4Fpv2QuHY4knJsQyYGKEHFGw3eMBwc1U",
                            "Destination": "g4eRqgZfzfj3132y17iaf2fp6HQj1gofjt",
                            "Amount": {
                                "currency": "USD",
                                "value": "2",
                                "issuer": "gBAde4mkDijZatAdNhBzCsuC7GP4MzhA3B"
                            }
                        }
                     }
                ]
            }
        data = json.dumps(data)
        r = requests.post(self.url,data)
        return r.json()


s = Stellar()
print s.make_payment()
