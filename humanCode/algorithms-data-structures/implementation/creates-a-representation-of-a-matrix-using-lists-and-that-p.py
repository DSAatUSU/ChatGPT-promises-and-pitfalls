class LIST_MATRIX:
    def __init__(self, size=(4, 4)):
        self.size = size
        self.matrix = [[0 for i in range(size[0])] for j in range(size[1])]

    def add_row(self, row_list):
        self.matrix.append(row_list)
        return self

    def delete_row(self, row_list):
        self.matrix.remove(row_list)
        return self

    def print_matrix(self):
        print(" _")
        for i, row in enumerate(self.matrix):
            if i == len(self.matrix) - 1:
                print("|", *row, end=" ")
            else:
                print("|", *row)
        print("\n ¯¯")


if __name__ == "__main__":
    matrix = LIST_MATRIX((4, 4))
    row_list = [1, 2, 3, 4]

    matrix.add_row(row_list)
    matrix.print_matrix()
    print("\n")
    matrix.delete_row(row_list)
    matrix.print_matrix()
