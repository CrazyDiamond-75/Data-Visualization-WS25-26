import pandas as pd
import altair as alt
import sklearn as skl
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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
#print(auto.describe())
#print(auto.sample(5))

numeric = auto.select_dtypes(include="number").dropna()
normalized = (numeric - numeric.mean()) / numeric.std()
covariance = normalized.cov(numeric_only=True)

print(numeric.info())

cov_simple = covariance.reset_index().melt(id_vars="index", var_name="col", value_name="value")

alt.Chart(cov_simple, title="Correlation Matrix of Auto datasets numeric values").mark_rect().encode(
    alt.Color("value", scale=alt.Scale(scheme="redblue")),
    alt.X("col", title=None),
    alt.Y("index", title=None)
).save("covariance.pdf")



#pcad = PCA(n_components=2).fit(numeric)

#print(pcad.explained_variance_ratio_)
#print(pcad.singular_values_)

color = auto.dropna()["origin"]

transformed = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(numeric))
#transformed = PCA(n_components=2).fit_transform(numeric)
print(transformed.shape)
df = pd.concat([auto["origin"], pd.DataFrame(transformed, columns=["PCA_Axis_1", "PCA_Axis_2"])], axis=1)

alt.Chart(df).mark_point().encode(
    x="PCA_Axis_1",
    y="PCA_Axis_2",
    color="origin"
).save("pcad.pdf")


pca = PCA().fit(StandardScaler().fit_transform(numeric))
components = pca.explained_variance_ratio_
print(components)
"""components = pd.DataFrame({
    "x": list(range(1, len(components)+1))[::-1],
    "y": pd.Series(components[::-1]).cumsum()
})"""

componentspd = pd.DataFrame({"y": components[::-1]})

print(components)
alt.Chart(componentspd).mark_bar().encode(
    x=alt.X("y:Q", title="Component percentage"),
    color=alt.Color("y:N", title=None).legend(format=".3f"),
    order=alt.Order("y", sort="descending")
).save("components.pdf")

# Task f
importances = pd.DataFrame(
    pca.components_.T,
    index=numeric.columns
)

print(importances)

print(f"\nMost important:\n{importances.abs().sum(axis=1)}")