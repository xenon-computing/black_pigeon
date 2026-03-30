import time
import os

class TrailingMarker:
    Exif_marker = "ffd9"
    EOI_marker = "0000000049454E44AE426082"


INTER_REP_NAME = "secret.zip"
NAME_PREFS = "secret"
INTER_PATH = "/"

DEF_OUTPUT_NAME = "{}—{}".format(
        NAME_PREFS, time.strftime(
            "%s"
            )
        )

DEF_OUTPUT_PATH = os.getcwd()

DEF_PASSWORD = "sEcrEt_cOdE"
KEEP_SOURCE_COPY = True
