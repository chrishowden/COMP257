import xml.etree.ElementTree as ET
import pandas as pd

def readxml(filename):
    """Read an xml file and return a dataframe"""
    
    tree = ET.parse(filename)
    root = tree.getroot()
    data = []
    for row in root:
        # create a dictionary for each row
        datarow = {}
        for child in row:
            # dictionary key is the tag name, value is the text in the tag
            datarow[child.tag] = child.text
        data.append(datarow)

    # now make a dataframe from this list of dictionaries
    df = pd.DataFrame(data)
    # sort on date
    df = df.sort_values('Date')
    # create a series from the dates as datetimes
    dates = pd.to_datetime(df.Date)
    # make this the index of the dataframe
    df.index = dates
    # remove the Date column (axis=1 means we're dropping a column, not rows)
    df.drop('Date', axis=1, inplace=True)
    
    return df