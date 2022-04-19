import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics as st
df = pd.read_csv('math.csv')
data1df=pd.read_csv("data3.csv")
data1=data1df['Math_score'].tolist()
math = df['Math_score'].tolist()
finaldata = []
def sampling():
    data = []
    for a in range(0,100):
        rn=random.randint(0,len(math)-1)
        data.append(math[rn])
    mean = st.mean(data)
    finaldata.append(mean)
for a in range(0,1000):
    sampling()

meanP = st.mean(math)
stdP=st.stdev(math)
meanS = st.mean(finaldata)
stdS=st.stdev(finaldata)
# print('mean population is',str(meanP))
# print('standard deviation population is',str(stdP))
# print('mean sampling is',str(meanS))
# print('standard deviation sampling is',str(stdS))
graph = ff.create_distplot([finaldata],['math'],show_hist=False)


fssts = meanS-stdS
fsste = meanS+stdS
sssts = meanS-stdS*2
ssste = meanS+stdS*2
tssts = meanS-stdS*3
tsste = meanS+stdS*3

mean_of_data1= st.mean(data1)
graph.add_trace(go.Scatter(x=[fsste,fsste],y=[0,0.17],mode='lines',name='fsst'))
graph.add_trace(go.Scatter(x=[ssste,ssste],y=[0,0.17],mode='lines',name='ssst'))
graph.add_trace(go.Scatter(x=[tsste,tsste],y=[0,0.17],mode='lines',name='tsst'))
graph.add_trace(go.Scatter(x=[mean_of_data1,mean_of_data1],y=[0,0.17],mode='lines',name='mean of data1',marker={'color':'black'}))
graph.show()