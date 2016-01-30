''' Functions for creating a times table '''

def table(nums):
    ''' Create a times table as a list of lists '''
    return [[n1 * n2 for n1 in nums] for n2 in nums]


def table_lines(nums, table_nums):
    ''' Generator for formatted table lines '''
    width_num = len(str(nums[-1]))
    width_max = len(str(pow(nums[-1], 2)))

    formatted_nums = [str(n).rjust(width_max) for n in nums]
    yield '{} |{}'.format(' ' * width_num, ' '.join(formatted_nums))

    line_len = (width_max + 1) * len(nums) + width_num + 1
    line = ['-'] * line_len
    line[width_num + 1] = '+'
    yield ''.join(line)

    formatted_table = [[str(n).rjust(width_max) for n in row] for row in table_nums]
    for num, row in zip(nums, formatted_table):
        yield '{} |{}'.format(str(num).rjust(width_num), ' '.join(row))
