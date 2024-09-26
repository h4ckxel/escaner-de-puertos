#!/bin/bash

# Colores ANSI
GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
LIME='\033[1;32m'
RESET='\033[0m'

# Arte ASCII estático
ascii_art=$(cat << "EOF"
  .uef^"            xeee              < .z@8"`                              x .d88"  
:d88E              d888R               !@88E           uL   ..               5888R   
`888E             d8888R          .    '888E   u     .@88b  @88R      .u     '888R   
 888E .z8k       @ 8888R     .udR88N    888E u@8NL  '"Y888k/"*P    ud8888.    888R   
 888E~?888L    .P  8888R    <888'888k   888E`"88*"     Y888L     :888'8888.   888R   
 888E  888E   :F   8888R    9888 'Y"    888E .dN.       8888     d888 '88%"   888R   
 888E  888E  x"    8888R    9888        888E~8888       `888N    8888.+"      888R   
 888E  888E d8eeeee88888eer 9888        888E '888&   .u./"888&   8888L        888R   
 888E  888E        8888R    ?8888u../   888E  9888. d888" Y888*" '8888c. .+  .888B . 
m888N= 888>        8888R     "8888P'  '"888*" 4888" ` "Y   Y"     "88888%    ^*888%  
 `Y"   888      "*%%%%%%**~    "P'       ""    ""                   "YP'       "%    
      J88"                                                                           
      @%                                                                             
    :"                                                                                
If you want to contribute, visit the creator's GitHub: https://github.com/h4ckxel
EOF
)

# Función para escanear un puerto específico
scan_port() {
    timeout 0.5 bash -c "</dev/tcp/$1/$2" &>/dev/null && echo -e "${LIME}Puerto $2 está abierto${RESET}" &
}

# Función para iniciar el escaneo de puertos
start_scan() {
    ip="$1"
    start_port="$2"
    end_port="$3"
    
    echo -e "${CYAN}Escaneando $ip desde el puerto $start_port hasta el puerto $end_port...${RESET}"
    
    for ((port=start_port; port<=end_port; port++)); do
        scan_port "$ip" "$port"
    done
    wait
}

# Pedir al usuario que ingrese la IP y los puertos
read -p "Ingrese la dirección IP a escanear: " ip
read -p "Ingrese el puerto inicial: " start_port
read -p "Ingrese el puerto final: " end_port

# Mostrar arte ASCII
echo -e "${GREEN}${ascii_art}${RESET}"

# Llamar a la función de escaneo
start_scan "$ip" "$start_port" "$end_port"

# Tag final
echo -e "${RED}--------------------> Modified by </H4ckxel> <-----------------${RESET}"
