from comicdialog import *

def main():

    # -------------------------------------------------------------------------
    # Create root Tcl window
    # -------------------------------------------------------------------------

    root = Tk()
    root.title("Comic Dialog Builder")

    # -------------------------------------------------------------------------
    # Decorate root window with app
    # -------------------------------------------------------------------------

    app = ComicDialogBuilder(root)
    app.run()

if __name__ == "__main__":
    main()
