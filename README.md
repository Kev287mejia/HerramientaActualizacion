# Herramienta de Actualizacion y Mantenimiento del Sistema

Solucion integral disenada para automatizar el mantenimiento preventivo, la actualizacion de controladores y programas, y la recuperacion de espacio en disco en computadoras de trabajo y personales.

---

## Indice de Contenido

1. Proposito del Proyecto
2. Que Hace la Herramienta
3. Por Que es Importante
4. Modos de Operacion
5. Instrucciones de Uso
6. Proximas Integraciones y Mejoras
7. Criterios de Seguridad y Buen Uso
8. Creditos

---

## 1. Proposito del Proyecto

En el dia a dia, la mayoria de las personas y equipos de trabajo descuidan el mantenimiento basico de sus computadoras. Con el paso de los meses, los programas quedan obsoletos, los controladores de hardware dejan de recibir mejoras del fabricante y el disco duro se llena de archivos temporales que ya no sirven.

Esto provoca lentitud, errores inesperados, problemas de compatibilidad y riesgos de seguridad. Realizar este proceso de forma manual requiere abrir aplicacion por aplicacion, buscar controladores en internet y revisar carpetas ocultas del sistema, lo cual consume demasiado tiempo.

Este proyecto fue creado para resolver ese problema de raiz: centralizar y automatizar todas esas tareas en una sola herramienta, para que cualquier usuario o administrador pueda dejar su equipo al dia en cuestion de minutos con un solo clic.

---

## 2. Que Hace la Herramienta

La herramienta organiza el mantenimiento de la computadora en tres tareas principales:

* **Actualizacion de Programas:** Revisa las aplicaciones instaladas en el equipo, comprueba cuales tienen una version mas reciente disponible y las actualiza de forma automatica y silenciosa, sin que el usuario tenga que descargar instaladores a mano.
* **Actualizacion de Controladores y Componentes:** Busca e instala las versiones mas recientes de los controladores de video, sonido, tarjetas de red, procesador y perifericos, asegurando que el hardware funcione correctamente con el sistema operativo.
* **Limpieza y Liberacion de Espacio en Disco:** Elimina de forma segura archivos temporales, vacia carpetas de descargas residuales del sistema, limpia la papelera de reciclaje y restablece la memoria de red, recuperando espacio valioso en el disco duro.
* **Gestion Automatica de Permisos:** Identifica si la cuenta cuenta con permisos de administrador para realizar cambios en el sistema y, si es necesario, solicita la autorizacion correspondiente de manera controlada.

---

## 3. Por Que es Importante

Mantener una computadora actualizada y limpia no es solo cuestion de orden, impacta directamente en el trabajo diario:

### Menos Errores y Cuelgues del Sistema
La mayoria de los bloqueos repentinos y pantallas azules ocurren cuando los controladores de hardware son incompatibles o estan desactualizados. Mantener los componentes al dia garantiza estabilidad.

### Mayor Seguridad
Las empresas que desarrollan software corrigen continuamente fallos de seguridad en cada nueva version. Trabajar con programas desactualizados deja puertas abiertas a virus o accesos no autorizados. Esta herramienta ayuda a cerrar esas brechas a tiempo.

### Mayor Rendimiento y Espacio Libre
Los archivos temporales y la basura acumulada con el uso diario reducen la velocidad de lectura del disco y saturan el almacenamiento. La limpieza periódica mantiene la fluidez del equipo.

### Ahorro de Tiempo de Soporte
Elimina la necesidad de que el personal tecnico o el propio usuario dedique horas a tareas repetitivas de mantenimiento, estandarizando el proceso en una rutina rapida y confiable.

---

## 4. Modos de Operacion

El sistema cuenta con un menu interactivo facil de entender que se adapta a las necesidades de cada momento:

| Modo | Descripcion | Cuando Utilizarlo |
| :--- | :--- | :--- |
| **Mantenimiento Completo** | Ejecuta la limpieza de disco, actualiza todos los programas y actualiza los controladores. | Recomendado para mantenimiento periodico (semanal o mensual). |
| **Solo Limpieza del Sistema** | Borra temporales, vacia papelera y limpia la memoria de red. | Cuando el disco este lleno o se necesite liberar espacio de inmediato. |
| **Solo Controladores** | Busca e instala actualizaciones de hardware y del sistema. | Si conectaste un dispositivo nuevo o experimentas fallos graficos o de red. |
| **Solo Programas** | Actualiza unicamente las aplicaciones instaladas de uso diario. | Para poner al dia navegadores, herramientas de trabajo y utilidades. |
| **Modo Desatendido** | Permite ejecutar tareas especificas por parametros sin mostrar menus. | Util para programaciones automaticas o administracion remota. |

---

## 5. Instrucciones de Uso

### Opcion Recomendada: Inicio Rapido
1. Abre la carpeta del proyecto.
2. Haz doble clic sobre el archivo:
   ```plaintext
   ejecutar_actualizador.bat
   ```
3. Si el sistema solicita permisos de Administrador, acepta la confirmacion para que la herramienta pueda trabajar sobre controladores y archivos del sistema.
4. Elige en pantalla la opcion de mantenimiento que deseas realizar.

### Opcion Avanzada: Ejecucion por Consola
Si deseas automatizar la ejecucion o integrarla en rutinas programadas:

* **Modo Interactivo:**
  ```plaintext
  actualizador_automatico
  ```
* **Mantenimiento Completo Automatico:**
  ```plaintext
  actualizador_automatico --all
  ```
* **Limpieza de Espacio Automatica:**
  ```plaintext
  actualizador_automatico --clean
  ```

---

## 6. Proximas Integraciones y Mejoras

Como lider del proyecto, se ha establecido la siguiente ruta de evolucion para futuras versiones:

* **Panel Central de Estado:** Desarrollo de una vista visual para consultar el historial de mantenimientos y el estado de actualizacion de varios equipos en una misma red.
* **Puntos de Restauracion Preventivos:** Creacion automatica de un respaldo previo antes de instalar controladores criticos, permitiendo deshacer cambios con un solo clic si algo falla.
* **Programacion de Mantenimiento Nocturno:** Opcion para configurar que el mantenimiento se ejecute de madrugada o fuera del horario laboral, apagando el equipo al finalizar.
* **Notificaciones y Reportes:** Envio de un resumen por correo electronico o mensaje notificando cuantos programas se actualizaron y cuanto espacio en disco se logro recuperar.
* **Diagnostico de Salud del Disco:** Alertas tempranas si el disco duro presenta fallas de hardware antes de intentar actualizarlo.

---

## 7. Criterios de Seguridad y Buen Uso

* **Proteccion de Documentos:** La rutina de limpieza unicamente elimina archivos temporales del sistema y descargas intermedias de instalacion. Ningun archivo personal, documento de trabajo o carpeta de usuario es tocado ni modificado.
* **Reinicios:** Si se actualizan controladores principales (como video o red), es recomendable reiniciar el equipo al finalizar para que el sistema operativo cargue los nuevos archivos.

---

MADE WITH LOVE BY KEVIN MEJIA
