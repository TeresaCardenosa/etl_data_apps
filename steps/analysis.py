# Analysis methods

def analysis(df_analysis):
    df_output = df_analysis.groupby(['Make'])[['Combined MPG']].mean().sort_values(by='Combined MPG', ascending=False).reset_index()
    df_output.to_csv('./data/combined_mpg_analysis.csv')
    return '---documento creado en data'