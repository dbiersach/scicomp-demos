# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

import time
from cedargrove_dst_adjuster import adjust_dst

# Today's date: 11/01/2020 00:00 Standard Time (xST)
datetime = time.struct_time((2020, 11, 1, 0, 0, 0, 6, 0, -1))

# Check datetime and adjust if DST
adj_datetime, is_dst = adjust_dst(datetime)

if is_dst:
    flag_text = "DST"
else:
    flag_text = "xST"

# Print the submitted time
print(
    "     {}/{}/{} {:02}:{:02}:{:02}  week_day={}".format(
        datetime.tm_mon,
        datetime.tm_mday,
        datetime.tm_year,
        datetime.tm_hour,
        datetime.tm_min,
        datetime.tm_sec,
        datetime.tm_wday,
    )
)

# Print the adjusted time
print(
    "{}: {}/{}/{} {:02}:{:02}:{:02}  week_day={}".format(
        flag_text,
        adj_datetime.tm_mon,
        adj_datetime.tm_mday,
        adj_datetime.tm_year,
        adj_datetime.tm_hour,
        adj_datetime.tm_min,
        adj_datetime.tm_sec,
        adj_datetime.tm_wday,
    )
)
