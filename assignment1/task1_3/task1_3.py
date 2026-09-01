import pandas as pd
import matplotlib.pyplot as plt

data = {
    "State": [
        "Iowa", "New Hampshire", "South Carolina", "Nevada",
        "Alabama", "Alaska", "Arkansas", "Colorado", "Georgia",
        "Massachusetts", "Minnesota", "North Dakota", "Oklahoma",
        "Tennessee", "Texas", "Vermont", "Virginia",
        "Kansas", "Kentucky", "Louisiana", "Maine",
        "American Samoa", "Hawaii", "Idaho", "Michigan", "Mississippi",
        "Guam", "Virgin Islands", "Puerto Rico",
        "Florida", "Illinois", "Missouri", "North Carolina",
        "Northern Marianas", "Ohio", "Arizona", "Utah",
        "Wisconsin", "New York", "Connecticut", "Delaware",
        "Maryland", "Pennsylvania", "Rhode Island",
        "Indiana", "Nebraska", "West Virginia", "Oregon", "Washington",
        "California", "Montana", "New Jersey", "New Mexico",
        "South Dakota", "District of Columbia"
    ],

    "Date": [
        "2026-02-01", "2026-02-09", "2026-02-20", "2026-02-23",
        "2026-03-01", "2026-03-01", "2026-03-01", "2026-03-01", "2026-03-01",
        "2026-03-01", "2026-03-01", "2026-03-01", "2026-03-01",
        "2026-03-01", "2026-03-01", "2026-03-01", "2026-03-01",
        "2026-03-05", "2026-03-05", "2026-03-05", "2026-03-05",
        "2026-03-08", "2026-03-08", "2026-03-08", "2026-03-08", "2026-03-08",
        "2026-03-12", "2026-03-12", "2026-03-13",
        "2026-03-15", "2026-03-15", "2026-03-15", "2026-03-15",
        "2026-03-15", "2026-03-15", "2026-03-22", "2026-03-22",
        "2026-04-05", "2026-04-19", "2026-04-26", "2026-04-26",
        "2026-04-26", "2026-04-26", "2026-04-26",
        "2026-05-03", "2026-05-10", "2026-05-10", "2026-05-17", "2026-05-24",
        "2026-06-07", "2026-06-07", "2026-06-07", "2026-06-07",
        "2026-06-07", "2026-06-14"
    ]
}

df = pd.DataFrame(data)

# Convert to real dates
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date").reset_index(drop=True)

import matplotlib.dates as mdates

plt.figure(figsize=(12, 14))

month_colors = {
    2: "tab:blue",
    3: "tab:orange",
    4: "tab:green",
    5: "tab:red",
    6: "tab:purple"
}

colors = df["Date"].dt.month.map(month_colors)

plt.scatter(df["Date"], df["State"], c=colors, s=50)



plt.xlabel("Date")
plt.ylabel("State")
plt.title("Dates by State")

ax = plt.gca()
import matplotlib.dates as mdates

ax = plt.gca()

# Major tick on the 1st of every month
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b 1"))

# Minor tick for every day
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Major ticks larger, daily ticks smaller
ax.tick_params(axis="x", which="major", length=8)
ax.tick_params(axis="x", which="minor", length=3)

plt.xticks(rotation=45)

# Display dates as e.g. "Feb 01", "Mar 01", etc.
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

plt.xticks(rotation=45)
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.show()