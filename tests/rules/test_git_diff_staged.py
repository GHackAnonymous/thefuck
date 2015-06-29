import pytest
from thefuck.rules.git_diff_staged import match, get_new_command
from tests.utils import Command


@pytest.mark.parametrize('command', [
    Command(script='git diff'),
    Command(script='git df'),
    Command(script='git ds')])
def test_match(command):
    assert match(command, None)


@pytest.mark.parametrize('command', [
    Command(script='git tag'),
    Command(script='git branch'),
    Command(script='git log')])
def test_not_match(command):
    assert not match(command, None)


@pytest.mark.parametrize('command, new_command', [
    (Command('git diff'), 'git diff --staged'),
    (Command('git df'), 'git df --staged'),
    (Command('git ds'), 'git ds --staged')])
def test_get_new_command(command, new_command):
    assert get_new_command(command, None) == new_command
