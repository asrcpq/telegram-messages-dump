import os
import sys
import importlib
import logging
from tgbk.telegram_dumper import TelegramDumper
from tgbk.chat_dump_settings import ChatDumpSettings
from tgbk.chat_dump_metadata import DumpMetadata
from tgbk.exporter import text

def main():
	""" Entry point. """
	settings = ChatDumpSettings(__doc__)

	# define the console output verbosity
	default_format = '%(levelname)s:%(message)s'
	if settings.is_verbose:
		logging.basicConfig(format=default_format, level=logging.DEBUG)
	else:
		logging.basicConfig(format=default_format, level=logging.INFO)

	metadata = DumpMetadata(settings.out_file)

	# when user specified --continue
	if settings.is_incremental_mode and settings.last_message_id == -1:
		metadata.merge_into_settings(settings)

	exporter = text()
	sys.exit(TelegramDumper(os.path.basename(__file__), settings, metadata, exporter).run())
