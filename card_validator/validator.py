def get_issuer(number: str) -> str:
    number = "".join(number.split())
    card_number_length = len(number)
    startswith_masterCard = number.startswith('51') or number.startswith('52') or number.startswith('53')\
                            or number.startswith('54') or number.startswith('55')
    startswith_americanExpress = number.startswith('34') or number.startswith('35') or number.startswith('36')\
                                 or number.startswith('37')

    if number.startswith('4') and card_number_length == 16:
        return "Visa"

    if startswith_masterCard and card_number_length == 16:
        return "MasterCard"
    if startswith_americanExpress and card_number_length == 15:
        return "American Express"

get_issuer("4321 2132 9903 3321")