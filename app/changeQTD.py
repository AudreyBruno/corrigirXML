import xml.etree.ElementTree as ET
import os
from tkinter import filedialog, messagebox

def processXml(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    ET.register_namespace("", "http://www.portalfiscal.inf.br/nfe")

    for prod in root.findall(".//{http://www.portalfiscal.inf.br/nfe}prod"):
        vProdTag = prod.find(f"{{http://www.portalfiscal.inf.br/nfe}}vProd")
        unComTag = prod.find(f"{{http://www.portalfiscal.inf.br/nfe}}vUnCom")
        if vProdTag is not None and unComTag is not None:
            newValue = float(vProdTag.text) / float(unComTag.text)
            qComTag = prod.find(f"{{http://www.portalfiscal.inf.br/nfe}}qCom")
            if qComTag is None:
                qComTag = ET.Element("qCom")
                prod.append(qComTag)
            qComTag.text = "{:.4f}".format(newValue)

            qTribTag = prod.find(f"{{http://www.portalfiscal.inf.br/nfe}}qTrib")
            if qTribTag is None:
                qTribTag = ET.Element("qTrib")
                prod.append(qTribTag)
            qTribTag.text = "{:.4f}".format(newValue)

    tree.write(xmlFile, encoding="utf-8", xml_declaration=True)

def fixQtd(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".xml"):
            xmlFile = os.path.join(pasta, arquivo)
            processXml(xmlFile)

def main():
    pasta = filedialog.askdirectory(title="Selecione a pasta com os XMLs")
    if pasta:
        fixQtd(pasta)
        messagebox.showinfo("Concluído", "XMLs corrigidos.")

if __name__ == "__main__":
    main()
