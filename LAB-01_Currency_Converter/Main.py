#!/bin/env python

import Currency_Aggregator
import Currency_Converter
import Currency_Model
import Parser
import Scrapper

class Main:
    @staticmethod
    def run_program():
        Scrapper.Scrapper.scrap()
        currency = Parser.Parser.parse()
        chosen_currency = currency.choose_current()
        exchanged_money = Currency_Converter.Currency_Converter.convert(chosen_currency)
        print(f"Waluta bazowa to {chosen_currency[0]}")
        print(f"Waluta docelowa to {chosen_currency[1]}")
        print(f"Kwota {exchanged_money[0]} w walucie docelowej wynosi {exchanged_money[1]}")

if __name__ == "__main__":
    Main.run_program()
