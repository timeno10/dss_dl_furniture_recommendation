import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import glob
import os.path
from numpy import dot
from numpy.linalg import norm
import numpy as np
from PIL import Image
import requests
import matplotlib.pyplot as plt


def load_img(path):
    img = tf.io.read_file(path)
    img = tf.io.decode_jpeg(img, channels=3)
    img = tf.image.resize_with_pad(img, 224, 224)
    img = tf.image.convert_image_dtype(img,tf.float32)[tf.newaxis, ...]
 
    return img

def get_image_feature_vectors():
    module = hub.load("https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/4")
    feature_df = []

    for filename in glob.glob('items/*.png'):

        img = load_img(filename)
        features = module(img)
        feature_set = np.squeeze(features)
        id = filename[6:-4]
        feature_df.append({'feature_vectors':list(feature_set), 'id':id})
        df = pd.DataFrame(feature_df)
        df.to_csv('feature_vectors/chair.csv', sep=',', encoding='UTF-8', index=False)

def sim_df():
    chair = pd.read_csv('database/Chair.csv')
    feature_vectors = pd.read_csv('feature_vectors/chair.csv')
    
    feature_vectors_df = pd.merge(chair, feature_vectors, on='id')
    feature_vectors_df.sort_values(by='id', inplace=True)
    feature_vectors_df.reset_index(drop=True, inplace=True)
    feature_vectors_df['feature_vectors'] = feature_vectors_df.feature_vectors.apply(lambda x: x[1:-1].split(', '))

    return feature_vectors_df

def cos_sim(x, y):
    return dot(x, y)/(norm(x)*norm(y))

def recommendation(input_path):
    df = sim_df()
    cos_sim_df = []

    module = hub.load("https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/4")
    img = load_img(input_path)
    features = module(img)
    target_image = np.squeeze(features)

    for idx in df.index:
        vect = [float(num) for num in df.iloc[idx]['feature_vectors']]
        cos_sim_df.append(cos_sim(target_image, vect))
    cos_sim_df = np.array(cos_sim_df)

    df['weight'] = cos_sim_df #cos_sim_df.dot(weight)
    df.sort_values('weight', ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)

    plt.figure(figsize = (16,9))
    
    plt.subplot(1,6,1)
    img = Image.open(input_path)
    plt.imshow(img)
    plt.title('My item')
    plt.axis('off')

    for i in range(5):
        url = df.loc[i].image_url
        image = Image.open(requests.get(url, stream=True).raw)
        # image.show()
        plt.subplot(1,6,i+2)
        plt.imshow(image)
        plt.title('Top {}'.format(i+1))
        plt.axis('off')
        print("{}번째 아이템 : https://ohou.se/productions/".format(i+1) + str(df.loc[i].id))

if __name__=="__main__":
    recommendation('pics/input.jpg')
    print('Done')