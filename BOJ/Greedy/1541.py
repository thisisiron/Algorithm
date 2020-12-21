import sys
import re
input = sys.stdin.readline


formula = input().rstrip()

number_or_symbol = re.compile('(\d+|[^ 0-9])')
formula = re.findall(number_or_symbol, formula)

new_formula = []
for i in range(len(formula)):
    if formula[i] == '+':
        continue
    elif formula[i - 1] == '+':
        x = new_formula.pop()
        new_formula.append(str(int(x) + int(formula[i])))
    else:
        if formula[i] == '-':
            new_formula.append(formula[i])
        else:
            new_formula.append(str(int(formula[i])))

print(eval(''.join(new_formula)))