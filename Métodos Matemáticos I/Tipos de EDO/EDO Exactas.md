## Motivación
$f(x,y)=c:y=y(x)$
Derivamos x con respecto de la igualdad (x)
$$partfx(x,y)+partfy(x,y)y'=0
<=> partfx+partfydy/dx = 0
<=> partfxdx+partfydy=0$$
Si $f$ es conocida, es una EDO..
Llamamos:
- $P(x,y)=partfx(x,y)$
- $Q(x,y)=partfy(x,y)$

Obtenemos una EDO de la forma: $P(x,y)dx+Q(x,y)dy=0$

#### Teorema de Schwarz de las derivadas cruzadas
Si la función es bastante "derivable" (es derivable en todas sus variables y estas tienen derivada segunda), se cumple el Teorema de Schwarz de las derivadas cruzadas:
$$ part(partfx)y = part(partfy)x <=> (del^2f)/(delydelx)=(del^2f)/(delxdely)$$

Aplicamos la propiedad de las derivadas cruzadas en la EDO: $P(x,y)dx+Q(x,y)dy=0$
$$ partPy=del/(dely)partfx=del/(delx)partfy=partQx$$
## Definición
Una EDO de la forma $P(x,y)dx+Q(x,y)dy=0$ se llama exacta ($P, Q$ funciones conocidas) si existe una función $f(x,y)$ tal que $partfx=P$ Es decir, el campo vectorial $(P,Q) = gradf$ 
La solución de esta EDO tiene como forma $f(x,y)=C,$ $C$ constante

#### Propiedad
La EDO $P(x,y)dx+Q(x,y)dy=0$ es exacta si y solo si $partPy=partQx$ 

### Método de resolución (a través de un ejemplo)
Partimos de la EDO de orden 1 siguiente:
$3y+e^x+(3x+cosy)y'=0$
Sabemos que $y'=dy/dx$
Podemos transformar esta ecuación a la forma $P(x,y)dx+Q(x,y)dy=0$:
$3y+e^x+(3x+cosy)dy/dx=0$
$=>(3y+e^x)dx+(3x+cosy)dy=0$
Ya podemos aislar $P$ y $Q$:
${P(x,y)=3y+e^x;Q(x,y)=3x+cosy:}$
Verificamos si es exacta:
${partPy=3;partQx=3:}=>partPy=partQx$
Sabemos también que $gradf(x,y)=(P;Q)$
Es decir, $P=partfx=>f(x,y)=intPdx$
Integramos:
$f(x,y)=intPdx=3xy+e^x+h(y)$ Donde $h(y)$ es una función que depende de $y$
Suponiendo que $h(y)$ es derivable, podemos entonces calcular $ppfy=Q$
$ppfy=3x+h'(y)=Q=3x+cosy$
$=> 3x+h'(y)=3x+cosy$
$=>h'(y)=cosy$
$=>h(y)=siny+K$
Obtenemos entonces nuestra expresión de la solución general:
$f(x,y)=3xy+e^x+siny+K=C$
Podemos juntar las dos constantes:
$f(x,y)=3xy+e^x+siny=C$
La solución forma un plano en $RR^2$.