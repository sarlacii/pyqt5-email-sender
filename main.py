from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
from email_sender import send_email

class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("main.ui", self)

        self.emailButton.clicked.connect(self.send_email)

    def send_email(self):
        msg='To:' + self.lineEdit.text() + '\nSubject:' + self.lineEdit_subject.text() + '\n'
        result = 0
        try:
            if self.lineEdit.text():
                result = send_email(recipient=self.lineEdit.text(), email=str("%s%s" % (msg, self.textEdit.toPlainText())), sender=self.lineEdit_sender.text(), smtp=str(self.comboBox_smtp.currentText()))
            else:
                message = QMessageBox()
                message.setIcon(QMessageBox.Critical)
                message.setText("Invalid recipient")
                message.setWindowTitle("Error!")
                message.exec_()
        except Exception as e:
            print(e)

        if result >= 1:
            self.lineEdit_result.setText("Sent email to " + self.lineEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()