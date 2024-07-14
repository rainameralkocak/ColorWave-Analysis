from PIL import Image
import matplotlib.pyplot as plt

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)

image = Image.open("parrot.jpg")

image.putpixel((0, 1), (1, 1, 5))
image.putpixel((0, 2), (2, 1, 5))

image.show()

histogram = image.histogram()

l1 = histogram[0:256]
l2 = histogram[256:512]
l3 = histogram[512:768]

# Combine histograms
combined_histogram = [l1[i] + l2[i] + l3[i] for i in range(256)]


plt.figure(0)
for i in range(0, 256):
    plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)

plt.figure(1)
for i in range(0, 256):
    plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)

plt.figure(2)
for i in range(0, 256):
    plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)


# Combined histogram
plt.figure(3)  # Create a new figure for the combined histogram
for i in range(0, 256):
    plt.bar(i, combined_histogram[i], color='#%02x%02x%02x' % (255, i, 255), edgecolor='#%02x%02x%02x' % (255, i, 255), alpha=0.3)

plt.show()