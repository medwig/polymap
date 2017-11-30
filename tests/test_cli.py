import pytest
from click.testing import CliRunner
from polygon_mapper import cli


@pytest.fixture
def runner():
    return CliRunner()

def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['[[4.33, 51.29], [4.33, 51.30], [4.35, 51.30], [4.35, 51.29], [4.33, 51.29]]', '-p'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'https://www.keene.edu/campus/maps/tool/?coordinates=4.33%2C%2051.29%0A4.33%2C%2051.3%0A4.35%2C%2051.3%0A4.35%2C%2051.29%0A4.33%2C%2051.29%0A'
