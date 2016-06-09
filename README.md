savepoint
=========

A context manager that creates savepoints, avoiding recalculating expensive parts of the code. Useful if you're running a script several times while developing it.

An example:

```python
from savepoint import SavePoint

state = {
    'a': 10,
    'b': 20
}
# do some expensive calculation here
with SavePoint("stuff.p", state):
    print "doing stuff"
    state['a'] += 10

print state['a'], state['b']
```

We now run the script twice:

```bash
$ python script.py
doing stuff
20 20

$ python script.py
20 20
```

The first time the code is ran the ``with`` block is executed, and the modifed `state` variable is pickled to ``stuff.p`` -- it is only picked if the `state` variable changes! Subsequent runs will update the `state` variable from the pickle file and skip the block completely.

Note that only changes in the `state` variable are stored, but not file modifications and other side effects of the block. Also, if the original input is different the code will fail.
