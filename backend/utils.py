import json
import pandas as pd
import os

def save_info_to_excel(json_data, discipline, education_level, location):
    """
    Save information about universities to an Excel file."

    Args:
        json_data (dict): A dictionary containing information about universities.
        discipline (str): The discipline searched for.
        education_level (str): The education level searched for.
        location (str): The location searched for.

    Returns:
        str: The name of the saved Excel file.
    """

    save_dir = "excel_files"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_path = os.path.join(save_dir, f"Top_Universities_{education_level}_{discipline}_{location}.xlsx")

    # Ensure json_data is a dictionary
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    # Convert to a DataFrame
    df = pd.DataFrame(data["universities"])
    
    # Save to an Excel file
    df.to_excel(file_path, index=False)
    
    print(f"Information saved successfully to {file_path}")
    return file_path