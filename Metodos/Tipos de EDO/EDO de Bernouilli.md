Son de forma $y'+a(x)y=b(x)y^n , n in RR$

En algunos casos son lineales
- Si $n=0$, $y^n=1 => y'+a(x)y=b(x)$
- Si $n=1$, $y^n=y => y'+(a(x)-b(x))y = 0$

Supongamos entonces que $n != 0, n != 1$ 
- Si $n>0$, $y=0$ es solucion
	- $y=0$ es una solucion singular, porque no forma parte de la solucion general (la que depende de $C$)

### Metodo de solucion general
1. Dividimos la [[Ecuacion diferencial ordinaria]] por $y^n$ ($y!=0$)
	- $=> (y')/y^n + a(x) y/y^n = b(x)$
	- $<=> (y')/y^n+a(x)y^(1-n)=b(x)$
	- Cambio de variable: $u=y^(1-n)$ 
		- $u'=(1-n)y^1y^(-n)$
	- $<=>(u')/(1-n)+a(x)u=b(x)$
	- $<=>u'+(1-n)a(x)u=b(x)(1-n)$
	- Resolvemos como una [[EDO lineal de orden 1]]
