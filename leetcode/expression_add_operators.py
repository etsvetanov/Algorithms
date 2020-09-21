class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):
            print('index:', index, 'prev_operand:', prev_operand, 'current_operand:', current_operand, 'value:', value, 'string:', string)
            if index == N:
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                print(u'\u23ce')
                return

            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:
                # print('NOOP')
                # print(f'NOOP: recurse(index = index + 1, '
                #       f'prev_operand = prev_operand, '
                #       f'current_operand = current_operand, '
                #       f'value = value, '
                #       f'string = string')
                recurse(index + 1, prev_operand, current_operand, value, string)  # NO OP recursion

            # ADDITION
            string.append('+'); string.append(str_op)
            # print('ADDITION')
            # print(f'recurse(index = index + 1, '
            #       f'prev_operand = current_operand, '
            #       f'current_operand = 0, '
            #       f'value = value + current_operand, '
            #       f'string = string')
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:  # SUBTRACTION
                string.append('-'); string.append(str_op)
                # print('SUBSTR')
                # print(f'recurse(index = index + 1, '
                #       f'prev_operand = - prev_operand, '
                #       f'current_operand = 0, '
                #       f'value = value - current_operand, '
                #       f'string = string')
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                # print(f'recurse(index={index + 1}, '
                #       f'prev_operand={current_operand * prev_operand}, '
                #       f'current_operand={0}, '
                #       f'value={value - prev_operand + (current_operand * prev_operand)}), '
                #       f'string={string}')
                # print(f'MLTP: recurse(index = index + 1, '
                #       f'prev_operand = current_operand * prev_operand, '
                #       f'current_operand = 0, '
                #       f'value = value - prev_operand + (current_operand * prev_operand), '
                #       f'string = string')
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(index=0, prev_operand=0, current_operand=0, value=0, string=[])
        return answers

s = Solution()

ans = s.addOperators('105', 6)
print('ans:', ans)
