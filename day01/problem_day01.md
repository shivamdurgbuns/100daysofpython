Problem

In an attempt to reduce the growing population, Archer was asked to come up with a plan. Archer being as intelligent as he is, came up with the following plan:

If NNN children, with names C1,C2,...,CNC_{1}, C_{2}, ... , C_{N}C1​,C2​,...,CN​, are born to parents with names AAA and BBB, and you consider CCC to be the concatenation of all the names of the children, i.e. C=C1+C2+...+CNC = C_{1} + C_{2} + ... + C_{N}C=C1​+C2​+...+CN​ (where +++ is concatenation operator), then CCC should be a substring of one of the permutations of A+BA + BA+B.

You are given the task to verify whether the names parents propose to give their children are in fact permissible by Archer's plan or not.
Input

The first line contains an integer TTT, the number of test cases. TTT test cases follow. Each test case stats with a line containing two space separated strings AAA and BBB, denoting the names of the parents. The next line contains a single integer NNN denoting the number of children AAA and BBB are planning to have. Following this are NNN lines, the ithi^{th}ith line containing CiC_{i}Ci​, the proposed name for the ithi^{th}ith child.
Output

For each test case output a single line containing YESYESYES if the names are permissible by Archer's plan, otherwise print NONONO.

Constraints

    1≤T≤100 
    1≤N≤1000
    The lengths of all the strings including AAA, BBB, and all CiC_{i}Ci​ will be in the range [1,40000][1, 40000][1,40000], both inclusive. All these strings will contain only lowercase English letters.
    The combined lengths of all names of children will not exceed the combined length of the names of their parents.

Sample 1:
Input

3
tom marvoloriddle
2
lord
voldemort
cheap up
1
heapcup
bruce wayne
2
bat
man

Output
YES
YES
NO

Explanation:

Let YYY denote the concatenation of names of all the children, and XXX denote the concatenation of the names of the parents.

Case 1: Here XXX = "tommarvoloriddle", and YYY = "lordvoldemort". Consider ZZZ = "iamlordvoldemort". It is not difficult to see that ZZZ is a permutation of XXX and YYY is a substring of ZZZ. Hence YYY is a substring of a permutation of XXX, so the answer is "YES".

Case 2: Here XXX = "cheapup", and YYY = "heapcup". Since YYY in itself is a permutation of XXX, and as every string is a substring of itself, YYY is a substring of XXX and also a permutation of XXX. Hence "YES".

Case 3: Here XXX = "brucewayne", and YYY = "batman". As "t" is not present in XXX, "t" wont be present in any permutation of XXX, hence the answer is "NO".

URL: https://www.codechef.com/submit-v2/NAME1
