## Motivacion
$f(x,y)=c:y=y(x)$
Derivacmos x con respecto de la igualdad (x)
$$partfx(x,y)+partfy(x,y)y'=0
<=> partfx+partfydy/dx = 0
<=> partfxdx+partfydy=0$$
Si $f$ es conocida, es una EDO..
Llamamos:
- $P(x,y)=partfx(x,y)$
- $Q(x,y)=partfy(x,y)$

Obtenemos una EDO de la forma: $P(x,y)dx+Q(x,y)dy=0$

#### Teorema de Schwarz de las derivadas cruzadas
Si la funcion es bastante "derivable" (es derivable en todas sus variables y estas tienen derivada segunda), se cumple el Teorema de Schwarz de las derivadas cruzadas:
$$ part(partfx)y = part(partfy)x <=> (del^2f)/(delydelx)=(del^2f)/(delxdely)$$

Aplicamos la propiedad de las derivadas cruzadas en la EDO: $P(x,y)dx+Q(x,y)dy=0$
$$ partPy=del/(dely)partfx=del/(delx)partfy=partQx$$
## Definicion
Una EDO de la forma $P(x,y)dx+Q(x,y)dy=0$ se llama exacta (P, Q funciones conocidas) si existe una funcion $f(x,y)$ tal que $partfx=P$ Es decir, el campo vectorial $(P,Q) = gradf$ 
La solucion de esta EDO tiene como forma $f(x,y)=C,$ $C$ constante

#### Propiedad
La EDO $P(x,y)dx+Q(x,y)dy=0$ es exacta si y solo si $partPy=partQx$ 

### Metodo de resolucion (a traves de un ejemplo)
Partimos de la [[Ecuacion diferencial ordinaria]] de orden 1 $$3y+e^x+(3x+cosy)y'=0$$$$y'=dy/dx$$
=> 