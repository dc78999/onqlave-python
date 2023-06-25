from hashlib import sha512
class Hasher:
    def __init__(self) -> None:
        pass

    def digest(self, body_data) -> None:
        """hash the body_data using sha-512() then encode with base64
        """
        digest_hash = sha512()
        # digest_hash.update(body_data)
        # digest_hash.digest()
        print("hashing the body content here ....")
        pass

    def sign(self,header_data, signing_key) -> None:
        """sign the header data with a signing key using hmac-sha512
        lowercase all the header data before signing
        """
        print("signing something here....")
        pass