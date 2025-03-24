# dj3nk

[English](README.md) | 简体中文

`dj3nk`是一个ID生成算法，它的理念来自[nightteam](https://www.v2ex.com/t/686977)。

## 1. 简介

* 可以使用`NaturalKeyGenerator`生成自增ID
* 在使用Django ORM时，可以继承`NKModel`类，自动生成自增ID

## 2. 使用

### 安装

```shell
pip install dj3nk

```

### 样例

* 直接使用

```python
from dj3nk.natural_key_generator import NaturalKeyGenerator

# 可选，重新配置
CONFIG = {
    "increment_main_key": "dj3nk",
    "random_bit_length": 16,
    "puzzle_count": 1000000,
    "rdb_conf_name": "default"
}

g = NaturalKeyGenerator(config=CONFIG)
g.generate_nk()

```

* 在Django ORM中使用

```python
# 可选，在settings.py中配置
DJ3NK = {
    "increment_main_key": "dj3nk",
    "random_bit_length": 16,
    "puzzle_count": 1000000,
    "rdb_conf_name": "default"
}

# models
from dj3nk.nk_model import NKModel


class XXX(NKModel):
    ...

```
