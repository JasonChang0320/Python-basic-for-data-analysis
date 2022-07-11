import re

#Question 1
text = 'Amit 0946579513 12-05-2007, XYZ 034695517 11-11-2011, ABC 025584963 12-01-2009, Frank 0979516482 3-16-2018'

pattern=r"\d{9,}"
answer = re.findall(pattern, text)
print(answer)

#==================================================================
#Question 2
files=['.vscode',
'0.01bar(45).csv',
'0.01bar(45).xlsx',
'0.01bar.csv',
'0.05bar(45).xlsx',
'0.1bar(44).csv',
'0.1bar(45).csv',
'0.1bar(45).xlsx',
'0.2bar(45).xlsx',
'0505practice.xlsx',
'0bar(45).xlsx',
'1935新竹台中地震_論文報告.pptx',
'21050501 Explanation dCFS on seismogenic structures.xlsx',
'21070504 Structure parameters from scaling law.xlsx',
'33c_Longitudinal_Valley_fault.xlsx',
'33c_position.csv',
'45fault_distance.xlsx',
'all_to_all(45x45).py',
'BPT',
'BPT.7z',
'CCH博士論文.pdf',
'CCH科技部計畫.pdf',
'change_criteria.py',
'change_criteria_table',
'coulomb34',
'coulomb_3D_plot.py',
'coulomb_plot',
'critiria',
'distance_faults.py',
'Fault Table.xlsx',
'fault_distance0.5km.xlsx',
'fault_distance10km.xlsx',
'fault_distance2.5km.xlsx',
'fault_distance20km.xlsx',
'fault_distance50km.xlsx',
'fault_distance5km.xlsx',
'fault_probability(multiple)',
'fault_probability(to_all)',
'fault_Probability.py',
'fault_Probability4multiple.py',
'How complex is the 2016 Mw 7.8 Kaikoura earthquake, South Island, New Zealand_.pdf',
'manuscript_template.doc',
'multiple 0.1bar',
'multiple 0.1bar(45)',
'multiple recurrence interval table.xlsx',
'multiple structure table(TEM2020).xlsx',
'multiple(2x2).py',
'multiple-structure rupture index.xlsx',
'multiple-structure rupture table(TEM2020)(考慮一對多).xlsx',
'multiple-structure rupture table(TEM2020).xlsx',
'multiple-structure rupture table(考慮一對多).xlsx',
'multiple-structure rupture table.xlsx',
'multiple-structure rupture(TEM2020).py',
'multiple-structure rupture.py',
'multiple-structure rupture_Recurrence Interval formula (updated).docx',
'multiple-structure rupture_Recurrence Interval formula.docx',
'Multiple-structure_rupture-MS-220127.docx',
'Multiple-structure_rupture-MS.docx',
'new',
'paper_image',
'plot Taiwan fault.7z',
'plot_fault.csv',
'recurrence interval compare table.xlsx',
'Scaling law for slip magnitude.xlsx',
'scaling law with yen & ma',
'source_TEM2018-fault-mean.xml',
'TAO期刊初稿.pdf',
'transform2inr.py',
'TW_faults(each)coulomb_input(inr)',
'TW_faults(multiple)coulomb_input',
'TW_faults(multiple)coulomb_input(45)',
'TW_faults(multiple)coulomb_output',
'TW_faults(multiple)coulomb_output(45)',
'TW_faults(to_all)coulomb_input',
'TW_faults(to_all)coulomb_input(new)',
'TW_faults(to_all)coulomb_input(new2)',
'TW_faults(to_all)coulomb_output',
'TW_faults(to_all)coulomb_output(new)',
'TW_faults(to_all)coulomb_output(new).7z',
'TW_faults(to_all)coulomb_output(new2)',
'TW_faults_position',
'uncertainty of area & slip rate',
'Updated Table 1 of multiple-rupture MS.xlsx',
'white_to_red.cpt',
'__MACOSX',
'顏銘萱1935新竹台中地震_碩論.pdf']

pattern=r".+\.py"
for file in files:
    answer = re.findall(pattern, file)
    if answer:
        print(answer)

#==================================================================
#Question 3

data = open('exercise 3 data.txt', 'r').read()

#write code here
pattern=r"地震"
answer=re.findall(pattern,data)
len(answer)

data.close()
