def average_tuple(two_dimentional_tuple):
    '''get the two dimentional tuple and return a tuple that have the averege of same index numbers'''
    # using the tuple execpt the zip is  faster and bether
    return tuple(map(lambda *args : sum(args)/len(args), *two_dimentional_tuple))

if __name__ == '__main__':
    expression_to_evaluate = input()
    print(eval(expression_to_evaluate))
