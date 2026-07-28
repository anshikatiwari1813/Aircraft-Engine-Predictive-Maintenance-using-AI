import pandas as pd



def preprocess_input(df):


    df = df.copy()



    # Remove target column

    if "RUL" in df.columns:

        df = df.drop(
            columns=["RUL"]
        )



    # Required features from training

    required_features = [

        'engine_id',
        'cycle',
        'setting1',
        'setting2',
        'sensor_2',
        'sensor_3',
        'sensor_4',
        'sensor_6',
        'sensor_7',
        'sensor_8',
        'sensor_9',
        'sensor_11',
        'sensor_12',
        'sensor_13',
        'sensor_14',
        'sensor_15',
        'sensor_17',
        'sensor_20',
        'sensor_21'

    ]



    # Keep only trained features

    df = df[
        [
            col
            for col in required_features
            if col in df.columns
        ]
    ]



    return df