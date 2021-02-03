def is_valid(s: str) -> bool:
    if len(s) < 2:
        return False
    open = ['(', '[', '{']
    closed = [')', ']', '}']
    parens_list = []
    for paren in s:
        if paren in open:
            parens_list.append(paren)
        else:
            if len(parens_list) > 0:
                if closed.index(paren) != open.index(parens_list[-1]):
                    return False
                else:
                    parens_list.pop()
            else:
                return False

    return len(parens_list) == 0


print(is_valid("{([])}{}"))
