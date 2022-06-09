def amorpm(t):
    if t >= 12:
        ti = t - 12
        if ti == 0:
            return "PM", 12
        return "PM", t - 12
    elif t == 0:
        return "AM", 12
    else:
        return "AM", t


def add_time(start, duration, day=None):
    days = [
        0, 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday'
    ]

    new_time = ''

    hrmin, ap = start.split()
    hr, min = hrmin.split(':')
    hr, min = int(hr), int(min)

    adhr, admin = duration.split(':')
    adhr, admin = int(adhr), int(admin)
    days_after = 0

    if ap == "PM":
        hr += 12

    if min + admin >= 60:
        hr += 1
        min = min + admin - 60
    else:
        min += admin

    min = str(min).zfill(2)
    hr += adhr
    if hr >= 24:
        days_after = hr // 24
        new_day = days_after % 7
        if new_day == 0:  new_day = 1
        final_hr = hr % 24
        final_ap = amorpm(final_hr)
        new_time = f"{final_ap[1]}:{min} {final_ap[0]}"
      
        if day:
            d = days.index(day.capitalize()) + new_day
            if d > 7:
              d -= 7
            final_day = days[d]
            new_time += f", {final_day}"

        if days_after == 1:
            new_time += " (next day)"
        else:
            new_time += f" ({days_after} days later)"

    else:
      final_ap = amorpm(hr)
      new_time = f"{final_ap[1]}:{min} {final_ap[0]}"

      if day:
        final_day = days[days.index(day.capitalize())]
        new_time += f", {final_day}"

    return new_time
