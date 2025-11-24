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
print(auto.sample(5))



hp_weight_year = alt.Chart(auto).mark_point().encode(
    color="weight",
    x="model year:T",
    y="horsepower"
)

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

mpg_date.save("cars.html")