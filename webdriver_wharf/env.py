import os

def str2bool(o):
    if isinstance(o, basestring):
        o = o.lower() in ['true', '1']
    return o

# Name of the docker image to use
image_name = os.environ.get('WEBDRIVER_WHARF_IMAGE', 'cfmeqe/sel_ff_chrome')

# Set to True if the container runs a VNC service
vnc_enabled = str2bool(os.environ.get('WEBDRIVER_WHARF_IMAGE_VNC_ENABLED',
    True))

# Set to True if the container runs an http service
http_enabled = str2bool(os.environ.get('WEBDRIVER_WHARF_IMAGE_HTTP_ENABLED',
    True))

# Number of containers to have on "hot standby" for checkout
pool_size = int(os.environ.get('WEBDRIVER_WHARF_POOL_SIZE', 4))

# Max time for an appliance to be checked out before it's forcibly checked in, in seconds.
max_checkout_time = int(os.environ.get('WEBDRIVER_WHARF_MAX_CHECKOUT_TIME', 3600))

# Interval to check for updates to the docker image (in seconds)
pull_interval = int(os.environ.get('WEBDRIVER_WHARF_IMAGE_PULL_INTERVAL', 3600))

# Interval to rebalance the active container pool
rebalance_interval = int(os.environ.get('WEBDRIVER_WHARF_REBALANCE_INTERVAL', 3600 * 6))
