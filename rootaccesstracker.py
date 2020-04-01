import os
import logging

STAGE = os.environ.get('Stage')
DEFAULT_REGION = 'us-east-1'

LOGGER = logging.getLogger()
LOGGER.handlers = []
dt_format = "[%(asctime)s][%(filename)s][%(levelname)s] %(message)s"
date_fmt = "%m-%d-%Y %H:%M:%S"
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(fmt=dt_format, datefmt=date_fmt))
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    This function will be triggered by a cloudwatch rule which monitors the console sign in event as Root
    or when MFA is disabled.
    :param event:
    :param context:
    :return:
    """
    try:
        if event.get('detail').get('eventName') == 'ConsoleLogin':
            LOGGER.info('AWS Root login detected')
        elif event.get('detail').get('eventName') == 'DeleteVirtualMFADevice' or event.get('detail').get('eventName') == "DeactivateMFADevice":
            LOGGER.info('MFA disablement has been detected')

    except Exception as exp:
        LOGGER.error(exp, exc_info=1)


