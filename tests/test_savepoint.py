import os
import pytest
from savepoint import SavePoint


@pytest.fixture
def test_file():
    fpath = "test.p"
    if os.path.exists(fpath):
        os.remove(fpath)
    return fpath



def test_should_not_skip_code_if_state_doesnt_change(test_file):
    counter = []
    state = {}
    def fn():
        with SavePoint(test_file, state):
            counter.append(1)
    fn()
    fn()
    fn()
    assert counter == [1, 1, 1]


def test_should_skip_code_if_state_changes(test_file):
    counter = []
    state = {}
    def fn():
        with SavePoint(test_file, state):
            counter.append(1)
            state['changed'] = True
    fn()
    fn()
    fn()
    assert counter == [1]


def test_should_skip_code_if_state_changes(test_file):
    counter = []
    state = {}
    def fn():
        with SavePoint(test_file, state):
            counter.append(1)
            state['changed'] = True
    fn()
    fn()
    fn()
    assert counter == [1]


def test_should_not_skip_code_if_body_raises_exception(test_file):
    counter = []
    state = {}
    def fn():
        with SavePoint(test_file, state):
            raise ValueError("boom!")
            state['changed'] = True
    pytest.raises(ValueError, fn)
    pytest.raises(ValueError, fn)
    pytest.raises(ValueError, fn)
