"""
Configuración de inspectores
Mapeo de username a nombre completo
"""
INSPECTORES = {
    'daniel': 'Daniel Salinas',
    # Agregar más inspectores aquí:
    # 'juan': 'Juan Pérez',
    # 'maria': 'María González',
    # etc.
}

def obtener_nombre_inspector(username):
    """
    Obtiene el nombre completo del inspector basado en su username.
    """
    return INSPECTORES.get(username, username.title())

