def get_percentage(total_number, col_id, conditional_name):
    length = len(df[df[col_id]== conditional_name])
    percentage = (length/total_number)*100
    result = f"The percentage of {conditional_name} is {percentage}"
    return result
get_percentage(1000, 'gender', 'male')