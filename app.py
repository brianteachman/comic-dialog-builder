from comicdialog import *
from ui.controller import Controller


def main():

    try:
        # Create root Tcl window
        root = Tk()
        # root = Toplevel
        root.title("Comic Dialog Builder")

        # Decorate root window with app
        app = ComicDialogBuilder(root)
        app.run()

    except Exception as e:
        logging.exception("Error: %s" % sys.exc_info()[0])


if __name__ == "__main__":
    main()
