import re

class Arguments(object):
    '''
    Wrapper class around docopt's args dictionnary, allowing direct attribute 
    access.
    '''

    # Simple validation checkers.
    # List them as argument_name: checker_function pairs.
    # argument_name should be listed as the attribute name, eg option instead
    # of --option.
    # Not all arguments need a checker function.
    # Checkers must accept the argument's attrname and value as parameters,
    # and return True if the argument is valid, False otherwise.
    arg_checkers = {

    }

    def __init__(self, args):
        for k, v in args.items():
            arg_name = self._to_name(k)
            if self._check_arg(arg_name, v):
                self.__dict__[arg_name] = v
            else:
                raise ValueError('Invalid argument %s %s' % (k, v))

    def _to_name(self, key):
        '''
        Convert dict key to a valid attribute name, removing any special 
        characters.
        '''
        return re.sub('\W', '_', key).strip('_')

    def _check_arg(self, arg, val):
        '''Single argument validation'''
        checker = self.arg_checkers.get(arg, None)
        if checker is not None: 
            return checker(val)
        return True
