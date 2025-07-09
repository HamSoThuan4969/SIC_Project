import csv
import os
import pandas as pd

# before creating csv, I want to find all files extensions with the below code:
def get_file_extensions(folder_path):
    file_extensions = set([os.path.splitext(filename)[1] for filename in os.listdir(folder_path)])
    return file_extensions

folder_path = 'C:/Users/kuroba/OneDrive - TRƯỜNG ĐẠI HỌC MỞ TP.HCM/Documents/Kan_project/SIC/DU DOAN TUI/Facial_Age_estimation_PyTorch/dataset/utkcropped'
# Create a csv file which contains labels
def create_csv(dataset_folder):
    image_files = os.listdir(dataset_folder)
    header = ['image_name', 'age', 'ethnicity', 'gender']
    with open('./csv_dataset/utkface_dataset.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for idx, image_file in enumerate(image_files):
            if len(image_file.split('_')) < 4:
                continue
            
            # convert values to int with map function
            age, gender, ethnicity = map(int, image_file.split('_')[:3])
    
            gender = 'Male' if gender == 0 else 'Female'
            if ethnicity != str:
                ethnicity = ['White', 'Black', 'Asian', 'Indian', 'Others'][ethnicity]

            if age < 85:
                data = [image_file, age, ethnicity, gender]
                writer.writerow(data)


# Replace with the actual path to your UTK dataset images folder
dataset_folder = 'C:/Users/kuroba/OneDrive - TRƯỜNG ĐẠI HỌC MỞ TP.HCM/Documents/Kan_project/SIC/DU DOAN TUI/Facial_Age_estimation_PyTorch/dataset/utkcropped'
create_csv(dataset_folder)

df = pd.read_csv('./csv_dataset/utkface_dataset.csv')
print(f'Dataframe length: {len(df)}')
print()
print(df.head())