from decimal import Decimal as D

from redsys.response import Response


class TestResponse:
    def test_create_response(self):
        parameters = {
            "Ds_Response": "90",
            "Ds_MerchantCode": "1056",
            "Ds_Terminal": "1",
            "Ds_TransactionType": "1",
            "Ds_Order": "000000000001",
            "Ds_Amount": "10054",
            "Ds_MerchantData": "test merchant data",
            "Ds_Currency": 978,
        }
        response = Response(parameters)
        assert response.code == 90
        assert response.message == "Transacción autorizada para pagos y preautorizaciones"
        assert len(response._parameters.keys()) == 8
        assert response.is_authorized is True
        assert response.is_paid is True
        assert response.is_canceled is False
        assert response.is_refunded is False

    def test_setattr(self):
        response = Response({
            "Ds_Response": "90",
            "Ds_MerchantCode": "1056",
            "Ds_Terminal": "1",
            "Ds_TransactionType": "1",
            "Ds_Order": "000000000001",
            "Ds_Amount": "10054",
            "Ds_Currency": 978,
        })
        response.merchant_data = "new data"
        assert "Ds_MerchantData" in response._parameters
        assert response._parameters["Ds_MerchantData"] == "new data"

    def test_parameters_property(self):
        parameters = {
            "Ds_Response": "90",
            "Ds_MerchantCode": "1056",
            "Ds_Terminal": "1",
        }
        response = Response(parameters)
        assert response.parameters == response._parameters

    def test_clean_amount(self):
        result = Response.clean_amount("10054")
        assert result == D("100.54")
