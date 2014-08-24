import requests
import json

class Stellar:

    def __init__(self):
        self.url = "https://test.stellar.org:9002"

    """Method to make a payment."""
    def make_payment(self, account, destination, value, issuer, trans_type='Payment', currency='USD'):
        params = {
                "method": "submit",
                "params": [
                    {
                        "secret": "sfwtwgV3zHekZMm6F2cNPzEGzogQqPMEZcdVftKnrstngZvotYr",
                        "tx_json": {
                            "TransactionType": trans_type,
                            "Account": account,
                            "Destination": destination,
                            "Amount": {
                                "currency": currency,
                                "value": value,
                                "issuer": issuer
                            }
                        }
                     }
                ]
            }
        data = json.dumps(params)
        r = requests.post(self.url,data)
        return r.json()


s = Stellar()
print s.make_payment('gM4Fpv2QuHY4knJsQyYGKEHFGw3eMBwc1U', 'g4eRqgZfzfj3132y17iaf2fp6HQj1gofjt', 2, 'gBAde4mkDijZatAdNhBzCsuC7GP4MzhA3B')
