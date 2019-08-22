from click.testing import CliRunner
from app import list, view, add, update, delete
import pdb
runner = CliRunner()


def test_add():
    response = runner.invoke(add, ["test-user", "-m", "0"])
    assert response.exit_code == 0
    assert "Contact test-user added!" in response.output
    assert "{'mobile': '0'}" in response.output

def test_list():
    response = runner.invoke(list)
    assert response.exit_code == 0
    assert "Here\'s a list of all your contacts:" in response.output
    assert "'test-user': {'mobile': '0'}" in response.output

def test_view():
    response = runner.invoke(view, "test-user")
    assert response.exit_code == 0
    assert "{'mobile': '0'}" in response.output
