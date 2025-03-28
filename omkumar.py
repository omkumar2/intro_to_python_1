def read_file(filename):
    """
    Read the file and print each line

    Argument:
        filename: string, name of the file to be read
    Return:
        None
    """
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
    return None

