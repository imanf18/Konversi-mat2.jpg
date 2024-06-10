import os
import numpy as np
import h5py
from PIL import Image
import matplotlib.pyplot as plt

def convert_images(input_folder, output_folder):
    # Loop melalui semua file dalam folder input
    for filename in os.listdir(input_folder):
        if filename.endswith('.mat'):
            mat_file_path = os.path.join(input_folder, filename)
            try:
                with h5py.File(mat_file_path, 'r') as f:
                    # Read cjdata struct
                    cjdata = f['cjdata']

                    # Extract information
                    label = cjdata['label'][0, 0]
                    PID = ''.join(chr(c[0]) for c in cjdata['PID'])
                    image = np.array(cjdata['image']).astype(np.float64)
                    
                    # Convert image to uint8
                    hi = np.max(image)
                    lo = np.min(image)
                    image = (((image - lo) / (hi - lo)) * 255).astype(np.uint8)
                    
                    # Save as jpeg
                    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
                    im = Image.fromarray(image)
                    im.save(output_path)

                    print(f"File {filename} berhasil dikonversi.")
            except Exception as e:
                print(f"Terjadi kesalahan saat mengonversi {filename}: {e}")
        else:
            print(f"File {filename} bukan file .mat, dilewati.")

if __name__ == "__main__":
    # Folder input dan output
    input_folder = r"D:\S2\PSO\Final Project\1512427\brainTumorDataPublic_1-766"
    output_folder = r"D:\S2\PSO\Final Project\1512427\brainTumorDataPublic_1-766\png_images"

    # Pastikan folder output ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_images(input_folder, output_folder)
