"""
Parse given XML file to model
"""

import xml.etree.ElementTree as ET

import Currency_Aggregator
import Currency_Model


class Parser():

    @staticmethod
    def parse(file_path : str = "./currency_list.xml"):

        list_of_currencies = Currency_Aggregator.Currency_Aggregator()
        tree = ET.parse(file_path)
        root = tree.getroot()

        for country in root.findall("pozycja"):

            # assign XML data to proper variables
            name           = country.find("nazwa_waluty").text
            converter      = country.find("przelicznik").text
            code           = country.find("kod_waluty").text
            avarage_course = country.find("kurs_sredni").text

            list_of_currencies.add_current(
                Currency_Model.Currency_Model(
                    currency_name    = name,
                    converter        = converter,
                    ISO_Code         = code,
                    avarage_exchange = avarage_course
                )
            )

            # add explicit PLN
            list_of_currencies.add_current(
                Currency_Model.Currency_Model(
                    currency_name    = "złoty (Polska)",
                    converter        = "1",
                    ISO_Code         = "PLN",
                    avarage_exchange = "1"
                )
            )

        return list_of_currencies
