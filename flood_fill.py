import matplotlib.pyplot as plt


def flood_fill(pic, x, y):
    pic_shape = pic.shape
    x_pic, y_pic = pic_shape
    if x >= x_pic or y >= y_pic or x < 0 or y < 0:
        return pic
    elif pic[x, y] == 0 or pic[x, y] == 2:
        return pic
    elif pic[x, y] == 1:
        pic[x, y] = 2
        plt.imshow(pic, cmap="gray")
        plt.show(block=False)
        plt.pause(0.01)
        plt.clf()
        flood_fill(pic, x + 1, y)
        flood_fill(pic, x - 1, y)
        flood_fill(pic, x, y - 1)
        flood_fill(pic, x, y + 1)
        return pic


def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    # img = floodfill(img, 0, 0)
    flood_fill(img, 0, 0)
    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

if __name__ == "__main__":
    main()
