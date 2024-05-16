- Unifican el campo magnético y eléctrico en uno solo
## Forma diferencial
### En el vacío
Ley de Gauss: $vecgradcdotvecE=rho/(epsilon_0)$
Ley de Gauss del campo magnético: $vecgradcdotvecB=0$
Ley de Faraday-Lenz: $vecgradxxE=-part(vecB)t$
Ley de Ampere-Maxwell: $vecgradxxvecB=mu_0vecJ+mu_0epsilon_0part(vecE)t$
### En medio material
Ley de Gauss: $vecgradcdotvecE=rho/(epsilon_repsilon_0)$
Ley de Gauss de $vecB$: $vecgradcdotvecB=0$
Ley de Faraday-Lenz: $vecgradxxE=-part(vecB)t$
Ley de Ampere-Maxwell: $vec grad xx vec B = mu_r mu_0 vecJ + mu_r mu_0 epsilon_r epsilon_0 part (vec E) t = mu vec J + mu epsilon part (vec E) t => 1/mu vec grad xx vec B = vec J + part (vec D) t$
## Forma Integral
Ley de Gauss: $int_V vecgradcdotvecEd"V"=int_Vrho/(epsilon_0) d"V"=>int_S vecEcdotvec(d"S")=int_V rho/(epsilon_0) d"V"=(q_("encerrada"))/(epsilon_0)$
Ley de Gauss para $vecB$: $int_V vecgradcdotBd"V"=0 => int_S vecBcdotvec(d"S")=0$
Ley de Faraday-Lenz: $oint_CvecEcdotdvecl=-del/(del t)int_SvecBcdotdvecS$
Ley de Ampere-Maxwell: $oint_cvecBcdotdvecl=muint_SvecJdvecS+muepsilondel/(del t)int_SEcdotdvecS$ 
### Tabla

|                          | Vacío                                             | Materia                                                    | Forma integral                                                                                             |
| ------------------------ | ------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Ley de Gauss             | $vecgradcdotvecE=rho/epsilon_0$                   | $vecgradcdotepsilonE=rho$                                  | $int_SvecE cdot  dvec"S"=1/epsilonint_vrhodV$                                                              |
| Ley de Gauss para $vecB$ | $vecgradcdotvecB=0$                               | $vecgradcdotB=0$                                           | $int_SvecB cdot dvec"S" = 0$                                                                               |
| Ley de Faraday-Lenz      | $vecgradxxE=-part(vecB)t$                         | $vecgradxxE=-part(vecB)t$                                  | $oint_c vecE cdot dvecl = -del/(del t) int_S vecB cdot dvec"S"$                                            |
| Ley de Ampere-Maxwell    | $vecgradxxvecB=mu_0vecJ+mu_0epsilon_0part(vecE)t$ | $1/mu vec grad xx vec B = vec J +  epsilon part (vec E) t$ | $oint_C vecB cdot dvecl$ $= mu int_S vecJ cdot d vec S + mu epsilon del/(del t) int_S vecE cdot d vec "S"$ |
