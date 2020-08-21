# TibiaBot12+
Bot para Tibia 12+. <br>
Isso não funciona no Global, somente em OtServer. <br>
Foi testado em OtServers com versões 12+. Os mesmos permitiam uso de bots.<br>

## Características
- Auto Heal
- Auto Speed
- Auto Food
- Auto Utamo
- Auto Utito Tempo
- Anti Idle

## Dependências
- Python 3.7+
- PyAutoGUI
- Pyscreenshot
- Pynput
- OpenCv
## Como instalar?
- Baixe Python: https://www.python.org/downloads/release/python-372/
- Após baixar, você pode usar o comando "pip" no terminal. Portanto, abre o terminal e digite os comandos:
    - Instalando PyAutoGUI: ```pip install pyautogui```
    - Instalando Pyscreenshot: ```pip3 install pyscreenshot```
    - Instalando Pynput: ```pip install pynput```
    - Instalando OpenCv: ```pip install opencv-python```
## Como o bot funciona?
 Ele usa PyAutoGui para gerenciar os cliques do mouse e teclas, como as telas do F (F1, F2, etc). Pyscreenshot permite identificar objetos na tela, como barra de vida e mana. Pynput é usado para trigar um ouvinte para salvar suas coordenadas (x, y) do mouse quando você está cortando as imagens da sua tela.
## Como configurar?
Primeiro de tudo, você precisa configurar sua tela. Para isso, você precisa configurar as coordenadas da sua barra de vida, mana, ferramentas e batalhas.<br>
Clique em "Config Screen" no bot. Depois de clicar, um ouvinte vai começar a salvar onde você clica com o botão esquerdo do mouse.<br> 
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/bot.png)<br>
Clique em 2 pontos para cortar uma imagem. Ao finalizar os cliques, clique com o botão direito e o ouvinte será parado e uma imagem será mostrada. Se a imagem estiver correta, copie as coordenadas da mensagem pop-up e salve em "config_screen.txt". Seguem alguns exemplos de imagens abaixo para ajudá-lo no corte. Eu recomendo que você corte com espaço após o valor da vida e mana. Isso porque conforme você sobe de nível, os números que representam sua vida e mana aumentam. Se a imagem não for suficiente para ver todos os números, o bot não funcionará.<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/lifeRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/manaRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/toolsRD.png)<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/images/battleRD.png)<br>
No projeto, existe um arquivo txt com as coordenadas. O conteúdo do arquivo é o seguinte:
```
***Life Bar*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Mana Bar*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Tools*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
***Battle*****
x:"P1.x" - y:"P1.y"
x:"P2.x" - y:"P2.y"
```
Outro exemplo<br>
```
***Life Bar*****
x:"1193" - y:"138"
x:"1344" - y:"154"
***Mana Bar*****
x:"1193" - y:"148"
x:"1357" - y:"167"
***Tools*****
x:"1197" - y:"310"
x:"1313" - y:"327"
***Battle*****
x:"1190" - y:"400"
x:"1357" - y:"477"
```
Esse é o padrão, por favor, não mude.<br>

Após todas essas etapas, você pode verificar suas coordenadas com o botão "Check Config Screen". Se estiver ok, o botão será pintado de verde.<br>

## Como usar?
Após a configuração, você pode usar. A forma como este bot funciona é analisando sua tela, então os recursos funcionarão *** SE VOCÊ MANTER NA TELA DO JOGO ***. Você pode mudar a tela, mas as funcionalidades serão executadas quando a tela do jogo estiver aparecendo.

## Aviso
Se você está tentando usar o bot, mas sempre consegue falhar na "Tela de Check Config", você deve tentar cortar os números do seu Tibia. Como você pode ver, dentro da pasta de imagens, temos várias imagens que representam os números. Corte todos os seus números dentro da tíbia e tente novamente. Apenas os números são necessários.
