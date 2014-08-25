import requests
import json

class Stellar:

    def __init__(self, mode="test"):
        """Constructor to set mode"""
        if mode == "test":
            self.url = "https://test.stellar.org:9002"
        else:
            self.url = "https://live.stellar.org:9002"

    def create_keys(self):
        params = {
            "method":"create_keys"
        }

        data = json.dumps(params)
        r = requests.post(self.url,data)
        return r.json()



    def make_payment(self, account, destination, value, issuer, trans_type='Payment', currency='USD'):
        """Method to make a payment."""
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

    def accept_payment(self):
        params = {}
        data = json.dumps(params)
        r = requests.post(self.url,data)
        return r.json()

    def account_info(self,account):
        params = {
            "method":"account_info",
            "params":[
                {
                    "account":account
                }
            ]
        }
        data = json.dumps(params)
        r = requests.post(self.url,data)
        return r.json()




#Sample data 'gM4Fpv2QuHY4knJsQyYGKEHFGw3eMBwc1U', 'g4eRqgZfzfj3132y17iaf2fp6HQj1gofjt', 2, 'gBAde4mkDijZatAdNhBzCsuC7GP4MzhA3B'
#Account g9SvjwimBbDvYhkJCd4UxTvTH7kwSRmhgc
s = Stellar("live")
print s.account_info("cyberomin")
