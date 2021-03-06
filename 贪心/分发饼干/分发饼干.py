g = [1, 3, 2, 5, 6]
s = [1, 2, 5, 6, 1]

def allocate_cookies(children, cookies):
    children.sort()
    cookies.sort()
    index = len(cookies) - 1
    result = 0

    for i in reversed(range(len(children))):
        if index >= 0 and cookies[index] >= children[i]:
            result += 1
            index -= 1
    return result

print(allocate_cookies(g, s))