class Solution:
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i] = [1 - x for x in image[i][::-1]]
        return image
