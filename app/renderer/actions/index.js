import path from "path";

import * as ActionType from '../constants/ActionType'

export function explore(path) {
  return {
    type: ActionType.EXPLORE,
    path: path
  }
}

export function exploreUp() {
  return {
    type: ActionType.EXPLORE_UP
  }
}

export function viewBook(path) {
  return {
    type: ActionType.BOOK_VIEW,
    path: path
  }
};