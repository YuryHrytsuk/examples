import multiprocessing

import click

from examples.web import WebApplication, create_app


@click.group()
def cli():
    pass


@cli.command()
def start_server():
    options = {
        "bind": "%s:%s" % ("127.0.0.1", "8080"),
        "workers": (multiprocessing.cpu_count() * 2) + 1,
    }
    WebApplication(create_app(), options).run()


if __name__ == "__main__":
    cli()
