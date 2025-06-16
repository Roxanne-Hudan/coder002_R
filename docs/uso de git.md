Conceptos Básicos de Git y GitHub
Repositorio
Un repositorio es una estructura de almacenamiento donde se guarda el historial de versiones de un proyecto. Puede estar en tu máquina local (repositorio local) o en un servidor remoto como GitHub (repositorio remoto).

Commits
Un commit es una instantánea del proyecto en un momento específico. Incluye un mensaje descriptivo que ayuda a entender los cambios realizados. Hacer commits regularmente permite crear un historial detallado del proyecto.

Ejemplo de comando para hacer un commit:


Copiar

git commit -m "Descripción de los cambios realizados
Ramas (Branches)
Las ramas permiten desarrollar funcionalidades nuevas de manera aislada del código principal (rama principal o master). Una vez que la funcionalidad está lista y probada, se puede fusionar (merge) con la rama principal.

Ejemplo de comando para crear una nueva rama:


Copiar

git branch nombre_de_la_rama
Fusión (Merge)
La fusión es el proceso de incorporar cambios de una rama en otra. Esto es comúnmente utilizado para integrar nuevas funcionalidades en la rama principal del proyecto.

Ejemplo de comando para fusionar una rama:


Copiar

git merge nombre_de_la_rama
Usando Git y GitHub
Configuración Inicial
Primero, debes instalar Git y configurarlo con tu nombre de usuario y correo electrónico:


Copiar

git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com
Creación de un Repositorio
Para iniciar un nuevo repositorio, navega a la carpeta de tu proyecto y ejecuta:


Copiar

git init
Añadir Archivos al Repositorio
Añade archivos al área de preparación (staging area) para incluirlos en el próximo commit:


Copiar

git add nombre_del_archivo
Para añadir todos los archivos modificados:


Copiar

git add .
Hacer un Commit
Guarda los cambios en el historial del proyecto:


Copiar

git commit -m "Descripción de los cambios
Conectar con GitHub
Para subir tu repositorio a GitHub, primero crea un repositorio en GitHub. Luego, conecta tu repositorio local al remoto:


Copiar

git remote add origin https://github.com/tuusuario/tu-repositorio.gi
Subir Cambios a GitHub
Para subir tus commits al repositorio remoto en GitHub:


Copiar

git push origin master
Clonar un Repositorio
Si deseas trabajar en un proyecto existente en GitHub, puedes clonarlo:


Copiar

git clone https://github.com/tuusuario/tu-repositorio.git
Flujo de Trabajo Básico
Crear una nueva rama para una nueva funcionalidad: bash git checkout -b nueva_funcionalidad

Trabajar en la nueva funcionalidad y hacer commits regularmente: bash git add . git commit -m "Implementa nueva funcionalidad

Cambiar a la rama principal y fusionar los cambios: bash git checkout master git merge nueva_funcionalidad

Subir los cambios a GitHub: bash git push origin master

Conclusión
El control de versiones con Git y GitHub es una práctica esencial para el desarrollo de software moderno. Facilita la colaboración, protege contra la pérdida de datos y mantiene un historial detallado de los cambios. Aprender a utilizar estas herramientas te permitirá gestionar tus proyectos de manera eficiente y profesional.