def get_mean(c_ids):
    for c_id in c_ids:
        df[c_id] = df[c_id].replace(0,np.NaN)
        mean = df[c_id].mean(skipna=True)
        df[c_id] =df[c_id].replace(np.NaN, mean)
get_mean([['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin']])