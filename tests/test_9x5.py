"""Testing legacy API with a 9x5 SLA."""
__author__ = "Andrea Dainese"
__contact__ = "andrea@adainese.it"
__copyright__ = "Copyright 2022, Andrea Dainese"
__license__ = "GPLv3"

import datetime
import sla_checker


def test_solved_within_the_working_day():
    """Ticket is solved within the day."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 0),
            minutes_to_resolve=120,
        )
        is True
    )


def test_failed_within_the_working_day():
    """SLA exceeded within the day."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 1),
            minutes_to_resolve=120,
        )
        is False
    )


def test_solved_between_working_days():
    """Ticket is solved across days."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 17, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 0),
            minutes_to_resolve=180,
        )
        is True
    )


def test_failed_between_working_days():
    """SLA exceeded across days."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 17, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 1),
            minutes_to_resolve=180,
        )
        is False
    )


def test_solved_before_working_days():
    """Ticket opened before opening hour is solved within the day."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 1, 0, 0),
            event_end=datetime.datetime(2019, 12, 12, 11, 0, 0),
            minutes_to_resolve=120,
        )
        is True
    )


def test_failed_before_working_days():
    """SLA exceeded within the day when ticket is opened before opening hours."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 1, 0, 0),
            event_end=datetime.datetime(2019, 12, 12, 11, 0, 1),
            minutes_to_resolve=120,
        )
        is False
    )


def test_solved_after_working_days():
    """Ticket opened after closing hour is solved within the next working day."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 21, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 0),
            minutes_to_resolve=120,
        )
        is True
    )


def test_failed_after_working_days():
    """SLA exceeded within the next working day when ticket is opened after closing hours."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 21, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 1),
            minutes_to_resolve=120,
        )
        is False
    )


def test_solved_across_holidays():
    """Ticket opened before holidays is solved within the next working day."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2020, 12, 24, 17, 0, 0),
            event_end=datetime.datetime(2020, 12, 28, 10, 0, 0),
            minutes_to_resolve=120,
        )
        is True
    )


def test_failed_across_holidays():
    """SLA exceeded within the next working day when ticket is opened before holidays."""
    sla = sla_checker.SLAChecker(
        country_code="IT",
        opening_hours=datetime.time(9, 0),
        closing_hours=datetime.time(18, 0),
        working_on_sat=False,
        working_on_holidays=False,
    )
    assert (
        sla.check(
            event_start=datetime.datetime(2020, 12, 24, 17, 0, 0),
            event_end=datetime.datetime(2020, 12, 28, 10, 0, 1),
            minutes_to_resolve=120,
        )
        is False
    )
