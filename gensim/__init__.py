"""
This package contains interfaces and functionality to compute pair-wise document
similarities within a corpus of documents.
"""

from gensim import parsing, matutils, interfaces, corpora, models, similarities, summarization
import logging

__version__ = '2.1.0'

class NullHandler(logging.Handler):
    """For python versions <= 2.6; same as `logging.NullHandler` in 2.7."""
    def emit(self, record):
        pass

logger = logging.getLogger('gensim')
if len(logger.handlers) == 0:	# To ensure reload() doesn't add another one
    logger.addHandler(NullHandler())
