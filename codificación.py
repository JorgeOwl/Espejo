# Abrir el archivo 'Prueba.txt', reemplazar grupos de 4 espacios por '(owl)' y guardar en 'n_file_cod.txt'
def codificar_espacios(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    # Reemplaza cada grupo de 4 espacios por '(owl)'
    contenido_codificado = contenido.replace('    ', '(owl)')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(contenido_codificado)

if __name__ == "__main__":
    n_file = 'Prueba'
    codificar_espacios(n_file + ".txt", n_file + '_cod.txt')