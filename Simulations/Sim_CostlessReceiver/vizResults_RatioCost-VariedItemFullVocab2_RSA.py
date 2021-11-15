import pandas as pd
import numpy as np
import os
import sys	
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, '..', '..'))
#import visualizationsRE as viz
import matplotlib.pyplot as plt
from Simulations.visualizationsRE import getProportionTargetReached, getPercentFromOptimalUtilityDF, getUtilityDifferenceSummaryStatistics, facetAccuracyByNItem, plotStackedCommunicationByItem
sim_r0 = pd.read_pickle('./simulation_costRaioReceiver_a4_r8_seed423_2-9ItemFullVocab_2000_RSA.pkl')#simulation_costRaioReceiver_a4_r8_seed423_2-9ItemFullVocab_500_RSA
df = pd.DataFrame(sim_r0,  

                columns =['nTargets','propRelevantSignalsInVocab', 'IW_S1R1_sAchievesGoal', 'IW_S1R1_rAchievesGoal', 'IW_S1R1_goalAchieved', 'IW_S1R1_utility',   'CentralControl_utility', 'targetDictionary' ])

dfr0 = sim_r0.copy(deep=True)
communicationDF = dfr0.copy().loc[dfr0['CentralControl_actor'] == 'receiver']
dlen = lambda x: len(x['targetDictionary'])
communicationDF['nTargets'] = communicationDF.apply(dlen, axis=1)
targetReached = getProportionTargetReached(sim_r0)
print(sim_r0.shape)

#print(df)
#print(getUtilityDifferenceSummaryStatistics(sim_r0.loc[sim_r0 == 'receiver']))
#print(sim_r0.loc[sim_r0['nTargets']])
b1_comm = sim_r0.loc[sim_r0['CentralControl_actor'] == 'receiver']
#print(b1_comm)
#print(sim_r0.loc[sim_r0['modelName'] == 'Imagined We'])
#print(getUtilityDifferenceSummaryStatistics(getPercentFromOptimalUtilityDF(b1_comm)))
#print(sim_r0.shape)#.iloc[0:5]
#print(pd.show_versions())
#gapminder.loc[:, gapminder.columns.str.endswith("1957")]
g = sim_r0.loc[:, sim_r0.columns.str.endswith("1")]
#print(g)
fig, ax = plt.subplots(3,1,figsize =(12,10))
#accDict = facetAccuracyByNItem(df)
accDict = facetAccuracyByNItem(sim_r0)
print(accDict)


plotStackedCommunicationByItem(ax[0],
                               accuracyDict= accDict, 
                               modelToPlot='RSA_S0R0_sAchievesGoal', 
                               modelName='RSA_S0R0_sAchievesGoal C_R 0',
                               sCanQuit = False,
                               showLegend = True, 
                               succCommColor = "#000650", failCommColor = '#9FA5BD', doColor = '#f8d7c0',quitColor='#f58960'
                              )
plotStackedCommunicationByItem(ax[1],
                               accuracyDict= accDict, 
                               modelToPlot='RSA_S0R0_sAchievesGoalC_R0.5', 
                               modelName='RSA_S0R0_sAchievesGoal C_R 0.5',
                               sCanQuit = False,
                               showLegend = True, 
                               succCommColor = "#000650", failCommColor = '#9FA5BD', doColor = '#f8d7c0',quitColor='#f58960'
                              )

plotStackedCommunicationByItem(ax[2],
                               accuracyDict= accDict, 
                               modelToPlot= 'RSA_S0R0_sAchievesGoalC_R1', 
                               modelName='RSA_S0R0_sAchievesGoal C_R 1',
                               sCanQuit = False,
                               showLegend = True, 
                               succCommColor = "#000650", failCommColor = '#9FA5BD', doColor = '#f8d7c0',quitColor='#f58960'
                              )

plt.show()


'''
nTargets                       5.82  2.341458  ...  5.361074  6.278926
propRelevantSignalsInVocab     1.00  0.000000  ...  1.000000  1.000000
IW_S1R1_sAchievesGoal          0.53  0.501614  ...  0.431684  0.628316
IW_S1R1_rAchievesGoal          0.07  0.256432  ...  0.019739  0.120261
IW_S1R1_goalAchieved           0.60  0.492366  ...  0.503496  0.696504
IW_S1R1_utility                2.45  2.602932  ...  1.939825  2.960175
CentralControl_utility
'''
