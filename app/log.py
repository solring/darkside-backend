ERROR = "ERR"
LOG = "INFO"
WARNING = "WARN"

def format(level, func_name, msg):
    return "[%s] %s(): %s" % (level, func_name, msg)

def log(func, msg):
    print(format(LOG, func.__name__, msg))

def warn(func, msg):
    print(format(WARNING, func.__name__, msg))

def err(func, msg):
    print(format(ERROR, func.__name__, msg))
