### File(s) Size Utils ###
##########################
    
def get_size(*files):
    '''Return the size in bytes of all the given files.'''
    size = 0
    for f in files:
        size += os.path.getsize(f)
    return size
    
def check_size(max_, *files):
    '''
    Return False if the given files' size exceeds max_.
    Will return true if max_ is set to None, causing all checks to pass.
    '''
    if max_ is None: 
        return True
    s = get_size(*files)
    return True if s < max_ else False

def check_size_warn(max_, *files):
    '''
    Checks the given files's list size and prompt the user for
    cancelation if size is too big.
    '''
    if check_size(max_, *files): return True
    # yes_no_prompt in cli.py
    return yes_no_prompt(
        'The given file list exceeds %s bytes.\n'
        'Are you sure you want to upload that much data ? '
        % conf.FILE_SIZE_WARN)
