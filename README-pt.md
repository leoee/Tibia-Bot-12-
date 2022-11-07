# TibiaBot12+
Bot para Tibia 12+. <br>
Isso não funciona no Global, somente em OtServer. <br>
Foi testado em OtServers com versões 12+. Os mesmos permitiam uso de bots.<br>

## Por que não funciona no Global?
A intenção deste bot é ser usado em servidores que os mesmos permitem o uso. Isso fica como uma alternativa gratuita.<br>
Além do mais, para funcionar no Global seria necessário adicionar novas ferramentas para visualização da tela, uma vez que screenshot é só através do jogo.
## Características
- Auto Heal 
- Auto Speed
- Auto Food
- Auto Utamo (Disabled)
- Auto Utito Tempo
- Anti Idle
- Auto SSA
- Auto Equip Ring (Might and Energy)
- Auto Sio (90%, 70% e 50%) (Disabled)

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
 Ele usa PyAutoGui para gerenciar os cliques do mouse e teclas, como as telas do F (F1, F2, etc). Pyscreenshot permite identificar objetos na tela, como barra de vida e mana. 
 Ao clicar em Config Screen, o código vai buscar pelas barra de vida, mana, ferramentas e pelo equipamento. Caso encontre, ele vai salvar as coordenadas em um arquivo JSON para consulta durante o jogo.

 #### Como ele identifica a porcentagem de vida e mana?
 A partir da barra identificada, ele tira uma screenshot do momento e passa a mesma para a grayscale. Com essa escala, conseguimos identificar a porcentagem de cinza - o que representa a falta de cor azul e vermelha - e a partir daí identificamos a porcentagem.
 Por isso é importante em cada máquina ser configurado o que representa cada porcentagem.

 #### Como ele sabe a hora de usar magias de suporte?
 Como foi previamente configurado a região da barra de ferramentas (símbolos de luta, speed, etc), ele consegue procurar por ícones.
 Ele sempre irá procurar pelos seguintes símbolos<br>
 ![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/src/images/speed.png)
 ![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/src/images/food.png)
 ![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/src/images/utito.jpeg)
 ![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/src/images/utamo.png)
## Como configurar? (Necessário somente a primeira vez)
Primeiro de tudo, você precisa configurar sua tela. Para isso, certifique que a barra lateral de vida/mana está ativa. Além disso, também deve estar aparecendo a barra de status e os equipamentos.<br>
Para conseguimos identificar sua barra de vida e mana, elas devem estar completas - isso é, com vida e mana full. Para a barra de ferramentas, você deve estar fora do templo em situação de combate (com o símbolo do fight). Veja o exemplo a seguir<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/src/images/exampleRD.png)<br>
Clique em "Config Screen" no bot. Depois de clicar, um pop-up irá dizer se a configuração foi bem sucedida. Você também pode abrir o arquivo config_location.json e confirmar de que todos os valores não estão zerados.<br> 


Após todas essas etapas, você está agora apto a configurar o que significa 90%, 70% e 50% da barra de vida/mana. Para isso, gaste somente sua mana de acordo com os valores desejados.<br>
Exemplo: se você possui 1000 de mana, use magias até chegar em 900 e clique no botão "Configure 90%". Use novamente até chegar em 700 e clique em "Configure 70%". Faça o mesmo para 50% e isso estará configurado.<br>
Para confirmar de que a configuração de porcentagem de valores funcionou, inicie o bot e acompanhe no título da janela a porcentagem de mana e vida. Elas sempre vão mostrar mais ou menos a porcentagem atual. Veja o exemplo na imagem abaixo.<br>
![alt text](https://github.com/leoee/bot_for_tibia12.01/blob/master/src/images/titleRD.png)<br>
*** Não é necessário gastar vida para configurar a barra. Apenas mana já é suficiente ***<br>
Uma vez que tudo está configurado, as próximas utilizações não vão exigir essa configuração. Desde que as barras fiquem em suas localizações de quando configurado e de que as resoluções da tela não mudem.

## Como usar?
Após a configuração, você pode usar. A forma como este bot funciona é analisando sua tela, então os recursos funcionarão *** SE VOCÊ MANTER NA TELA DO JOGO ***. Você pode mudar a tela, mas as funcionalidades serão executadas quando a tela do jogo estiver aparecendo.

- Você pode usar o "Insert" para iniciar e pausar o bot quando quiser.
- Você pode usar o "Delete" para fechar todo o bot a qualquer momento.
- Para que o Auto Sio funcione, você deve abrir o Party list e filtrar pela ***ÚNICA*** pessoa que você deseja curar. Encha a vida da pessoal e clique em "Check Party List". Neste ponto, é importante que a vida da pessoa esteja em 100% para usar o botão. Caso seja identificado, o botão ficará verde e você está apto para usar a funcionalidade. Certifique-se de ter adicionado a localização do Party List no arquivo config_screen.txt. (disabled)
- Para as funcionalidades que não possuem uma caixa de seleção para ativar, basta colocar a hotkey em branco para não executar a funcionalidade.
- Auto SSA deve ter um hotkey associadas que equipe o SSA.
- Auto Equip Ring deve também possuir hotkey associadas que equipam o ring (Might ou Energy).
- Em caso de Auto SSA e Auto Equip estiverem configurados, o tibia não permite subir os 2 ao mesmo tempo, portanto a prioridade será SSA.

## Avisos
- Recomendado sempre utilizar as barras na sequência já mencionado acima;
- Alguns pontos de melhoria ainda estão sendo implementados. Pode ser que a configuração não funcione 100% em sua máquina;
- O bot foi testado em diferentes telas;
- Caso você utiliza mais de 1 monitor com a opção de estender, o bot pode apresentar lags;
- Por enquanto Auto Sio e Auto Utamo estão desativados. Estavam apresentando problemas com telas diferentes;
- O código está passando por alguns refactors graduais visando melhorar a manutebilidade/legibilidade.