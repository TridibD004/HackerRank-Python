#!/bin/python

import math
import os
import random
import re
import sys

N = int(raw_input().strip())

if (N%2):
    print ("Weird")
elif (N>=2 and N<=5):
    print ("Not Weird")
elif (N>=6 and N<=20):
    print ("Weird")
else: print ("Not Weird")
