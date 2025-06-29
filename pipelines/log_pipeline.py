from etls.log_etl import connect_API, transform_data, fetch_data, load_file
from utils.constanst import API_URL, OUTPUT_PATH, HEADERS


def log_pipeline(filename):
    """
    fetch data from API -> extract -> transform -> load
    """
    
    file_path = f"{OUTPUT_PATH}/{filename}.csv"
    print(file_path)
    events = connect_API(API_URL, HEADERS)
    new_events = fetch_data(events)
    df = transform_data(new_events)
    load_file(df,file_path)


    print(df)

    return file_path
