import requests


class CurrencyLayer():
    RATE_TOKEN = '44f2c2f7d9f6da932fad2af012f4a7d5'
    BASE_URL = 'http://apilayer.net/api/live?access_key={}&currencies={}&source={}&format=1'

    def get_rate_from_currencylayer(self, ccy_from='GBP', ccy_to='EUR'):
        return requests.get(self.BASE_URL.format(self.RATE_TOKEN, ccy_from, ccy_to))


