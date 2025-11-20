# Wine Dataset - Angel Garcia Romero 22760920

Este proyecto usa un clasificador utilizando el algoritmo de decision tree aplicado al dataset "Wine" usando la libreria scikit-learn

## Objetivo de la practica
- Aprender a entrenar un árbol de decisión como clasificador
- Comprender cómo el modelo genera reglas lógicas interpretables
- Explorar un dataset real (vino) y analizar sus características

## Actividades
- Desarrollar un script en Python que genere el modelo y muestre la precisiopn conseguida
- Cambiar el parametro `max_depth` de `DecisionTreeClassifier` y observar cómo cambian las reglas del arbol
- Entrenar el modelo sin limitar la profundidad y evaluar resultados

## Resultados


max_depth = 2

El arbol es pequeño y tiene muy pocas caracteristicas:
|--- proline <= 755.00
|   |--- flavanoids <= 1.24
|   |   |--- class: 2
|   |--- flavanoids >  1.24
|   |   |--- class: 1
|--- proline >  755.00
|   |--- flavanoids <= 2.28
|   |   |--- class: 2
|   |--- flavanoids >  2.28
|   |   |--- class: 0

max_depth = 4

Se observa que se usan más caracteristicas y el arbol crece en tamaño
|--- proline <= 755.00
|   |--- color_intensity <= 4.85
|   |   |--- flavanoids <= 0.52
|   |   |   |--- class: 2
|   |   |--- flavanoids >  0.52
|   |   |   |--- alcohol <= 13.14
|   |   |   |   |--- class: 1
|   |   |   |--- alcohol >  13.14
|   |   |   |   |--- class: 1
|   |--- color_intensity >  4.85
|   |   |--- hue <= 0.91
|   |   |   |--- class: 2
|   |   |--- hue >  0.91
|   |   |   |--- alcohol <= 13.16
|   |   |   |   |--- class: 1
|   |   |   |--- alcohol >  13.16
|   |   |   |   |--- class: 2
|--- proline >  755.00
|   |--- flavanoids <= 1.61
|   |   |--- malic_acid <= 2.08
|   |   |   |--- class: 1
|   |   |--- malic_acid >  2.08
|   |   |   |--- class: 2
|   |--- flavanoids >  1.61
|   |   |--- magnesium <= 147.00
|   |   |   |--- class: 0
|   |   |--- magnesium >  147.00
|   |   |   |--- class: 1

max_depth = 8 (o none)

El arbol se vuelve mucho más complejo con multiples niveles y reglas muy especificas:

|--- od280/od315_of_diluted_wines <= 2.11
|   |--- color_intensity <= 3.45
|   |   |--- class: 1
|   |--- color_intensity >  3.45
|   |   |--- class: 2
|--- od280/od315_of_diluted_wines >  2.11
|   |--- proline <= 755.00
|   |   |--- flavanoids <= 0.80
|   |   |   |--- class: 2
|   |   |--- flavanoids >  0.80
|   |   |   |--- malic_acid <= 3.86
|   |   |   |   |--- class: 1
|   |   |   |--- malic_acid >  3.86
|   |   |   |   |--- proline <= 630.00
|   |   |   |   |   |--- class: 1
|   |   |   |   |--- proline >  630.00
|   |   |   |   |   |--- class: 0
|   |--- proline >  755.00
|   |   |--- color_intensity <= 3.46
|   |   |   |--- class: 1
|   |   |--- color_intensity >  3.46
|   |   |   |--- class: 0


## Analisis de Resultados
Cuando el max_depth era de 2, el arbol era muy pequeño y tenía muy pocas caracteristicas, pero conforme max_depth fue aumentando empezaba a hacerce mas largo y complejo

Cuando puse el max_depth en None paso lo mismo que cuando iba aumentando la profundidad poco a poco: el arbol se volvió mas complejo y largo y usaba muchas caracteristicas y entre más profundidad (depth) tuviera, mas precisos eran los resultados

¿Crees que tu base de conocimiento cumple con los requerimientos para utilizarse en un modelo de arbol de decisiones?

Respuesta: yo digo que no la podriamos usar en un modelo de arbol de decisiones ya que esta basada en reglas y no en una base de datos estructurada