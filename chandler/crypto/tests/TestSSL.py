"""
Unit test for SSL context, connection and related security checks.

@copyright = Copyright (c) 2004 Open Source Applications Foundation
@license   = http://osafoundation.org/Chandler_0.1_license_terms.htm
"""

import unittest
import crypto.ssl
import TestM2CryptoInitShutdown
from M2Crypto import SSL
import socket

# XXX This should not inherit from InitShutdown because that makes us
#     run it's tests too
class TestSSL(TestM2CryptoInitShutdown.InitShutdown):
    
    def testSSL(self):
        if not self.isOnline():
            return

        site = 'www.verisign.com'
        
        ctx = crypto.ssl.getSSLContext(protocol='sslv3')
        conn = SSL.Connection(ctx)

        # We wrap the connect() in try/except and filter some common
        # network errors that are not SSL-related.
        #
        # XXX Potential candidates to filter (need to check if ok):
        #     - SSLError: (54, 'Connection reset by peer')
        try:
            self.assert_(conn.connect((site, 443)) >= 0)
        except socket.gaierror, e:
            if e.args[0] == 7: #'No address associated with nodename'
                return
            raise

        crypto.ssl.postConnectionCheck(conn, '0FA5B0527BA98FC66276CA166BA22E44A73636C9', hostCheck=True)

        conn.clear()

    def isOnline(self):
        import socket
        try:
            a = socket.gethostbyname('www.osafoundation.org')
            return True
        except:
            return False

        
if __name__ == "__main__":
    unittest.main()