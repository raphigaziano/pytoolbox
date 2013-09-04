import fnmatch
import os

### Path manipulations ###
##########################

def path_to_basename(path, stripext=False):
    """
    Return the basename of the passed path, without the extension if
    `stripext` is True.
    """
    basename = os.path.basename(path)
    if stripext:
        return os.path.splitext(basename)[0]
    return basename

### File listing ###
####################

def list_files(startdir, recursive=False, abspathes=True, pattern=None):
    """
    Yield files contained in `startdir`.
    Optionnal parameters:
    `recursive`: Look for files recursively. Defaults to False.
    `abspathes`: Return absolute pathes. Defaults to True.
    `pattern`:   Unix glob pattern to filter files further
    """
    for f in os.listdir(startdir):
        path = os.path.join(startdir, f)
        if os.path.isfile(path):
            if not abspathes:
                path = os.path.relpath(path)
            if pattern is not None and not fnmatch.fnmatch(path, pattern):
                continue
            yield path
        elif recursive and os.path.isdir(path):
            for sub in list_files(path, recursive, abspathes, pattern):
                yield sub

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
