@echo off
echo ========================================
echo    ClassIA - Upload para GitHub
echo ========================================
echo.

echo Inicializando repositório Git...
git init

echo.
echo Adicionando arquivos ao repositório...
git add .

echo.
echo Fazendo commit inicial...
git commit -m "feat: implementa ClassIA - classificacao de cores com rede neural"

echo.
echo Configurando repositório remoto...
git remote add origin https://github.com/ZacariusY/ClassIA.git

echo.
echo Fazendo push para o GitHub...
git branch -M main
git push -u origin main

echo.
echo ========================================
echo    Upload concluído com sucesso!
echo ========================================
echo.
echo Acesse: https://github.com/ZacariusY/ClassIA
echo.
pause
