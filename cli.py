import sys

# adapted from:
# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def cli_progressbar(label, val, end_val=100, bar_length=20, char='#'):
    """
    Simple progress bar.
    label: Text to display before the progress bar.
    val: current value
    end_val: max value (defaults to 100)
    bar_length: total length of the progress bar (defaults to 20)
    char: character for filling up the bar (defaults to #)

    Usage:

    >>> for i in range(11): # doctest fails for some weird indentation bug
    ...     cli_progressbar("TEST: ", i, end_val=10, char='-')
    TEST: [--------------------] 100%
    """
    percent = float(val) / end_val
    hashes  = char * int(round(percent * bar_length))
    spaces  = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\r{0}[{1}] {2}%".format(label, hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()

### User Interaction ###
########################

def yes_no_prompt(msg):
    '''
    Prompt the user with a yes/no question.
    Returns True for yes, False for no.
    '''        
    prompt = input(msg).lower()
    while True:
        if prompt.startswith('y'):
            return True
        elif prompt.startswith('n'):
            return False
        else:
            prompt = input('Please answer by y(es) or n(o) ').lower()

# Shamelessly stolen from the grin source
_COLOR_TABLE = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
                'white', 'default']

def colorize(s, fg=None, bg=None, bold=False, underline=False, reverse=False):
    """ Wraps a string with ANSI color escape sequences corresponding to the
    style parameters given.
    
    All of the color and style parameters are optional.
    
    Parameters
    ----------
    s : str
    fg : str
        Foreground color of the text.  One of (black, red, green, yellow, blue, 
        magenta, cyan, white, default)
    bg : str
        Background color of the text.  Color choices are the same as for fg.
    bold : bool
        Whether or not to display the text in bold.
    underline : bool
        Whether or not to underline the text.
    reverse : bool
        Whether or not to show the text in reverse video.

    Returns
    -------
    A string with embedded color escape sequences.
    """
    
    style_fragments = []
    if fg in _COLOR_TABLE:
        # Foreground colors go from 30-39
        style_fragments.append(_COLOR_TABLE.index(fg) + 30)
    if bg in _COLOR_TABLE:
        # Background colors go from 40-49
        style_fragments.append(_COLOR_TABLE.index(bg) + 40)
    if bold:
        style_fragments.append(1)
    if underline:
        style_fragments.append(4)
    if reverse:
        style_fragments.append(7)
    style_start = '\x1b[' + ';'.join(map(str,style_fragments)) + 'm'
    style_end   = '\x1b[0m'
    return style_start + s + style_end

# Test

def test():
    print colorize(
        "test",
        fg        = "green",
        bg        = "red",
        bold      = True,
        underline = True,
    )
    print colorize("reversed test", reverse=True)

    import time
    for i in range(11):
        cli_progressbar("testing progress bar: ", i, end_val=10)
        time.sleep(0.05)
    print

if __name__ == "__main__":
    test()
