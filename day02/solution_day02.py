from math import gcd
# cook your dish here
def probab(n,m):
    n_even = n//2
    n_odd = n - n_even
    m_even = m//2
    m_odd = m - m_even
    
    total_outcomes = n*m
    num_of_even = n_even*m_odd + n_odd*m_even
    
    if num_of_even == 0:
        print(f"0/{total_outcomes}")
    else:
        g = gcd(num_of_even, total_outcomes)
        print(f"{num_of_even//g}/{total_outcomes//g}")
    

if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        n,m = input().split()
        n,m = int(n), int(m)
        probab(n,m)