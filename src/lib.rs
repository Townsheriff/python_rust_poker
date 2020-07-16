#![feature(test)]

#[macro_use]
extern crate lazy_static;
extern crate test;
extern crate rand;
extern crate crossbeam;

mod hand_indexer;

pub use hand_indexer::hand_indexer_s;

pub mod hand_range;
pub mod constants;
pub mod hand_evaluator;

pub mod equity_calculator;
