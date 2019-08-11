# pyinstaller matters
# must explicitly import all commands

from . import master
from . import gateway
from . import strategy
from . import watcher
from . import controller

from kungfu.command.extension import __all__
from kungfu.command.journal import __all__
from kungfu.command.backtest import __all__

from kungfu.command.dev import __all__
