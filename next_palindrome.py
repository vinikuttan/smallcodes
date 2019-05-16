
# global variables
odds = []
az = [0] * 26


def is_palindrome(a):
    """ boolean function - Is string can make palindrome """
    a_len = len(a)
    
    for i in a:
       index = ord(i) - ord('a')
       az[index] += 1

    for k in range(26):
        if az[k] and az[k] %2 != 0:
            odds.append(k)

    # palindrome conditions
    if a_len % 2 == 0 and len(odds) == 0:
        return True
    if a_len % 2 != 0 and len(odds) == 1:
        return True        
    return False


def generate_palidrome(a):
    """ generate next palindrome in alphabetical order"""
    a_len = len(a)
    top = 0
    rear = a_len -1
    res = [''] * a_len

    for i in range(26):
        if az[i] != 0 and i not in odds:
            value = chr(ord('a') + i)
            freq = az[i]

            for j in range(freq/2):
                res[top] = value
                res[rear] = value
                top += 1
                rear -= 1
    if odds:
        res[top] = chr(ord('a') + odds[0])
    return ''.join(res)


def main():
    a = raw_input()
    
    if not is_palindrome(a):
        return "It is not palindrome"
    print generate_palidrome(a)


if __name__=="__main__":
    # step1 - palindrome possiblity check
    # step2 - generate next palindrome string in alphabetical order
    main()
