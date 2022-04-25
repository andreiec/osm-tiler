from PIL import Image
import glob
import secrets


def crop_images():
    area = (517, 335, 767, 585)

    for i, filename in enumerate(glob.glob('./files/images/*.png')):
        image = Image.open(filename)
        cropped = image.crop(area)
        cropped.save('./files/cleaned_images/' + str(i) + '.png')


def augmentate_images():
    for filename in glob.glob('./files/cleaned_images/*.png'):
        image = Image.open(filename)
        image.save('./files/final_images/' + secrets.token_urlsafe(16) + '.png')

        rotate1 = image.rotate(90)
        rotate1.save('./files/final_images/' + secrets.token_urlsafe(16) + '.png')

        rotate2 = rotate1.rotate(90)
        rotate2.save('./files/final_images/' + secrets.token_urlsafe(16) + '.png')

        rotate3 = rotate2.rotate(90)
        rotate3.save('./files/final_images/' + secrets.token_urlsafe(16) + '.png')


if __name__ == "__main__":
    augmentate_images()