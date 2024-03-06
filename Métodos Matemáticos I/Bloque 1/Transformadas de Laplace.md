## Funciones de tipo exponencial
$f : [0, +oo;[ -> RR$ (o $f: RR->RR$ pero $f(x)=0$ si $x<0$)
Se dice que $f$ es de tipo exponencial si existen constantes $c>0$ y $a in RR$ tales que $|f(x)| <= Ce^(ax)$ para cada $x >=0$

### Ejemplos
1. Las constantes son de tipo exponencial $f(x)=D, AA x>=0 => |f(x)|=|D| <= |D| e^(ax), AAx>=0$   si $a>0$. Tomamos $C=|D|$
2. Si $f(x)=P(x)$, un polinomio $lim_(x->+oo)P(x)/(e^(ax))=0$ si $a>0$ => existe $c>0$ tal que $|P(x)| <=Ce^(ax), AAx>=0$, $P(x)$ es de tipo exponencial
3. $sin(x), cos(x).$ $$ |sin(x)| <=1, AAx $$ $$|cos(x)| <=1, AAx$$ $$ => |sin(x)| <= 1 <= e^(ax), AAx$$ si a >0. $sin(x), cos(x)$ son tambien de tipo exponencial
4. $f(x) = e^(bx)$ obviamente es de tipo exponencial: $$|e^(bx)| = e^bx, a = b $$ 
Podemos suponer ademas que es continua a trozos en $[0, +oo[$ 
### Ejemplo
$f(x) = {(1, " si " 0<=x<=1), (x^2-1, " si " x>=1)}$
es continua a trozos

Requerimos funciones $f:[0,+oo[ -> RR$ de tipo exponencial y continuas a trozos.

## Transformada de Laplace
$f: [0, +oo[->RR$ como antes. se define la transformada de Laplace de $f$ en un punto $s in RR$ como $L[f](s)=int_0^(oo)e^(-st)f(t)dt$ 
La integral es *impropia* y se entiende como $lim_(N->+oo) int_0^Ne^(-st)f(t)dt$ 
Supongamos que $f$ es continua a trozos y $|f(x)| <= Ce^(ax)$ para ciertas constantes $C>0, a in RR$ y todo $x>=0$ 
Como $f$ es continua a trozos, las integrales $int_0^N e^(-st)f(t)dt$ existen $AA N>=0$ (o $N in NN$, es decir $N=1,2,...$ )
Si acotamos el integrando, $|e^(-st)f(t)| = e^(-st) |f(t)| <= Ce^(at)e(-st)=Ce^((a-s)t) => int_0^N |e^(-st)f(t)|dt <= C int_0^Ne^((a-s)t)dt = [C(e^(a-s)t)/(a-s)]_(t=0)^(t=N) = C/(a-s)(e^((a-s)N) -1)$
Supongamos que $s>a$: 
$=> lim_(N->+oo)c/(a-s)(e^((a-s)N)-1) = c/(s-a)$
=> La integral $int_0^(+oo) e^(-st)f(t)dt$ converge absolutamente (y por lo tanto converge) si $s>a$ $L[f]: ] a, +oo [  -> RR$ 
	
### Ejemplos
1. $f(x) = P(x)$: $|P(x)| <= Ce^(ax), x>=0$ para ciertas $C>0, a>0$ (pero $a>0$ puede tomarse tan pequeña como queramos).$=> L[P](s)$ Esta bien definida si $s>a$, pero $a>0$ es cualquiera $=>L[P](s) " bien definida si " s>0$
2. $f(x)=e^(bx) => a=b$,  $L [e^(bx)] (s) " bien definida si " s>b$
Ejemplo concreto: $f(t)=e^(-t), L[e^(-t)](s)$ definida si $s< -1$ 

### Propiedad
$L$ es lineal, es decir,, si $f,g: [0, +oo[->RR$ continuas a trozos y de tipo exponencial y $alpha, beta in RR$, entonces $L[alphaf(t)+betag(t)](s)=alphaL[f](s) + betaL[g](s)$ 

### Ejemplos concretos
1. $L[1](s)=int_0^(+oo)e^(-st)dt=[-1/se^(-st)]_(t=0)^(+oo) = 1/s => L[1] = 1/s$ 
2. $L[t](s) = int_0^(+oo)te^(-st) dt = lim_(N->+oo)int_0^Nte^-stdt$$obrace(=)^("por partes") lim_(N->+oo)([-t/se^(-st)]_(t=0)^(t=N) - int_0^N(-1/s)e^(-st)dt)$ $= lim_(N->+oo)(-N/se^(-sn)+int_0^N1/se^(-st)d)$$=1/sint_0^(+oo)e^(-st)dt=1/sL[1](s) = 1/(s^2)$

Veamos que si $n in NN$ entonces $L[t^n](s)=(n!)/(s^(n+1))$ 
**Por induccion**:
1. para $n=1$ es correcto, lo acabamos de ver
2. Supongamos que $L[t^n](s) = (n!)/(s^(n+1))$ y veamos que $L[t^(n+1)](s)=((n+1)!)/(s^(n+2))$ $L[t^(n+1)](s) = int_0^(+oo)t^(n+1)e^(-st)dt obrace=^("por partes")$ $[t^(n+1)/(-s)e^(-st)]_(t=0)^(+oo) - int_0^(+oo)((n+1)t^n)/(-s)e^(-st)dt$  $=(n+1)/s int_0^(+oo)t^ne^(-st)dt=(n+1)/sL[t^n](s)$ $obrace=^("Hipotesis de induccion")=(n+1)/scdot(n!)/(s^(n+1))=((n+1)!)/s^(n+2)$ 
3. $ubrace(L[t^n])_(s>0) = (n!)/(s^(n+1))$

#### Ejemplo
$L[e^(bt)] = int_0^(+oo)e^(bt)e^(-st)dt=int_0^(+oo)e^((b-s)t)dt$ 
Supongamos que $s>b$ 
$= [1/(b-s)e^((b-s)t)]^(+oo)_(t=0)$
$=-1/(b-s)=1/(s-b)$
$L[e^(bt)]=1/(s-b)$

#### Ejemplo
$L[sin(at)] = ?$ ($s>0$)
$L[sin(at)](s) = int_0^(+oo)e^(-st)sin(at)dt$
Calculamos primero la primitiva
$I = inte^(-st)sin(at)dt$
$=-1/se^(-st)sin(at)+a/s inte^(-st)cos(at)dt$
$= -1/se^(-st)sin(at)-a/(s^2)cos(at)e^(-st)-(a^2)/(s^2) ubrace(inte^(-st)sin(at)dt)_I$  
$=(1+(a^2)/(s^2))I = -1/se^(-st)(sin(at) + a/scos(at))#$
$= (s^2+a^2)/(s^2) => I = (-s)/(s^2+a^2)e^(-st)(sin(at)+a/s cos(at))$  
$L[sin(at)] = [(-s)/(s^2+a^2)e^(-st)(sin(at) + a/s cos(at))]_(t=0)^(+oo)$ 
$= s/(s^2+a^2)a/s=a/(s^2+a^2)$ 
$=>L[sin(at)]=a/(s^2+a^2)$ 
### Otras formas de calcular
$L[sin(at)] " y " L[cos(at)]$ 
(usando números complejos)
De las formulas de Euler
$e^(iat) = cos(at) + isin(at)$ 
$|e^(iat)|=1, AA t$ 
=> $e^(iat)$ es de tipo exponencial
$L[e^(iat)](s) = int_0^(+oo)e^(-st)e^(iat)dt ubrace(=)_"Se debe entender" int_0^(+oo) e^(-st) cos(at)dt+i int_0^(+oo)e^(-st)sin(at)dt$ 
$= int_0^(+oo) e^((ai-s)t)dt$
$=[1/(ai-s)e^(-st)]_(t=0)^(+oo)$ 
$=1/(s-ia)$
$=>L[e^(iat)]=1/(s-ia)$
$=(s+ia)/(s-ia)$

Como $L[e^(iat)] = L[cos(at)] +iL[sin(at)]$ 
$=s/(s^2+a^2) + i a/(s^2 + a^2)$
$=> {(L[cos(at)]=s/(s^2+a^2), L[sin(at)]=a/(s^2+a^2))}$  
### Propiedades
Sea $f:[0,+oo[->RR$ continua a trozos de tipo exponencial.
1. $L[e^(ct)f(t)](s)=L[f](s-c)$
2. Si $f$ es derivable y $f'$ es continua a trozos y de tipo exponencial, $L[f'](s)=sL[f](s)-f(0)$. 
	- Si $f''$ existe, es continua a trozos y también de tipo exponencial, $L[f''](s) = s^2 L[f](s)-s f(0)-f'(0)$ 
3. Supongamos que $phi(t)$ es una primitiva de $f(t)$ tal que $phi(0)=0$, por ejemplo $phi(t)=int_0^tf(u)du => phi'(t)=f(t), phi(0)=0$ , $L[phi(t)]=L[int_0^tf(u)du]=1/sL[f]$ 
4. $d/(ds) L[f]=-L[tf(t)]$. En general, $d^n/(ds^n)(L[f])=(-1)^nL[t^nf(t)]$ 
5. Convolucion: Sea $g:[0,+oo[->RR$ continua a trozos y de tipo exponencial. Se define la convolucion de $f$ y $g$ como $(f ** g)(t)=int_(-oo)^(+oo)f(t-u)g(u)du$ 
	- $(f**g)(t)=(g**f)(t)=int_(-oo)^(+oo)g(t-u)f(u)du$ 
	- Si ademas $f$ y $g$ son cero en $]-oo,0[$ $(f**g)(t)=int_0^tf(t-u)g(u)du$, ya que $g(u)=0$ si $u<0$, $f(t-u)=0$ si $t-u<0 iff t<u$
	- Ademas, $f**g$ es continua y ademas de tipo exponencial y se cumple $L[f**g]=L[f]*L[g]$ 
6. La transformada de Laplace es inyectiva $L[f]=L[g]ifff=g$ 
	- Ejemplo generico: $F(s)$ sabemos que es la transformada de Laplace de alguna funcion => es funcion, digamos $f(t)$ es unica: $L[f](s)=F(s)$ => $ubrace(L^(-1)[F(t)](t)=f(t))_"Antitransformada de Laplace"$ 

Demostraciones de algunas de las propiedades: 
1. $L[e^(ct)f(t)](s)=int_0^(+oo)e^(-st)e^(ct)f(t)dt$ $=int_0^(+oo)e^(-(s-c)t)f(t)dt$ $=L[f](s-c)$  
3. $phi(t)=int_0^tf(u)du$ Como $phi'(t)=f(t)$, $Lubrace([phi'])_f(s)=s L[phi]-ubrace(phi(0))_=0$$=>L[phi]=L[f]/s$$=>L[int_0^tf(u)du](s)=(L[f](s))/s$ 
4.  $f$ es de tipo exponencial => $tf(t)$ tambien es de tipo exponencial => $L[tf(t)](s)$ existe. Ademas si derivamos $L[f](s)$ respecto de $s$ aparece $L[tf(t)]$ $d/(ds)L[f]=d/(ds)(int_0^(+oo)e^(-st) f(t)dt)$ $=int_0^(+oo)d/(ds)(e^(-st)f(t))dt$ $int_0^(+oo)-te^(-st)f(t)dt$ $=-int_0^(+oo)e^(-st)tf(t)dt$ $=-L[tf(t)](s)$ 
	- Para el caso general se gasta la misma idea $d^n/(ds^n)(L[f](s))=(-1)^nL[t^nf(t)](s)$ 
