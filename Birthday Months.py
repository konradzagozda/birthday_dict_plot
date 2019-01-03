import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

with open("info.json", "r") as f:
    birthdays = json.load(f)

months = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}

counted_months = dict(Counter(list(map(lambda x: months[x[3:5]], list(birthdays.values())))))
print(counted_months)

output_file("plot.html")

x_categories = list(months.values())
x = list(counted_months.keys())
y = list(counted_months.values())

p = figure(x_range=x_categories)
p.vbar(x=x, top=y,width=0.5)
show(p)