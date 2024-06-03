import tkinter as tk
import changeNCM as changeNCM
import changeQTD as changeQTD

class AppLayout:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Correção")

        largura_janela = 650
        altura_janela = 350

        # Obtendo as dimensões da tela
        largura_tela = master.winfo_screenwidth()
        altura_tela = master.winfo_screenheight()

        # Calculando as coordenadas para centralizar a janela
        x_pos = largura_tela // 2 - largura_janela // 2
        y_pos = altura_tela // 2 - altura_janela // 2

        # Definindo a posição e o tamanho da janela
        master.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

        self.btn_corrigir_ncm = tk.Button(master, text="Corrigir NCM", command=self.fixNcm)
        self.btn_corrigir_ncm.grid(row=0, column=0, padx=20, pady=20)

        self.btn_corrigir_quantidade = tk.Button(master, text="Corrigir Quantidade", command=self.fixQtd)
        self.btn_corrigir_quantidade.grid(row=0, column=1, padx=20, pady=20)

    def fixNcm(self):
        changeNCM.main()

    def fixQtd(self):
        changeQTD.main()

def main():
    root = tk.Tk()
    app = AppLayout(root)
    root.mainloop()

if __name__ == "__main__":
    main()
