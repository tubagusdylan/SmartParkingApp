import cv2
import texttract
import numpy as np

#====================================================================
# Initiliaze CV cascade and character recognition 
cascade = cv2.CascadeClassifier('plat-stage.xml')
blnKNNTrainingSuccessful = texttract.loadKNNDataAndTrainKNN()
if blnKNNTrainingSuccessful == False:
    print("\nerror: KNN traning was not successful\n")
    exit()

#====================================================================
# Class potential plate to store potential rectangulars
class potential_plate:

    def __init__(self, img, x, y, w, h):
        self.imgOriginal = img
        self.imgGrayscale = None
        self.imgThreshold = None
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.intArea = w*h
        self.recognizedstring = ""

#====================================================================
# Image preprocessing 
GAUSSIAN_SMOOTH_FILTER_SIZE = (3, 3)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9

def preprocess(imgOriginal):

    imgGrayscale = extractValue(imgOriginal)
    imgMaxContrastGrayscale = maximizeContrast(imgGrayscale)
    kernel = np.ones((3,3),np.uint8)
    #imgGrayscale = cv2.dilate(imgGrayscale, kernel, iterations=3)
    #imgGrayscale = cv2.erode(imgGrayscale, kernel, iterations=2)
    
    height, width = imgGrayscale.shape
    imgBlurred = np.zeros((height, width, 1), np.uint8)
    imgBlurred = cv2.GaussianBlur(imgMaxContrastGrayscale, GAUSSIAN_SMOOTH_FILTER_SIZE, 0)
    imgThresh = cv2.adaptiveThreshold(imgBlurred, 255.0, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)

    return imgGrayscale, imgThresh

def extractValue(imgOriginal):

    height, width, numChannels = imgOriginal.shape
    imgHSV = np.zeros((height, width, 3), np.uint8)
    imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)
    imgHue, imgSaturation, imgValue = cv2.split(imgHSV)
    return imgValue

def maximizeContrast(imgGrayscale):

    height, width = imgGrayscale.shape

    imgTopHat = np.zeros((height, width, 1), np.uint8)
    imgBlackHat = np.zeros((height, width, 1), np.uint8)

    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    imgTopHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_TOPHAT, structuringElement)
    imgBlackHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_BLACKHAT, structuringElement)

    imgGrayscalePlusTopHat = cv2.add(imgGrayscale, imgTopHat)
    imgGrayscalePlusTopHatMinusBlackHat = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

    return imgGrayscalePlusTopHatMinusBlackHat

#====================================================================
# Main function to extract plate number from image 
def extract_platenumber(img_name):

    global read
    potential_plates = []

    # Open image file and save original copy
    try:
        img = cv2.imread(img_name)
        img_original = img.copy()
    except:
        print("Error opening image file ", img_name)
        return

    # Convert to graysacle and detect potential blocks
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=1, minSize=(75, 75))

    # Save potential blocks, coordinates and including grayscale and threshold images  
    for (x,y,w,h) in plates:
        crop_img = img[y:y+h, x:x+w]
        crop_img = 255-crop_img
        Gray, Tresh = preprocess(crop_img)
        # cv2.imshow("potential", crop_img)
        # cv2.waitKey(0)
        
        a_pot_plate = potential_plate(crop_img, x, y, w, h)
        a_pot_plate.imgGrayscale = Gray
        a_pot_plate.imgThreshold = Tresh
        potential_plates.append(a_pot_plate)

    # Sort based on size of the potential block rectangular  
    if len(potential_plates) > 0:
        potential_plates.sort(key = lambda a_pot_plate: a_pot_plate.intArea, reverse = True)

    # For each detected potential block, try to recognize characters and quit when plate number identified
    for pot_plate in potential_plates:
        read = texttract.detectCharsInPlates(pot_plate.imgGrayscale, pot_plate.imgThreshold)
        # read = pytesseract.image_to_string(pot_plate.imgGrayscale)
        # read = ''.join(e for e in read if e.isalnum())
        read = read[0:8]
        
        # reduce false reading by applying condition of > 4 chars read
        if len(read) > 4:
            # Mark detected plate number on the original image and show along with grayscale
            cv2.rectangle(img_original, (pot_plate.x, pot_plate.y), 
                (pot_plate.x+pot_plate.w, pot_plate.y+pot_plate.h), (0, 0, 255), 2)
            cv2.rectangle(img_original, (pot_plate.x, pot_plate.y-40), 
                (pot_plate.x+pot_plate.w, pot_plate.y), (0, 0, 255), 2)
            cv2.putText(img_original, read, (pot_plate.x, pot_plate.y), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 0, 255), 2, cv2.LINE_AA)

            # cv2.imshow("detected-number", pot_plate.imgGrayscale)
            # cv2.imshow("original", img_original)
            # cv2.waitKey(0)         
           

            # print('Detected plate number = ', read)
            return read
 
            #cv2.imwrite(img_name+'-detected.jpg', pot_plate.imgGrayscale)        
            # break

# files = os.listdir("./sample_images")
# for filename in files:
#     extract_platenumber("./sample_images/" + filename)
# extract_platenumber("./sample_images/test9.jpg")