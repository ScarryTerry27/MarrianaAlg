import streamlit as st

from utils.common import change_other


def gipo():
    ex1 = st.expander("1️⃣ Риск неблагоприятных последствий постепенно увеличивается с тяжестью и продолжительностью "
                      "гипогликемии")
    ex1.caption("Hartmann AF, Jaudon JC, Morton M. Hypoglycemia. J pediatrics (1937) 11:1–36.")
    ex2 = st.expander("2️⃣ Первый аномально вызванный сенсорный потенциал при концентрации глюкозы в крови "
                       "0,7-2,5 ммоль/л")
    ex2.caption("""Koh TH, Aynsley-Green A, Tarbit M, Eyre JA. Neural dysfunction during
hypoglycaemia. Arch Dis Child (1988) 63(11):1353–8. doi: 10.1136/adc.63.11.1353""")
    ex3 = st.expander('''3️⃣ Нейровизуализационные исследования выявляют структурные церебральные
повреждения, связанные с тяжелой, рецидивирующей или симптоматической
неонатальной гипогликемией, включая поражения белого вещества преимущественно в
теменно-затылочных долях, атрофию коры, изменения в глубоких структурах серого
вещества базальных ганглиев и таламуса, перивентрикулярные поражения,
паренхиматозное кровоизлияние и ишемические инсульты''')
    ex3.caption("""Burns CM, Rutherford MA,
Boardman JP, Cowan FM. Patterns of cerebral injury and neurodevelopmental outcomes after
symptomatic neonatal hypoglycemia. Pediatrics (2008) 122(1):65–74. doi: 10.1542/peds.2007-
2822; Nivins S, Kennedy E, Thompson B, Gamble GD, Alsweiler JM, Metcalfe R, et al.
Associations between neonatal hypoglycaemia and brain volumes, cortical thickness and white
matter microstructure in mid-childhood: an MRI study. NeuroImage Clin (2022) 33:102943.
doi: 10.1016/j.nicl.2022.102943""")
    ex4 = st.expander('''4️⃣ Клинические проявления гипогликемического поражения мозга включают детский
церебральный паралич, эпилепсию, задержку нейроразвития и умственную отсталость,
микроцефалию, нарушения зрения и слуха''')
    ex4.caption("""Roeper M, Salimi Dafsari R, Hoermann H,
Mayatepek E, Kummer S, Meissner T. Risk factors for adverse neurodevelopment in transient or
persistent congenital hyperinsulinism. Front Endocrinol (Lausanne) (2020) 11:580642.
doi: 10.3389/fendo.2020.580642""")
    ex5 = st.expander('''5️⃣ Неонатальная гипогликемия коррелирует с повышенным риском плохой исполнительной
функции (RR 2,32 [95% (ДИ) 1,17–4,59] и плохой зрительно-моторной функции''')
    ex5.caption("""RR 3,67 [95% ДИ 1,15–11,69] в возрасте 4,5 лет (McKinlay CJD, Alsweiler JM, Anstice NS,
Burakevych N, Chakraborty A, Chase JG, et al. Association of neonatal glycemia with
neurodevelopmental outcomes at 4.5 years. JAMA Pediatr (2017) 171(10):972–83.
doi: 10.1001/jamapediatrics.2017.1579""")
    ex6 = st.expander('''6️⃣ Перинатальные данные 1395 детей, прошедших скрининг глюкозы после рождения и
оценкой успеваемости в школе. Даже один эпизод гипогликемии &lt;2,5 ммоль/л (&lt;45 мг/дл)
был связан со снижением успеваемости в школе по грамотности (коэффициент шансов
(ОШ) 0,62 [95% ДИ 0,45–0,85], а эпизоды &lt;2,2 ммоль/л (&lt;40 мг/дл) были связаны со
снижением успеваемости по математике (ОШ 0,51 [95% ДИ 0,34–0,78] в возрасте 10 лет''')
    ex6.caption("""Kaiser JR, Bai S, Gibson N, Holland G, Lin TM, Swearingen CJ, et al. Association between
transient newborn hypoglycemia and fourth-grade achievement test proficiency: a population-
based study. JAMA Pediatr (2015) 169(10):913–21. doi: 10.1001/jamapediatrics.2015.1631""")
    ex7 = st.expander('''7️⃣ Факторы риска, для которых скрининг уровня глюкозы в крови рекомендуется
единообразно, является диабет у матери, дети с низкой массой тела при рождении  и с
новорожденные с массой тела &gt;90  -го  процентиля или &gt;+2 SDS &gt;4,500 г''')
    ex7.caption("""\tWorking Group of the Swiss Society of
Neonatology (SSN). Prevention and treatment of hypoglycaemia in neonates with a gestational
age from 35 0/7 weeks in maternity wards: Swiss society of neonatology guidelines (2020).
Available at: https://www.neonet.ch/;
\tWackernagel D, Gustafsson A, Edstedt Bonamy AK, Reims A, Ahlsson F, Elfving M, et al. Swedish National
guideline for prevention and treatment of neonatal hypoglycaemia in newborn infants with
gestational age &gt;/=35 weeks. Acta Paediatr (2020) 109(1):31–44. doi: 10.1111/apa.14955
\tGovernment of
Western Australia. Child and adolescent health service. hypoglycaemia guideline (2021).
Available at: https://www.cahs.health.wa.gov.au/""")
    st.button("🔚Назад", on_click=change_other, kwargs={"what": 0})


def giper():
    ex1 = st.expander('''1️⃣ Перифокальная инфекция в месте операции (4,3% с дисгликемией против 3,1% с
нормогликемией, p  = 0,028), остановка сердца (2,6% против 0,1%, p  &lt; 0,001) и сепсис
(3,7% против 1,3%, p  &lt; 0,001); с большей вероятностью подвергаются повторной
операции (11,3% против 5,8%, p  &lt; 0,001); и с большей вероятностью останутся в
больнице после 30 дней (33,0% против 6,1%, p &lt;  0,001)''')
    ex1.caption("""Vanderhoek S. M. et al.
Association of dysglycemia with post-operative outcomes in pediatric surgery //Journal of
pediatric surgery. – 2023. – Т. 58. – №. 3. – С. 365-372.)
*медиастинит после кардиохирургических операций (Leininger S. Blood glucose
management for reducing cardiac surgery infections //Critical Care Nursing Quarterly. – 2018. –
Т. 41. – №. 4. – С. 399-406""")
    ex2 = st.expander('''2️⃣ Возрастание риска развития ВЖК, некротического энтероколита и центральной мозговой
ишемии''')
    ex2.caption("""Ritrosky H. Prevalance of and risk factors for intraoperative non-euglycemia evens in
premature neonates &lt; 2500 grams./H. Ritrosky// A doctoral thesis submitted in partial fulfillment
of the requirements for the degree of Doctor of Nursing Practice. – 2010. – P.3-25.
URL:https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=5325&amp;context=etd (дата
обращения: 31.03.24""")
    ex3 = st.expander('''3️⃣ Многовариантный анализ показывает, что уровень глюкозы в крови достоверно связан с
перипротезной инфекцией сустава в практике эндопротезирования''')
    ex3.caption("""KheirM.M. Postoperative Blood Glucose Levels Predict Infection After Total Joint Arthroplasty./M.M.
Kheir, T.L. Tan, M. Kheir, [et al.]// J Bone Joint Surg Am.- 2018.- Vol.100, №16 - Pp.1423-
1431. doi: 10.2106/JBJS.17.01316""")
    st.button("🔚Назад", on_click=change_other, kwargs={"what": 0})


