import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dimuon_DoubleMu.csv")
dfN = df["InvMass"]
plt.title("Masa Invariante Dimoun")
plt.xlabel("Numero de eventos")
plt.ylabel("Masa Invariante (m)")
dfN.plot()
plt.savefig("1.jpg")
