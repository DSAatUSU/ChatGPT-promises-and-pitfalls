import pandas as pd
import plotly
import chart_studio.plotly as py

def genSankey(df, cat_cols=[], value_cols='', title='Sankey Diagram'):
    # Maximum of 6 value cols -> 6 colors
    colorPalette = ['#ee8f8f', '#87b787', '#FFE873', '#FFD43B', '#646464', 'yellow']  # Added 'yellow' to the palette
    labelList = []
    colorNumList = []
    
    for catCol in cat_cols:
        labelListTemp = list(set(df[catCol].values))
        colorNumList.append(len(labelListTemp))
        labelList = labelList + labelListTemp

    # Remove duplicates from labelList
    labelList = list(dict.fromkeys(labelList))

    # Define colors based on the number of levels
    colorList = []
    for idx, colorNum in enumerate(colorNumList):
        colorList = colorList + [colorPalette[idx]] * colorNum

    # Transform df into a source-target pair
    for i in range(len(cat_cols) - 1):
        if i == 0:
            sourceTargetDf = df[[cat_cols[i], cat_cols[i + 1], value_cols]]
            sourceTargetDf.columns = ['source', 'target', 'count']
        else:
            tempDf = df[[cat_cols[i], cat_cols[i + 1], value_cols]]
            tempDf.columns = ['source', 'target', 'count']
            sourceTargetDf = pd.concat([sourceTargetDf, tempDf])
        sourceTargetDf = sourceTargetDf.groupby(['source', 'target']).agg({'count': 'sum'}).reset_index()

    # Add index for source-target pair
    sourceTargetDf['sourceID'] = sourceTargetDf['source'].apply(lambda x: labelList.index(x))
    sourceTargetDf['targetID'] = sourceTargetDf['target'].apply(lambda x: labelList.index(x))

    # Creating the Sankey diagram
    data = dict(
        type='sankey',
        node=dict(
            pad=15,
            thickness=20,
            line=dict(
                color="black",
                width=0.5
            ),
            label=labelList,
            text=sourceTargetDf['count'].astype(str),
            color=colorList
        ),
        link=dict(
            source=sourceTargetDf['sourceID'],
            target=sourceTargetDf['targetID'],
            value=sourceTargetDf['count'],
            label=sourceTargetDf['count'].astype(str),  # Show counts as labels
            text=sourceTargetDf['count'].astype(str),   # Show counts as text on the links
            
        )
    )

    layout = dict(
        title=title,
        font=dict(
            size=20
        )
        
    )

    fig = dict(data=[data], layout=layout)
    return fig

if __name__ == "__main__":
    full_df = pd.read_csv("Full_dataset.csv")
    # Generate the Sankey diagram figure
    fig = genSankey(full_df, cat_cols=full_df.columns[:-1], value_cols='Code', title='Dataset Sankey Plot')
    plotly.offline.plot(fig, validate=False)
