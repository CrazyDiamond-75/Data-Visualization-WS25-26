import pandas as pd
import altair as alt
from functools import reduce

abi = pd.read_csv("4/abinoten_2011-21_sh_clean.csv", sep=";", decimal=",")

print(abi.info())
print(abi.sample(5))

year = 2021

row = abi.melt(["Jahr", "Durchschnitt"]).query(f"Jahr == {year}")
#row["variable"] = pd.to_numeric(row["variable"].map(lambda x: x[-3:]), "coerce")
rowcont = row.copy()

rowcont["variable"] = pd.to_numeric(rowcont["variable"].replace("Nicht bestanden", "Note 5.0").map(lambda x: x[-3:]))
print(row)

cb_friendly_hues = ["#46b548",
"#452493",
"#75ec85",
"#b52490",
"#d8db59",
"#00368d",
"#ffc14d",
"#007ddc",
"#c86605",
"#4c9eff",
"#e55e36",
"#00d2b9",
"#cc1670",
"#004300",
"#d66dde",
"#757900",
"#9c51c4",
"#ebd387",
"#590036",
"#ffbf75",
"#bfb0ff",
"#765c00",
"#ff91de",
"#843600",
"#916fb1",
"#a70020",
"#ffa7dd",
"#622300",
"#dc2b5f",
"#782925",
"#ff7f80",
"#750028"]

chart = alt.Chart(row).mark_bar()
xc = alt.X("variable").title("Note")
yc = alt.Y("value").title("Anzahl")


charts = [alt.Chart(row).mark_bar().encode(
    x=xc,
    y=yc,
    color=alt.Color("variable").scale(range=c).title("Note")
) for c in ["category", cb_friendly_hues]]

charts.append(alt.Chart(rowcont).mark_bar().encode(
    x=alt.X("variable:O").title("Note").bin(step=0.2),
    y=yc,
    color=alt.Color("variable").scale(range=cb_friendly_hues).title("Note").bin(step=0.2)
))

charts.append(alt.Chart(rowcont).mark_bar().encode(
    x=alt.X("variable:O").title("Note").bin(step=0.8, nice=False),
    y=yc,
    color=alt.Color("variable").scale(range=cb_friendly_hues).title("Note").bin(step=0.8, nice=False)
))


#alt.vconcat(*charts).save("abi-barchart.pdf")
# For some reason, when you vconcat charts they suddenly share colour schemes
for n, c in enumerate(charts):
    c.save(f"abi-{n}.pdf")

