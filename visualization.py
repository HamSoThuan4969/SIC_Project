import os
import random
import matplotlib.pyplot as plt
from PIL import Image


# Replace with the actual path to your UTK dataset images folder

dataset_folder = 'C:/Users/kuroba/OneDrive - TRƯỜNG ĐẠI HỌC MỞ TP.HCM/Documents/projeck/SIC/DU DOAN TUI/Facial_Age_estimation_PyTorch/csv_dataset/utkface_dataset.csv'
def show_random_samples(num_samples=9):
    image_files = os.listdir(dataset_folder)
    selected_image_files = random.sample(image_files, num_samples)

    plt.figure(figsize=(8, 8))
    for idx, image_file in enumerate(selected_image_files, 1):
        image_path = os.path.join(dataset_folder, image_file)
        age, gender, ethnicity = image_file.split('_')[:3]

        image = Image.open(image_path)

        gender = 'Male' if int(gender) == 0 else 'Female'
        ethnicity = ['White', 'Black', 'Asian', 'Indian', 'Others'][int(ethnicity)]

        plt.subplot(3, 3, idx)
        plt.imshow(image)
        plt.title(f"Age: {age}\nGender: {gender}\nEthnicity: {ethnicity}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()


# Call the function to display random samples - đã sửa
show_random_samples()
