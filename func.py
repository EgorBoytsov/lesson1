def get_summ(one, two, delimiter='&'):
    one = str(one).upper()
    two = str(two).upper()
    return f'{one} {str(delimiter)} {two}'


one = 'Learn'
two = 'python'
sum_string = get_summ(one, two, delimiter='&')
print(sum_string)