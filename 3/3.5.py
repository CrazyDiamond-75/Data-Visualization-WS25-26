import pandas as pd
import altair as alt

auto = pd.read_csv("3/auto-mpg.csv")

# hp is numeric but contains a few "?"
auto["horsepower"] = pd.to_numeric(auto["horsepower"], errors="coerce")

# model year to date
auto["model year"] = pd.to_datetime(
    auto["model year"],
    format="%y",
    errors="coerce")

# 1 USA 2 Europe 3 Japan
auto["origin"] = auto["origin"].map(lambda n: ["USA", "Europe", "Japan"][n-1])

print(auto.info())
print(auto.describe())
print(auto.sample(5))



hp_weight_year = alt.Chart(auto).mark_line().encode(
    color="origin",
    x="model year:T",
    y="median(horsepower)",
    #y2="media(mpg)"
)

mpg_year = alt.Chart(auto).mark_line().encode(
    color="origin",
    x="model year",
    y="median(mpg)"
)

weight_year = alt.Chart(auto).mark_line().encode(
    color="origin",
    x="model year",
    y="median(weight)"
)

years = mpg_year | hp_weight_year | weight_year

mpg_origin = alt.Chart(auto).mark_circle(size=100).encode(
    color="origin",
    x="model year",
    y="mpg"
)

accel_mpg = alt.Chart(auto).mark_point().encode(
    x="acceleration",
    y="mpg",
    #size="origin",
    color="origin"
)

mpg_date = alt.Chart(auto).mark_line().encode(
    x="model year",
    y="mean(mpg)",
    color="origin"
)

# strong correlation visible
mpg_weight_accel = alt.Chart(auto).mark_circle(size=200).encode(
    x=alt.X("mpg", scale=alt.Scale(zero=False)).title("Miles / Gallon"),
    y=alt.Y("acceleration", scale=alt.Scale(zero=False)),
    color="origin",
    fillOpacity="weight"
).properties(
    height=500,
    width=500
)

mpg_weight_accel2 = alt.Chart(auto).mark_bar().encode(
    x=alt.X("mpg", scale=alt.Scale(zero=False)).bin().title("Miles / Gallon (binned)"),
    y=alt.Y("count()", scale=alt.Scale(zero=False, reverse=True)),
    color="origin"
).properties(
    height=200,
    width=500
)

mpg_weight_accel3 = alt.Chart(auto).mark_bar().encode(
    x=alt.X("count()", scale=alt.Scale(zero=False)),
    y=alt.Y("acceleration", scale=alt.Scale(zero=False)).bin(),
    color="origin"
).properties(
    height=500,
    width=200
)

# No trend in model counts visible
origin_count = alt.Chart(auto).mark_bar().encode(
    x="model year",
    y="count()",
    color="origin"
)

"""
alt.hconcat(
    alt.vconcat(mpg_weight_accel,
                mpg_weight_accel2),
    mpg_weight_accel3
    ).save("cars.html")
"""

years.save("cars.html")


# origin, displacement, mpg
noZ = alt.Scale(zero=False)

odm = alt.Chart(auto).mark_point()

odm1 = odm.encode(
    x=alt.X("mpg", scale=noZ).title("Miles / Gallon"),
    y=alt.Y("displacement", scale=noZ),
    color="origin"
)

odm2 = odm.encode(
    x=alt.X("mpg", scale=noZ).title("Miles / Gallon"),
    y=alt.Y("displacement", scale=noZ),
    shape="origin"
)

odm3 = odm.encode(
    x=alt.X("mpg", scale=noZ).title("Miles / Gallon"),
    y=alt.Y("displacement", scale=noZ),
    opacity="origin"
)

(odm1 | odm2 | odm3).save("encodings.html")