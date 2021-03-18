""" 
Download XML file with currency table
"""

import urllib.request as req

class Scrapper():

    @staticmethod
    def scrap(URL : str = "https://www.nbp.pl/kursy/xml/lasta.xml"):
        """
        Downloads file from given URL to local folder
        (for this project URL link to avarage exchange rates by NBP)
        """
        try:
            req.urlretrieve(URL, "./currency_list.xml")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            exit(1)
