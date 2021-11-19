import cv2
import pytesseract
import pyttsx3


class Image:
    def __init__(self, image, path):
        self.image = cv2.imread(image)
        # self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        pytesseract.pytesseract.tesseract_cmd = path

    def rectangle(self):
        data = pytesseract.image_to_data(self.image, output_type="dict")
        boxes = len(data["level"])
        for i in range(boxes):
            (x, y, w, h) = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imwrite("saved_image.jpg", self.image)

    def image_to_text(self):
        x = pytesseract.image_to_string(self.image)
        file = open("text.txt", "w")
        file.write(x)
        file.close()

    def text_to_speech(self, file, play=False):
        file = open(file, "r")
        txt = file.read()
        file.close()
        voice = pyttsx3.init()

        voice.save_to_file(txt, "speech.mp3")
        voice.runAndWait()
        if play:
            voice.say(txt)
            voice.runAndWait()


if __name__ == "__main__":
    y = Image("./pic3.png", r"D:\softwares\tesseract\tesseract.exe")
    y.text_to_speech("text.txt")
