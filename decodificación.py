def decodificar_espacios(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    # Reemplaza '(owl)' por 4 espacios
    contenido_decodificado = contenido.replace('(owl)', '    ')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(contenido_decodificado)

if __name__ == "__main__":
    n_file = 'Prueba_cod'
    decodificar_espacios(n_file + ".txt", n_file + "_decod.py")