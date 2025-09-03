# ClassIA - Análise da Rede Neural para Classificação de 10 Cores

## Cores Utilizadas no Treinamento

### Cores Claras (Light):
1. **White** (255, 255, 255) - Branco puro
2. **LightGray** (211, 211, 211) - Cinza claro
3. **Green** (0, 255, 0) - Verde puro
4. **Yellow** (255, 255, 0) - Amarelo puro
5. **Cyan** (0, 255, 255) - Ciano (azul claro)

### Cores Escuras (Dark):
1. **Black** (0, 0, 0) - Preto puro
2. **Navy** (0, 0, 128) - Azul marinho
3. **Red** (255, 0, 0) - Vermelho puro
4. **Blue** (0, 0, 255) - Azul puro
5. **Purple** (128, 0, 128) - Roxo

## Análise das Cores

### Critério de Classificação
A rede neural foi treinada para classificar cores como "light" (clara) ou "dark" (escura) baseado nos valores RGB. O critério parece ser:
- **Cores claras**: Valores RGB altos que resultam em luminosidade perceptível
- **Cores escuras**: Valores RGB baixos que resultam em baixa luminosidade

### Observações Interessantes:

1. **Vermelho (255, 0, 0)** foi classificado como "dark" - isso pode parecer contra-intuitivo, mas faz sentido considerando que:
   - Apenas o canal vermelho está no máximo
   - Os canais verde e azul estão em zero
   - A luminosidade percebida pode ser menor que cores com múltiplos canais altos

2. **Verde (0, 255, 0)** foi classificado como "light" - similar ao vermelho, mas talvez a percepção de luminosidade do verde seja diferente

3. **Azul (0, 0, 255)** foi classificado como "dark" - interessante, pois o azul puro tende a ser percebido como mais escuro

4. **Amarelo (255, 255, 0)** foi classificado como "light" - correto, pois combina vermelho e verde no máximo

## Cores de Teste Adicionais

Para testar a generalização da rede, foram adicionadas 5 cores não vistas durante o treinamento:

1. **Dark Blue** (0, 0, 128) - Azul escuro
2. **Orange** (255, 165, 0) - Laranja
3. **Pink** (255, 192, 203) - Rosa
4. **Brown** (139, 69, 19) - Marrom
5. **Lime** (50, 205, 50) - Verde lima

## Resultados Esperados

### Cores de Treinamento:
- **White**: Deve ter alta confiança para "light"
- **LightGray**: Deve ter alta confiança para "light"
- **Black**: Deve ter alta confiança para "dark"
- **Navy**: Deve ter alta confiança para "dark"
- **Red**: Deve classificar como "dark" (pode ser controverso)
- **Green**: Deve classificar como "light"
- **Blue**: Deve classificar como "dark"
- **Yellow**: Deve ter alta confiança para "light"
- **Cyan**: Deve ter alta confiança para "light"
- **Purple**: Deve ter alta confiança para "dark"

### Cores de Teste:
- **Dark Blue**: Esperado "dark" com alta confiança
- **Orange**: Esperado "light" (combina vermelho e verde)
- **Pink**: Esperado "light" (tons claros)
- **Brown**: Esperado "dark" (tons escuros)
- **Lime**: Esperado "light" (verde claro)

## Configuração da Rede Neural

- **Arquitetura**: 3 entradas (RGB) → 6 neurônios ocultos → 2 saídas (light/dark)
- **Iterações**: 2000
- **Taxa de Aprendizado**: 0.03
- **Função de Ativação**: Sigmoid (padrão do brain.js)

## Comentários sobre os Resultados

A rede neural deve conseguir classificar corretamente a maioria das cores, mas pode haver algumas classificações controversas, especialmente com cores primárias puras como vermelho e azul. A performance em cores de teste mostrará a capacidade de generalização da rede.
