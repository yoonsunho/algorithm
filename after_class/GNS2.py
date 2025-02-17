import sys
sys.stdin = open("txt/GNS.txt", "r")

num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num_dict = {key:val for vla,key in enumerate(num_str)}

T = int(input())
tc_num ,sdsf