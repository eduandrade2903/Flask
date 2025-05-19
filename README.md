# Status do Computador - Monitoramento em Tempo Real 🚀

Este projeto é uma aplicação web desenvolvida com **Flask** que permite monitorar o status do computador em tempo real. A interface exibe informações importantes, como o uso da CPU, memória RAM e disco, de forma visual e interativa, utilizando gráficos dinâmicos.

## 🖥️ Funcionalidades

- **Monitoramento de CPU**: Exibe a porcentagem de uso atual da CPU.
- **Monitoramento de Memória RAM**: Mostra o uso atual da memória RAM.
- **Monitoramento de Disco**: Apresenta a porcentagem de uso do disco.
- **Interface Responsiva**: A interface se adapta a diferentes dispositivos, como desktops, tablets e smartphones.
- **Gráficos Dinâmicos**: Utiliza gráficos do **Chart.js** para uma visualização clara e interativa.
- **Design Moderno**: Inclui ícones representativos e um layout estilizado com **Bootstrap**.

## 🐳 Como Rodar com Docker

1. **Construa a imagem Docker**:
   ```bash
   docker build -t flask-app .

2. **Rode o contêiner**:
   ```bash
   docker run -p 5000:5000 flask-app

3.  **Acesse a aplicação: Abra o navegador e vá para http://localhost:5000**

## 🛠️ Tecnologias Utilizadas
- **Flask**: Framework web para Python.
- **Chart.js** : Biblioteca para gráficos dinâmicos.
- **Bootstrap** : Framework CSS para design responsivo.
- **Docker** : Para containerização da aplicação.
- **Python**: Linguagem de programação principal.
## 📦 Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las manualmente, use:
```bash
pip install -r requirements.txt 
```

