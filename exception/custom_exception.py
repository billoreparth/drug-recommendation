import sys

class custom_exception(Exception):  
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)  
        _, _, exc_tb = error_details.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.error_message = error_message

    def __str__(self):
        return f"The error occurred in file: {self.file_name} on line {self.line_no}. Error message: {str(self.error_message)}"

        

