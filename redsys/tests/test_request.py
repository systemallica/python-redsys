from decimal import ROUND_HALF_UP
from decimal import Decimal as D
from random import choice

import pytest

from redsys.constants import EUR
from redsys.constants import STANDARD_PAYMENT
from redsys.request import Request


class TestRequest:
    def test_create_request(self):
        parameters = {
            "merchant_code": "100000001",
            "terminal": "1",
            "transaction_type": STANDARD_PAYMENT,
            "currency": EUR,
            "order": "000000000001",
            "amount": D("10.56489").quantize(D(".01"), ROUND_HALF_UP),
            "merchant_data": "test merchant data",
            "merchant_name": "Example Commerce",
            "titular": "Example Ltd.",
            "product_description": "Products of Example Commerce",
            "merchant_url": "https://example.com/redsys/response",
        }
        self.request = Request(parameters)
        assert self.request.product_description == "Products of Example Commerce"

    def test_bad_request_parameters(self):
        parameters = {
            "merchant_code": "100000001",
            "terminal": "1",
            "bad_key": "test",
        }
        with pytest.raises(ValueError, match="Unknown parameter"):
            self.request = Request(parameters)

    def test_prepare_parameters(self):
        parameters = {
            "merchant_code": "100000001",
            "terminal": "1",
            "transaction_type": STANDARD_PAYMENT,
            "currency": EUR,
            "order": "000000000001",
            "amount": D("10.56489").quantize(D(".01"), ROUND_HALF_UP),
            "merchant_data": "test merchant data",
            "merchant_name": "Example Commerce",
            "titular": "Example Ltd.",
            "product_description": "Products of Example Commerce",
            "merchant_url": "https://example.com/redsys/response",
        }
        prepared_parameters = Request(parameters).prepare_parameters()
        assert len(prepared_parameters.keys()) == 11
        assert prepared_parameters.get("Ds_Merchant_MerchantData") == "test merchant data"

    def test_super_long_merchant_data_throws_error(self):
        merchant_data = "".join(choice("abcdefghijklmnopqrtsuvwxyz-0123456789") for _ in range(1025))
        with pytest.raises(ValueError):
            assert Request.check_merchant_data(merchant_data)

    def test_super_long_merchant_url_throws_error(self):
        merchant_url = "".join(choice("abcdefghijklmnopqrtsuvwxyz-0123456789") for _ in range(251))
        with pytest.raises(ValueError):
            assert Request.check_merchant_url(merchant_url)

    def test_setattr(self):
        request = Request({
            "merchant_code": "100000001",
            "terminal": "1",
            "transaction_type": STANDARD_PAYMENT,
            "currency": EUR,
            "order": "000000000001",
            "amount": D("10.00"),
        })
        request.merchant_data = "new data"
        assert request.merchant_data == "new data"

    def test_check_order_invalid_format(self):
        with pytest.raises(ValueError, match="order format is not valid"):
            Request.check_order("invalid")

    def test_check_transaction_type_invalid(self):
        with pytest.raises(ValueError, match="transaction_type is not valid"):
            Request.check_transaction_type("X")

    def test_check_currency_invalid(self):
        with pytest.raises(ValueError, match="currency is not valid"):
            Request.check_currency(999)

    def test_check_amount_wrong_type(self):
        with pytest.raises(TypeError, match="amount must be defined as decimal.Decimal"):
            Request.check_amount("10.00")

    def test_check_sum_total_wrong_type(self):
        with pytest.raises(TypeError, match="sum_total must be defined as decimal.Decimal"):
            Request.check_sum_total("10.00")

    def test_check_merchant_cof_ini_invalid(self):
        with pytest.raises(ValueError, match="merchant_cof_ini is not valid"):
            Request.check_merchant_cof_ini("X")

    def test_check_merchant_cof_type_invalid(self):
        with pytest.raises(ValueError, match="merchant_cof_type is not valid"):
            Request.check_merchant_cof_type("X")

    def test_check_merchant_excep_sca_invalid(self):
        with pytest.raises(ValueError, match="merchant_excep_sca is not valid"):
            Request.check_merchant_excep_sca("X")

    def test_check_url_ok_too_long(self):
        url_ok = "".join(choice("a") for _ in range(251))
        with pytest.raises(ValueError, match="url_ok cannot be longer than 250 characters"):
            Request.check_url_ok(url_ok)

    def test_check_url_ko_too_long(self):
        url_ko = "".join(choice("a") for _ in range(251))
        with pytest.raises(ValueError, match="url_ko cannot be longer than 250 characters"):
            Request.check_url_ko(url_ko)

    def test_check_consumer_language_invalid(self):
        with pytest.raises(ValueError, match="consumer_language is not valid"):
            Request.check_consumer_language("999")

    def test_prepare_sum_total(self):
        result = Request.prepare_sum_total(D("100.50"))
        assert result == 10050

    def test_check_authorization_code_invalid_format(self):
        with pytest.raises(ValueError, match="authorization_code format is not valid"):
            Request.check_authorization_code("invalid!")
        with pytest.raises(ValueError, match="authorization_code format is not valid"):
            Request.check_authorization_code("12345678")
