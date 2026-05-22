# Currencies
""" Euro """
EUR = 978
""" United States dollar """
USD = 840
""" Pound sterling """
GBP = 826
""" Japanese yen """
JPY = 392
""" Argentine peso """
ARS = 32
""" Canadian dollar """
CAD = 124
""" Chilean Peso """
CLP = 152
""" Colombian peso """
COP = 170
""" Indian rupee """
INR = 356
""" Mexican peso """
MXN = 484
""" Peruvian Sol """
PEN = 604
""" Swiss franc """
CHF = 756
""" Brazilian real """
BRL = 986
""" Venezuelan bolivar """
VEF = 937
""" Turkish lira """
TRY = 949

CURRENCIES = [EUR, USD, GBP, JPY, ARS, CAD, CLP, COP, INR, MXN, PEN, CHF, BRL, VEF, TRY]

# Languages
CUSTOMER = "000"
SPANISH = "001"
ENGLISH = "002"
CATALAN = "003"
FRENCH = "004"
GERMAN = "005"
DUTCH = "006"
ITALIAN = "007"
SWEDISH = "008"
PORTUGUESE = "009"
VALENCIAN = "010"
POLISH = "011"
GALICIAN = "012"
EUSKERA = "013"

LANGUAGES = [
    CUSTOMER,
    SPANISH,
    ENGLISH,
    CATALAN,
    FRENCH,
    GERMAN,
    DUTCH,
    ITALIAN,
    SWEDISH,
    PORTUGUESE,
    VALENCIAN,
    POLISH,
    GALICIAN,
    EUSKERA,
]

# Transaction types
""" Standard payment """
STANDARD_PAYMENT = "0"
""" Pre-authorization """
PREAUTHORIZATION = "1"
""" Confirmation of pre-authorization """
PREAUTHORIZATION_CONFIRMATION = "2"
""" Partial or total refund """
REFUND = "3"
""" Recurring transaction """
RECURRING_TRANSACTION = "5"
""" Successive transaction """
SUCCESSIVE_TRANSACTION = "6"
""" Authentication """
AUTHENTICATION = "7"
""" Confirmation of authentication """
AUTHENTICATION_CONFIRMATION = "8"
""" Cancellation of pre-authorization """
PREAUTHORIZATION_CANCELATION = "9"
""" Deferred pre-authorization """
DEFERRED_PREAUTHORIZATION = "O"
""" Confirmation of deferred pre-authorization """
DEFERRED_PREAUTHORIZATION_CONFIRMATION = "P"
""" Cancelation of deferred pre-authorization """
DEFERRED_PREAUTHORIZATION_CANCELATION = "Q"
""" Recurring deferred pre-authorization """
RECURRING_DEFERRED_PREAUTHORIZATION = "R"
""" Confirmation of recurring deferred pre-authorization and successive transaction """
SUCCESSIVE_RECURRING_TRANSACTION = "S"

TRANSACTIONS = [
    STANDARD_PAYMENT,
    PREAUTHORIZATION,
    PREAUTHORIZATION_CONFIRMATION,
    REFUND,
    RECURRING_TRANSACTION,
    SUCCESSIVE_TRANSACTION,
    AUTHENTICATION,
    AUTHENTICATION_CONFIRMATION,
    PREAUTHORIZATION_CANCELATION,
    DEFERRED_PREAUTHORIZATION,
    DEFERRED_PREAUTHORIZATION_CONFIRMATION,
    DEFERRED_PREAUTHORIZATION_CANCELATION,
    RECURRING_DEFERRED_PREAUTHORIZATION,
    SUCCESSIVE_RECURRING_TRANSACTION,
]


"""
Tokenization
------------

Tokenization is a security process that replaces sensitive card information 
(such as the PAN, expiration date, and CVV) with a randomly generated unique 
identifier known as a token . This token has no value outside the specific 
system for which it was created and cannot be used to conduct fraudulent 
transactions if intercepted.

Credential on File (COF)
------------------------

A COF transaction, also known as Credential on File or Card on File, is a 
transaction in which the merchant uses the cardholder's card data (PAN or 
tokenized PAN and expiration date), with the cardholder having explicitly 
authorized the merchant to store and use this data in that and subsequent 
transactions. A COF transaction can be initiated by the cardholder or by 
the merchant as a result of an agreement between the cardholder and the 
merchant. When performing a COF transaction, you must identify the specific 
scenario in which you intend to operate.

Types of COF operations
-----------------------

It's necessary to consider whether the operation is the first COF operation, 
meaning the request and storage of credentials, or a subsequent one, meaning 
you'll be using previously saved credentials. Additionally, you need to know 
what type of operation you're going to perform:

Main operations.

* Installments / Deferred Payment: Always referring to an individual 
  purchase, the amount of the transactions must be fixed, and with a defined 
  time interval.
* Recurring / Recurring Payment: The amount of the transactions can be 
  variable, but the time interval must be defined.

Special operations.

* Reauthorization: This is usually done for partial shipments or when the 
  customer extends the paid service (hotel stay, vehicle rental, etc.) or when, 
  having an estimated authorization, the final amount is requested.
* Resubmission: Used when the original has been refused due to "insufficient 
  funds." It can only be used in certain sectors; you should consult the 
  trademark regulations for more information.
* Delayed: Charges made after the main transaction for services rendered, 
  such as use of the minibar in a hotel stay or damage to the rented vehicle.
* Incremental: Used when the contracted service incurs additional expenses 
  not included in the main operation. 
* No Show: Type used when the business charges for services that the account 
  holder contracted but ultimately did not show up or did not use, such as a 
  hotel reservation that was not cancelled.
  
More info: https://pagosonline.redsys.es/desarrolladores-inicio/documentacion-funcionalidades-avanzadas/tokenizacion/  
"""
COF_TYPE_INSTALLMENTS = "I"
COF_TYPE_RECURRING = "R"
COF_TYPE_REAUTHORISATION = "H"
COF_TYPE_RESUBMISSION = "E"
COF_TYPE_DELAYED = "D"
COF_TYPE_INCREMENTAL = "M"
COF_TYPE_NO_SHOW = "N"
COF_TYPE_OTRAS = "C"

TYPES_OF_COF = [
    COF_TYPE_INSTALLMENTS,
    COF_TYPE_RECURRING,
    COF_TYPE_REAUTHORISATION,
    COF_TYPE_RESUBMISSION,
    COF_TYPE_DELAYED,
    COF_TYPE_INCREMENTAL,
    COF_TYPE_NO_SHOW,
    COF_TYPE_OTRAS,
]


"""
COF Transition Indicator
 S: It is first COF transaction (store credentials)
 N: It is not the first COF transaction
"""
COF_FIRST_TRANSACTION = "S"
COF_NOT_FIRST_TRANSACTION = "N"
COF_TRANSACTIONS = [
    COF_FIRST_TRANSACTION,
    COF_NOT_FIRST_TRANSACTION,
]


"""
Strong Customer Authentication (SCA):
 
PSD2 requires payment service providers (also called PSPs) to implement 
additional security measures to verify the customer's identity when making 
electronic transactions, such as using one-time codes via SMS or accepting 
the transaction within their bank's mobile application.
"""

SCA_EXCEP_MIT = "MIT" # Merchant-Initiated Transactions
SCA_EXCEP_LWV = "LWV" # Low-value transactions
SCA_EXCEP_TRA = "TRA" # Low-risk transactions
SCA_EXCEP_COR = "COR" # Corporate Payment
SCA_EXCEP_ATD = "ATD" # Trusted Beneficiaries

SCA_EXEMPTIONS = [
    SCA_EXCEP_MIT,
    SCA_EXCEP_LWV,
    SCA_EXCEP_TRA,
    SCA_EXCEP_COR,
    SCA_EXCEP_ATD,
]
