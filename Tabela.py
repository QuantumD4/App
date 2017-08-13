import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class MenuDemo(QMainWindow):
    def __init__(self):
        super().__init__()


        bar = self.menuBar()


        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')
        Help = bar.addMenu('Help')



        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)


        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)
        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)



        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("App")
        self.resize(600, 400)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')



app = QApplication(sys.argv)
menus = MenuDemo()
sys.exit(app.exec_())