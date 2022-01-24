import turtle


def main():
    screen = turtle.Screen()
    michaelangelo = turtle.Turtle()
    screen.colormode(255)

    michaelangelo.speed(50)
    michaelangelo.color(150, 90, 90)

    for i in range(1000):
        michaelangelo.forward(50 + i)
        michaelangelo.right(93)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
