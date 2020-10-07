from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from Screen_cap import grab_screen
from PIL import Image
import cv2




def main():
    while True:
        img = grab_screen(region=(0,30,1250,750))
        screen = cv2.resize(img, (500, 300))
        R = 1
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        #image = Image.fromarray(img.astype('uint8'), 'RGB')
        screen = entropy(screen, disk(R))
        cv2.imshow("sss",screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

main()
