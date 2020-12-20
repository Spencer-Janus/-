import re
from decimal import *
def calculate(n1, n2, operator):
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 / n2
    else:
        raise Exception("operator is not support now...")
    return result
def is_operator(e):
    operators = ["+", "-", "*", "/", "(", ")"]
    return True if e in operators else False
def formula_format(formula):

    """
    步骤需要处理的是区分负数还是减号
    """

    formula = re.sub(' ', '', formula)

    # 以 '横杠数字' 分割， -> \- 表示匹配横杠开头； \d+ 表示匹配数字1次或多次；\.?表示匹配小数点0次或1次;\d*表示匹配数字1次或多次。
    formula_list = [i for i in re.split('(\-\d+\.?\d*)', formula) if i]

    final_formula = []
    for item in formula_list:

        # 第一个是以横杠开头的数字（包括小数）final_formula。即第一个是负数，横杠就不是减号
        if len(final_formula) == 0 and re.search('^\-\d+\.?\d*$', item):
            final_formula.append(item)
            continue

        if len(final_formula) > 0:

            # 如果final_formal最后一个元素是运算符['+', '-', '*', '/', '('], 则横杠数字是负数
            if re.search('[\+\-\*\/\(]$', final_formula[-1]):
                final_formula.append(item)
                continue

        # 剩下的按照运算符分割开
        item_split = [i for i in re.split('([\+\-\*\/\(\)])', item) if i]
        final_formula += item_split

    return final_formula
def decision(tail_op, now_op):

 #return: 1 出栈计算， 0 弹出左括号不做操作， -1 入栈

    # 运算符等级
    rate1 = ["+", "-"]
    rate2 = ["*", "/"]
    rate3 = ["("]
    rate4 = [")"]

    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3:
            return -1
        else:
            return 1

    elif tail_op in rate2:
        if now_op in rate3:
            return -1
        else:
            return 1

    elif tail_op in rate3:
        if now_op in rate4:
            return 0
        else:
            return -1  # 只要栈顶元素为(，当前元素不是)都应入栈
    else:
        return -1
def final_cal(formula_list):
    num_stack = []
    op_stack = []
    for e in formula_list:
        operator = is_operator(e)
        if not operator:
            num_stack.append(float(e))
        else:
            while True:
                if len(op_stack) == 0:
                    op_stack.append(e)
                    break
                tag = decision(op_stack[-1], e)
                if tag == -1:
                    op_stack.append(e)
                    break
                elif tag == 0:  # 左右括号相遇不理会右括号并弹出左括号
                    op_stack.pop()
                    break
                elif tag == 1:
                    op = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num_stack.append(calculate(num1, num2, op))
    while len(op_stack) != 0:
        op = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(calculate(num1, num2, op))
    return num_stack, op_stack

def cal(a):
    formula_list = formula_format(a)
    print(formula_list)
    result, _ = final_cal(formula_list)
    print(result)
    list_result_1=[round(i,1) for i in result]
    list_result=[str(i) for i in list_result_1]
    result=''.join(list_result)
    result1 = Decimal(result).quantize(Decimal("0.1"), rounding="ROUND_HALF_UP")
    return str(result1)

'''
if __name__ == "__main__":
    # formula = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))"
    formula = "12.1-13.0"
    formula_list = formula_format(formula)
    result, _ = final_cal(formula_list)
    print('result = ', result)
    '''
