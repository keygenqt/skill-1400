import click

from tasks.src.chapter1.commands import cli_chapter1
from tasks.src.chapter10.commands import cli_chapter10
from tasks.src.chapter11.commands import cli_chapter11
from tasks.src.chapter12.commands import cli_chapter12
from tasks.src.chapter13.commands import cli_chapter13
from tasks.src.chapter14.commands import cli_chapter14
from tasks.src.chapter2.commands import cli_chapter2
from tasks.src.chapter3.commands import cli_chapter3
from tasks.src.chapter4.commands import cli_chapter4
from tasks.src.chapter5.commands import cli_chapter5
from tasks.src.chapter6.commands import cli_chapter6
from tasks.src.chapter7.commands import cli_chapter7
from tasks.src.chapter8.commands import cli_chapter8
from tasks.src.chapter9.commands import cli_chapter9


@click.group()
@click.pass_context
def cli(ctx):
    """Solving tasks from the book "1400 задач по программированию\""""


cli.add_command(cli_chapter1)
cli.add_command(cli_chapter2)
cli.add_command(cli_chapter3)
cli.add_command(cli_chapter4)
cli.add_command(cli_chapter5)
cli.add_command(cli_chapter6)
cli.add_command(cli_chapter7)
cli.add_command(cli_chapter8)
cli.add_command(cli_chapter9)
cli.add_command(cli_chapter10)
cli.add_command(cli_chapter11)
cli.add_command(cli_chapter12)
cli.add_command(cli_chapter13)
cli.add_command(cli_chapter14)

if __name__ == '__main__':
    cli(obj={})
