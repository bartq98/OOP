import Currency_Model

class Currency_Aggregator():

    def __init__(self):
        self.__currency = []

    def add_current(self, current: Currency_Model):
        self.__currency.append(current)

    def find_current_by_code(self, ISO_code: str):
        for current in self.__currency:
            if current.ISO_Code == ISO_code.upper():
                return current
        return None

    def choose_current(self):

        print(f"Podaj kod ISO waluty wejściowej:", end=" ")
        code_to_find = input()
        chosen_base_current = self.find_current_by_code(code_to_find)

        while chosen_base_current is None:
            print(f"Kod {code_to_find} nie istnieje w bazie!\nWybierz ponownie:", end=" ")
            code_to_find = input()
            chosen_base_current = self.find_current_by_code(code_to_find)

        print(f"Podaj kod ISO waluty docelowej:", end=" ")
        code_to_find = input()
        chosen_exchange_current = self.find_current_by_code(code_to_find)

        while chosen_exchange_current is None:
            print(f"Kod {code_to_find} nie istnieje w bazie!\nWybierz ponownie:", end=" ")
            code_to_find = input()
            chosen_exchange_current = self.find_current_by_code(code_to_find)

        return chosen_base_current, chosen_exchange_current

