import click

from tasks.src.chapter1.commands import cli_chapter1


@click.group()
@click.pass_context
def cli(ctx):
    """Solving tasks from the book "1400 задач по программированию" Zlatopolsky Dmitry Mikhailovich"""


cli.add_command(cli_chapter1)

if __name__ == '__main__':
    cli(obj={})
