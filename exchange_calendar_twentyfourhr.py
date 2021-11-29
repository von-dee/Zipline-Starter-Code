# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:16:18 2019

@author: Sela
"""


from datetime import time
from zipline.utils.memoize import lazyval
from pandas.tseries.offsets import CustomBusinessDay
from pytz import timezone
# from .trading_calendar import TradingCalendar

# for setting our open and close times
from datetime import time
# for setting our start and end sessions
import pandas as pd
# for setting which days of the week we trade on
from pandas.tseries.offsets import CustomBusinessDay
# for setting our timezone
from pytz import timezone

# for creating and registering our calendar
from trading_calendars import register_calendar, TradingCalendar
from zipline.utils.memoize import lazyval

class TwentyFourHR(TradingCalendar):
    """
    Exchange calendar for 24/7 trading.

    Open Time: 12am, UTC
    Close Time: 11:59pm, UTC

    """

    """
    Exchange calendar for the Taiwan Stock Exchange
    on 2001 https://www.ithome.com.tw/node/7930
    Open Time: 9:00 AM, GMT
    Close Time: 1:30 PM, GMT
    """
    @property
    def name(self):
        return "twentyfourhr"

    @property
    def tz(self):
        tz = timezone("UTC")
        return tz
    
    open_times = (
        (None, time(0)),
    )
    
    close_times = (
        (None, time(23, 59)),
    )


