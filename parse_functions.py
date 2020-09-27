from image_adjustment import predict

from keras.models import load_model
from keras.preprocessing.image import save_img

def predict_parser_func(args):
    model = load_model("model")
    pred = predict(model, args.img_path)
    save_img("C:\\Users\\rishi\\Desktop\\img.png", pred)
