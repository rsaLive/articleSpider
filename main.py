from scrapy.cmdline import execute

import sys
import os
from scrapy.http import request
from urllib import  parse
try:
    num = float("123好")
except Exception as result:
    print(result)

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","jobbole"])