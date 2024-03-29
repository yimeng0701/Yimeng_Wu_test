# PYTHON TECHNICAL TEST 

## Question A
### Description
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
### Idea
Given two lines l1: (x1,x2) and l2: (x3,x4) on the x-axis (x1,x2,x3,x4 could be any rantional numbers)：
1. sort the lines first to make x1<x2 and x3<x4
2. If x3>x2 or x4<x1, the two lines don't overlap, otherwise they overlap.

### Test
#### Test on pre-defined test cases
Run test.py under the Q_A folder. I provide 10 test cases:
1. (1,5) and (6,8)
2. (1,5) and (2,6)
3. (-5.634563464,4.3123424) and (-10.61324,-2.123131)
4. (-10.61324,-2.123131) and (-5.634563464,4.3123424)
5. (10,7) and (20,3)
6. (-9.01,-3.228) and (-2.18,5)
7. (-2.18,5) and (-9.01,-3.228)
8. (0,-1.76) and (-1.0004,9)
9. (2,100) and (3,6)
10. (-2,9) and (-3.7,-2.01)

Run in command-Line: python -m unittest -v  test.TestSolution
#### Test on your own test cases
Run overlap.py under the Q_A folder and enter the input by following the instruction. 


## Question B
### Description
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
### Valid Versions
The regular Expression is used to check version validity. I define the valid version format as: MAJOR.several levels of MINOR (optional).pre-released version (optional):
* MAJOR: Only contains numbers (*)
* MINOR (optional): Several levels of minor versions, seperated by"." are accepted. Each level of minor versions only contains numbers.
* Pre-released version (optional): Some versions may have a pre-released version like"1.2.3a". Here, the pre-released one is defined as numbers followed by **one** **lower-case** letter (without ".").

All other types of versions are considered as **Invalid** versions and will not be accepted by the compare function. 

*: Versions with a prefix "v" are also accepted and are ignored during comparison. For example, "v1.2.3" are seen as "1.2.3".

### Comparison Rules
1. Compare each level of version numbers from left to right numerically.
2. The default version number for each level of a version number is assumed to be 0. E.g.: "1.0" is equal to "1.0.0" since the third level version number of "1.0" is default to "0".
3. Leading zeros are accepted and ignored during comparison. E.g.: "1.01" is equal to "1.001".
4. A pre-release version has lower precedence than a normal version. E.g.: "1.2.3a" is less than "1.2.3" . Two pre-release versions with the same MAJOR and MINOR parts are compared based on the ASCII of the last lower-case letter. For example: "1.2.3a" is less than "1.2.3b".

### Test
#### Test on pre-defined test cases
Run test.py under the Q_B folder. I provide 10 test cases:
1. 0.1 and 1.5
2. 1.0 and 1
3. 1.0.1 and 1.0.1.0
4. 1.0 and 1.001
5. v1.0 and v1.001
6. 1.2.1 and 1.2.1b
7. 1.3.1 and 1.2.1b
8. 3.7b and 1.2.1b
9. 5 and 5.0.0b
10. 3.2.5 and 3.2.7

Run in command-Line: python -m unittest -v  test.TestSolution
#### Test on your own test cases
Run compareVersion.py under the Q_B folder and enter the input by following the instruction. 



## Author

* **Yimeng Wu** - *Electrical and Computer Engineering, McGill University* - [Yimeng Wu](https://github.com/yimeng0701/)


