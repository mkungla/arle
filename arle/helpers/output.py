from click import secho

class Output(object):
    """The Output object

    Attributes:
        _verbose: A boolean either output is verbose or not.
    """

    def set_verbosity(self, verbose):
        """Set output verbosity."""
        self._verbose = verbose
        if(verbose):
            self.info('Enabling verbose output!')

    @staticmethod
    def dynamic_docstring(*sub):
        """Add dynamic variables to __doc__ which are shown by click help"""
        def __docstring(obj):
            obj.__doc__ = obj.__doc__.format(*sub)
            return obj
        return __docstring

    def info(self, msg):
        """Prints info message"""
        self.message(msg, 'cyan', 'info')

    def ok(self, msg):
        """Prints ok message"""
        self.message(msg, 'green', 'ok')

    # WARNING Messages
    def warning(self, msg):
        """Prints warning message"""
        self.message(msg, 'yellow', 'warning')

    # ERROR Messages
    def error(self, msg):
        """Prints error message"""
        self.message(msg, 'red', 'error')

    def message(self, msg, fg = 'white', status = 'debug'):
        """Prints message"""

        # should message be printed
        if self._verbose is False:
            return

        # Message format
        display_message = "[ARLE][ %s ]: %s" %('{{0: <{}}}'.format(8).format(status), msg)

        # Use click secho to print output
        secho(display_message, fg = fg)

# Initialize display
Display = Output();
