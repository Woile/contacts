"""Main module."""
import click


@click.command()
@click.option('--count', default=1, help='Chupala gato')
def main(count):
    for x in range(count):
        click.echo('Counting %s' % x)

value = click.prompt('Please enter a valid integer', type=int)

if __name__ == '__main__':
    main()
