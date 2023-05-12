from controller import *

def main():
    application = QApplication([])
    window = controller()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()