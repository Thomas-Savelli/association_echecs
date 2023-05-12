from controllers.base import Controller
from views.base import View

if __name__ == '__main__':
    controller = Controller(view=View)
    controller.start()
