from datetime import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

MY_BIRTHDAY = "October 2, 2005"

def birthday_summary():
    """Parses birthday string and shows how long ago it was."""
    now = datetime.now()
    birthday = parser.parse(MY_BIRTHDAY)

    age = relativedelta(now, birthday)

    summary = ("=" * 50 + "\n"
        + "**              Birthday Summary                **\n"
        + "=" * 50 + "\n"
        + f"Jaira's Birthday: {birthday.strftime('%A, %B %d, %Y')}\n"
        + f"Today is:         {now.strftime('%A, %B %d, %Y')}\n\n"
        + f"Jaira is {age.years} year(s), {age.months} month(s), "
        + f"and {age.days} day(s) old!")
    
    return summary