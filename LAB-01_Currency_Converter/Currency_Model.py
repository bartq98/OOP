class Currency_Model():
    
    def __init__(self,
        currency_name,    # nazwa waluty
        converter,        # przelicznik
        ISO_Code,         # kod waluty ISO 4217
        avarage_exchange, # kurs średni
    ):
        self.currency_name = currency_name
        self.converter = converter
        self.ISO_Code = ISO_Code
        self.avarage_exchange = avarage_exchange

    @property
    def currency_name(self):
        return self.__currency_name

    @currency_name.setter
    def currency_name(self, name : str):
        self.__currency_name = name

    @property
    def converter(self):
        return float(self.__converter)

    @converter.setter
    def converter(self, amount : str):
        self.__converter = float(amount)

    @property
    def ISO_Code(self):
        return self.__ISO_Code

    @ISO_Code.setter
    def ISO_Code(self, code : str):
        self.__ISO_Code = code.upper()

    @property
    def avarage_exchange(self):
        return self.__avarange_exchange

    @avarage_exchange.setter
    def avarage_exchange(self, exchange : str):
        self.__avarange_exchange = float(exchange.replace(",", "."))

    def __str__(self):
        return f"{self.__currency_name} \nkod ISO 4217 : {self.__ISO_Code} \nprzelicznik {self.__converter} po kursie {self.__avarange_exchange}"
