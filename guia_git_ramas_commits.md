# Guía — Git: Conventional Commits y Branches

## Tipos de Conventional Commits
```
feat: nueva funcionalidad
fix: correccion de un error
docs: cambios en documentacion
style: cambios de formato, sin afectar la logica
refactor: reestructurar codigo sin cambiar su comportamiento
test: agregar o corregir pruebas
chore: tareas de mantenimiento
```

## .gitignore — qué excluir y por qué
```
__pycache__/    archivos temporales que Python genera solo
*.pyc            archivos compilados temporales
venv/             entorno virtual, cada quien crea el suyo
.env               contraseñas o claves secretas
```

## Comandos de ramas (branches)
```bash
git branch                    # ver ramas existentes
git branch nombre-rama        # crear una rama
git checkout nombre-rama      # cambiar a esa rama
git checkout -b nombre-rama   # crear Y cambiar en un solo paso
git branch -m nuevo-nombre    # renombrar la rama actual
git branch -M main            # renombrar de master a main
```

## Flujo de una rama, de principio a fin
```bash
git checkout -b mejoras       # crear y cambiar a la rama
# ... hacer cambios en el código ...
git add .
git commit -m "feat: descripcion del cambio"
git checkout main             # volver a la rama principal
git merge mejoras              # fusionar los cambios
git log --oneline              # verificar el historial completo
```

## Ejemplo visual del flujo
```
main:     A---B---C-------F (merge)
                      \    /
mejoras:                D---E
```
"main" sigue su línea principal. "mejoras" se separa para trabajar 
algo nuevo sin afectar main, y al final se fusiona de vuelta.
