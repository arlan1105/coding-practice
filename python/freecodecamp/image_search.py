def image_search(images, term):
    return [img for img in images if term.lower() in img.lower()]

print(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "jpeg"))
print(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"))