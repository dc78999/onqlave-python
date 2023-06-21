# This is a list of constants for log messages
SDK = "SDK"

FETCHING_ENCRYPTION_KEY_OPERATION = "[onqlave] SDK: %s - Fetching encryption key"
FETCHING_ENCRYPTION_KEY_RESPONSE_UNMARSHALING_FAILED = (
    "[onqlave] SDK: %s - Failed unmarshalling encryption key response"
)
FETCHED_ENCRYPTION_KEY_OPERATION = (
    "[onqlave] SDK: %s - Fetched encryption key: operation took %s"
)

FETCHING_DECRYPTION_OPERATION = "[onqlave] SDK: %s - Fetching decryption key"
FETCHING_DECRYPTION_KEY_RESPONSE_UNMARSHALING_FAILED = (
    "[onqlave] SDK: %s - Failed unmarshalling decryption key response"
)
FETCHED_DECRYPTION_OPERATION = (
    "[onqlave] SDK: %s - Fetched decryption key: operation took %s"
)

KEY_INVALID_WRAPPING_ALGO = "[onqlave] SDK: %s - Invalid wrapping algorithm"
KEY_INVALID_WRAPPING_OPERATION = "[onqlave] SDK: %s - Invalid wrapping operation"
KEY_UNWRAPPING_KEY_FAILED = "[onqlave] SDK: %s - Failed unwrapping encryption key"
KEY_INVALID_ENCRYPTION_OPERATION = "[onqlave] SDK: %s - Invalid encryption operation"
KEY_INVALID_DECRYPTION_OPERATION = "[onqlave] SDK: %s - Invalid encryption operation"

ENCRYPTING_OPERATION = "[onqlave] SDK: %s - Encrypting plain data"
ENCRYPTED_OPERATION = "[onqlave] SDK: %s - Encrypted plain data: operation took %s"
ENCRYPTION_OPERATION_FAILED = "[onqlave] SDK: %s - Failed encrypting plain data"

DECRYPTING_OPERATION = "[onqlave] SDK: %s - Decrypting cipher data"
DECRYPTED_OPERATION = "[onqlave] SDK: %s - Decrypted cipher data: operation took %s"
DECRYPTION_OPERATION_FAILED = "[onqlave] SDK: %s - Failed decrypting cipher data"

CLIENT_ERROR_EXTRACTING_CONTENT = (
    "[onqlave] SDK: %s - Failed extracting request content"
)
CLIENT_ERROR_CALCULATING_DIGEST = (
    "[onqlave] SDK: %s - Failed calculating request digest"
)
CLIENT_ERROR_CALCULATING_SIGNATURE = (
    "[onqlave] SDK: %s - Failed calculating request signature"
)
CLIENT_ERROR_PORTING_REQUEST = "[onqlave] SDK: %s - Failed sending %s request"

CLIENT_OPERATION_STARTED = "[onqlave] SDK: %s - Sending request started"
CLIENT_OPERATION_SUCCESS = (
    "[onqlave] SDK: %s - Sending request finished successfully: operation took %s"
)
HTTP_OPERATION_STARTED = "[onqlave] SDK: %s - Http operation started"
HTTP_OPERATION_SUCCESS = (
    "[onqlave] SDK: %s - Http operation finished successfully: operation took %s"
)
