from typing import List, Set, Tuple, Optional

p1_meetings = [('10:30', '11:30'), ('12:00', '12:15'), ('12:30', '12:45'), ('13:00', '13:15'), ('16:45', '17:30')]
p2_meetings = [('9:30', '10:15'), ('12:00', '13:15'), ('13:45', '14:00'), ('14:15', '14:30'), ]


def convert_time_str_to_minutes_int(time: str):
    h, m = map(int, time.split(':'))

    return h * 60 + m


def convert_minutes_to_str_time(minutes: int):
    h = minutes // 60
    m = minutes % 60

    return '{h}:{m:02d}'.format(h=h, m=m)


DAY_START = convert_time_str_to_minutes_int('8:30')
DAY_END = convert_time_str_to_minutes_int('18:30')


class Meeting:
    def __init__(self, start: int, end: int):
        self.s, self.e = start, end

    @property
    def duration(self):
        return self.e - self.s

    @staticmethod
    def from_str_tuple(start_end: Tuple[str, str]):
        start, end = map(convert_time_str_to_minutes_int, start_end)

        return Meeting(start, end)

    def __str__(self):
        return '({s}, {e})'.format(s=convert_minutes_to_str_time(self.s), e=convert_minutes_to_str_time(self.e))

    def __repr__(self):
        return str(self)


def try_merge(mt1: Meeting, mt2: Meeting) -> Optional[Meeting]:
    # we know mt1.s <= mt2.s is True
    if mt1.e < mt2.s:
        # no overlap
        return None
    else:
        # overlap
        merged_m = Meeting(start=mt1.s, end=max(mt1.e, mt2.e))

        return merged_m


def get_earlier_meeting(mt1: Meeting, mt2: Meeting):
    if mt1 and mt2:
        return mt1 if mt1.s <= mt2.s else mt2
    else:
        return mt1 or mt2


def find_free_windows(p1_schedule: List[Tuple[str, str]], p2_schedule: List[Tuple[str, str]], at_least=30):
    ptr_1 = 0
    ptr_2 = 0
    overlapping_busy = []

    while ptr_1 < len(p1_schedule) or ptr_2 < len(p2_schedule):
        m1 = Meeting.from_str_tuple(p1_schedule[ptr_1]) if ptr_1 < len(p1_schedule) else None
        m2 = Meeting.from_str_tuple(p2_schedule[ptr_2]) if ptr_2 < len(p2_schedule) else None

        next_m = get_earlier_meeting(m1, m2)

        if next_m is m1:
            ptr_1 += 1
        else:
            ptr_2 += 1

        if not overlapping_busy:
            overlapping_busy.append(next_m)
        else:
            merged = try_merge(overlapping_busy[-1], next_m)

            if not merged:
                # merge was unsuccessful, add new busy block
                overlapping_busy.append(next_m)  # make copy of next_m ?
            else:
                # merge was successful, extend current block
                overlapping_busy[-1].e = merged.e

    print('overlapping_busy:')
    print(overlapping_busy)

    common_free_times = []

    if DAY_START < overlapping_busy[0].s:
        common_free_times.append(Meeting(start=DAY_START, end=overlapping_busy[0].s))

    for i in range(len(overlapping_busy) - 1):
        left = overlapping_busy[i]
        right = overlapping_busy[i + 1]
        free_time = Meeting(start=left.e, end=right.s)
        common_free_times.append(free_time)

    if DAY_END > overlapping_busy[-1].e:
        common_free_times.append(Meeting(start=overlapping_busy[-1].e, end=DAY_END))

    return list(filter(lambda m: m.duration >= at_least, common_free_times))


assert convert_time_str_to_minutes_int('5:30') == 330
assert convert_time_str_to_minutes_int('17:30') == 1050

print('p1_meetings:')
print(p1_meetings)
print('p2_meetings:')
print(p2_meetings)

result = find_free_windows(p1_meetings, p2_meetings)
print('free windows:')
print(result)
