# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:15:16 2019

@author: prettyyang2
"""
import re

class Solution:
    
    def checkInput(self,data):
        valid_input = re.compile(r"(\s*)?\(([+-]?\d+(\.\d+)?)\,(\s*)?([+-]?\d+(\.\d+)?)\)$")  # coordinates: rational number
        if valid_input.match(data):
            return True
        else: return False
    
    def overlap (self,l1,l2):
        """ 
        l1: list or tuple
        l2: list or tuple
        output: boolean
        """
        x1 = min(l1)
        x2 = max(l1)  # x1 should be smaller than x2
        
        x3 = min(l2)
        x4 = max(l2)  # x3 should be smaller than x4
        
        if x3>x2 or x4<x1:
            return False
        else: return True
    
def main():
    while True:
        data1 = input("Please enter the first line (e.g.: (1, 5)):")
        if Solution().checkInput(data1):
            break
        else:
            print("Wrong Input! Try again:")
            continue
    while True:
        data2 = input("Please enter the second line (e.g.: (6, 8)):")
        if Solution().checkInput(data2):
            break
        else:
            print("Wrong Input! Try again:")
            continue
    p1 = re.findall(r'[(](.*?)[)]', data1)
    l1 = p1[0].split(',')
    l1 = [float(i) for i in l1]
    p2 = re.findall(r'[(](.*?)[)]', data2)
    l2 = p2[0].split(',')
    l2 = [float(i) for i in l2]
    ans = Solution().overlap(l1,l2)
    if ans:
        print ("{} and {} overlaps".format(data1,data2))
    else:
        print ("{} and {} do not overlaps".format(data1,data2))
            
if __name__ == "__main__":
    main()
    
            
        
        
        
