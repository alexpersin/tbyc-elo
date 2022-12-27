# parameters for the Elo algorithm -- setting kind of arbitrarily for now, should tune once we have more data
DEFAULT_K_VALUE = 80
DEFAULT_D_VALUE = 600
DEFAULT_SCORING_FUNCTION_BASE = 1.0
INITIAL_RATING = 1000

# Google Sheets info for reading input data
GSHEETS_CREDENTIALS_FILE = "./google-credentials.json"
SPREADSHEET_ID = "17em2c8aP1zPWXQSSEDTYau8yRhKCvKfvzWnyv1LEsys"
DATA_SHEET_ID = 302447166
DUMMY_PLAYER_NAME = "_dummy_"

# dashboard settings
DBC_THEME = "FLATLY"  # others I liked: DARKLY, SIMPLEX, LUMEN (https://bootswatch.com/flatly/)
PLOTLY_THEME = "plotly_white"
LOGO_PATH = "/assets/tbycsprints.png"
GITHUB_LOGO_PATH = "assets/GitHub-Mark-32px.png"
GITHUB_URL = "https://github.com/alexpersin/tbyc-elo"
TITLE = "TBYC Sprint 15 Rankings"
SUBTITLE = "Home of Uncommonly Smooth Sailing"
