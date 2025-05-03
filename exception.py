import traceback
import logging


logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def exception_catcher(target_function, *args, context=None, **kwargs):
    try:
        return target_function(*args, **kwargs)
    except FileNotFoundError as fnf_error:
        error_message = f"FileNotFoundError in {target_function.__name__}: {fnf_error}"
        print(error_message)
        logging.error(error_message)
    except ValueError as value_error:
        error_message = f"ValueError in {target_function.__name__}: {value_error}"
        print(error_message)
        logging.error(error_message)
    except TypeError as type_error:
        error_message = f"TypeError in {target_function.__name__}: {type_error}"
        print(error_message)
        logging.error(error_message)
    except Exception as e:
        error_message = f"An error occurred in {target_function.__name__}: {e}"
        detailed_traceback = traceback.format_exc() 
        if context:
            error_message = f"{context} - {error_message}"
        
        print(error_message)
        print(detailed_traceback)
        logging.error(f"{error_message}\n{detailed_traceback}")
    return None