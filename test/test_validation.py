from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert get_issuer("4321 2132 9903 3321") == "Visa"
    assert not get_issuer("4323 3432 332 3") == "Visa"


def test_get_issuer_masterCard():
    assert get_issuer("5122 3212 4444 3333") == "MasterCard"
