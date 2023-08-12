import base64
import hashlib

from .settings import settings


def generate_signature(data: bytes) -> str:
    m = hashlib.md5()
    b64data = base64.b64encode(data)
    m.update(b64data + settings.security_key)
    return m.hexdigest()
