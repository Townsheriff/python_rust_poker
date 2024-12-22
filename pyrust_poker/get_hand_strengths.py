import numpy as np
from .pyrust_poker import poker_hand, evaluate_list

poker_keys = np.array([card.key for card in poker_hand.get_cards()], dtype=np.uint64)
poker_mask = np.array([card.mask for card in poker_hand.get_cards()], dtype=np.uint64)


def get_hand_strengths(hand_masks: np.array):
  """Maps hand mask to poker rank strength

  Args:
      hand_masks (np.array(n, 52)): every n element contains an independent hand mask containing 52 cards
      0 index - 2 of a suite one
      1 index - 3 of a suite two
      ...
      12 index - ace of suite one
      ...
      51 index - ace of of suite 4
      
  Returns:
      (np.array(n, 1): for every n hand masked is mapped to an absolute value u16 for hand strength. 
      To determine which hand is stronger just compare with ><= operators
  """
  # avoids floating point errors
  hand_masks = hand_masks.astype(np.bool)
  
  keep_keys = np.multiply(poker_keys, hand_masks).astype(np.uint64)
  keep_mask = np.multiply(poker_mask, hand_masks).astype(np.uint64)
  
  hand = poker_hand.Hand()
  
  all_cards_sum = hand.key + np.sum(keep_keys, axis=1)
  all_cards_mask = np.bitwise_or.reduce(keep_mask, axis=1)
  
  eval_list = list(zip(all_cards_sum, all_cards_mask))
  
  return evaluate_list(eval_list)