import click


@click.group(name='chapter1')
def cli_chapter1():
    """Chapter 1. Displaying information on the screen."""
    pass


@cli_chapter1.command()
def task_1():
    """The task in the book: 1.1"""
    click.echo(' '.join(str(i) for i in [31, 18, 79]))
