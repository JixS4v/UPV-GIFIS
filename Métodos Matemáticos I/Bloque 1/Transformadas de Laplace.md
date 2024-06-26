## Funciones de tipo exponencial
$f : [0, +oo;[ -> RR$ (o $f: RR->RR$ pero $f(x)=0$ si $x<0$)
Se dice que $f$ es de tipo exponencial si existen constantes $c>0$ y $a in RR$ tales que $|f(x)| <= Ce^(ax)$ para cada $x >=0$

### Ejemplos
1. Las constantes son de tipo exponencial $f(x)=D, AA x>=0 => |f(x)|=|D| <= |D| e^(ax), AAx>=0$   si $a>0$. Tomamos $C=|D|$
2. Si $f(x)=P(x)$, un polinomio $lim_(x->+oo)P(x)/(e^(ax))=0$ si $a>0=>EEc>0$ tal que $|P(x)| <=Ce^(ax), AAx>=0$, $P(x)$ es de tipo exponencial
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
5. Convolución: Sea $g:[0,+oo[->RR$ continua a trozos y de tipo exponencial. Se define la convolución de $f$ y $g$ como $(f ** g)(t)=int_(-oo)^(+oo)f(t-u)g(u)du$ 
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
### Resolución del PVI con Transformada de Laplace
#### Idea
1. Tomamos transformada de Laplace en la EDO en $y(t)$
2. Despejamos $ccL[y]=(P(s))/(Q(s))$ función racional
3. Tomamos la transformada inversa $y(t)=ccL^(-1)[P/Q](t)$ (descomponemos en fracciones simples y luego "identificamos" la inversa en cada sumando)
#### Ejemplo
${y'+y=3e^(2t);y(0)=0:}$  
Tomamos la transformada de Laplace: $bary=ccL[y]$
	$ccL[y']+ccL[y]=ccL[3e^(2t)]$
	Como $ccL[f'](s)=s ccL[f]-f(0)$, $s ccL[y]-y(0)+ccL[y]=3ccL[e^(2t)] = 3/(s-2)$
	Usamos $bary=ccL[y]$; $sbary-underbrace(y(0))_("0 "->" C.I.")+bary(s)=3/(s-2)$ 
$=>bary(s)=3/((s+1)(s-2))$ ;  $y(t)=ccL^(-1)[3/((s+1)(s-2))]$ 
Descomponemos en fracciones simples
	$3/((s+1)(s-2))=A/(s+1)+B/(s-2)$ , $A,B$ por determinar
	$3/((s+1)(s-2))=(A(s-2)+B(s+1))/((s+1)(s-2))$
	$iffA(s-2)+B(s+1)=3iff(A+B)s-2A+B=3$
	$=>{A+B=0, => B=-A;-2A+B=3,=>-3A=3:}=>{A=-1;B=1:}$
	$=>bary(s)=-1/(s+1)+1/(s-2)$
	Es una descomposición única ya que son monomios linealmente independientes que solo tienen una solución.
Tomamos la transformada inversa
	$=>y(t)=ccL^(-1)[bary(s)](t)=ccL^(-1)[-1/(s+1)](t)+L^(-1)[1/(s-2)](t)=-e^t+e^(2t)$
#### Ejemplo

${y''-4y'+4y=0;y(0)=0", "y'(0)=3:}$

Tomamos la transformada de Laplace:
	$ccL[y'']-4ccL[y]+4ccL[y]=0;$
	$ccL[y'']=s^2bary-sy(0)-y'(0);$
	$ccL[y']=s bary-y(0)$
	Con $bary=ccL[y]$
$=>s^2bary-sy(0)-y'(0)-4(sbary-y(0))+4bary=s^2bary-3-4sbary+4bary=0$
$=>(s^2+4s+4)bary=3=>bary=3/(s^2-4s+4)$
$bary=3/((s-2)^2)$ 
$y=ccL^(-1)[3/((s-2)^2)](t)$ 
Como $ccL[t]=1/(s^2)$ , y $ccL[e^ctf(t)]=ccL[f](s-c)$

#### Ejemplo

${y''+2y'+2y=2;y(0)=0", "y'(0)=1:}$ 

Tomamos transformada de Laplace ($bary=ccL[y]$):
	$s^2bary-sy(0)-y'(0)+2(sbary-y(0))+2bary=s^2bary-1+2sbary+2bary=2/s$
	$=>(s^2-2s+2)bary=2/s+1=(2+s)/s=>bary=(2+s)/(s(s^2-2s+2))$
$s^2+2s+2=0$ no tiene raíces reales, completamos cuadrados:
	$s^2+2s+1+1=(s+1)^2+1$
$bary=(2+s)/(s((s+1)^2+1))$
Descomponemos en fracciones simples:
	$(2+s)/(s((s+1)^2+1))=A/s+(Bs+C)/((s+1)^2+1)$ 
	$=(A((s+1)^2+1)+(Bs+C)s)/(s((s+1)^2+1)$
	$=>s+2=A((s+1)^2+1)+Bs^2+Cs$
	${A+B=0;2A+C=1;2A=2:}=>{A=1;B=-1;C=-1:}$ 
	$bary(s)=1/s-(s+1)/((s+1)^2+1)$ 
	$(ccL[cost]=s/(s^2+1);ccL[e^(-t)cost]=(s+1)/((s+1)^2+1);ccL[1]=1/s)$ 
	$=>y(t)=1-e^tcost$ 
#### Ejemplo
Calcula la transformada de Laplace de $F(t)={5,"si "0<t<3;0,"si "t>3:}$ 
Aplicando la definición de la transformada de Laplace:
	$ccL[F](s)=int_0^ooe^(-st)F(t)dt$
	$=int_0^3e^(-st)F(t)dt+int_3^ooe^(-st)F(t)dt$
	$=5int_0^3e^(-st)dt=[-5/3e^(-st)]^(t=3)_(t=0)=-5/3(1-e^(-3s))$ 
$L[F](s)=-5/3(1-e^(-3s))$ 
#### Problema 2 (PoliformaT)
Ya sabemos que si $f$ es de tipo exponencial, $tf(t)$ también es de tipo exponencial, además $ccL[t^nf(t)](s)=(-1)^n(d^n)/(ds^n)ccL[f](s)$ 
$ccL[tcost]=d/(ds)ccL[cost]=-d/(ds)(s/(s^2+1))=-(s^2+1-2s^2)/((s^2+1)^2)=(s^2-1)/((s^2+1)^2)$ 
$ccL[t^2sint]=(d^2)/(ds^2)(1/(s^2+1))=d/(ds)(-(2s)/((s^2+1)^2))=(-2(s^2+1)^2-2s(2s)2(s^2+2))/((s^2+1)^4)=(6s^4+4s^2-2)/((s^2+1)^4)$
#### Propiedad
Si $(f(t))/t$ es de tipo exponencial, $f(t)$ también será de tipo exponencial $=>ccL[(f(t))/t](s)=int_s^ooccL[f](u)du$ . ($**$)
Para demostrarlo, usamos primero otra propiedad.
##### Propiedad
Si $f$ es de tipo exponencial, entonces $lim_(s->+oo)ccL[f](s)=0$
##### Demonstración
Supongamos que $|f(t)|<=ce^(at)$ para ciertas contstantes $c>0, a in RR$, y $AAt>=0$ $|ccL[f](s)|=|int_0^ooe^(-st)|f(t)|dt<=c int_0^ooe^(-st)e^atdt=c int_0^ooe^(-(s-a)t)dt$ 
Si $s>a$, la integral anterior converge (y además $ccL[f](s)$ está bien definida)
Pero $int_0^ooe^(-(s-a)t)dt=[-(e^(-(s-a)t))/(s-a)]^(t=oo)_(t=0)=1/(s-a)$
Por tanto, $|ccL[f](s)|<=c/(s-a), s>a " si " s->oo$
$=>lim_(s->+oo)ccL[f](s)=0$ 

Volviendo a ($**$), definimos $g(t)=(f(t))/t=>f(t)=tg(t)$,
Tomamos transformada de Laplace:
	$ccL[f]=ccL[tg(t)]=-d/(ds)ccL[g]$
	$=>int_s^(+oo)ccL[f](u)du=int_s^ood/(ds)ccL[g](u)du$
	$=[ccL[g](u)]_(u=s)^(u=+oo)$
	$=ubrace(-lim_(u->+oo)ccL[g](u))_(underset("Por Propiedad anterior")(0))+ccL[g](s)$
Hemos probado ($**$) ya que $g(t)=(f(t))/t$ 
#### Aplicación
Cálculo de integrales. Queremos calcular integrales del tipo $int_0^ooe^(-at)f(t)dt$. Esto recuerda a $ccL[f](s)$ en $s=a$.
##### Ejemplo
$int_0^ooe^(-3t)cos2tdt$ Calculamos primero $ccL[cos2t](s)=s/(s^2+2^2)=>int_0^ooe^(-3t)cos(2t)dt=ccL[cos2t](3)=3/(9+4)=3/13$
##### Ejemplo
$f(t)=1/t -> ccL[1/t]$ **NO EXISTE**
$ccL[1/t](s)=int_0^oo 1/te^(-st)dt$  
$=ubrace(int_0^1 1/t e^(-st)dt)_"no converge"+ubrace(int_1^(+oo)1/te^(-st)dt)_"converge"$ 
$ccL[(e^(-t)-e^(-3t))/t] != underbrace(ccL[(e^(-t))/t]-ccL[e^(-3t)/t])_("No existen")$ 
Si existe $ubrace(ccL[t^(-1/2)]=int_0^1t^(-1/2)e^(-st)dt+int_1^oot^(-1/2)e^(-st)dt)_"Convergen"$ 
#### Problema 3 (PoliformaT)
a. $int_0^oo e^(-st) (sint)/tdt = "?"$
**Opción 1:** $ccL[e^(-t)(sint)/t](0)$
**Opción 2**: $ccL[(sint)/t](1)$
$ccL[(sint)/t](s)=int_s^ooL[sint](u)du$ 
$= int_s^oo 1/(u^2+1)du=arctan(u)|_(u=s)^(u=+oo)$ 
$=pi/2 - arctan(s)=arctan(1/s) -> "apartado b$ 
$tan(pi/2-5) = (sin(pi/2-s))/(cos(pi/2=s))=(coss)/(sins)=1/(tans)$ 
Basta tomar tan a los lados
$=>ccL[e^(-t)(sint)/t](s)=ccL[(sint)/t](s+1)=arctan(1/(s+1))$
$=>int_0^ooe^(-t)(sint)/tdt={ccL[(sint)/t](1)=arctan1=pi/4;overset("o")(=)ccL[e^(-t)(sint)/t](0)=arctan(1/(s+1))|_(s=0)=pi/4:}$ 
c. $ccL[int_0^t(sinu)/udu](s)=(ccL[(sint)/t](s))/s$ 
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
## Teoremas Límite
### Teorema del Valor Inicial
Bajo las condiciones adecuadas sobre $f: [0,+oo[->R$ se cumple:$lim_(t->0^+)f(t)=lim_(s->+oo)s ccL[f(s)]$
#### Demostración
- Supongamos que $f$ es de tipo exponencial (entonces $f'$ es también de tipo exponencial)
- Como $f'$ es de tipo exponencial, sabemos que $ccL[f'](s)->0$ si $s->+oo$ (lo vimos)
- Usamos ahora que $ccL[f']=s ccL[f]-f(0)$ 
- Si tomamos límite cuando $s->+oo$: $0=lim_(s->+oo)ccL[f'](s)=lim_(s->+oo)[s ccL[f](s)-f(0)]$ 
- Supongamos que $f$ es continua en $t=0$
	- $=>lim_(t->0^+)f(t)=f(0)$
- $=>lim_(t->0^+)f(t)=f(0)=lim_(s->+oo)s ccL[f](s)$
- si $f$ no fuera continua en $t=0$, basta tomar $lim_(t->0^+)f(t)$ en vez de $f(0)$
## Teorema del Valor Final
Bajo las condiciones adecuadas sobre la función $f:[0,+oo[->RR$ se cumple $lim_(t->+oo)f(t)=lim_(s->0^+)ccL[f](s)$ 
### Propiedad
Supongamos que $f$ es de tipo exponencial: $|f(t)|<=Ce^(at)$ para ciertas $C>0, ainRR$ y todo $t>=0$. Si $s,s_0>a$, entonces $lim _(s->s_0)ccL[f](s)=ccL[f](s_0)$. Es decir, $ccL[f]$ es continua en $s_0$. Si $s_0$ es arbitrario, entonces es continua en $]a,+oo[$ 
#### Demostración
$|ccL[f](s)-ccL[f](s_0)|$ 
veamos que tiende a 0 si $s->s_0$. 
$=|int_0^ooe^(-st)f(t)dt-int_0^ooe^(-s_0t)f(t)dt|$
$=|int_0^oo(e^(-st)-e^(-s_0t))f(t)dt|$
	$<=int_0^oo |e^(-st)-e^(-s_0t)|cdot|f(t)|dt$ 
$<=Cint_0^oo|e^(-st)-e^(-sot)|e^(-at)$
$=Cint_0^oo|e^(-(s-a)t)-e^(-(s-a)t)|dt$
##### Caso 1 ($s>s_0$) 
($s>s_0) ->-(s-a)<=(s_0-a)$
$=Cint_0^ooe^(-(s_0-a)t)-e^(-(s-a)t)dt=C[-(e^(-(s_0-a)t))/(s_0-a)+(e^(-(s-a)t))/(s-a)]_0^oo$
$=C1/(s_0-a)-C1/(s-a)=C(s-s_0)/((s_0-a)(s-a))->(C cdot 0)/((s_0-a)^2)=-$  
##### Caso 2 ($s<s_0$): es cambiar $s$ por $s_0$
$|ccL[f](s)-ccL[f](s_0)|<=C(s_0-s)/((s_0-a)(s-a))$
$=>|ccL[f](s)-ccL[f](s_0)|<=C|s-s_0|/((s_0-a)(s-a))$
### Aplicación de los Teoremas del Valor Inicial y Valor Final
$ccL[int_0^t(sinu)/u" d"u]=?$
$G(t)=int_0^t=(sinu)/u" d"u=>G'(t)=(sint)/t$
$=>tG'(t)=sint$
$=>ubrace(ccL[tG'(t)])_(-d/(ds)ccL[G'(t)])=ccL[sint]$
Integramos: $ccL[G'(t)]=-arctans+C$
$=>s ccL[G]-G(0)=-arctans+C$
Pero $G(0)=0=>s ccL[G]=-arctans+C$
Por el teorema del Valor Inicial, sabemos que: $lim_(t->0+)G(t)=lim_(s->+oo) s ccL[G]$
Aplicándolo a nuestro caso: 
$lim_(s->+oo)(-arctans+C)=G(0)=0$
$=>-pi/2+C=0$
$=>C=pi/2$
$=>s ccL[G]=pi/2-arctans=arctan1/s$
$=>ccL[G]=1/sarctan1/s$
Ahora, el Teorema del Valor Final dice:
$lim_(t->+oo)G(t)=lim_(s->0^+)s ccL[G]$
$lim_(t->+oo)G(t)=lim_(t->+oo)int_0^t(sinu)/u" d"u=int_0^(+oo)(sinu)/u" d"u$
$lim_(s->0^+)s ccL[G]=lim_(s->0^+)arctan1/s=pi/2$
$=>int_0^+oo (sinx)/xdx=pi/2$
##### Consecuencia
Si $a<0$, podemos tomar $s, s_0>=0$, en particular podemos tomar $s_0=0$,
$=>lim_(s->0)ccL[f](s)underset(s_0=0)(=)ccL[f](0)=int_0^oof(t)dt$ 
Veamos el teorema del Valor Final:
¿$lim_(t->+oo)f(t)=lim_(s->0^+)s ccL[f[(s)$ ?
Supongamos que $f'$ es de tipo exponencial $|f'(t)|<=Ce^(at)$, con $a<0$
$ccL[f'](s)=s ccL[f](s)-f(0) underset("si " s->0^+)(->)ccL[f'](0)=int_0^oof'(t)dt=[f(t)]_(t=0)^(t=oo)$
$=lim_(t->+oo)f(t)-f(0)$
$=>lim_(s->0^+)(s ccL[f](s)-f(0))$
$=lim_(t->+oo)f(t)-f(0)$
$=>lim_(s->0^+) s ccL[f](s)=lim_(t->+oo)f(t)$
$Ci(t)=int_t^(+oo)(cosu)/udu$
$C_i(0)$ no está bien definida ($int_0^1(du)/u$ no converge)
$ccL[G(t)=(sint)/t]$
$tG(t)=sint$
$ccL[tG(t)]=-d/(ds)ccL[G(t)]$
$=>ccL[sint]=1/(1+s^2)=>ccL[G(t)]=arctans+c => -pi/2+C => C=pi/2$
$=>ccL[G]=pi/2-arctans=arctan(1/2)$
**Se cumple** $int_t^oo(cosu)/udu = -gamma -lnt + int_0^t(1-cosu)/udu$
$gamma$ es la constante de Euler.
$gamma=-int_0^ooe^(-u)lnudu$
$ccL[ln(t)]=int_0^ooe^(-st)lntdt$
$|ln|<=c/(sqrtt)$ cerca de 0
$=[u=st,t=u/s;dt=(du)/(ds)]$
$=int_0^ooe^(-u)lnu/sdu$
$=int_0^ooe^(-u)(lnu-lns)du$
$=ubrace(1/s int_0^ooe^(-u)lnudu)_(-gamma/s)-(lns)/s int_0^ooe^(-u)du$
$=-gamma/s+(lns)/s e^(-u)|^(u=+oo)_(u=0)$
$ccL[-gamma]=-gamma/3$
$ccL[int_0^t(1-cosu)/udu]=1/s ccL[(1-cost)/t]$
$=1/s int_s^ooccL[1-cost](u)du$
$=1/s int_s^oo(1/u-u/(u^2+1))dt$
$=1/s[lnu/(sqrt(u^2+1))]_(u=s)^(u=+oo)$ 
$=-1/sln(s/(sqrt(s^2+1)))$
$=>ccL[C_i(t)](s)=ccL[int_t^oo(cosu)/udu]$
$=-gamma/s+gamma/s+(lns)/s-1/s(lns-1/2ln(s^2+1))$
$=(ln(s^2+1))/(2s)$
##### Ejercicio
$ccL[Ie(t)](s)=?$
$Ie(t)=int_t^oo(e^(-u))/udu$
$Ie(0)$ no está bien definida
**Se cumple**: $int_t^oo(e^(-u))/udu=-gamma-lnt+int^t_0(1-e^u)/udu$
$=>ccL[Ie(t)](s)=(ln(s+1))/s$

#### Ejercicios
a. $ccL[(1-cost)/(t^2)]=int_s^ooccL[(1-cost)/t](u)du$
$=int_s^ooint_u^ooccL[1-cost](v)" d"v" d"u$ 
$=int_s^ooint_u^oo 1/v - v/(v^2+1) " d"v " d"u$
$=int_s^oo 1/2ln(u^2+1)-lnu " d"u$
El procedimiento de esta integral se deja como un ejercicio para el lector
$ccL[(1-cost)/(t^2)]=[1/2 u ln(u^2+1)-2u ln u+arctanu]_s^(+oo)$
$=[u/2(ln(u^2+1)-2lnu)+arctanu]_s^oo$
$=[u/2 ln(u^2+1)/(u^2)+arctanu]^oo_s$
$lim_(u->+oo)u/2ln(u^2+1)/(u^2)+arctanu=lim_(u->+oo)u/2ln(1+u^2)+arctanu$
$=lim_(u->+oo)(u^2)/(2u)ln(1+1/(u^2))+arctanu=1/(2u) ln(1+1/(u^2))^(u^2)+arctanu$
$=lim_(u->+oo)1/(2u)lne+arctanu=0+pi/2$
$ccL[(1-cost)/(t^2)]=pi/2 - arctans + s/2 ln((s^2)/(s^2+1))=arctan(1/s)-s/2ln(s^2+1)/(s^2)$
$int_0^oo(1-cost)/(t^2)dt=lim_(s->0^+)ccL[(1-cost)/(t^2)](s)=pi/2$