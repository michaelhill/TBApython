"""This script handles information pertaining to event data from The Blue
Alliance API
"""

from TBA import API_URL
from TBA import get_data
from TBA.exceptions import EventFormattingError
from TBA.exceptions import StatsFormattingError

class Event:
    """Model for event information from The Blue Alliance

    More information here.
    More information here.

    Attributes:
        key: String containing TBA event key with the format yyyy[EVENT_CODE],
            where yyyy is the year, and EVENT_CODE is the event code of the
            event. Example: 2010sc
        name: String containing the official name of event on record either
            provided by FIRST or organizers of offseason event. Example:
            Palmetto Regional
        short_name: String containing name but doesn't include event
            specifiers, such as 'Regional' or 'District'. May be null.
            Example: Palmetto
        event_code: String containing event short code. Example: SC
        event_type_string: A human readable string that defines the event type.
            Example: 'Regional', 'District', 'District Championships'.
        event_type: An integer that represents the event type as a constant.
            Event Types:
                0: Regional
                1: District
                2: District CMP
                3: CMP Division
                4: CMP Finals
                99: Offseason
                100: Preseason
                -1: Unlabeled
        event_district_string: A human readable string that defines the event's
            district. Example: 'Michigan', 'Mid Atlantic', null (if regional)
        event_district: An integer that represents the event district as a
            constant.
            Event Districts:
                0: No District
                1: Michigan
                2: Mid Atlantic
                3: New England
                4: Pacific Northwest
                5: Indiana
        year: Integer containing the year the event data is for. Example: 2015
        location: String containing the long form address that includes city,
            and state provided by FIRST. Example: Clemson, SC
        venue_address: String containing address of the event's venue, if
            available. Line breaks included. Example: Long Beach Arena\n300
            East Ocean Blvd\nLong Beach, CA 90802\nUSA
        website: String containing the event's website, if any. Example:
            http://www.firstsv.org
        official: Boolean containing whether this is a FIRST official event, or
            an offseason event.
        teams: List of team models that attended the event.
        matches: List of match models for the event.
        webcast: If the event has webcast data associated with it, this
            contains JSON data of the streams
        alliances: If we have alliance selection data for this event, this
            contains a JSON array of the alliances. The captain is the first
            team, followed by their picks, in order.
        district_points: If this event is part of a district, this contains
            the number and breakdown of points that each team attending earned.
        stats: JSON containing events statistics
    """
    # pylint: disable=R0902
    # All of these are available from the API and need to maintain constistency.

    def __init__(self, key=None):
        self.key = key
        self.name = None
        self.short_name = None
        self.event_code = None
        self.event_type_string = None
        self.event_type = None
        self.event_district_string = None
        self.event_district = None
        self.year = None
        self.location = None
        self.venue_address = None
        self.website = None
        self.official = None
        self.teams = []
        self.matches = []
        self.awards = []
        self.webcast = None
        self.alliances = None
        self.district_points = None
        self.stats = None
        if key is not None:
            self.url = API_URL + 'event/' + key.lower()
            raw_data = get_data(self.url)
            self = self.event_from_raw_data(raw_data)
        else:
            return None

    def __repr__(self):
        return self.key

    def event_from_raw_data(self, raw_data):
        """Populates event model from raw json data.

        Insert description here.

        Args:
            raw_data: string of json data

        Returns:
            self

        Raises:
            Raises a EventFormattingError if raw_data doesn't have proper
            formatting.

        """
        try:
            self.key = raw_data['key']
            self.website = raw_data['website']
            self.official = raw_data['official']
            self.end_date = raw_data['end_date']
            self.name = raw_data['name']
            self.short_name = raw_data['short_name']
            self.facebook_eid = raw_data['facebook_eid']
            self.event_district_string = raw_data['event_district_string']
            self.venue_address = raw_data['venue_address']
            self.event_district = raw_data['event_district']
            self.location = raw_data['location']
            self.event_code = raw_data['event_code']
            self.year = raw_data['year']
            self.webcast = raw_data['webcast']
            self.alliances = raw_data['alliances']
            self.event_type_string = raw_data['event_type_string']
            self.start_date = raw_data['start_date']
            self.event_type = raw_data['event_type']
            return self
        except KeyError:
            raise EventFormattingError()

    def get_teams(self):
        """Retreives team json data from API.

        Insert description here.

        Args:
            None

        Returns:
            None

        Raises:
            None

        """
        from TBA.team import Team

        self.teams.clear()
        get_teams_url = API_URL + 'event/' + self.key + '/teams'
        get_teams_raw_data = get_data(get_teams_url)
        for team in get_teams_raw_data:
            this_team = Team()
            this_team.team_from_raw_data(team)
            self.teams.append(this_team)

    def get_matches(self):
        """Retreives match json data from API.

        Insert description here.

        Args:
            None

        Returns:
            None

        Raises:
            None

        """

        from TBA.match import Match

        self.matches.clear()
        get_matches_url = API_URL + 'event/' + self.key + '/matches'
        get_matches_raw_data = get_data(get_matches_url)
        for match in get_matches_raw_data:
            this_match = Match()
            this_match.match_from_raw_data(match)
            self.matches.append(this_match)

    def get_awards(self):
        """Retreives awards json data from API.

        Insert description here.

        Args:
            None

        Returns:
            None

        Raises:
            None

        """
        from TBA.award import Award

        self.awards.clear()
        get_awards_url = API_URL + 'event/' + self.key + '/awards'
        get_awards_raw_data = get_data(get_awards_url)
        for award in get_awards_raw_data:
            this_award = Award()
            this_award.award_from_raw_data(award)
            self.awards.append(this_award)

    def get_stats(self):
        """Retreives stats json data from API.

        Insert description here.

        Args:
            None

        Returns:
            None

        Raises:
            Raises a StatsFormattingError if raw_data doesn't have proper
            formatting.

        """
        get_stats_url = API_URL + 'event/' + self.key + '/stats'
        get_stats_raw_data = get_data(get_stats_url)
        try:
            self.stats = get_stats_raw_data
        except KeyError:
            raise StatsFormattingError()

    # pylint: enable=R0902
