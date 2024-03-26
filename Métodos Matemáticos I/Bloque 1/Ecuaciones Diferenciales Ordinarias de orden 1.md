## Ecuación Diferencial Ordinaria
### Definición
Una ecuación diferencial ordinaria (EDO)  es una ecuación de la forma siguiente: $F(x,y,y',...,y^((n))) = 0$ 
Donde
- $x$ es una variable independiente
- $y=y(x)$ es la incognita
- $y',y'',...,y^((n))$ son sus derivadas sucesivas
### Ejemplos
- $y'=0 <=>y=C$
- $y'=x<=>y=x^2/2+C$
- $y'+xy=1$
- $y'+y''=3y^2$
- $y'+sin(y)=1$
## Orden de una EDO
### Definición
El orden de una EDO es el mayor orden de derivación que aparece en esta.
### Ejemplos
- $y'+y=x$ --> Orden 1
- $y''+yy'$ --> Orden 2
- $(y'')^2 + y^((4))=1$ --> Orden 4
## Solución de una EDO
### Definición
Una solución de una EDO es una función $phi : I -> RR$ ($I = [a,b]$ intervalo en $RR$) que cumple la ecuación $F(x, phi(x), phi'(x), phi''(x),...,phi^((n))(x))=0$ 
### Ejemplo
- $phi(x)=2sinx-1/3cosx$ es solución de $y''+y=cos2x$ 
	- Lo verificamos:
		- $phi'(x) = 2cosx+2/3sin2x$
		- $phi''(x)=4/3cos2x-2sinx$
		- $phi''+phi=4/3cosx-2sinx+2sinx-1/3cos2x = cos2x$
## EDO lineal de orden 1
Son de forma $y'+a(x)y=b(x)$ tal que $a,b:I->RR$ continuas en $I sube RR$, $a$ y $b$ son conocidas
### Método de solución
$y'+a(x)y=b(x)$
1. Calculamos una primitiva de $a(x)$
	- $A(x) = int a(x) dx$
2. Multiplicamos la EDO por $mu(x)=e^(A(x))$ (factor integrante)
	- Queda $e^(A(x))y'+e^(A(x))a(x)y = e^(A(x))b(x)$
3. Observamos que la derivada de $e^(A(x))y$ es la parte izquierda de la ecuación anterior
4. Integramos
	$int (e^(A(x))y' = e^(A(x))a(x)y))dx=int e^(A(x)) b(x)dx$ 
	$<=> e^(A(x))y = int e^(A(x))b(x)dx + C=$
	$<=> y(x) = e^(-A(x)) int (e^(A(x))b(x) e^(-A(x))C)$ 
## EDO de Bernouilli
Son de forma $y'+a(x)y=b(x)y^n , n in RR$
En algunos casos son lineales
- Si $n=0$, $y^n=1 => y'+a(x)y=b(x)$
- Si $n=1$, $y^n=y => y'+(a(x)-b(x))y = 0$
Supongamos entonces que $n != 0, n != 1$ 
- Si $n>0$, $y=0$ es solución
	- $y=0$ es una solución singular, porque no forma parte de la solución general (la que depende de $C$)
### Método de solución general
1. Dividimos la EDO por $y^n$ ($y!=0$)
	- $=> (y')/y^n + a(x) y/y^n = b(x)$
	- $<=> (y')/y^n+a(x)y^(1-n)=b(x)$
	- Cambio de variable: $u=y^(1-n)$ 
		- $u'=(1-n)y^1y^(-n)$
	- $<=>(u')/(1-n)+a(x)u=b(x)$
	- $<=>u'+(1-n)a(x)u=b(x)(1-n)$
	- Resolvemos como una EDO lineal de orden 1
## EDO de variables separadas y separables
### EDO de variables separadas
Son de forma $P(x)dx+Q(y)dy=0$
#### Método de solución
- $P(x)dx+Q(y)dy=0 <=>P(x)dx+Q(y)y'dx$
- Integramos: $int P(x)dx + int Q(y)y'dx=C$
- Integramos respecto a $x$ y $y$ de forma separada: $int P(x)dx + int Q(y)dy=C$
### EDO de variables separables
- Son de forma $P_1(x)Q_1(y)dx+P_2(x)Q_2(y)dy=0$
#### Método de solución
- Dividimos por $Q_1 cdot P_2$
- $(P_1)/(P_2)dx + (Q_1)/(Q_2)dy = 0$
- Resolvemos por variables separadas
## EDO exactas
### Motivación
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
$part(partfx)y = part(partfy)x <=> (del^2f)/(delydelx)=(del^2f)/(delxdely)$
Aplicamos la propiedad de las derivadas cruzadas en la EDO: $P(x,y)dx+Q(x,y)dy=0$
$partPy=del/(dely)partfx=del/(delx)partfy=partQx$
### Definición
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