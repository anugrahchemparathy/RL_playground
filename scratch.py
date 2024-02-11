from basic_env import *


def main():
    gw = GridWorld()
    gw.render()
    gw.step(Action.RIGHT)
    gw.render()
    gw.step(Action.RIGHT)
    gw.render()
    gw.step(Action.UP)
    gw.render()
    gw.step(Action.RIGHT)
    gw.render()
    gw.step(Action.RIGHT)
    gw.render()
    gw.step(Action.UP)
    gw.render()
    gw.visualize()

if __name__ == "__main__":
    main()