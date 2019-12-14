import datetime
import holidays


class sla_checker(object):
    def __init__(self):
        pass

    def check(
        self,
        event_start: datetime.datetime,
        event_end: datetime.datetime,
        minutes_to_resolve: int,
        country_code: str = None,
        opening_hours: str = None,
        closing_hours: str = None,
        working_on_sat: bool = False,
        working_on_holidays: bool = False,
    ) -> bool:
        # Checking start and end time
        if (event_end - event_start).total_seconds() <= 0:
            raise Exception("event_end must follow event_start")

        # Checking opening and closing hours
        if (not opening_hours and closing_hours) or (
            opening_hours and not closing_hours
        ):
            raise Exception(
                "opening_hours and closing_hours must be both set or unset"
            )
        if opening_hours:
            try:
                opening_hour = int(opening_hours.split(":")[0])
                opening_minute = int(opening_hours.split(":")[1])
                datetime.datetime(2000, 1, 1, opening_hour, opening_minute)
            except Exception:
                raise Exception(
                    'opening_hours must be in the format of "HH:MM"'
                )
            try:
                closing_hour = int(closing_hours.split(":")[0])
                closing_minute = int(closing_hours.split(":")[1])
                datetime.datetime(2000, 1, 1, closing_hour, closing_minute)
            except Exception:
                raise Exception(
                    'closing_hours must be in the format of "HH:MM"'
                )

        # If opening and closing hours are defined, country_code is mandatory
        if opening_hours and not country_code:
            raise Exception("a non 24x7 SLA requires country_code")

        if not opening_hours:
            # 24x7 service
            resolution_time = (event_end - event_start).total_seconds()
            if resolution_time <= minutes_to_resolve * 60:
                return True
            return False

        # Working hours service
        country_holidays = holidays.CountryHoliday(country_code)
        remaining_time = minutes_to_resolve * 60
        current_time = event_start
        while remaining_time > 0:
            weekday = current_time.weekday()
            if (
                (current_time in country_holidays and working_on_holidays)
                or (weekday == 5 and working_on_sat)
                or (current_time not in country_holidays and weekday < 5)
            ):
                # Working day
                if (
                    current_time
                    - datetime.datetime(
                        current_time.year,
                        current_time.month,
                        current_time.day,
                        opening_hour,
                        opening_minute,
                    )
                ).total_seconds() < 0:
                    # Before opening hours
                    current_time = datetime.datetime(
                        current_time.year,
                        current_time.month,
                        current_time.day,
                        opening_hour,
                        opening_minute,
                    )
                elif (
                    current_time
                    - datetime.datetime(
                        current_time.year,
                        current_time.month,
                        current_time.day,
                        closing_hour,
                        closing_minute,
                    )
                ).total_seconds() > 0:
                    # After closing hours
                    current_time = datetime.datetime(
                        current_time.year,
                        current_time.month,
                        current_time.day,
                        opening_hour,
                        opening_minute,
                    ) + datetime.timedelta(days=1)
                else:
                    # Within opening hours
                    if (
                        current_time
                        + datetime.timedelta(seconds=remaining_time)
                        - datetime.datetime(
                            current_time.year,
                            current_time.month,
                            current_time.day,
                            closing_hour,
                            closing_minute,
                        )
                    ).total_seconds() > 0:
                        # Remaining time exceed working hours
                        remaining_time = (
                            remaining_time
                            - (
                                datetime.datetime(
                                    current_time.year,
                                    current_time.month,
                                    current_time.day,
                                    closing_hour,
                                    closing_minute,
                                )
                                - current_time
                            ).total_seconds()
                        )
                        current_time = datetime.datetime(
                            current_time.year,
                            current_time.month,
                            current_time.day,
                            opening_hour,
                            opening_minute,
                        ) + datetime.timedelta(days=1)
                    else:
                        # Checking SLA
                        if (
                            event_end - current_time
                        ).total_seconds() <= remaining_time:
                            return True
                        return False
            else:
                # Not a working day
                current_time = current_time + datetime.timedelta(days=1)
