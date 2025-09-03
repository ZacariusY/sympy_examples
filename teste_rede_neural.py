#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulação da Rede Neural para Classificação de 10 Cores
Este script simula o comportamento da rede neural brain.js em Python
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.patches as patches

# Cores de treinamento (mesmas do exemplo HTML)
cores_treinamento = [
    ("White", (255, 255, 255), "light"),
    ("LightGray", (211, 211, 211), "light"),
    ("Black", (0, 0, 0), "dark"),
    ("Navy", (0, 0, 128), "dark"),
    ("Red", (255, 0, 0), "dark"),
    ("Green", (0, 255, 0), "light"),
    ("Blue", (0, 0, 255), "dark"),
    ("Yellow", (255, 255, 0), "light"),
    ("Cyan", (0, 255, 255), "light"),
    ("Purple", (128, 0, 128), "dark"),
]

# Cores de teste
cores_teste = [
    ("Dark Blue", (0, 0, 128)),
    ("Orange", (255, 165, 0)),
    ("Pink", (255, 192, 203)),
    ("Brown", (139, 69, 19)),
    ("Lime", (50, 205, 50)),
]

def normalizar_rgb(rgb):
    """Normaliza valores RGB para [0,1]"""
    return [r/255.0, g/255.0, b/255.0]

def calcular_luminancia(rgb):
    """Calcula luminância percebida usando fórmula padrão"""
    r, g, b = rgb
    return 0.299 * r + 0.587 * g + 0.114 * b

def treinar_rede_neural():
    """Treina a rede neural com as cores de treinamento"""
    
    # Preparar dados
    X = []
    y = []
    
    for nome, rgb, label in cores_treinamento:
        X.append(normalizar_rgb(rgb))
        y.append(1 if label == "light" else 0)
    
    X = np.array(X)
    y = np.array(y)
    
    # Criar e treinar rede neural
    mlp = MLPClassifier(
        hidden_layer_sizes=(6,),  # 6 neurônios na camada oculta
        activation='logistic',    # Sigmoid
        solver='sgd',            # Stochastic Gradient Descent
        learning_rate_init=0.03, # Taxa de aprendizado
        max_iter=2000,           # Iterações
        random_state=42
    )
    
    mlp.fit(X, y)
    
    return mlp, X, y

def testar_cores(mlp, cores, tipo="treinamento"):
    """Testa a rede neural com um conjunto de cores"""
    
    print(f"\n=== RESULTADOS - CORES DE {tipo.upper()} ===")
    print("-" * 60)
    
    resultados = []
    
    for nome, rgb in cores:
        # Normalizar entrada
        entrada = normalizar_rgb(rgb)
        
        # Fazer predição
        predicao = mlp.predict([entrada])[0]
        probabilidades = mlp.predict_proba([entrada])[0]
        
        # Calcular luminância real
        luminancia = calcular_luminancia(rgb)
        
        # Determinar classe
        classe = "light" if predicao == 1 else "dark"
        confianca = max(probabilidades)
        
        # Armazenar resultado
        resultado = {
            'nome': nome,
            'rgb': rgb,
            'luminancia': luminancia,
            'predicao': classe,
            'confianca': confianca,
            'prob_light': probabilidades[1],
            'prob_dark': probabilidades[0]
        }
        resultados.append(resultado)
        
        # Exibir resultado
        print(f"{nome:12} RGB{rgb:15} → {classe:5} "
              f"(conf: {confianca:.3f}) | Luminância: {luminancia:.1f}")
    
    return resultados

def analisar_resultados(resultados_treinamento, resultados_teste):
    """Analisa e comenta os resultados obtidos"""
    
    print("\n" + "="*80)
    print("ANÁLISE DETALHADA DOS RESULTADOS")
    print("="*80)
    
    # Análise das cores de treinamento
    print("\n1. CORES DE TREINAMENTO:")
    print("-" * 40)
    
    for resultado in resultados_treinamento:
        nome = resultado['nome']
        rgb = resultado['rgb']
        predicao = resultado['predicao']
        confianca = resultado['confianca']
        luminancia = resultado['luminancia']
        
        # Comentários específicos
        comentario = ""
        if nome == "Red":
            comentario = " (Interessante: vermelho puro classificado como escuro)"
        elif nome == "Green":
            comentario = " (Verde puro classificado como claro)"
        elif nome == "Blue":
            comentario = " (Azul puro classificado como escuro)"
        elif nome == "Yellow":
            comentario = " (Amarelo corretamente classificado como claro)"
        elif nome == "Cyan":
            comentario = " (Ciano corretamente classificado como claro)"
        
        print(f"  {nome}: {predicao} (conf: {confianca:.3f}, lum: {luminancia:.1f}){comentario}")
    
    # Análise das cores de teste
    print("\n2. CORES DE TESTE (GENERALIZAÇÃO):")
    print("-" * 40)
    
    for resultado in resultados_teste:
        nome = resultado['nome']
        rgb = resultado['rgb']
        predicao = resultado['predicao']
        confianca = resultado['confianca']
        luminancia = resultado['luminancia']
        
        # Comentários sobre generalização
        comentario = ""
        if nome == "Orange":
            comentario = " (Boa generalização: laranja é efetivamente claro)"
        elif nome == "Pink":
            comentario = " (Boa generalização: rosa é efetivamente claro)"
        elif nome == "Brown":
            comentario = " (Boa generalização: marrom é efetivamente escuro)"
        elif nome == "Lime":
            comentario = " (Boa generalização: verde lima é claro)"
        
        print(f"  {nome}: {predicao} (conf: {confianca:.3f}, lum: {luminancia:.1f}){comentario}")
    
    # Estatísticas gerais
    print("\n3. ESTATÍSTICAS:")
    print("-" * 40)
    
    confianca_media_treinamento = np.mean([r['confianca'] for r in resultados_treinamento])
    confianca_media_teste = np.mean([r['confianca'] for r in resultados_teste])
    
    print(f"  Confiança média (treinamento): {confianca_media_treinamento:.3f}")
    print(f"  Confiança média (teste): {confianca_media_teste:.3f}")
    print(f"  Diferença de confiança: {abs(confianca_media_treinamento - confianca_media_teste):.3f}")
    
    # Análise de luminância vs predição
    print("\n4. ANÁLISE LUMINÂNCIA vs PREDIÇÃO:")
    print("-" * 40)
    
    todos_resultados = resultados_treinamento + resultados_teste
    light_cores = [r for r in todos_resultados if r['predicao'] == 'light']
    dark_cores = [r for r in todos_resultados if r['predicao'] == 'dark']
    
    if light_cores:
        lum_light = np.mean([r['luminancia'] for r in light_cores])
        print(f"  Luminância média (cores claras): {lum_light:.1f}")
    
    if dark_cores:
        lum_dark = np.mean([r['luminancia'] for r in dark_cores])
        print(f"  Luminância média (cores escuras): {lum_dark:.1f}")

def criar_visualizacao(resultados_treinamento, resultados_teste):
    """Cria visualização das cores e resultados"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Cores de treinamento
    ax1.set_title('Cores de Treinamento', fontsize=14, fontweight='bold')
    y_pos = 0
    for resultado in resultados_treinamento:
        rgb = resultado['rgb']
        nome = resultado['nome']
        predicao = resultado['predicao']
        confianca = resultado['confianca']
        
        # Criar retângulo colorido
        rect = patches.Rectangle((0, y_pos), 1, 0.8, 
                               facecolor=[c/255.0 for c in rgb], 
                               edgecolor='black', linewidth=1)
        ax1.add_patch(rect)
        
        # Adicionar texto
        ax1.text(1.1, y_pos + 0.4, f"{nome}\n{predicao} ({confianca:.3f})", 
                va='center', fontsize=10)
        
        y_pos += 1
    
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, len(resultados_treinamento))
    ax1.set_yticks([])
    ax1.set_xticks([])
    
    # Cores de teste
    ax2.set_title('Cores de Teste', fontsize=14, fontweight='bold')
    y_pos = 0
    for resultado in resultados_teste:
        rgb = resultado['rgb']
        nome = resultado['nome']
        predicao = resultado['predicao']
        confianca = resultado['confianca']
        
        # Criar retângulo colorido
        rect = patches.Rectangle((0, y_pos), 1, 0.8, 
                               facecolor=[c/255.0 for c in rgb], 
                               edgecolor='black', linewidth=1)
        ax2.add_patch(rect)
        
        # Adicionar texto
        ax2.text(1.1, y_pos + 0.4, f"{nome}\n{predicao} ({confianca:.3f})", 
                va='center', fontsize=10)
        
        y_pos += 1
    
    ax2.set_xlim(0, 3)
    ax2.set_ylim(0, len(resultados_teste))
    ax2.set_yticks([])
    ax2.set_xticks([])
    
    plt.tight_layout()
    plt.savefig('c:\\Users\\Yago\\sympy_examples\\resultados_rede_neural.png', 
                dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Função principal"""
    
    print("REDE NEURAL - CLASSIFICAÇÃO DE CORES")
    print("="*50)
    
    # Treinar rede neural
    print("Treinando rede neural...")
    mlp, X, y = treinar_rede_neural()
    print("Treinamento concluído!")
    
    # Testar cores de treinamento
    resultados_treinamento = testar_cores(mlp, 
                                        [(nome, rgb) for nome, rgb, _ in cores_treinamento], 
                                        "treinamento")
    
    # Testar cores de teste
    resultados_teste = testar_cores(mlp, cores_teste, "teste")
    
    # Analisar resultados
    analisar_resultados(resultados_treinamento, resultados_teste)
    
    # Criar visualização
    print("\nCriando visualização...")
    criar_visualizacao(resultados_treinamento, resultados_teste)
    print("Visualização salva como 'resultados_rede_neural.png'")
    
    print("\n" + "="*80)
    print("ANÁLISE CONCLUÍDA!")
    print("="*80)

if __name__ == "__main__":
    main()
