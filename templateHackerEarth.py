#!/usr/bin/python
#For python < 3.2
import sys

T = int(input());
for test_case_number in range(T):
    line2 = list(map(int, input().split()));
    line3 = list(map(int, input().split()))
    print (line2, line3)
