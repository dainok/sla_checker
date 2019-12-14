import datetime
import sla_checker


def test_solved_within_the_day():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 0),
            minutes_to_resolve=120,
        )
        is True
    )


def test_failed_within_the_day():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 15, 0, 0),
            event_end=datetime.datetime(2019, 12, 13, 17, 0, 1),
            minutes_to_resolve=120,
        )
        is False
    )


def test_solved_between_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 22, 0, 0),
            event_end=datetime.datetime(2019, 12, 14, 1, 0, 0),
            minutes_to_resolve=180,
        )
        is True
    )


def test_failed_between_days():
    sla = sla_checker.sla_checker()
    assert (
        sla.check(
            event_start=datetime.datetime(2019, 12, 13, 22, 0, 0),
            event_end=datetime.datetime(2019, 12, 14, 1, 0, 1),
            minutes_to_resolve=180,
        )
        is False
    )
