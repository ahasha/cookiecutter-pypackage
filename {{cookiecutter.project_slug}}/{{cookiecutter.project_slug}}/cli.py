{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
"""Usage: {{cookiecutter.project_cli}} [-vqrh] [FILE] ...
          {{cookiecutter.project_cli}} (--left | --right) CORRECTION FILE
Process FILE and optionally apply correction to either left-hand side or
right-hand side.
Arguments:
  FILE        optional input file
  CORRECTION  correction angle, needs FILE, --left or --right to be present
Options:
  -h --help
  -v       verbose mode
  -q       quiet mode
  -r       make report
  --left   use left-hand side
  --right  use right-hand side
"""
{%- else %}
"""Console script for {{cookiecutter.project_slug}}."""
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
from docopt import docopt
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""

    arguments = docopt(__doc__)
    print("Arguments: " + str(arguments))
    print("Change this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    print("See docopt documentation at http://docopt.org/")

{%- endif %}

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
