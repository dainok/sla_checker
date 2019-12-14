import datetime
import sla_checker


def test_solved_within_the_working_day():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 0),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is True
    )


def test_failed_within_the_working_day():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 1),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is False
    )


def test_solved_between_working_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 17, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 0),
            country_code="IT",
            minutes_to_resolve=180,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is True
    )


def test_failed_between_working_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 17, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 1),
            country_code="IT",
            minutes_to_resolve=180,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is False
    )


def test_solved_before_working_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 1, 0, 0),
            event_end=datetime.datetime(2019, 12, 12, 11, 0, 0),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is True
    )


def test_failed_before_working_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 1, 0, 0),
            event_end=datetime.datetime(2019, 12, 12, 11, 0, 1),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is False
    )


def test_solved_after_working_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 21, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 0),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is True
    )


def test_failed_after_working_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 12, 21, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 11, 0, 1),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is False
    )


def test_solved_across_holidays():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2020, 12, 24, 17, 0, 0),
            event_end=datetime.datetime(2020, 12, 28, 10, 0, 0),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is True
    )


def test_failed_across_holidays():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2020, 12, 24, 17, 0, 0),
            event_end=datetime.datetime(2020, 12, 28, 10, 0, 1),
            country_code="IT",
            minutes_to_resolve=120,
            opening_hours="09:00",
            closing_hours="18:00",
        )
        is False
    )
