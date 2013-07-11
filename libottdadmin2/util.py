#
# This file is part of libottdadmin2
#
# License: http://creativecommons.org/licenses/by-nc-sa/3.0/
#

import logging

from datetime import datetime, timedelta

GAMEDATE_BASE_DATE = datetime(1, 1, 1)

def gamedate_to_datetime(date):
    return GAMEDATE_BASE_DATE + timedelta(days = date  - 365)

def datetime_to_gamedate(datetime):
    return (datetime - GAMEDATE_BASE_DATE).days + 366

class LoggableObject(object):
    """
    Loggable Object MixIn.

    This exposes the .log property, which dynamically creates a logging.logger formatted for the class.
    """

    @property
    def log(self):
        """
        The log property. retrieving this the first time will generate a logging.logger for the inheriting class.
        """
        log = getattr(self, '_logger', None)
        if log is None:
            log = logging.getLogger('%s.%s' % (
                                                self.__class__.__module__, 
                                                self.__class__.__name__))
            setattr(self, '_logger', log)
        return log

    def reset_log(self):
        """
        Resets the current created logger.
        """
        if hasattr(self, '_logger'):
            delattr(self, '_logger')
