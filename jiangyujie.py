def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


result = []


def DFS(s: str, partion, s2):
    tmp = ''
    for i, v in enumerate(s):
        tmp += v
        if is_palindrome(tmp):  # 判断是否是回文串
            partion.append(tmp)
            if ''.join(partion) == s2:
                result.append(partion[:])
                DFS(s[i + 1:], [], s2)
            else:
                DFS(s[i + 1:], partion, s2)
    return result


def partition(s):
    partion = []
    DFS(s, partion, s)
    print(result)


if __name__ == '__main__':
    print(partition('aaba'))
