import click

from arle.package import help_summary
from arle import output
from arle.utils import keyboard

# Asus ROG Linux Extras CLI
@click.group()
@click.option('--verbose', '-v', is_flag=True,
    help='Toggle verbosity')

# Set __doc__ for help
@output.Display.dynamic_docstring(help_summary)
def entry_point(verbose):
    # Print help summary!
    '''{0}'''
    # Set verbosity
    output.Display.set_verbosity(verbose);
    pass

@entry_point.command('kb-backlight')
@click.argument('value', nargs=1, type=click.Choice(['+', '-']))
def kb_backlight(value):
    '''[ARGS] +|- Control keyboard backlight'''
    backlight = keyboard.BackLight()
    # Use dictionary
    def opt(val):
        return {
            '+' : backlight.up,
            '-' : backlight.down
        }.get(val, '+')
    # Call method based on option
    opt(value)()


if __name__ == '__main__':
    entry_point()