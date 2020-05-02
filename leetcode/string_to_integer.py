def myAtoi(s: str) -> int:
    non_white_space_str = s.lstrip(' ')
    numeric_chars = {str(i) for i in range(10)}
    sign_chars = {'-', '+'}

    if non_white_space_str[0] not in numeric_chars:
        if non_white_space_str[0] not in sign_chars and s[1] not in numeric_chars:
            return 0

    end_index_of_numeric_chars = len(non_white_space_str)

    for i in range(len(non_white_space_str)):
        if non_white_space_str[i] not in numeric_chars:
            end_index_of_numeric_chars = i
            break
    print('non_white_space_str:', non_white_space_str)
    print('end_index_of_numeric_chars:', end_index_of_numeric_chars)
    parsed_int = int(non_white_space_str[:end_index_of_numeric_chars])
    MIN_INT = -(2 ** 31)
    MAX_INT = 2 ** 31 - 1

    if MIN_INT <= parsed_int <= MAX_INT:
        return parsed_int
    elif parsed_int < MIN_INT:
        return MIN_INT
    else:
        return MAX_INT

print(myAtoi("  -42"))