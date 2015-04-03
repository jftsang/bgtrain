import os

DEBUG = 0

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

POSITIONS_VERSION_TO_USE_FOR_AUTO_SELECTION = 55

POSITIONS_VERSION_TO_USE = 4

CHEQUER_DECISION_PORTION = .85
TAKE_OR_DROP_DECISION_PORTION = .075

STD_THRESHOLD = .015
MAX_ATTEMPTS_FOR_INTERESTING = 15

EQUITY_DIFF_BOUNDS_FOR_CUBE_DECISION_INTEREST = (.010, .100)
EQUITY_DIFF_BOUNDS_FOR_CHECKER_DECISION_INTEREST = (.002, .100)
RATING_BOUND_FOR_POSITION_SELECTION = 50

SUBMISSIONS_LIMIT_FOR_LEADERBOARD = 10
LEADERBOARD_ROWS = 25

COMMENTS_LIST_ROWS = 25
COMMENTS_LIST_SUMMARY_LENGTH = 45

POSITION_HIST_ROWS = 10

NUMBER_OF_CANDIDATES = 15

RATING_DECREMENT_FOR_POS_SELECTION = 20.

PLY_PENALTY = .005

MAX_USERNAME_LENGTH_FOR_HOME_PAGE = 15
MAX_USERNAME_LENGTH_FOR_LEADERBOARD_PAGE = 80

PIPS_THRESHOLD = 181

POSITIONS_PER_CLUSTER = 5000

RATING_HISTORY_MAX_POINTS = 1000

