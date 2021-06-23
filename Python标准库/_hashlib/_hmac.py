import hmac
import hashlib
import base64

_hmac = hmac.new("1234".encode("utf-8"), "111".encode("utf-8"), hashlib.sha256).hexdigest()
print(_hmac, len(_hmac), type(_hmac))
