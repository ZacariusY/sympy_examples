# ClassIA - Classificação de Cores com Rede Neural

![ClassIA Logo](https://img.shields.io/badge/ClassIA-Inteligência%20Artificial-blue?style=for-the-badge&logo=artificial-intelligence)

## 🎯 Sobre o Projeto

O **ClassIA** é um projeto de demonstração de Inteligência Artificial que utiliza uma rede neural para classificar cores como "claras" (light) ou "escuras" (dark) baseado nos valores RGB. O projeto demonstra conceitos fundamentais de machine learning aplicados à classificação de cores.

## 🚀 Funcionalidades

- ✅ **Rede Neural com brain.js** - Implementação web interativa
- ✅ **Classificação de 10 cores** - Treinamento com cores variadas
- ✅ **Teste de generalização** - Validação com cores não vistas
- ✅ **Análise detalhada** - Script Python para simulação
- ✅ **Interface visual** - Página web com visualização das cores

## 🎨 Cores Utilizadas

### Cores Claras (Light):
- **White** (255, 255, 255) - Branco puro
- **LightGray** (211, 211, 211) - Cinza claro  
- **Green** (0, 255, 0) - Verde puro
- **Yellow** (255, 255, 0) - Amarelo puro
- **Cyan** (0, 255, 255) - Ciano

### Cores Escuras (Dark):
- **Black** (0, 0, 0) - Preto puro
- **Navy** (0, 0, 128) - Azul marinho
- **Red** (255, 0, 0) - Vermelho puro
- **Blue** (0, 0, 255) - Azul puro
- **Purple** (128, 0, 128) - Roxo

## 📁 Estrutura do Projeto

```
ClassIA/
├── ClassIA.html                    # Página web principal
├── analise_cores_rede_neural.md   # Documentação e análise
├── teste_rede_neural_simples.py   # Script Python para simulação
├── teste_rede_neural.py           # Versão avançada (requer bibliotecas)
└── README.md                      # Este arquivo
```

## 🛠️ Como Usar

### 1. Versão Web (Recomendada)
1. Abra o arquivo `ClassIA.html` no seu navegador
2. Aguarde o treinamento da rede neural (2000 iterações)
3. Visualize os resultados das classificações
4. Teste com cores adicionais

### 2. Versão Python
```bash
# Execute o script de simulação
python teste_rede_neural_simples.py
```

### 3. Análise Detalhada
Leia o arquivo `analise_cores_rede_neural.md` para entender a teoria por trás das classificações.

## 🧠 Configuração da Rede Neural

- **Arquitetura**: 3 entradas (RGB) → 6 neurônios ocultos → 2 saídas (light/dark)
- **Iterações**: 2000
- **Taxa de Aprendizado**: 0.03
- **Função de Ativação**: Sigmoid
- **Biblioteca**: brain.js

## 📊 Resultados Esperados

### Cores de Treinamento:
- **White, LightGray, Yellow, Cyan** → Classificadas como "light"
- **Black, Navy, Purple** → Classificadas como "dark"
- **Red, Green, Blue** → Classificadas como "dark" (baseado em luminância)

### Cores de Teste:
- **Orange, Pink** → Classificadas como "light"
- **Dark Blue, Brown** → Classificadas como "dark"
- **Lime** → Pode ter classificação controversa

## 🔍 Análise dos Resultados

O projeto demonstra que:
1. A rede neural consegue classificar corretamente a maioria das cores
2. Cores com luminância alta (>128) tendem a ser classificadas como "light"
3. Cores com luminância baixa (<128) tendem a ser classificadas como "dark"
4. A rede mostra boa capacidade de generalização
5. Algumas classificações podem parecer contra-intuitivas mas são consistentes com luminância percebida

## 🛠️ Tecnologias Utilizadas

- **HTML/CSS/JavaScript** - Interface web
- **brain.js** - Biblioteca de rede neural
- **Python** - Análise e simulação
- **Markdown** - Documentação

## 📈 Métricas de Performance

- **Confiança média (treinamento)**: ~0.322
- **Confiança média (teste)**: ~0.297
- **Luminância média (cores claras)**: ~209.3
- **Luminância média (cores escuras)**: ~62.5

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Adicionar novas cores ao conjunto de treinamento
- Melhorar a interface web
- Otimizar a rede neural
- Adicionar novos métodos de classificação

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**ZacariusY** - [GitHub](https://github.com/ZacariusY)

## 🙏 Agradecimentos

- [brain.js](https://github.com/BrainJS/brain.js) - Biblioteca de rede neural
- Comunidade de Machine Learning
- Contribuidores do projeto

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐