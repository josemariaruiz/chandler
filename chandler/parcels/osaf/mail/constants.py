__revision__  = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2005 Open Source Applications Foundation"
__license__   = "http://osafoundation.org/Chandler_0.1_license_terms.htm"

""" Contains constants shared across the Mail Domain (SMTP, IMAP4, POP3) """

#XXX: Look at moving much of the data to items

#python imports
import version

DEFAULT_CHARSET = "utf-8"
LF    = unicode("\n", DEFAULT_CHARSET)
CR    = unicode("\r", DEFAULT_CHARSET)
EMPTY = unicode("",   DEFAULT_CHARSET)

"""First step on Localization is to centralize message strings and
   use getText looks ups for translation. This will be replaced with
   calls to the repository to retrieve LocalizableString types
   in the near future """

CHANDLER_USERAGENT = "Chandler (%s %s)" % (version.release, version.build)
CHANDLER_HEADER_PREFIX = "X-Chandler-"

INVALID_EMAIL_ADDRESS = _("%s Address %s is not a valid Email Address")


"""Translatable message strings for downloads (POP, IMAP)"""
DOWNLOAD_ERROR = _("An error occurred while downloading mail: %s")
DOWNLOAD_NO_MESSAGES = _("No new messages found")
DOWNLOAD_MESSAGES = _("%s messages downloaded to Chandler")
DOWNLOAD_CHECK_MESSAGES = _("Checking for new mail messages")
DOWNLOAD_REQUIRES_TLS = _("The Server only allows secure login. Please enable TLS or SSL.")

"""Translatable message strings for uploads(SMTP)"""
UPLOAD_FAILED = _("Unable to send: %s")
UPLOAD_FAILED_FOR_RECIPIENTS = _("Send failed for the following recipients:")
UPLOAD_SUCCESS = _("Message sent to [%s]")
UPLOAD_BAD_REPLY_ADDRESS = _("The Reply-To Address %s is not valid")
UPLOAD_FROM_REQUIRED = _("A From Address is required to send a Mail Message")
UPLOAD_BAD_FROM_ADDRESS = _("%s is not a valid From Address")
UPLOAD_TO_REQUIRED = _("A To Address is required to send an SMTP Mail Message")


"""Translatable message strings for account testing"""
TEST_ERROR = _("%s Test Results\n\nPlease correct the following configuration error:\n\n%s")
TEST_SUCCESS = _("%s Test Results\n\nTest was successful.")

SHARING_HEADER  = "Sharing-URL"
SHARING_DIVIDER = ";"
SMTP_SUCCESS = 250

"""Number of seconds to wait to timeout connection for account testing"""
TESTING_TIMEOUT = 10

"""If set to True dumps MailMessage structure
   during parsing to the chandler.log.
   This will only work in debugging mode
   i.e. __debug__ == True
"""
VERBOSE = False


