"""
Responsible for exchange specified amount of money between two currency
"""

import Currency_Model

class Currency_Converter:

    @staticmethod
    def ask_for_amount():
        print(f"Podaj kwotę do przeliczenia:", end=" ")
        try:
            quantity = float(input())
        except ValueError as e:
            print(f"Wystąpił błąd: {e}")
            exit(1)
        return quantity

    @staticmethod
    def convert(currency: tuple):
        """Returns amount of money after exchange with 5 decimal places"""
        source_currency = currency[0]
        destination_currency = currency[1]
        quantity = Currency_Converter.ask_for_amount()
        return quantity, round((destination_currency.converter / source_currency.converter) * (source_currency.avarage_exchange / destination_currency.avarage_exchange) * quantity, 5)