import sys    # it provides various function and variables that are used to manipulate difff part of the python env
import logging
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()   # exc_tb tells in which file of which line the error occur
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occur ion Python script name [{0}] line number [{1}] error messagee [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message    



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)

    def __str__(self):
        return self.error_message
    

# to check wheather it's work or not
# if __name__ == "__main__":  
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide by zero')
#         raise CustomException(e, sys)