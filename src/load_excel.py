def save_excel(df, OUTPUT_PATH):

    df.to_excel(
        OUTPUT_PATH,
        index=False
    )