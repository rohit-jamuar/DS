#1/usr/bin/env python
import sys

if sys.version_info.major == 3:
    from io import StringIO
else:
    from StringIO import StringIO

def exec_and_capture_stdout(func_to_call):
    #redirect output of STDOUT to StringIO buffer before calling func_to_call
    #revert the sys.stdout's behavior, post-execution of func_to_call
    def executor(*args, **kwargs):
        orig_stdout = sys.stdout
        stringIO_obj = StringIO()
        sys.stdout = stringIO_obj
        try:
            func_to_call(*args, **kwargs)
        finally:
            sys.stdout = orig_stdout
            stringIO_obj.close()
    return executor
