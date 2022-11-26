import cv2

img = cv2.imread('rose.jpg')

#print("Image Properties")
#print("- Number of Pixels: " + str(img.size))
#print("- Shape/Dimensions: " + str(img.shape))
blue, green, red = cv2.split(img) # Split the image into its channels
img_gs = cv2.imread('rose.jpg', cv2.IMREAD_GRAYSCALE) # Convert image to grayscale

cv2_imshow(red) # Display the red channel in the image
cv2_imshow(blue) # Display the red channel in the image
cv2_imshow(green) # Display the red channel in the image
cv2_imshow(img_gs) # Display the grayscale version of image