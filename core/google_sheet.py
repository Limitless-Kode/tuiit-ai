import gspread

class GoogleSheet:
    def __init__(self, sheet_name):
        self.gc = gspread.service_account('service_account.json')
        self.sheet_name = sheet_name
        self.service = self.get_service()

    def get_service(self):
        wks = self.gc.open(self.sheet_name).sheet1
        return wks

    def get_all_records(self):
        return self.service.get_all_records()

    def get_all_values(self):
        return self.service.get_all_values()

    def get_row(self, row_number):
        return self.service.row_values(row_number)

    def get_col(self, col_number):
        return self.service.col_values(col_number)

    def get_cell(self, row_number, col_number):
        return self.service.cell(row_number, col_number).value

    def update_cell(self, row_number, col_number, value):
        self.service.update_cell(row_number, col_number, value)

    def update_row(self, row_number, values):
        self.service.update(row_number, [values])

    def update_col(self, cell_numbers, values):
        self.service.update_cells(cell_numbers, values)

    def append_row(self, values):
        self.service.append_row(values)

    def append_rows(self, values):
        self.service.append_rows(values)

    def delete_row(self, row_number):
        self.service.delete_row(row_number)

    def delete_rows(self, row_number, number_of_rows):
        self.service.delete_rows(row_number, number_of_rows)

    def delete_col(self, col_number):
        self.service.delete_col(col_number)

    def delete_cols(self, col_number, number_of_cols):
        self.service.delete_cols(col_number, number_of_cols)

    def clear(self):
        self.service.clear()

    def resize(self, rows, cols):
        self.service.resize(rows, cols)