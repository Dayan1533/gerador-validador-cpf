import sys
from validacpf import valida_cpf
from geradorcpf import gera_cpf
from interfaceApp import Ui_MainWindow
import pyperclip as pc

from PyQt5.QtWidgets import QApplication, QMainWindow

class GeraValidaCpf(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCpf.clicked.connect(self.gera_cpf)
        self.btnValidaCpf.clicked.connect(self.valida_cpf)
        self.btnCopiarCpf.clicked.connect(self.copiar_cpf)
        self.btnLinkDayan.clicked.connect(self.linkDayan)

    def gera_cpf(self):
        self.labelRetorno.setText(gera_cpf())

    def valida_cpf(self):
        cpf = self.inputValidaCpf.text()
        if self.inputValidaCpf.text() == '':
            self.labelRetorno.setText('Digite um CPF')
        else:
            if valida_cpf(cpf):
                self.labelRetorno.setText('CPF Válido')
            else:
                self.labelRetorno.setText('CPF Inválido')

    def copiar_cpf(self):
        # Copia o CPF gerado e não copia o CPF válido ou inválido
        if not self.labelRetorno.text() == 'CPF Válido' or self.labelRetorno.text() == 'CPF Inválido' or self.labelRetorno.text() == '':
            pc.copy(self.labelRetorno.text())
            self.inputValidaCpf.setText(pc.paste())
    

    def linkDayan(self):
        import webbrowser
        webbrowser.open('https://www.linkedin.com/in/dayan-gomes-129087213/')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCpf()
    gera_valida_cpf.show()
    qt.exec_()