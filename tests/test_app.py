from click.testing import CliRunner
from app import list, view, add, update, delete

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


def test_update():
    response = runner.invoke(update, ["test-user", "-m", "12345"])
    assert response.exit_code == 0
    assert "Contact updated!" in response.output
    assert "{'mobile': '12345'}" in response.output


def test_delete():
    response = runner.invoke(delete, "test-user")
    assert response.exit_code == 0
    assert "Contact deleted!" in response.output

    # call view on test-user to confirm it doesn't exist
    response = runner.invoke(view, "test-user")
    assert response.exit_code == 0
    assert "The contact you searched for does'nt exist" in response.output
