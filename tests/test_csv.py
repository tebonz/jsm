# coding=utf-8
#---------------------------------------------------------------------------
# Copyright 2011 utahta
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------
from tests import CCODE
import jsm
import tempfile
import datetime
import time

def test_save():
    c = jsm.QuotesCsv()
    c.save_price(tempfile.mktemp(dir='/tmp/'), CCODE)

def test_save_range():
    c = jsm.QuotesCsv()
    start_date = datetime.date.fromtimestamp(time.time() - 604800) # 1週間前
    end_date = datetime.date.today()
    for range_type in (jsm.DAILY, jsm.WEEKLY, jsm.MONTHLY):
        c.save_historical_prices(tempfile.mktemp(dir='/tmp/'), CCODE, range_type, start_date, end_date)

def test_save_all():
    c = jsm.QuotesCsv()
    for range_type in (jsm.DAILY, jsm.WEEKLY, jsm.MONTHLY):
        c.save_historical_prices(tempfile.mktemp(dir='/tmp/'), CCODE, range_type, all=True)