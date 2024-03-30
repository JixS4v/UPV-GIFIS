Son de forma $y''=a(x)y'+b(x)y=f(x)$, con $a,b,f$ funciones conocidas y continuas en un intervalo. 
Se dice homogénea si $f=0$, y completa si $f!=0$
## Wronskiano
Sean $phi_1, phi_2$ dos funciones definidas en un intervalo $I$. El Wronskiano de $phi_1$ y $phi_2$, denotado $W(phi_1,phi_2)$, se calcula según la siguiente formula: $W(phi_1,phi_2)=|phi_1(x),phi_2(x);phi_1'(x),phi_2'(x)|$
### Propiedad
Si $W(phi_1,phi_2)(x_0)!=0$ para algún $x_0inI$, entonces $phi_1$ y $phi_2$ son linealmente independientes.
#### Demostración
Basta probar que si $phi_1, phi_2$ con linealmente dependientes (existe $kinRR, phi_1(x)=kphi_2(x)$ $AA x in I$) , entonces $W(phi_1,phi_2)(x)=0 " " AA x in I$ 
## Método de variación de parámetros
$y''+ay'+by=f(x) {a", "b " constantes" ; f(x) " continua en un intervalo " SFS {phi_1(x),phi_2(x)}:}$
1. Buscamos la solución general de la EDO homogénea
	Para una ecuación que presenta esta forma, la solución general de la EDO homogénea $y_h''+ay_h'+by_h=0$ es dada por $y_h=C_1phi_1(x)+C_2phi_2(x)$ 
	Para encontrar $phi_1$ y $phi_2$, resolvemos la ecuación característica, dada por $r^2+ar+b=0$. A partir de las soluciones ${r_1,r_2}$ de la ecuación, calculamos ${phi_1, phi_2}$ como ${phi_1=e^(r_1);phi_2=e^(r_2):}$
2. Buscamos una solución particular de la EDO completa
	Buscamos ahora una solución particular de la EDO completa ($**$), de la forma $y_p=v_1(x)phi_1(x)+v_2(x)phi_2(x)$
	Las funciones $v_1'$ y $v_2'$ deben cumplir el sistema ${phi_1v_1'+phi_2v_2'=0;phi_1'(x)v_1'+phi_2'(x)v_2'=f(x):}$
	El determinante del sistema es $W(phi_1, phi_2)=|phi_1(x),phi_2(x);phi_1'(x),phi_2'(x)|!=0$
	El sistema siempre tiene solución y se puede resolver por la regla de Cramer (altamente ilegal)
	$v_1'(x)=|0,phi_2;f,phi_2'|/(W(phi_1,phi_2))=-(f(x)phi_2)/(W(phi_1,phi_2))$ 
	$v_1(x)=-int(f(x)phi_2)/(W(phi_1,phi_2))dx$
	$v_2'(x)=|phi_1,0;phi_1',f|/(W(phi_1,phi_2))=(f(x)phi_1)/(W(phi_1,phi_2))$
	$v_2=int(f(x)phi_1)/(W(phi_1,phi_2))dx$
	Ya tenemos $y_p$
3. Obtenemos la solución general: $y=y_h+y_p=(v_1(x)+C_1)phi_1(x)+(v_2(x)+C_2)phi_2(x)$
### Ejemplo
$y''-4y'+3y=2e^x$
1. Solución general de la EDO Homogénea
	- Ecuación característica: $r^2-4r+3=0$
	- $r=(4+-sqrt(16-12))/2=(4+-2)/2={3,1}~ SFS ={e^x,e^(3x)}$
	- $y_h=C_1e^x+C_2e^(3x)$
2. Solución particular (con variación de parámetros)
	- $y_p=v_1(x)e^x+v_2(x)e^(3x)$
	- Queremos resolver el sistema en $v_1',v_2'$
	- ${e^xv_1'+e^(3x)v_2'=0;e^xv_1'+3e^(3x)v_2'=2e^x:}$
	- Calculamos $W(e^x,e^(3x))=|e^x,e^(3x);e^x,3e^(3x)|$
	- Regla de Cramer
		- $v_1'= |0,e^(3x) ; 2e^x,3e^(3x)| =(-2e^(4x))/2e^(4x)=-1$ 
		- $v_1=-x$
		- $v_2'= |e^x,0;e^x,2e^x|/(2e^(4x))=(2e^(2x))/(2e^(4x))=e^(-2x)$
		- $v_2=inte^(-2x)dx=-1/2e^(-2x)$
	- $y_p=v_1phi_1+v_2phi_2=-xe^x-1/2e^(-x)e^(3x)=-e^x-(e^x)/2$
	- $y=y_h+y_p=C_1e^x+C_2e^(3x)-e^x(x+1/2)$
### Observación teórica
Por qué un sistema? 
Supongamos que se cumple:
$(S){phi_1v_1'+phi_2v_2'=0;phi_1'v_1'+phi_2'v_2'=0:}$
Veamos que $y''_p+ay'_p+by_p=f(x)$
$y'_p=ubrace(v_1'phi_1+v_2'phi_2)_0+v_1phi_1'+v_2phi_2'=v_1phi_1'+v_2phi_2'$
$y_p''=v_1'phi_1'+v_2'phi_2'+v_1phi_1''+v_2phi_2''$
$=f(x)+v_1phi_1''+v_2phi_2''$
$y_p''+ay_p'+by_p=f(x)+v_1phi_1''+v_2phi_2''+a(v_1phi_1'+v_2phi_2')+b(v_1phi_1+v_2phi_2)$
$=f(x)+v_1(phi_1''+aphi_1'+bphi_1)+v_2(phi_2''+aphi_2+bphi_2)$
$=f(x)$
$=>y_p''+ay_p'+by_p=f(x)$
Volvemos a nuestra ecuación.
## Método de coeficientes indeterminados (tanteo juicioso)
$y''+ay'+by=f(x)$, con $f(x)$ producto de polinomios, exponenciales y senos o cosenos
**Más concretamente**: 
- $f(x)=e^(alphax)(P_n(x)cosbetax+Q_m(x)sinbetax)$
- Con $P_n$ un polinomio de grado $n$, $Q_m$ un polinomio de grado $m$, y $alpha,betainRR$
Buscamos una solución particular de la forma siguiente:
$y_p=e^(alphax)(tildePk(x)cosbetax+tildeQ_k(x)sinbetax)x^s$
con $k=max(m,n)$
$s$ es la multiplicidad de $alpha+-ibeta$ como raíz del polinomio característico.