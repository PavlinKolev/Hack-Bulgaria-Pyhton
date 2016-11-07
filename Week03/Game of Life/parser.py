class Parser:

    def parse_start_info(file_name):
        f = open(file_name, 'r')
        matrix_size = int(f.readline())
        live_cells_count = int(f.readline())
        live_cells = []

        for index in range(live_cells_count):
            Parser.add_live_cell(live_cells, f)

        f.close()
        return (matrix_size, live_cells)


    def add_live_cell(live_cells, f):
        line = f.readline().split(' ')
        cell = []
        cell.append(int(line[0]))
        cell.append(int(line[1]))
        live_cells.append(cell)
