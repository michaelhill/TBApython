"""This script handles information pertaining to match data from The Blue
Alliance API
"""

from TBApython import API_URL
from TBApython import get_data
from TBApython.exceptions import MatchFormattingError

class Match:
    """Model for match information from The Blue Alliance

    More information here.
    More information here.

    Attributes:
        key: String containing TBA event key with the format
            yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER], where yyyy is the
            year, and EVENT_CODE is the event code of the event, COMP_LEVEL is
            (qm, ef, qf, sf, f), and MATCH_NUMBER is the match number in the
            competition level. A set number may append the competition level if
            more than one match is required per set. Example: 2010sc_qm10,
            2011nc_qf1m2
        comp_level: String containing the competition level the match was
            played at. Example: qm, ef, qf, sf, f
        set_number: Integer containing the set number in a series of matches
            where more than one match is required in the match series. Example:
            2010sc_qf1m2, would be match 2 in quarter finals 1.
        match_number: Integer containing the match number of the match in the
            competition level. Example: 2010sc_qm20 *would be 20)
        alliances: List of alliances, the teams on the alliances and their
            score.
        score_breakdown: Score breakdown for auto, teleop, etc. Points. Varies
            from year to year. May be null.
        event_key: Event key of the event the match was played at. Example:
            2011sc
        videos: JSON array of videos assoiated with this match and
            corresponding information. Example: "videos": [{"key":
            "xswGjxzNEoY", "type": "youtube"}, {"key":
            "http://videos.thebluealliance.net/2010cmp/2010cmp_f1m1.mp4",
            "type": "tba"}]
        time_string: Time string for this match as published on the official
            schedule. Of course this may or may not be accurate, as events
            often run ahead or behind schedule. Example: 11:15 AM
        time: Integer containing UNIX timestamp of match time, as taken from
            the published schedule.
    """

    # pylint: disable=R0902, R0903
    # All of these are available from the API and need to maintain constistency.

    def __init__(self, key=None):
        self.key = key
        self.comp_level = None
        self.set_number = None
        self.match_number = None
        self.alliances = None
        self.score_breakdown = None
        self.event_key = None
        self.videos = None
        self.time_string = None
        self.time = None
        if key is not None:
            self.url = API_URL + 'match/' + key.lower()
            raw_data = get_data(self.url)
            self = self.match_from_raw_data(raw_data)
        else:
            return None

    def __repr__(self):
        return self.key

    def match_from_raw_data(self, raw_data):
        """Populates match model from raw json data.

        Insert description here.

        Args:
            raw_data: string of json data

        Returns:
            self

        Raises:
            Raises a MatchFormattingError if raw_data doesn't have proper
            formatting.

        """
        try:
            self.comp_level = raw_data['comp_level']
            self.match_number = raw_data['match_number']
            self.videos = raw_data['videos']
            self.time_string = raw_data['time_string']
            self.set_number = raw_data['set_number']
            self.key = raw_data['key']
            self.time = raw_data['time']
            self.score_breakdown = raw_data['score_breakdown']
            self.alliances = raw_data['alliances']
            self.event_key = raw_data['event_key']
            return self
        except KeyError:
            raise MatchFormattingError()

    # pylint: enable=R0902, R0903
    # All of these are available from the API and need to maintain constistency.
    