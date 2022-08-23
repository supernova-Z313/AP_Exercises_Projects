import time

def log(original_function):
    def inner1(*args, **kwargs):
        print(f"Function Name: \'{original_function.__name__}\'")
        st = time.perf_counter()
        returned_value = original_function(*args, **kwargs)
        if returned_value != False:
            print(f"Number of Positional Arguments: {len(args)}")
            print(f"Keyword Arguments: {kwargs}")
            print(f"return value: {returned_value}")
        time.sleep(0.65)
        en = time.perf_counter()
        if (en-st) < 1:
            print("Time Consumption: less than a second")
        else:
            print("Time Consumption: more than a second")
        return returned_value
    return inner1

@log
def calculator(*args, operation="ADD", output_format='float'):
    ope = ["ADD", "SUB", "MUL", "DIV"]
    if len(args) < 1:
        print("Value Error: At least one number must be entered.")
        print("return value: None")
        return False
    elif operation not in ope:
        print("Value Error: Operation must be ADD, SUB, MUL or DIV.")
        print("return value: None")
        return False
    elif not(output_format == "float" or output_format == "int"):
        print("Value Error: Format must be float or int.")
        print("return value: None")
        return False
    else:
        if len(args) == 1:
            return args
        else:
            args = list(args)
            if operation == "ADD":
                if output_format == "float":
                    return float(sum(args))
                else:
                    return int(sum(args))

            if operation == "SUB":
                if output_format == "float":
                    x = args[0]
                    args.remove(x)
                    for i in args:
                        x -= i
                    return float(x)
                else:
                    x = args[0]
                    args.remove(x)
                    for i in args:
                        x -= i
                    return int(x)

            if operation == "MUL":
                if output_format == "float":
                    x = args[0]
                    args.remove(x)
                    for i in args:
                        x *= i
                    return float(x)
                else:
                    x = args[0]
                    args.remove(x)
                    for i in args:
                        x *= i
                    return int(x)
    
            if operation == "DIV":
                if output_format == "float":
                    x = args[0]
                    args.remove(x)
                    for i in args:
                        x /= i
                    return float(x)
                else:
                    x = args[0]
                    args.remove(x)
                    for i in args:
                        x /= i
                    return int(x)


if __name__ == '__main__':
    code_to_execute = input()
    exec(code_to_execute)
