# ₪ Resolução de Labirinto Com Algoritmo A* ₪

## 🧑 Integrantes
- Guilherme Matos — RA: 2225202220
Turma: 41 | Curso: Ciência da Computação | Período: Noturno | Ano: 2025

## 🚩 Problema
 A automação de um objeto que partindo de um inicio estipulado e querendo chegar em um objetivo determinado encontre o melhor caminho idenpendente se houve obstáculos ou não, juntamente com a geração de um labirinto que crie um caminho possível entre o inicio e objetivo

## 🤖 Abordagem de IA
Para o labirinto foi usado o DFS interativo e para encontar o caminho o algortimo de A*

## 📈 Dados
Todos os dados gerados foram feitos por código. Como a matriz que armazena os estados das células no programa.

## 🛠 Tecnologias

- Python 3.11+  
- Pygame  2.6+


## ▶️ Como reproduzir
Clone o Repositório
```bash
git clone https://github.com/GuiMatosDev/Labirinto-Projeto-IA
```
Instale os requerimentos
```bash
pip install -r requirements.txt
```
Execute o main
```bash
python main.py
```

## 🎯 Resultados do Projeto
Criação do labirinto e Caminho Encontrado<img width="1500" height="500" alt="criação do Labirinto" src="https://github.com/user-attachments/assets/f9198c22-e376-4a36-bbd6-454ec7862f42" />

<img width="800" height="500" alt="caminho" src="https://github.com/user-attachments/assets/e0146a21-936a-4014-9414-d5a3d7b8c815" />



## 🏗️ Estrutura
```bash
├──gitignore	     #Desconsiderações
├──READme.md	     #Documentação
├──camera.py         #Visão do usuário
├──config.py         #Configurações
├──ia.py			 #Algoritmo A*
├──main.py           #Execução da Aplicação
├──mapa.py           #Grade Lógica, visual e geração do labirinto
├──npc.py	     	 #Personagem que segue o algoritmo          
├──requerements.txt  #Dependências
```




