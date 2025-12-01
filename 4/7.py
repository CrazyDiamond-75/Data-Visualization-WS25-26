import pandas as pd
import altair as alt

abi = pd.read_csv("4/abinoten_2011-21_sh_clean.csv", sep=";", decimal=",")

print(abi.info())
print(abi.sample(5))

year = 2021

row = abi.melt(["Jahr", "Durchschnitt"]).query(f"Jahr == {year}")
#row["variable"] = pd.to_numeric(row["variable"].map(lambda x: x[-3:]), "coerce")

print(row)

cb_friendly_hues = ["#ffb269",
"#005eb8",
"#00eab9",
"#d83545",
"#73a519"]

chart = alt.Chart(row).mark_bar()
xc = alt.X("variable").title("Note")
yc = alt.Y("value").title("Anzahl")


default = alt.Chart(row).mark_bar().encode(
    x=alt.X("variable").title("Note"),
    y=alt.Y("value").title("Anzahl"),
    color=alt.Color("variable").title("Note")
)

cb_friendly = alt.Chart(row).mark_bar().encode(
    x=alt.X("variable").title("Note"),
    y=alt.Y("value").title("Anzahl"),
    color=alt.Color("variable").scale(range=cb_friendly_hues).title("Note")
)

alt.vconcat(default, cb_friendly).save("abi-barchart.pdf")