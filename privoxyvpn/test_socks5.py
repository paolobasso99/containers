import pycurl
from dotenv import load_dotenv
import os

load_dotenv()

c1 = pycurl.Curl()
c1.setopt(pycurl.URL, 'https://ifconfig.me')
c1.setopt(pycurl.PROXY, os.getenv("TEST_PROXY_HOST", "localhost"))
c1.setopt(pycurl.PROXYPORT, os.getenv("TEST_PROXY_PORT", 9118))
c1.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
c1.setopt(pycurl.PROXYUSERNAME, os.getenv("SOCKS_USER"))
c1.setopt(pycurl.PROXYPASSWORD, os.getenv("SOCKS_PASS"))

c1.perform() 