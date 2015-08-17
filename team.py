"""This script handles information pertaining to team data from The Blue
Alliance API
"""

from TBApython import API_URL
from TBApython import get_data
from TBApython.exceptions import TeamFormattingError
from TBApython.exceptions import YearsParticipatedFormattingError

class Team:
    """Model for team information from The Blue Alliance

    More information here.
    More information here.

    Attributes:
        website: String containing the official website associated with the
            team. Example: http://www.entech281.com
        name: String containing the official long form name registered with
            FIRST. Example: Michelin/Caterpillar/Greenville Technical College/
            Greenville...
        locality: String containing the city of team derived from parsing the
            address registered with FIRST. Example: Greenville
        region: String containing the state of team derived from parsing the
            address registered with FIRST. Example: SC
        country_name: String containing country of team derived from parsing
            the address registered with FIRST. Example: USA
        location: String containing the long form address that includes city,
            state, and country provided by FIRST. Example: Greenville, SC, USA
        team_number: Integer containing the official team number issued by
            FIRST. Example: 281
        key: String containing TBA team key with the format frcyyyy. Example:
            frc281
        nickname: String containing nickname provided by FIRST. Example: EnTech
            GreenVillians
        rookie_year: Integer containing the team's rookie year. Example: 1999
        events: list containing event objects the team is attending.
        matches: list containing match objects the team is participating in.
        awards: list containing award objects the team has won
        years_participated: list containing years in which the team
            participated.
    """

    # pylint: disable=R0902
    # All of these are available from the API and need to maintain constistency.

    def __init__(self, key=None):
        self.website = None
        self.name = None
        self.locality = None
        self.region = None
        self.team_number = None
        self.key = key
        self.nickname = None
        self.rookie_year = None
        self.events = []
        self.matches = []
        self.awards = []
        self.years_participated = []
        if key is not None:
            self.url = API_URL + 'team/' + key.lower()
            raw_data = get_data(self.url)
            self = self.team_from_raw_data(raw_data)
        else:
            return None

    def __repr__(self):
        return str(self.team_number)

    def team_from_raw_data(self, raw_data):
        """Populates team model from raw json data.

        Insert description here.

        Args:
            raw_data: string of json data

        Returns:
            self

        Raises:
            Raises a TeamFormattingError if raw_data doesn't have proper
            formatting.
        """
        try:
            self.website = raw_data['website']
            self.name = raw_data['name']
            self.locality = raw_data['locality']
            self.rookie_year = raw_data['rookie_year']
            self.region = raw_data['region']
            self.team_number = raw_data['team_number']
            self.location = raw_data['location']
            self.key = raw_data['key']
            self.country_name = raw_data['country_name']
            self.nickname = raw_data['nickname']
            return self
        except KeyError:
            raise TeamFormattingError()

    def get_events(self, year=None):
        """Retreives event json data from API.

        Insert description here.

        Args:
            Year: Integer containing year of interest. Example: 2015

        Returns:
            None

        Raises:
            None

        """
        from TBApython.event import Event

        self.events.clear()
        if year is not None:
            get_events_url = (API_URL + 'team/' + self.key + '/' + str(year) +
                              '/events')
        else:
            get_events_url = API_URL + 'team/' + self.key + '/events'
        get_events_raw_data = get_data(get_events_url)
        for event in get_events_raw_data:
            this_event = Event()
            this_event.event_from_raw_data(event)
            self.events.append(this_event)


    def get_matches(self, event_key):
        """Retreives match json data from API.

        Insert description here.

        Args:
            event_key: string containing key of event. Example: 2015papi

        Returns:
            None

        Raises:
            None

        """
        from TBApython.match import Match

        self.matches.clear()
        get_matches_url = (API_URL + 'team/' + self.key + '/event/' + event_key
                           + '/matches')
        get_matches_raw_data = get_data(get_matches_url)
        for match in get_matches_raw_data:
            this_match = Match()
            this_match.match_from_raw_data(match)
            self.matches.append(this_match)

    def get_awards(self, event_key=None):
        """Retreives awards json data from API.

        Insert description here.

        Args:
            event_key: string containing key of event. Example: 2015papi

        Returns:
            None

        Raises:
            None

        """
        from TBApython.award import Award

        self.awards.clear()
        if event_key is not None:
            get_awards_url = (API_URL + 'team/' + self.key + '/event/' +
                              event_key + '/awards')
        else:
            get_awards_url = API_URL + 'team/' + self.key + '/history/awards'
        get_awards_raw_data = get_data(get_awards_url)
        for award in get_awards_raw_data:
            this_award = Award()
            this_award.award_from_raw_data(award)
            self.awards.append(this_award)

    def get_years_participated(self):
        """Populates years participated from raw json data.

        Insert description here.

        Args:
            raw_data: string of json data

        Returns:
            self

        Raises:
            Raises a YearsParticipatedFormattingError if raw_data doesn't have
            proper formatting.
        """

        self.years_participated.clear()
        get_years_participated_url = (API_URL + 'team/' + self.key +
                                      '/years_participated')
        get_years_participated_raw_data = get_data(get_years_participated_url)
        try:
            self.years_participated = get_years_participated_raw_data
        except KeyError:
            raise YearsParticipatedFormattingError()

    # pylint: enable=R0902
