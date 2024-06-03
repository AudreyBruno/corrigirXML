# Sistema de Correção de XMLs

Este é um sistema em Python para corrigir arquivos XML de acordo com as necessidades específicas de correção de NCM e quantidade. Ele possui uma interface gráfica construída com Tkinter.

## Funcionalidades

- Corrigir NCM: Permite ao usuário selecionar uma pasta contendo arquivos XML e alterar o valor da tag NCM.
- Corrigir Quantidade: Calcula a quantidade a partir das tags `vProd` e `vUnCom`, e atualiza as tags `qCom` e `qTrib`.

## Estrutura do Projeto

O projeto está dividido nos seguintes arquivos:

- `app.py`: Contém a interface gráfica do usuário.
- `changeNCM.py`: Contém a lógica para corrigir a tag NCM nos arquivos XML.
- `changeQTD.py`: Contém a lógica para corrigir a quantidade nos arquivos XML.

## Pré-requisitos

- Python 3.x
- Bibliotecas padrão do Python (não são necessárias bibliotecas adicionais)

## Como Executar

1. Clone o repositório ou baixe os arquivos.
2. Certifique-se de que todos os arquivos (`app.py`, `changeNCM.py`, `changeQTD.py`) estejam no mesmo diretório.
3. Execute o arquivo `app.py`:

```bash
python app.py
```

## Uso

- Abra o programa executando app.py.

### Para corrigir o NCM

- Clique no botão "Corrigir NCM" para corrigir a tag NCM:
- Selecione a pasta contendo os arquivos XML.
- Digite o novo valor do NCM quando solicitado.
- Os NCMs serão substituídos pelo novo.

### Para corrigir o NCM

- Clique no botão "Corrigir Quantidade" para corrigir as quantidades:
- Selecione a pasta contendo os arquivos XML.
- As quantidades (qCom e qTrib) serão atualizadas com base nos valores de vProd e vUnCom.

### Obs

- Os arquivos XML corrigidos irão substituir os antigos.

## Contribuição

- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

- Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
