		Son de forma $y'+a(x)y=b(x)$ tal que $a,b:I->RR$ continuas en $I sube RR$, $a$ y $b$ son concidas

### Metodo de solucion
$y'+a(x)y=b(x)$
1. Calculamos una primitiva de a(x)
	- $A(x) = int a(x) dx$
2. Multiplicamos la EDO por $mu(x)=e^(A(x))$ (factor integrante)
	- Queda $e^(A(x))y'+e^(A(x))a(x)y = e^(A(x))b(x)$
3. Observamos que la derivada de $e^(A(x))y$ es la parte izquierda de la ecuacionanterior
4. Integramos$$int (e^(A(x))y' = e^(A(x))a(x)y))dx=int e^(A(x)) b(x)dx$$ $$<=> e^(A(x))y = int e^(A(x))b(x)dx + C=$$$$ <=> y(x) = e^(-A(x)) int (e^(A(x))b(x) e^(-A(x))C)$$ 