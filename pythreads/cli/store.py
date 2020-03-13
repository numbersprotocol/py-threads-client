import click

from pythreads import Client
from pythreads.cli.main import cli


@cli.group()
@click.option('--local', default=True)
@click.pass_context
def store(ctx, local):
    ctx.ensure_object(dict)
    ctx.obj['local'] = local
    if local:
        client = Client()
    ctx.obj['client'] =  client


@store.command()
@click.option('--id', prompt=True)
@click.pass_context
def link(ctx, id):
    client = ctx.obj['client']
    if ctx.obj['local']:
        client.start(id)
    links = client.get_store_link(id)
    for link in links:
        print('{}\n'.format(link))


@store.command()
@click.option('--id', prompt=True)
@click.option('--model', '-m', prompt=True)
@click.pass_context
def ls(ctx, id, model):
    client = ctx.obj['client']
    if ctx.obj['local']:
        client.start(id)
    models = client.model_find(id, model)
    for model in models:
        print('{}\n'.format(model))
