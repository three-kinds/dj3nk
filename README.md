# dj3nk

`dj3nk` is an ID generation algorithm, the principle of which is from [nightteam](https://www.v2ex.com/t/686977).

## Install

```shell script
pip install dj3nk

```

## Examples

```python
# settings.py
NATURAL_KEY = {
    "increment_main_key": "a3:dj:nk",
    "random_bit_length": 16,
    "puzzle_count": 1000000,
    "rdb_conf_name": "default"
}

# models
from dj3nk import NKModel


class XXX(NKModel):
    ...

```
