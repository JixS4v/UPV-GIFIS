## Funciones de tipo exponencial
$f : [0, +oo;[ -> RR$ (o $f: RR->RR$ pero $f(x)=0$ si $x<0$)
Se dice que $f$ es de tipo exponencial si existen constantes $c>0$ y $a in RR$ tales que $|f(x)| <= Ce^(ax)$ para cada $x >=0$

### Ejemplos
1. Las constantes son de tipo exponencial $f(x)=D, AA x>=0 => |f(x)|=|D| <= |D| e^(ax), AAx>=0$   si $a>0$. Tomamos $C=|D|$
2. Si $f(x)=P(x)$, un polinomio $lim_(x->+oo)P(x)/(e^(ax))=0$ si $a>0$ => existe $c>0$ tal que $|P(x)| <=Ce^(ax), AAx>=0$, $P(x)$ es de tipo exponencial
3. $sin(x), cos(x).$ 
	- $|sin(x)| <=1, AAx$ 
	- $|cos(x)| <=1, AAx$ 
	- $=> |sin(x)| <= 1 <= e^(ax), AAx$
	- si a >0. $sin(x), cos(x)$ son también de tipo exponencial
1. $f(x) = e^(bx)$ obviamente es de tipo exponencial: $$|e^(bx)| = e^bx, a = b $$ 
Podemos suponer ademas que es continua a trozos en $[0, +oo[$ 
### Ejemplo
$f(x) = {1, " si " 0<=x<=1; x^2-1, " si " x>=1:}$
es continua a trozos

Requerimos funciones $f:[0,+oo[ -> RR$ de tipo exponencial y continuas a trozos.

## Transformada de Laplace
$f: [0, +oo[->RR$ como antes. se define la transformada de Laplace de $f$ en un punto $s in RR$ como $cc ccL[f](s)=int_0^(oo)e^(-st)f(t)dt$ 
La integral es *impropia* y se entiende como $lim_(N->+oo) int_0^Ne^(-st)f(t)dt$ 
Supongamos que $f$ es continua a trozos y $|f(x)| <= Ce^(ax)$ para ciertas constantes $C>0, a in RR$ y todo $x>=0$ 
Como $f$ es continua a trozos, las integrales $int_0^N e^(-st)f(t)dt$ existen $AA N>=0$ (o $N in NN$, es decir $N=1,2,...$ )
Si acotamos el integrando, $|e^(-st)f(t)| = e^(-st) |f(t)| <= Ce^(at)e(-st)=Ce^((a-s)t) => int_0^N |e^(-st)f(t)|dt <= C int_0^Ne^((a-s)t)dt = [C(e^(a-s)t)/(a-s)]_(t=0)^(t=N) = C/(a-s)(e^((a-s)N) -1)$
Supongamos que $s>a$: 
$=> lim_(N->+oo)c/(a-s)(e^((a-s)N)-1) = c/(s-a)$
$=>$ La integral $int_0^(+oo) e^(-st)f(t)dt$ converge absolutamente (y por lo tanto converge) si $s>a$ $ccL[f]: ] a, +oo [  -> RR$ 

### Ejemplos
1. $f(x) = P(x)$: $|P(x)| <= Ce^(ax), x>=0$ para ciertas $C>0, a>0$ (pero $a>0$ puede tomarse tan pequeña como queramos).$=>  ccL[P](s)$ Esta bien definida si $s>a$, pero $a>0$ es cualquiera $=> ccL[P](s) " bien definida si " s>0$
2. $f(x)=e^(bx) => a=b$,  $L [e^(bx)] (s) " bien definida si " s>b$
Ejemplo concreto: $f(t)=e^(-t),  ccL[e^(-t)](s)$ definida si $s< -1$ 

### Propiedad
$ccL$ es lineal, es decir,, si $f,g: [0, +oo[->RR$ continuas a trozos y de tipo exponencial y $alpha, beta in RR$, entonces $cc ccL[alphaf(t)+betag(t)](s)=alphacc ccL[f](s) + beta ccL[g](s)$ 

### Ejemplos concretos
1. $cc ccL[1](s)=int_0^(+oo)e^(-st)dt=[-1/se^(-st)]_(t=0)^(+oo) = 1/s =>  ccL[1] = 1/s$ 
2. $ccL[t](s) = int_0^(+oo)te^(-st) dt = lim_(N->+oo)int_0^Nte^-stdt$$overset("por partes")(=) lim_(N->+oo)([-t/se^(-st)]_(t=0)^(t=N) - int_0^N(-1/s)e^(-st)dt)$ $= lim_(N->+oo)(-N/se^(-sn)+int_0^N1/se^(-st)d)$$=1/s int_0^(+oo)e^(-st)dt=1/s ccL[1](s) = 1/(s^2)$

Veamos que si $n in NN$ entonces $ccL[t^n](s)=(n!)/(s^(n+1))$ 
**Por induccion**:
1. para $n=1$ es correcto, lo acabamos de ver
2. Supongamos que $ccL[t^n](s) = (n!)/(s^(n+1))$ y veamos que $ccL[t^(n+1)](s)=((n+1)!)/(s^(n+2))$ $ccL[t^(n+1)](s) = int_0^(+oo)t^(n+1)e^(-st)dt overset("por partes")(=)$ $[t^(n+1)/(-s)e^(-st)]_(t=0)^(+oo) - int_0^(+oo)((n+1)t^n)/(-s)e^(-st)dt$  $=(n+1)/s int_0^(+oo)t^ne^(-st)dt=(n+1)/s ccL[t^n](s)$ $overset("Hipotesis de induccion")(=)(n+1)/scdot(n!)/(s^(n+1))=((n+1)!)/s^(n+2)$ 
3. $ubrace( ccL[t^n])_(s>0) = (n!)/(s^(n+1))$

#### Ejemplo
$ccL[e^(bt)] = int_0^(+oo)e^(bt)e^(-st)dt=int_0^(+oo)e^((b-s)t)dt$ 
Supongamos que $s>b$ 
$= [1/(b-s)e^((b-s)t)]^(+oo)_(t=0)$
$=-1/(b-s)=1/(s-b)$
$ccL[e^(bt)]=1/(s-b)$

#### Ejemplo
$ccL[sin(at)] = ?$ ($s>0$)
$ccL[sin(at)](s) = int_0^(+oo)e^(-st)sin(at)dt$
Calculamos primero la primitiva
$I = inte^(-st)sin(at)dt$
$=-1/se^(-st)sin(at)+a/s inte^(-st)cos(at)dt$
$= -1/se^(-st)sin(at)-a/(s^2)cos(at)e^(-st)-(a^2)/(s^2) ubrace(inte^(-st)sin(at)dt)_I$  
$=(1+(a^2)/(s^2))I = -1/se^(-st)(sin(at) + a/scos(at))#$
$= (s^2+a^2)/(s^2) => I = (-s)/(s^2+a^2)e^(-st)(sin(at)+a/s cos(at))$  
$ccL[sin(at)] = [(-s)/(s^2+a^2)e^(-st)(sin(at) + a/s cos(at))]_(t=0)^(+oo)$ 
$= s/(s^2+a^2)a/s=a/(s^2+a^2)$ 
$=> ccL[sin(at)]=a/(s^2+a^2)$ 
### Otras formas de calcular
$ccL[sin(at)] " y "  ccL[cos(at)]$ 
(usando números complejos)
De las formulas de Euler
$e^(iat) = cos(at) + isin(at)$ 
$|e^(iat)|=1, AA t$ 
=> $e^(iat)$ es de tipo exponencial
$ccL[e^(iat)](s) = int_0^(+oo)e^(-st)e^(iat)dt underset("Se debe entender")(=) int_0^(+oo) e^(-st) cos(at)dt+i int_0^(+oo)e^(-st)sin(at)dt$ 
$= int_0^(+oo) e^((ai-s)t)dt$
$={:1/(ai-s)e^(-st)|_(t=0)^(+oo)$ 
$=1/(s-ia)$
$=> ccL[e^(iat)]=1/(s-ia)$
$=(s+ia)/(s-ia)$

Como $ccL[e^(iat)] =  ccL[cos(at)] +i ccL[sin(at)]$ 
$=s/(s^2+a^2) + i a/(s^2 + a^2)$
$=> { ccL[cos(at)]=s/(s^2+a^2);  ccL[sin(at)]=a/(s^2+a^2) :}$  
### Propiedades
Sea $f:[0,+oo[->RR$ continua a trozos de tipo exponencial.
1. $ccL[e^(ct)f(t)](s)= ccL[f](s-c)$
2. Si $f$ es derivable y $f'$ es continua a trozos y de tipo exponencial, $ccL[f'](s)=s ccL[f](s)-f(0)$. 
	- Si $f''$ existe, es continua a trozos y también de tipo exponencial, $ccL[f''](s) = s^2  ccL[f](s)-s f(0)-f'(0)$ 
3. Supongamos que $phi(t)$ es una primitiva de $f(t)$ tal que $phi(0)=0$, por ejemplo $phi(t)=int_0^tf(u)du => phi'(t)=f(t), phi(0)=0$ , $ccL[phi(t)]= ccL[int_0^tf(u)du]=1/s  ccL[f]$ 
4. $d/(ds)  ccL[f]=- ccL[tf(t)]$. En general, $d^n/(ds^n)( ccL[f])=(-1)^n ccL[t^nf(t)]$ 
5. Convolucion: Sea $g:[0,+oo[->RR$ continua a trozos y de tipo exponencial. Se define la convolucion de $f$ y $g$ como $(f ** g)(t)=int_(-oo)^(+oo)f(t-u)g(u)du$ 
	- $(f**g)(t)=(g**f)(t)=int_(-oo)^(+oo)g(t-u)f(u)du$ 
	- Si ademas $f$ y $g$ son cero en $]-oo,0[$ $(f**g)(t)=int_0^tf(t-u)g(u)du$, ya que $g(u)=0$ si $u<0$, $f(t-u)=0$ si $t-u<0 iff t<u$
	- Ademas, $f**g$ es continua y ademas de tipo exponencial y se cumple $ccL[f**g]= ccL[f]* ccL[g]$ 
6. La transformada de Laplace es inyectiva $ccL[f]= ccL[g]ifff=g$ 
	- Ejemplo genérico: $F(s)$ sabemos que es la transformada de Laplace de alguna función $=>$ es función, digamos $f(t)$ es única: $ccL[f](s)=F(s)$ $=>underset("Antitransformada de Laplace")(ccL^(-1)[F(t)](t)=f(t))$ 

Demostraciones de algunas de las propiedades: 
1. $ccL[e^(ct)f(t)](s)=int_0^(+oo)e^(-st)e^(ct)f(t)dt$ $=int_0^(+oo)e^(-(s-c)t)f(t)dt$ $= ccL[f](s-c)$  
3. $phi(t)=int_0^tf(u)du$ Como $phi'(t)=f(t)$, $Lubrace([phi'])_f(s)=s  ccL[phi]-ubrace(phi(0))_(= 0)$$=> ccL[phi]= ccL[f]/s$$=> ccL[int_0^tf(u)du](s)=( ccL[f](s))/s$ 
4.  $f$ es de tipo exponencial $=>$ $tf(t)$ también es de tipo exponencial => $ccL[tf(t)](s)$ existe. Ademas si derivamos $ccL[f](s)$ respecto de $s$ aparece $ccL[tf(t)]$ $d/(ds) ccL[f]=d/(ds)(int_0^(+oo)e^(-st) f(t)dt)$ $=int_0^(+oo)d/(ds)(e^(-st)f(t))dt$ $int_0^(+oo)-te^(-st)f(t)dt$ $=-int_0^(+oo)e^(-st)tf(t)dt$ $=- ccL[tf(t)](s)$ 
	- Para el caso general se gasta la misma idea $d^n/(ds^n)( ccL[f](s))=(-1)^n ccL[t^nf(t)](s)$ 

#### Propiedad
Sea $P/Q(t)$ un cociente de polinomios ($P$,$Q$ polinomios), es decir, una función racional, donde el grado de $P$ es estrictamente menor a el grado de $Q$. Descomponemos en fracciones simples, y aplicamos la anti-transformada de Laplace $=>f(t)= ccL^(-1)[F](t)$ es suma de exponencial por polinomios y exponenciales por senos y cosenos.
- **Ejemplo**: $ccL^(-1)[(s-1)/(s^2-3)]$ 
	- $ccL[cosat]=s/(s^2+a^2)$ => $ccL^(-1)[s/(s^2+3)]=cossqrt3t$
	- $ccL[sinat]=a/(s^2+a^2)$ => $1/(sqrt3) ccL^(-1)[(sqrt3)/(s^2+(sqrt3)^2)]=1/(sqrt3)sinsqrt3t$ 
	- $=>ccL^(-1)[(s-1)/(s^2+30)]=cossqrt3t-1/(sqrt3)sinsqrt3t$ 
- **Ejemplo**: $ccL^(-1)[(s+2)/(s(s^2+2s+2))]$
	- $(s+2)/(s^2(s^2+2s+2)^2)$
	- $A/s+(B_s+C)/(s^2+2s+20)+D/(s^2)$
	- $A=1,B=-1,C=1$ 

# TODO: Contenido de la clase del 12/03/2024
### Resolución del PVI con Transformada de Laplace
#### Idea
1. Tomamos transformada de Laplace en la EDO en $y(t)$
2. Despejamos $ccL[y]=(P(s))/(Q(s))$ función racional
3. Tomamos la transformadad inversa $y(t)=ccL^(-1)[P/Q](t)$ (descomponemos en fracciones simples y luego "identificamos" la inversa en cada sumando)
#### Ejemplo
${y'+y=3e^(2t);y(0)=0:}$  
Tomamos la transformada de Laplace: $bary=ccL[y]$
$ccL[y']+ccL[y]=ccL[3e^(2t)]$
Como $ccL[f'](s)=sccL[f]-f(0)$, $s ccL[y]-y(0)+ccL[y]=3ccL[e^(2t)] = 3/(s-2)$

# Clase del 13/03/2024

$f(t)=1/t -> ccL[1/t]$ **NO EXISTE**
$ccL[1/t](s)=int_0^oo 1/te^(-st)dt$  
$=ubrace(int_0^1 1/t e^(-st)dt)_"no converge"+ubrace(int_1^(+oo)1/te^(-st)dt)_"converge"$ 
$ccL[(e^(-t)-e^(-3t))/t] != underbrace(ccL[(e^(-t))/t]-ccL[e^(-3t)/t])_("No existen")$ 
Si existe $ubrace(ccL[t^(-1/2)]=int_0^1t^(-1/2)e^(-st)dt+int_1^oot^(-1/2)e^(-st)dt)_"Convergen"$ 
3 
a) $int_0^oo e^(-st) (sint)/tdt = "?"$
**Opción 1:** $ccL[e^(-t)(sint)/t](0)$
**Opción 2**: $ccL[(sint)/t](1)$
$ccL[(sint)/t](s)=int_s^ooL[sint](u)du$ 
$= int_s^oo 1/(u^2+1)du=arctan(u)|_(u=s)^(u=+oo)$ 
$=pi/2 - arctan(s)=arctan(1/s) -> "apartado b$ 
$tan(pi/2-5) = (sin(pi/2-s))/(cos(pi/2=s))=(coss)/(sins)=1/(tans)$ 
Basta tomar tan a los lados
$=>ccL[e^(-t)(sint)/t](s)=ccL[(sint)/t](s+1)=arctan(1/(s+1))$
$=>int_0^ooe^(-t)(sint)/tdt={ccL[(sint)/t](1)=arctan1=pi/4;overset("o")(=)ccL[e^(-t)(sint)/t](0)=arctan(1/(s+1))|_(s=0)=pi/4:}$ 
c) $ccL[int_0^t(sinu)/udu](s)=(ccL[(sint)/t](s))/s$ 
$=1/sarctan(1/s)$ 
### Función de Heaviside
$H(t)={1, "si " t>0 ; 0, "si " t<0:}$ 
Sea $f(t)={f_1(t), t<t_0;f_2(t), t>t_0:} ,t_0>0$ 
$H(t-t_0)={1, "si " t>t_0;0, "si " t<t_0:}$ 
$f(t) = f_1(t)+ underset("si " t>t_0)((f_2(t)-f_1(t)))H(t-t_0)$
$g(t)={g_1(t), "si " t<t_0;g_2(t), "si " t_0<t<t_1;g_3(t), "si " t>t_1:}, 0<t_0<t_1$
$g(t)= g_1(t) + (g_2(t)-g_1(t))H(t-t_0)+(g_3(t)-g_2(t))H(t-t_1)$
Veamos que $ccL[f(t-t_0)H(t-t_0]=e^(-st_0)L[f]$
$f(t)=0 " si " t<0$
$f(t-t_0)H(t-t_0)underset(t_0>0)(=){f(t-t_0), "si "t>t_0;0, "si " t<t_0:}$ 
$ccL[f(t-t_0)H(t-t_0)](s)=int_0^oo e^(-st)f(t-t_0)H(t-t_0)dt$
$underset(t_0>0)(=) int_(t_0)^ooe^(-st)f(t-t_0)dt=[u=t-t_0;du=dt]$
$=int_0^ooe^(s(u+t_0))f(u)du$
$=e^(-st_0)int_0^ooe^(-su)f(u)du$
$=e^(-st_0) ccL[f](s)$

#### Ejemplos
$ccL[H(t-a)]=?$ 
$(a>0) e^(-sa)ccL[1]=(e^(-as))/s$ 
$ccL[(t-7)^2e^(3(t-7))H(t-7)](s)=e^(-7s)ccL[t^2e^(3t)]$
$=e^(-7s)ccL[t^2](s-3)=e^(-7s)2/((s-3)^3)$
$L[sintH(t-3)]$

>$sin(t)=sin((t-3)+3)=sin(t-3)cos3+cos(t-3)sin(3)$
>$sin(alpha+-beta)=sinalphacosbeta+-sinbetacosalpha$ 
>$cos(alpha +-beta)=cosalphacosbeta -+sinalphasinbeta$

$ccL[sintH(t-3)]=cos3ccL[sin(t-3)H(t-3)] + sin3ccL[cos(t-3)H(t-3)]$
$=cos3e^(-3s)ccL[sint]+sin3e^(-3s)ccL[cost]$ 
$=e^(-3s)(cos3+s cdot sin3)/(s^2+1)$

6.
$ccL^(-1)[(e^(-5s))/((s+2)^4)]$
$ccL^(-1)[1/((s+2)^4)]=(e^(-2t)t^3)/(3!)=1/6e^(-2t)t^3$
$1/6e^(-2(t-5))(t-5)^3H(t-5)$

7.
 ${y''+2y'+2y=f(t);y(0)=y'(0)=0:}$
 
#### Solución genérica
Tomamos transformada de Laplace:
$bary=ccL[y[$
$ccL[y'']=s^2bary-sy(0)-y'(0)=s^2bary$
$ccL[y']=sbary-y(0)=sbary$
$-> s^2bary+2sbary+2bary = ccL[f]$
$(s^2+2s+2)bary=ccL[f]$
$=> bary=(ccL[f])/(s^2+2s+2)$
$=ccL[f]1/(s^2+2s+2)$
$ccL^(-1)[1/(s^2+2s+2)]$
$ccL^(-1)[1/((s+1)^2+1)]=e^(-t)sint$
$=>bary=ccL[f] cdot ccL[e^(-t)sint]$
$f**g(t)=int_0^tf(t-u)g(u)du$
$=>ccL[f**g]=ccL[f]ccL[g]$
$=>bary=ccL[f**e^(-t)sint]$
$=ccL[int_0^tf(t-u)e^(-u)sinudu]$
Tomamos la transformada inversa
$y(t)=int_0^tf(t-u_e^(-u)sinudu$

#### PVI genérico
${y'''+2y'+5y=f(t);y(0)=C_0", "y'(0)=C_1:}$

Expresamos genéricamente la transformada de $y$ y sus derivadas
$ccL[y]=bary$
$ccL[y']=sbary-y(0)=sbary-C_0$
$ccL[y'']=s^2bary-sy(0)-y'(0)=s^2bary-C_0s-C_1$

Aplicamos la transformada a la EDO
$ccL[f]=s^2bary-C_0s-C_1+2(sbary-C_0)+5bary$
$=>(s^2+2s+5)bary=ccL[f]+C_0s+C_1+2C_0$
$=>bary=(ccL[f])/(s^2+2s+5)+(C_0s+C_1+2C_0)/(s^2+2s+5)$
Completamos el cuadrado
$s^2+2s+5=s^2+2s+1+4=(s+1)^2+2^2$
$ccL^(-1)[1/((s+1)^2+2^2)]=1/2e^(-t)sin2t$
$ccL[e^ctsinat]=a/((s-c)^2+a^2)$
$(C_0s+C_1+2C_0)/((s+1)^2+2^2)=(C_0(s+1)-C_0+C_1+2C_0)/((s+1)^2+2^2)$
$=C_0(s+1)/((s+1)^2+2^2)+(C_0+C_1)1/((s+1)^2+2^2)$
$ccL^(-1)[(C_0s+C_1+2C_0)/((s+1)^2+2^2)]=C_0e^(-t)cos2t+(C_0+C_1)/2e^(-t)sin2t$
$=>y(t)=1/2int_0^tf(t-u)e^(-u)sin(2u)du + C_0e^(-t)cos2t+(C_0+C_1)/2e^(-t)sin2t$ 
Podemos llegar a una solución general de nuestra EDO:
$y(t)=Ae^(-t)cos2t+Be^(-t)sin2+int_0^tf(t-u)e^(-u)sin(u) du$

### Ejemplo
${x=2x-3y;y'=y-2x:}, x(0)=8,y(0)=3$
Definimos las transformadas de $x,y$ y sus derivadas
$barx=ccL[x], bary=ccL[y]$
$ccL[x']=sbarx-x(0)=sbarx-8$
$ccL[y']=sbary-y(0)=sbary-3$

Transformamos el sistema
${sbarx-=2barx-3bary;sbary-3=bary-2barx:} iff {(s-2)barx+3bary=8;2barx+(s-1)bary=3:}$

**Regla de Cramer** (Joaquín nos mata)
Calculamos el determinante del sistema:
$|s-2,3;2,s-1| =(s-2)(s-1)-6=s^2-3s-4=(s+1)(s-4)$
$=>barx = |8,3;3,s-1| / ((s+1)(s-4))=(8s-8-9)/((s+1)(s-4)=(8s-17)/((s+1)(s-4))$
$=>bary=|s-2,8;2,3| /((s+1)(s-4))=(3s-6-16)/((s+1)(s-4))$
Descomponemos en fracciones simples:
$(8s-17)/((s+1)(s-4))=A/(s+1) + B/(s-4)= (A(s-4)+B(s+1))/((s+1)(s-4))$
${A+B=8;-4A+B=-17:}->5A=25->{A=5;B=3:}$
$barx=5/(s+1) + 3/(s-4)$
$(3s-22)/((s+1)(s-4))=A/(s+1)+B/(s-4)=(A(s-4)+B(s+1))/((s+1)(s-4))$
$=>{A+B=3;-4A+B=-22:}->{A=5;B=-2:}$
$bary=5/(s+1)-2/(s-4)$
$=>{x(t)=ccL^(-1)[5/(s+1)+3/(s-4)]=5e^(-t)+3e^(4t); y(t)=ccL^(-1)[5/(s+1)-2/(s-4)]=5e^(-t)-2e^(4t):}$ 