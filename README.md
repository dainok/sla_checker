# SLA Checker

SLA Checker helps to check if an event is within the defined SLA.

## Installation

~~~
pip3 install sla-checker
~~~

## Usage

Input parameters:

* `country_code`: the country code (e.g. IT). Optional if `working_on_holidays == True`.
* `opening_hours`: define opening hours (e.g. `datetime.time(6, 0)`).
  Optional if full day service. If set must be lower than `closing_hours`.
* `closing_hours`: define closing hours (e.g. `datetime.time(22, 0)`).
  Optional if full day service. If set must be greater than `opening_hours`.
* `working_on_sat`: define if Saturday is a working day.
  Optional, default is `True`.
* `working_on_holidays`: define if Sunday and Holidays are working days.
  Optional, default is `True`. If False `country_code` is mandatory.

Example (24x7 service with 2 hours SLA):

~~~
sla = sla_checker.SLAChecker()
sla.check(
  event_start = datetime.datetime(2020, 12, 24, 17, 0, 0),
  event_end = datetime.datetime(2020, 12, 28, 10, 0, 1),
  minutes_to_resolve = 120,
)
~~~

Example (9x5 service with 2 hours SLA):

~~~
sla = sla_checker.SLAChecker(
  country_code = "IT",
  opening_hours = "09:00",
  closing_hours = "18:00",
  working_on_sat = False,
  working_on_holidays = False,
)
sla.check(
  event_start = datetime.datetime(2020, 12, 24, 17, 0, 0),
  event_end = datetime.datetime(2020, 12, 28, 10, 0, 1),
  minutes_to_resolve = 120,
)
~~~

Example (9x6 service with 2 hours SLA):

~~~
sla = sla_checker.SLAChecker(
  country_code = "IT",
  opening_hours = "09:00",
  closing_hours = "18:00",
  working_on_sat = True,
  working_on_holidays = False,
)
sla.check(
  event_start = datetime.datetime(2020, 12, 24, 17, 0, 0),
  event_end = datetime.datetime(2020, 12, 28, 10, 0, 1),
  minutes_to_resolve = 120,
)
~~~
