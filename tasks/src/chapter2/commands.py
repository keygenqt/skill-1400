from math import sqrt, sin, fabs

import click


@click.group(name='chapter2')
def cli_chapter2():
    """Formula calculations"""
    pass


@cli_chapter2.command()
def task_1_a():
    x = click.prompt('Please enter x', type=click.INT)
    y = 17 * (x ** 2) - 6 * x + 13
    click.echo('Result: {}'.format(y))


@cli_chapter2.command()
def task_1_b():
    a = click.prompt('Please enter a', type=click.INT)
    y = 3 * (a ** 2) + 5 * a - 21
    click.echo('Result: {}'.format(y))


@cli_chapter2.command()
def task_2():
    a = click.prompt('Please enter a', type=click.INT)
    y = ((a ** 2) + 10) / sqrt((a ** 2) + 1)
    click.echo('Result: {}'.format(y))


@cli_chapter2.command()
def task_3_a():
    a = click.prompt('Please enter a', type=click.INT)
    y = sqrt((2 * a + sin(fabs(3 * a))) / 3.56)
    click.echo('Result: {}'.format(y))


@cli_chapter2.command()
def task_3_b():
    x = click.prompt('Please enter x', type=click.INT)
    y = (3.2 + sqrt(1 + x)) / fabs(5 * x)
    click.echo('Result: {}'.format(y))


@cli_chapter2.command()
def task_4():
    pass


@cli_chapter2.command()
def task_5():
    pass


@cli_chapter2.command()
def task_6():
    pass


@cli_chapter2.command()
def task_7():
    pass


@cli_chapter2.command()
def task_8():
    pass


@cli_chapter2.command()
def task_9():
    pass


@cli_chapter2.command()
def task_10():
    pass


@cli_chapter2.command()
def task_11():
    pass


@cli_chapter2.command()
def task_12():
    pass


@cli_chapter2.command()
def task_13():
    pass


@cli_chapter2.command()
def task_14():
    pass


@cli_chapter2.command()
def task_15():
    pass


@cli_chapter2.command()
def task_16():
    pass


@cli_chapter2.command()
def task_17():
    pass


@cli_chapter2.command()
def task_18():
    pass


@cli_chapter2.command()
def task_19():
    pass


@cli_chapter2.command()
def task_20():
    pass


@cli_chapter2.command()
def task_21():
    pass


@cli_chapter2.command()
def task_22():
    pass


@cli_chapter2.command()
def task_23():
    pass


@cli_chapter2.command()
def task_24():
    pass


@cli_chapter2.command()
def task_25():
    pass


@cli_chapter2.command()
def task_26():
    pass


@cli_chapter2.command()
def task_27():
    pass


@cli_chapter2.command()
def task_28():
    pass


@cli_chapter2.command()
def task_29():
    pass


@cli_chapter2.command()
def task_30():
    pass


@cli_chapter2.command()
def task_31():
    pass


@cli_chapter2.command()
def task_32():
    pass


@cli_chapter2.command()
def task_33():
    pass


@cli_chapter2.command()
def task_34():
    pass


@cli_chapter2.command()
def task_35():
    pass


@cli_chapter2.command()
def task_36():
    pass


@cli_chapter2.command()
def task_37():
    pass


@cli_chapter2.command()
def task_38():
    pass
