from django.shortcuts import render_to_response

from celery import task
from decimal import Decimal
from rates.models import Currency, Rate
from rates.currencylayer import CurrencyLayer
import datetime


#--------------------------------------------------------------------------------------------------------------
#                                          NEW DEAL
#--------------------------------------------------------------------------------------------------------------

def new_deal(request):
    template = "rates/trades/new_deal.html"
    context = {}

    return render_to_response(template, context)


# @task
def create_rate(ccy_from=None, ccy_to=None, rate_value=Decimal('0'), last_rate=None):
    """
    Create a rate instance if there is no currency pair in database
    :param ccy_from: string (max_length=3)
    :param ccy_to: string (max_length=3)
    :param rate_value: Decimal
    :param last_rate: datetime
    :return:
    """
    rate = Rate()
    rate.ccy_from = Currency.objects.get(symbol=ccy_from)
    rate.ccy_to = Currency.objects.get(symbol=ccy_to)
    rate.rate = rate_value
    rate.last_rate = datetime.datetime.now()
    rate.save()

    return rate


def get_rate(ccy_from=None, ccy_to=None):
    """
    Get rate of a currency pair, if the rate do not exists in database we use CurrencyLayer API REST
    otherwise we use the stored rate in database.
    :param ccy_from: string (max_length=3)
    :param ccy_to: string (max_length=3)
    :return: Decimal (rate value)
    """
    if currencies_available(ccy_from, ccy_to):
        rate = Rate.objects.filter(ccy_from__symbol=ccy_from, ccy_to__symbol=ccy_to)
        if not rate.exists():
            ccy_pair = ccy_to + ccy_from
            try:
                cl = CurrencyLayer()
                cl_response = cl.get_rate_from_currencylayer(ccy_from, ccy_to)
                if cl_response.status_code == 200:
                    cl_response = cl_response.json()
                    rate_value = cl_response['quotes'][ccy_pair]

                    rate = create_rate.delay(ccy_from, ccy_to, rate_value, datetime.datetime.now())
                else:
                    raise Exception("There is no available connection with Currencylayer")
            except:
                raise Exception("There is no available rate for {} currency pair".format(ccy_pair))
    else:
        raise Exception("There is no available currencies for the chosen pair {}".format(ccy_to + ccy_from))

    return rate.rate


#--------------------------------------------------------------------------------------------------------------
#                                       AUXILIARY FUNCTIONS
#--------------------------------------------------------------------------------------------------------------

def currencies_available(ccy_from, ccy_to):
    return Currency.objects.filter(symbol=ccy_from).exists() and Currency.objects.filter(symbol=ccy_to).exists()