from ._version import __version_info__, __version__

__author__ = "Leonhard Neuhaus <neuhaus@lkb.upmc.fr>"
__license__ = "GNU General Public License 3 (GPLv3)"


#set up loggers
import logging
logging.basicConfig()
logger = logging.getLogger(name=__name__)
# only show errors or warnings until userdefine log level is set up
logger.setLevel(logging.INFO)

from .pysine import *
