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

# Imprimir el arte ASCII una vez al inicio y mantenerlo en la pantalla
clear
echo -e "${GREEN}${ascii_art}${RESET}"
echo -e "${CYAN}----------------------- Escáner de Puertos -----------------------${RESET}"

# Función para escanear un puerto específico
scan_port() {
    timeout 0.00001 bash -c "</dev/tcp/$1/$2" &>/dev/null && echo -e "${LIME}Puerto $2 está abierto${RESET}" &
}

# Función para iniciar el escaneo de puertos
start_scan() {
    ip="$1"
    echo -e "${CYAN}Escaneando todos los puertos de $ip...${RESET}"
    
    for port in {1..65535}; do
        scan_port "$ip" "$port"
    done
    wait
}

# Pedir al usuario que ingrese la IP
read -p "Ingrese la dirección IP a escanear: " ip

# Llamar a la función de escaneo
start_scan "$ip"

# Tag final
echo -e "${RED}--------------------> Modified by </H4ckxel> <-----------------${RESET}"
