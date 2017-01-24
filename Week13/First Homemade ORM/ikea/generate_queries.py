def create_table_query(cl):
    res = "CREATE TABLE IF NOT EXISTS {} (\n".format(cl.__tablename__)
    columns_count = len(cl._fields)
    index = 0
    for k, v in cl._fields.items():
        res += k + ' ' + str(v)
        index += 1
        if index == columns_count:
            res += '\n'
        else:
            res += ',\n'
    res += ')'
    return res
