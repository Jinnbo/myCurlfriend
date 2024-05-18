import cv2

# Read the image
image = cv2.imread('./img.jpg')

# Display the image
cv2.imshow('Test Image', image)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
