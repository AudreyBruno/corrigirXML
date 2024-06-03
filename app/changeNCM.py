import xml.etree.ElementTree as ET
import os
from tkinter import filedialog, messagebox, simpledialog

def processXml(xmlFile, newNcm):
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    ET.register_namespace("", "http://www.portalfiscal.inf.br/nfe")

    for ncmTag in root.findall(".//{http://www.portalfiscal.inf.br/nfe}NCM"):
        ncmTag.text = newNcm

    tree.write(xmlFile, encoding="utf-8", xml_declaration=True)

def fixNcm(pasta, newNcm):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".xml"):
            xmlFile = os.path.join(pasta, arquivo)
            processXml(xmlFile, newNcm)

def main():
    pasta = filedialog.askdirectory(title="Selecione a pasta com os XMLs")
    if pasta:
        newNcm = simpledialog.askstring("Novo Valor do NCM", "Digite o novo valor do NCM:")
        if newNcm is not None:
            fixNcm(pasta, newNcm)
            messagebox.showinfo("Concluído", "XMLs corrigidos.")

if __name__ == "__main__":
    main()
