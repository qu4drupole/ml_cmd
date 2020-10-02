from image_adjustment import predict

from keras.models import load_model
from keras.preprocessing.image import save_img

def predict_parser_func(args):
    model = load_model("model")
    pred = predict(model, args.img_path)
    #save_img("C:\\Users\\rishi\\Desktop\\img.png", pred)
    save_img("D:\\Dropbox (SBG)\\David-Smith\\Jefferson-Desktop\\Code\\EM_hepatocyte\\output\\img.png", pred)
