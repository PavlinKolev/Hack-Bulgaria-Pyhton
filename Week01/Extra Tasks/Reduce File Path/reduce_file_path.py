def reduce_file_path(path):
    paths_names = path.split('/')
    reduced_path = []
    for indx in range(len(paths_names)):
        if(paths_names[indx] == "."):
            continue
        if(paths_names[indx] == ".."):
            for i in range(indx + 1, len(paths_names)):
                if not reduced_path:
                    break
                reduced_path.pop()
        else:
            reduced_path.append(paths_names[indx])

    reduced_path_str = ""
    for elem in reduced_path:
        if elem != "":
            reduced_path_str += '/' + elem
    if reduced_path_str == "":
        return "/"
    return reduced_path_str
