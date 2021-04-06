import math

import click


@click.group(name='chapter1')
def cli_chapter1():
    """Displaying information on the screen"""
    pass


@cli_chapter1.command()
def task_1():
    click.echo(' '.join(str(i) for i in [31, 18, 79]))


@cli_chapter1.command()
def task_2():
    click.echo('  '.join(str(i) for i in [47, 52, 150]))


@cli_chapter1.command()
def task_3():
    click.echo('\n'.join(str(i) for i in [50, 10]))


@cli_chapter1.command()
def task_4():
    click.echo('\n'.join(str(i) for i in [5, 10, 21]))


@cli_chapter1.command()
def task_5():
    click.echo('\n \n'.join(str(i + 1) for i in range(2)))


@cli_chapter1.command()
def task_6():
    click.echo('{:.3f}'.format(math.pi))


@cli_chapter1.command()
def task_7():
    click.echo('{:.1f}'.format(math.e))


@cli_chapter1.command()
def task_8():
    value = click.prompt('Please enter number', type=click.INT)
    click.echo('Your number: {}'.format(value))


@cli_chapter1.command()
def task_9():
    value = click.prompt('Please enter number', type=click.INT)
    click.echo('{} - your number'.format(value))


@cli_chapter1.command()
def task_10():
    value = click.prompt('Please enter name', type=click.STRING)
    click.echo('Your name: {}'.format(value.strip().capitalize()))


@cli_chapter1.command()
def task_11():
    value = click.prompt('Please enter football team', type=click.STRING)
    click.echo('{} - it\'s winner!'.format(value.strip().capitalize()))


@cli_chapter1.command()
def task_12():
    value = click.prompt('Please enter name', type=click.STRING)
    click.echo('Hello {}!'.format(value.strip().capitalize()))


@cli_chapter1.command()
def task_13():
    value = click.prompt('Please enter number', type=click.INT)
    click.echo('After number {} - {}'.format(value, value + 1))
    click.echo('Before number {} - {}'.format(value, value - 1))
