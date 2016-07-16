import os
import random
import string

def get_random_chars(length=5):
    chars = []
    for i in range(length):
        chars.append(random.choice(string.ascii_letters))
    return ''.join(chars)


def create_temp_directory(dirname):
    try:
        location = os.path.join('/tmp/', dirname)
        if not os.path.exists(location):
            os.mkdir(location)
        return location
    except Exception, e:
        print str(e)
        decrease_current_count_by_one()
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error_msg = str(exc_type.__name__) + ' at line "' + str(exc_traceback.tb_lineno) + '" in "' + __file__ + '"'
        write_log(str(error_msg))