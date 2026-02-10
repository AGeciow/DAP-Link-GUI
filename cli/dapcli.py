import click
from backend.pyocd_backend import PyOCDBackend


@click.group()
def cli():
    pass


@cli.command()
def list():
    for p in PyOCDBackend().list_probes():
        click.echo(p)


@cli.command()
@click.argument("firmware")
def flash(firmware):
    b = PyOCDBackend()
    b.connect()
    b.flash(firmware)
    b.reset()
    b.disconnect()
    click.echo("Flash OK")


if __name__ == "__main__":
    cli()
