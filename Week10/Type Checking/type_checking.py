import sys


class Function:
    def __init__(self, func_name, first_type, second_type):
        self.name = func_name
        self.first_type = first_type
        self.second_type = second_type

    def __str__(self):
        return "{}::{}->{}".format(self.name, self.first_type, self.second_type)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_correct_composition(func_1, func_2):
        if func_1.first_type == func_2.second_type:
            return True
        return False


def make_functions_list(lines):
    list_ = []
    for line in lines:
        line = line.rstrip('\n')
        list_.append(read_single_function(line))
    return list_


def read_single_function(line):
    func_name = line.split('::')[0].rstrip(' ')
    types = line.split('::')[1]
    first_type = types.split('->')[0].strip(' ')
    second_type = types.split('->')[1].strip(' ')
    return Function(func_name, first_type, second_type)


def get_function(funstions, name):
    for i in range(len(funstions)):
        if funstions[i].name == name:
            return funstions[i]


def get_funtions_names_list(composition):
    names = composition.split('.')
    for i in range(len(names)):
        names[i] = names[i].strip(' ')
    return names


def main():
    inpt = list(sys.stdin)
    composition = inpt[-1].rstrip('\n')
    del inpt[-2:]
    functions = make_functions_list(inpt)
    names = get_funtions_names_list(composition)
    result = True
    for i in range(1, len(names)):
        f = get_function(functions, names[i - 1])
        g = get_function(functions, names[i])
        result = result and Function.is_correct_composition(f, g)
    print(result)


if __name__ == '__main__':
    main()
