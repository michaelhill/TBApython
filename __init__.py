"""This script sets up the API for The Blue Alliance"""

import json
import urllib.request
import os
from TBA.exceptions import APIUnavailableError
from TBA.exceptions import ResourceUnavailableError
from TBA.exceptions import UnexpectedDataError
from TBA.exceptions import APPIDNotSetError

API_URL = 'http://www.thebluealliance.com/api/v2/'

try:
    # Set your own APPID as the environment variable 'TBA_APPID'
    API_APPID = os.environ['TBA_APPID']
except KeyError:
    # Set your own APPID.  Example of a valid one is frc281:scouting-system:v01
    # Valid format is <team/person id>:<app description>:<version>
    API_APPID = ''

def get_data(url):
    """Retrieves JSON data from TBA API



    Args:
        raw_data: string of json data

    Returns:
        self

    Raises:
        Raises a KeyError if raw_data doesn't have proper formatting.

    """
    if API_URL is  '':
        raise APPIDNotSetError()
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'X-TBA-App-Id': API_APPID
        }
    )

    try:
        response = urllib.request.urlopen(req)
        str_response = response.readall().decode('utf-8')
        return json.loads(str_response)
    except urllib.error.HTTPError:
        raise ResourceUnavailableError(url=url)
    except urllib.error.URLError:
        raise APIUnavailableError()
    except ValueError:
        raise UnexpectedDataError(url=url)
