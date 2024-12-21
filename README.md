# RustPoker

[![Build Status](https://travis-ci.org/kmurf1999/rust_poker.svg?branch=master)](https://travis-ci.org/kmurf1999/rust_poker)
[![docs.rs](https://docs.rs/rust_poker/badge.svg)](https://docs.rs/rust_poker)
[![crates.io](https://img.shields.io/crates/v/rust_poker.svg)](https://crates.io/crates/rust_poker)

A poker library written in rust.

 - Multithreaded range vs range equity calculation
 - Fast hand evaluation
 - Efficient hand indexing

## Developing Bindings

Use virtual env `virtualenv .venv`.

Enable the envirnmoent `source .venv/bin/activate`

Run `maturin develop` to create ptyhon lib with bindings, it will automatically put it inside the python packages dir.

To test out point the ipynb notebooks kernel to virtualenv and then just run the package.

To install pytohn packages `pip install poetry && poetry install --no-root`

## Hand Evaluator

Evaluates the strength of any poker hand using up to 7 cards.

### Usage

```python
import pyrust_poker

keep_cards_mask = np.zeros(shape=(2, 52), dtype=np.uint64)

keep_cards_mask[0, [0, 4, 8, 12, 48]] = 1 # 36865 - straight flush 5 high
keep_cards_mask[1, [48, 44, 40, 36, 32]] = 1 # 36874 - straight flush S high

pyrust_poker.get_hand_strengths(keep_cards_mask)
```

## Equity Calculator

Calculates the range vs range equities for up to 6 different ranges specified by equilab-like range strings.
Supports monte-carlo simulations and exact equity calculations

## Credit

The hand evaluator and equity calculator library is a rust rewrite of **zekyll's** C++ equity calculator, [OMPEval](https://github.com/zekyll/OMPEval)

## License

This project is MIT Licensed

Copyright (c) 2020 Kyle Murphy
