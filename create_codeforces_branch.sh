#!/bin/bash

# Script para crear una rama para problemas de diferentes competencias de Codeforces

# Solicitar información
echo "==================================="
echo "     CREACIÓN DE NUEVA RAMA       "
echo "==================================="
echo
echo "Tipos de competencia disponibles:"
echo "---------------------------------"
echo "1) Codeforces"
echo "2) EducationalCodeforces"
echo "3) CodeTon"
echo "4) Otro (ingresa el nombre)"
echo "---------------------------------"

# Función para seleccionar el tipo de competencia
select_competition_type() {
    read -p "Tu selección (1-4 o escribe el nombre directamente): " choice
    echo
    
    case $choice in
        1) 
            echo "Has seleccionado: Codeforces"
            competition_type="Codeforces"
            ;;
        2) 
            echo "Has seleccionado: EducationalCodeforces"
            competition_type="EducationalCodeforces"
            ;;
        3) 
            echo "Has seleccionado: CodeTon"
            competition_type="CodeTon"
            ;;
        4) 
            read -p "Ingresa el nombre de la competencia: " custom_type
            echo "Has ingresado: $custom_type"
            competition_type="$custom_type"
            ;;
        *) 
            echo "Has ingresado un nombre personalizado: $choice"
            competition_type="$choice"
            ;;
    esac
    echo
    echo "Tipo de competencia: $competition_type"
    return 0
}

# Función para validar que un valor sea un número
is_number() {
    [[ $1 =~ ^[0-9]+$ ]]
}

# Capturar el tipo de competencia
select_competition_type
# El tipo de competencia ahora está en la variable $competition_type

echo "==================================="
echo "       NÚMERO DE RONDA            "
echo "==================================="
echo
# Solicitar y validar el número de ronda
while true; do
    read -p "Introduce el número de ronda: " round_number
    if is_number "$round_number"; then
        echo "Número de ronda válido: $round_number"
        break
    else
        echo "Error: Por favor ingresa un número válido"
    fi
done
echo

echo "==================================="
echo "       SELECCIÓN DE DIVISIÓN      "
echo "==================================="
echo
echo "Divisiones disponibles:"
echo "---------------------------------"
echo "1) Div1"
echo "2) Div2"
echo "3) Div3"
echo "4) Div4"
echo "0) Terminar selección"
echo "---------------------------------"

# Función para seleccionar las divisiones
select_divisions() {
    local divisions=()
    
    while true; do
        if [ ${#divisions[@]} -gt 0 ]; then
            echo
            echo "Divisiones seleccionadas: ${divisions[*]}"
            echo
            echo "Divisiones disponibles:"
            echo "---------------------------------"
            echo "1) Div1"
            echo "2) Div2"
            echo "3) Div3"
            echo "4) Div4"
            echo "0) Terminar selección"
            echo "---------------------------------"
        fi
        
        read -p "Tu selección (0-4): " choice
        echo
        
        case $choice in
            1) 
                divisions+=("Div1")
                echo "División 1 agregada"
                ;;
            2) 
                divisions+=("Div2")
                echo "División 2 agregada"
                ;;
            3) 
                divisions+=("Div3")
                echo "División 3 agregada"
                ;;
            4) 
                divisions+=("Div4")
                echo "División 4 agregada"
                ;;
            0) 
                echo "Finalizando selección de divisiones..."
                break
                ;;
            *) echo "Opción inválida, intenta nuevamente";;
        esac
    done
    
    if [ ${#divisions[@]} -eq 0 ]; then
        echo "Sin división"
        divisions_result="Sin_division"
    else
        local IFS="-"
        divisions_result="${divisions[*]}"
        echo "Divisiones seleccionadas: $divisions_result"
    fi
    echo
    return 0
}

# Capturar las divisiones
select_divisions
# Las divisiones ahora están en la variable $divisions_result

# Formatear el nombre de la rama (usando guiones en lugar de barras)
if [ "$divisions_result" == "Sin_division" ]; then
    branch_name="${competition_type}-Round_${round_number}"
    folder_structure="${competition_type}/Round_${round_number}"
else
    branch_name="${competition_type}-Round_${round_number}_${divisions_result}"
    folder_structure="${competition_type}/Round_${round_number}"
fi

echo "==================================="
echo "     COMANDOS A EJECUTAR          "
echo "==================================="
echo
echo "Para crear la estructura de carpetas, ejecuta:"
echo "mkdir -p \"$folder_structure\""
echo
echo "Para crear y cambiar a la nueva rama, ejecuta:"
echo "git checkout -b \"$branch_name\""
echo
echo "==================================="
echo "       INFORMACIÓN DE RAMA        "
echo "==================================="
echo
echo "Crea la rama:"
echo "git checkout -b \"$branch_name\""
echo
echo crea la carpeta con el comando:
echo "mkdir -p \"$folder_structure\""
echo
echo "==================================="