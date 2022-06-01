# cook your code here
def validname(p, c):
    p_letters= dict()
    c_letters = dict()
    ans = ''
    
    for letter in ''.join(p):
        p_letters[letter] = p_letters.get(letter,0) + 1
    for letter in ''.join(c):
        c_letters[letter] = c_letters.get(letter,0) + 1
    
    for letter,value in c_letters.items():
        if letter in p_letters.keys() and value <= p_letters[letter]:
            ans = 'YES'
        else:
            ans = 'NO'
            break
            
    print(ans)

if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        p_name = input().split()
        children_num = int(input())
        children_names = [input() for c in range(children_num)]
        validname(p_name, children_names)
