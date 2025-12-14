import pandas as pd
import altair as alt


data = pd.DataFrame.from_dict({
    'R': [0.74, 0.15, 0.10, 0.01],
    'Both': [0.11, 0.49, 0.38, 0.01],
    'Python': [0.05, 0.04, 0.91, 0.01],
    'Other': [0.17, 0.04, 0.19, 0.60]
}, orient='index', columns=['R', 'Both', 'Python', 'Other'])

data_unbiased = pd.DataFrame.from_dict({
    'R': [0.42 * 0.74, 0.42 * 0.15, 0.42 * 0.10, 0.42 * 0.01],
    'Both': [0.08 * 0.11, 0.08 * 0.49, 0.08 * 0.38, 0.08 * 0.01],
    'Python': [0.34 * 0.05, 0.34 * 0.04, 0.34 * 0.91, 0.34 * 0.01],
    'Other': [0.16 * 0.17, 0.16 * 0.04, 0.16 * 0.19, 0.16 * 0.60]
}, orient='index', columns=['R', 'Both', 'Python', 'Other'])

data_simple = pd.DataFrame.from_dict({
    'R': [0.42, 0.36],
    'Both': [0.08, 0.12],
    'Python': [0.34, 0.41],
    'Other': [0.16, 0.11]
}, orient='index', columns=['2016', '2017'])

data_long = (
    data
    .reset_index()
    .rename(columns={'index': 'Usage in 2016'})
    .melt(
        id_vars='Usage in 2016',
        var_name='Usage in 2017',
        value_name='Portion'
    )
)

data_unbiased_long = (
    data_unbiased
    .reset_index()
    .rename(columns={'index': 'Usage in 2016'})
    .melt(
        id_vars='Usage in 2016',
        var_name='Usage in 2017',
        value_name='Portion'
    )
)

data_unbiased_long['2016 -> 2017'] = (
    data_unbiased_long['Usage in 2016'] + " -> " + data_long['Usage in 2017']
)

data_simple_long = (
    data_simple
    .reset_index()
    .rename(columns={'index': 'Language'})
    .melt(id_vars='Language', var_name='Year', value_name='Value')
)

# print(data_simple_long)
# print(alt.datasets.data.barley())
# exit()

## PIE CHARTS ##
cats = {'Movement from 2016': data_unbiased.columns}
for cat, line in zip(data_unbiased.columns, data_unbiased):
    vals = {'Portion': list(data_unbiased[line])}
    source = pd.DataFrame(cats | vals)

    # Subtitle: Users of {cat} in 2017 from users in 2016.
    alt.Chart(source, title=f'Pie Chart: {cat}').mark_arc().encode(
        theta='Portion',
        color=alt.Color(
            'Movement from 2016',
            scale=alt.Scale(
                domain=data_unbiased.columns,
                range=["#1a66ba", '#ff6596', '#ffcf3c', 'grey']
            )
        )
    ).save(f'6.3.PLOT_PI_{cat}.pdf')

## STACKED BAR CHART ##
# Subtitle: Users in 2017 from users in 2016.
alt.Chart(data_unbiased_long, title='Stacked Bar Chart').mark_bar().encode(
    x=alt.X('Usage in 2017', sort='y'),
    y='sum(Portion)',
    color=alt.Color(
        'Usage in 2016',
        scale=alt.Scale(
            domain=data_unbiased.columns,
            range=["#1a66ba", '#ff6596', '#ffcf3c', 'grey']
        )
    )
).save('6.3.PLOT_STACKED_BAR.pdf')

## BAR CHART ##
# Subtitle: All language usage movements between 2016 and 2017.
alt.Chart(data_unbiased_long, title='Bar Chart').mark_bar().encode(
    x=alt.X('2016 -> 2017', sort='y'),
    y='Portion',
    color=alt.Color(
        'Usage in 2017',
        scale=alt.Scale(
            domain=data.columns,
            range=["#1a66ba", '#ff6596', '#ffcf3c', 'grey']
        )
    )
).save('6.3.PLOT_BAR.pdf')

## SLOPE GRAPH ##
# Subtitle: Change in total language usage between years.
alt.Chart(data_simple_long, title='Slope Graph').mark_line().encode(
    x='Year',
    y='Value',
    color=alt.Color(
        'Language',
        scale=alt.Scale(
            domain=data.columns,
            range=["#1a66ba", '#ff6596', '#ffcf3c', 'grey']
        )
    )
).properties(width=200).save('6.3.PLOT_SLOPE.pdf')
