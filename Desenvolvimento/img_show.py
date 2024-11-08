import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import pandas as pd

images_path = r"..\Desenvolvimento\data_sets\random_imgs\train"
info_path = r"..\Desenvolvimento\info_id\id_image.csv"
data_frame = pd.read_csv(info_path)
all_files = os.listdir(images_path)
image_files = [file for file in all_files if file.endswith(('.jpg', '.png', '.jpeg'))]

def get_user_id():
    while True:
        try:
            return int(input("Digite seu Id (inteiro): "))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def random_image(file):
    selected_image = random.choice(file)
    image_path = os.path.join(images_path, selected_image)
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    return selected_image

def inside_df(df, id, image, time, sequence):
    new_row = {'Id': id, 'Image': image, 'Sec': time, 'Sequence': sequence}
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index = True)
    return df

def last_img_seen(df, user_id):

    user_data = df[df['Id'] == user_id]
    print(user_data)
    if not user_data.empty:
        current_sequence = user_data['Sequence'].max()
        return current_sequence + 1
    return 1

def main():
    global data_frame
    stop = ''
    id_user = get_user_id()
    sequence = last_img_seen(data_frame, id_user)

    while stop != 'stop':
        init_time = time.time()
        selected_image = random_image(image_files)
        print(f"The img shown to you is:{selected_image}")
        stop = input("Press a key: ")
        end_time = time.time()
        tempo = round(end_time - init_time, 2)
        data_frame = inside_df(data_frame, id_user, selected_image, tempo, sequence)
        print(f"Your screen time was: {tempo}")
        sequence += 1

    data_frame.to_csv(info_path, index=False, mode='w')

if __name__ == '__main__':
    main()