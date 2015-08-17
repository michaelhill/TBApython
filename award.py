"""This scripts holds information pertaining to award data from The Blue
Alliance API
"""
# pylint: disable=R0903


class Award(object):
    """Model for award information from The Blue Alliance

    More information here.
    More information here.

    Attributes:
        name: String containing the name of the award from TIMS. May vary for
            the same award type. Example: Engineering Inspiration
        award_type: Integer that represents the award type as a constant.
        event_key: String containing the event_key of the event the award was
            won. Example: 2011sc
        recipient_list: A list of recipients of the award at the event. Either
            team_number or awardee for the individual awards. Example:
            {"team_number": 281, "awardee": null}
        year: Integer containing the year this award was won. Example: 2010

    """

    def __init__(self):
        self.name = None
        self.award_type = None
        self.event_key = None
        self.recipient_list = None
        self.year = None
        return None

    def __repr__(self):
        return "%s %s" % (self.event_key, self.name)

    def award_from_raw_data(self, raw_data):
        """Populates award model from raw json data.

        Insert description here.

        Args:
            raw_data: string of json data

        Returns:
            self

        Raises:
            Raises a KeyError if raw_data doesn't have proper formatting.

        """
        try:
            self.name = raw_data['name']
            self.award_type = raw_data['award_type']
            self.event_key = raw_data['event_key']
            self.recipient_list = raw_data['recipient_list']
            self.year = raw_data['year']
            return self
        except KeyError:
            print("ERROR: Award data is not properly formatted.")

# pylint: enable=R0903
