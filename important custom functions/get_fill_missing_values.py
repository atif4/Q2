# filling with most common class
df = df.apply(lambda x: x.fillna(x.value_counts().index[0]))
df