import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

plt.savefig('foo.png')


df=pd.read_csv("data/penguins_pimped.csv")
species='Adelie'
df_species= df.loc[df['species']==species]

fig,ax=plt.subplots()
ax=sns.scatterplot(data=df_species, x="bill_length_mm", y="flipper_length_mm", hue="sex")
plt.savefig('plots/scatter_plot.png')
