import click
import sys
from polygon_mapper.src import get_url

@click.command()
@click.argument('coords', required=False)
@click.option('-p', is_flag=True, help='print output without launching')
def main(coords, p):
    """Opens a webbrowser displaying input polygon on a satellite map

    Example: 

    \b
    $ echo '[[4.33, 51.29], [4.33, 51.30], [4.35, 51.30], [4.35, 51.29], [4.33, 51.29]]' | polymap    
    $ polymap -p '[[4.33, 51.29], [4.33, 51.30], [4.35, 51.30], [4.35, 51.29], [4.33, 51.29]]' 
    """
    if not coords:
        if not sys.stdin.isatty():
            coords = sys.stdin.readline().strip()
        else:
            raise click.UsageError('Error: No polygon coordinates provided.\nSee polymap --help')

    try:
        url = get_url(coords)
    except Exception as e:
        click.echo('Error: {0}'.format(e))
        return None

    if p:
        click.echo('{0}'.format(url))
    else:
        click.launch('{0}'.format(url))
