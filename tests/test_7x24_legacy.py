"""Testing legacy API with a 24x7 SLA."""
__author__ = "Andrea Dainese"
__contact__ = "andrea@adainese.it"
__copyright__ = "Copyright 2022, Andrea Dainese"
__license__ = "GPLv3"

import datetime
import sla_checker


def test_solved_within_the_day():
    """Ticket is solved within the day."""
    sla = sla_checker.SLAChecker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 0),
            minutes_to_resolve=120,
        )
        is True
    )


def test_failed_within_the_day():
    """SLA exceeded within the day."""
    sla = sla_checker.SLAChecker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 1),
            minutes_to_resolve=120,
        )
        is False
    )


def test_solved_between_days():
    """Ticket is solved across days."""
    sla = sla_checker.SLAChecker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 22, 0, 0),
            event_end=datetime.datetime(2019, 12, 14, 1, 0, 0),
            minutes_to_resolve=180,
        )
        is True
    )


def test_failed_between_days():
    """SLA exceeded across days."""
    sla = sla_checker.SLAChecker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 22, 0, 0),
            event_end=datetime.datetime(2019, 12, 14, 1, 0, 1),
            minutes_to_resolve=180,
        )
        is False
    )
