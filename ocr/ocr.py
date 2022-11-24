import pytesseract
from PIL  import Image
import easyocr


def ocr(img_path):
    img = Image.open(img_path)
    
    # pytesseract
    print("########## pytesseract ##########")
    content = pytesseract.image_to_string(img, lang='chi_sim')
    print(content)


    print("\n \n \n")
    
    ## easyocr
    print("########## easyocr ##########")
    reader = easyocr.Reader(['ch_sim','en'], gpu = True) # need to run only once to load model into memory
    ocr_result = reader.readtext(img_path, detail = 0)
    print(ocr_result)
    #return ocr_result


if __name__== '__main__':
    img_path = r"./asset/1.jpg"
    result = ocr(img_path)
    #print(result)
