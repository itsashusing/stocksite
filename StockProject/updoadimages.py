# set up django 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockProject.settings')
import django
django.setup()

from baseApp.models import Stock  # Import your model

def upload_images_from_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png')):  # Adjust file extensions as needed
            image_path = os.path.join(folder_path, filename)
            upload_image(image_path)

def upload_image(image_path):
    instance = Stock()
    with open(image_path, 'rb') as f:
        instance.photo.save(os.path.basename(image_path), f, save=True)
    print(f'Successfully uploaded {image_path}')


folder_path = 'D:/photos_scarp/'  # Update with your image folder path
upload_images_from_folder(folder_path)
