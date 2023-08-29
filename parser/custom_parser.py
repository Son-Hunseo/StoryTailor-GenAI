# custom output parser
def cut_before_and_after_braces(input_string):
    # 첫 문자가 '{'가 아닐 경우, '{' 이전 부분을 잘라냄
    if input_string and input_string[0] != '{':
        brace_index = input_string.find('{')
        if brace_index != -1:
            input_string = input_string[brace_index:]
        else:
            return ''

    # stack을 사용하여 '{'의 개수를 세고, 쌍이 맞는 '}'를 찾음
    stack = []
    for index, char in enumerate(input_string):
        if char == '{':
            stack.append(index)
        elif char == '}':
            if stack:
                stack.pop()
            else:
                # 불균형한 '}'를 발견한 경우 문자열 자르기
                return input_string[:index]

            # stack이 비었다면 균형잡힌 '{}' 쌍을 찾은 것임
            if not stack:
                return input_string[:index + 1]

    # stack이 여전히 비어있지 않다면 불완전한 문자열 반환
    return input_string if stack else ''
