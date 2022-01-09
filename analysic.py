#Import required libraries tải các thư viện
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# tải dữ liệu 10 loại tiền điện tử phổ biến Bitcoin, Ethereum, BinanceCoin, Cardano,Tether,xrp,dogecoin,usdcoin,polkadot,solana
c_bitcoin = pd.read_csv('coin_Bitcoin.csv')
c_ethereum = pd.read_csv('coin_Ethereum.csv')
c_binance_coin = pd.read_csv('coin_BinanceCoin.csv')
c_cardano = pd.read_csv('coin_Cardano.csv')
c_tether = pd.read_csv('coin_Tether.csv')
c_xrp = pd.read_csv('coin_XRP.csv')
c_dogecoin = pd.read_csv('coin_Dogecoin.csv')
c_usd_coin = pd.read_csv('coin_USDCoin.csv')
c_polkadot = pd.read_csv('coin_Polkadot.csv')
c_solana = pd.read_csv('coin_Solana.csv')

# kiểm tra dữ liệu bitcoin
c_bitcoin.head()
c_bitcoin.info()
# Kiểm tra dữ liệu ethereum
c_ethereum.head()
c_ethereum.info()
# Tương tự
c_binance_coin.head()
c_binance_coin.info()
c_cardano.shape
c_cardano.info()
#Check the data dimensions for tether
c_tether.shape
c_tether.info()
#Check the data dimensions for XRP
c_xrp.shape
c_xrp.info()
#Check the data dimensions for Dogecoin
c_dogecoin.shape
c_dogecoin.info()
#Check the data dimensions for USD coin
c_usd_coin.shape
c_usd_coin.info()
#Check the data dimensions for Polkadot
c_polkadot.shape
c_polkadot.info()
#Check the data dimensions for Solana
c_solana.shape
c_solana.info()

## Làm sạch và chuẩn bị dữ liệu

#Chuyển đổi loại đối tượng Cột ngày thành loại ngày giờ
c_bitcoin['Date'] = pd.to_datetime(c_bitcoin['Date'], format='%Y/%m/%d %H:%M')
c_ethereum['Date'] = pd.to_datetime(c_ethereum['Date'], format='%Y/%m/%d %H:%M')
c_binance_coin['Date'] = pd.to_datetime(c_binance_coin['Date'], format='%Y/%m/%d %H:%M')
c_cardano['Date'] = pd.to_datetime(c_cardano['Date'], format='%Y/%m/%d %H:%M')
c_tether['Date'] = pd.to_datetime(c_tether['Date'], format='%Y/%m/%d %H:%M')
c_xrp['Date'] = pd.to_datetime(c_xrp['Date'], format='%Y/%m/%d %H:%M')
c_dogecoin['Date'] = pd.to_datetime(c_dogecoin['Date'], format='%Y/%m/%d %H:%M')
c_usd_coin['Date'] = pd.to_datetime(c_usd_coin['Date'], format='%Y/%m/%d %H:%M')
c_polkadot['Date'] = pd.to_datetime(c_polkadot['Date'], format='%Y/%m/%d %H:%M')
c_solana['Date'] = pd.to_datetime(c_solana['Date'], format='%Y/%m/%d %H:%M')

#### Khi chúng tôi đang cố gắng tìm hiểu mối tương quan giữa các loại tiền tệ trong một năm,
#  các cột nội dung sẽ là Ngày, đóng cửa, vốn hóa thị trường và khối lượng. Ngoài ba cột này,
#  chúng ta có thể xóa phần còn lại của dữ liệu khỏi tập dữ liệu.
c_bitcoin.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_ethereum.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_binance_coin.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_cardano.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_tether.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_xrp.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_dogecoin.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_usd_coin.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_polkadot.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)
c_solana.drop(['SNo','Name','Symbol','Open', 'High','Low'], axis = 1, inplace = True)

### Tổng hợp dữ liệu

#Mất thông tin thời gian

c_bitcoin['Date'] = c_bitcoin['Date'].dt.date
c_ethereum['Date'] = c_ethereum['Date'].dt.date
c_binance_coin['Date'] = c_binance_coin['Date'].dt.date
c_cardano['Date'] = c_cardano['Date'].dt.date
c_tether['Date'] = c_tether['Date'].dt.date
c_xrp['Date'] = c_xrp['Date'].dt.date
c_dogecoin['Date'] = c_dogecoin['Date'].dt.date
c_usd_coin['Date'] = c_usd_coin['Date'].dt.date
c_polkadot['Date'] = c_polkadot['Date'].dt.date
c_solana['Date'] = c_solana['Date'].dt.date

#Ngày chuyển đổi dưới dạng chỉ mục

c_btc = pd.pivot_table(c_bitcoin, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_eth = pd.pivot_table(c_ethereum, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_bnb = pd.pivot_table(c_binance_coin, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_ada = pd.pivot_table(c_cardano, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_usdt = pd.pivot_table(c_tether, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_xrp_c = pd.pivot_table(c_xrp, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_doge = pd.pivot_table(c_dogecoin, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_usdc= pd.pivot_table(c_usd_coin, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_dot = pd.pivot_table(c_polkadot, values=['Close', 'Volume','Marketcap'], index=['Date'])
c_sol = pd.pivot_table(c_solana, values=['Close', 'Volume','Marketcap'], index=['Date'])


c_btc.head()


#Hiểu các xu hướng
#Hãy đặt một số câu hỏi để hiểu xu hướng

# Giá trị đóng trung bình cao nhất trong khoảng thời gian từ tháng 3 năm 2013 đến năm 2021-07-06 là bao nhiêu?

btc = c_btc['Close'].max()
eth= c_eth['Close'].max()
bnb= c_bnb['Close'].max()
ada = c_ada['Close'].max()
usdt = c_usdt['Close'].max()
xrp = c_xrp_c['Close'].max()
doge = c_doge['Close'].max()
usdc  = c_usdc['Close'].max()
dot = c_dot['Close'].max()
sol = c_sol['Close'].max()


print("Highest average value of BTC ", btc,"was recorded on ",c_btc[c_btc['Close'] == btc].index.values[0])
print("Highest average value of ETH ", eth,"was recorded on ",c_eth[c_eth['Close'] == eth].index.values[0])
print("Highest average value of BNB ", bnb,"was recorded on ",c_bnb[c_bnb['Close'] == bnb].index.values[0])
print("Highest average value of ADA ", ada,"was recorded on ",c_ada[c_ada['Close'] == ada].index.values[0])
print("Highest average value of USDT ",usdt,"was recorded on ",c_usdt[c_usdt['Close'] == usdt].index.values[0])
print("Highest average value of XRP ", xrp,"was recorded on ",c_xrp_c[c_xrp_c['Close'] == xrp].index.values[0])
print("Highest average value of DOGE ", doge,"was recorded on ",c_doge[c_doge['Close'] == doge].index.values[0])
print("Highest average value of USDC ", usdc,"was recorded on ",c_usdc [c_usdc ['Close'] == usdc].index.values[0])
print("Highest average value of DOT ", dot,"was recorded on ",c_dot[c_dot['Close'] == dot].index.values[0])
print("Highest average value of SOL ", sol,"was recorded on ",c_sol[c_sol['Close'] == sol].index.values[0])
data = {"Bitcoin":btc,"Ethereum  ":eth,"Binance Coin":bnb,"Cardano":ada,"Tether":usdt,"XRP":xrp,"Dogecoin":doge,"USD Coin":usdc,"Polkadot":dot,"Solana":sol}
Cryptocurrencies = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (15, 5))
plt.bar(Cryptocurrencies,values,color ='orange', width = 0.4)
plt.xlabel("Cryptocurrencies")
plt.ylabel("Highest volume")
plt.title("Comparision of highest closing value in a day between March 2013 and 2021-07-06")
plt.show()

#Khối lượng giao dịch cao nhất trong một ngày trong khoảng thời gian từ tháng 3 năm 2013 đến tháng 7 năm 2021 là bao nhiêu?

btc = c_btc['Volume'].max()
eth= c_eth['Volume'].max()
bnb= c_bnb['Volume'].max()
ada = c_ada['Volume'].max()
usdt = c_usdt['Volume'].max()
xrp = c_xrp_c['Volume'].max()
doge = c_doge['Volume'].max()
usdc  = c_usdc['Volume'].max()
dot = c_dot['Volume'].max()
sol = c_sol['Volume'].max()


# tìm volume cao nhất và khi nào
print("Highest average volume of BTC ", btc,"was recorded on ",c_btc[c_btc['Volume'] == btc].index.values[0])
print("Highest average volume of ETH ", eth,"was recorded on ",c_eth[c_eth['Volume'] == eth].index.values[0])
print("Highest average volume of BNB ", bnb,"was recorded on ",c_bnb[c_bnb['Volume'] == bnb].index.values[0])
print("Highest average volume of ADA ", ada,"was recorded on ",c_ada[c_ada['Volume'] == ada].index.values[0])
print("Highest average volume of USDT ",usdt,"was recorded on ",c_usdt[c_usdt['Volume'] == usdt].index.values[0])
print("Highest average volume of XRP ", xrp,"was recorded on ",c_xrp_c[c_xrp_c['Volume'] == xrp].index.values[0])
print("Highest average volume of DOGE ", doge,"was recorded on ",c_doge[c_doge['Volume'] == doge].index.values[0])
print("Highest average volume of USDC ", usdc,"was recorded on ",c_usdc [c_usdc ['Volume'] == usdc].index.values[0])
print("Highest average volume of DOT ", dot,"was recorded on ",c_dot[c_dot['Volume'] == dot].index.values[0])
print("Highest average volume of SOL ", sol,"was recorded on ",c_sol[c_sol['Volume'] == sol].index.values[0])
data = {"Bitcoin":btc,"Ethereum  ":eth,"Binance Coin":bnb,"Cardano":ada,"Tether":usdt,"XRP":xrp,"Dogecoin":doge,"USD Coin":usdc,"Polkadot":dot,"Solana":sol}
Cryptocurrencies = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(Cryptocurrencies, values,color ='gold',width = 0.4)
plt.xlabel("Cryptocurrencies")
plt.ylabel("Highest volume")
plt.title("Comparision of highest volume in a day between March 2013 and 2021-07-06")
plt.show()

#Khối lượng giao dịch cao nhất trong một ngày trong khoảng thời gian từ tháng 3 năm 2013 đến tháng 7 năm 2021 là bao nhiêu?

btc = c_btc['Marketcap'].max()
eth= c_eth['Marketcap'].max()
bnb= c_bnb['Marketcap'].max()
ada = c_ada['Marketcap'].max()
usdt = c_usdt['Marketcap'].max()
xrp = c_xrp_c['Marketcap'].max()
doge = c_doge['Marketcap'].max()
usdc  = c_usdc['Marketcap'].max()
dot = c_dot['Marketcap'].max()
sol = c_sol['Marketcap'].max()



# finding the highest Marketcap and when 
print("Highest average market capitalization of BTC ", btc,"was recorded on ",c_btc[c_btc['Marketcap'] == btc].index.values[0])
print("Highest average market capitalization of ETH ", eth,"was recorded on ",c_eth[c_eth['Marketcap'] == eth].index.values[0])
print("Highest average market capitalization of BNB ", bnb,"was recorded on ",c_bnb[c_bnb['Marketcap'] == bnb].index.values[0])
print("Highest average market capitalization of ADA ", ada,"was recorded on ",c_ada[c_ada['Marketcap'] == ada].index.values[0])
print("Highest average market capitalization of USDT ",usdt,"was recorded on ",c_usdt[c_usdt['Marketcap'] == usdt].index.values[0])
print("Highest average market capitalization of XRP ", xrp,"was recorded on ",c_xrp_c[c_xrp_c['Marketcap'] == xrp].index.values[0])
print("Highest average market capitalization of DOGE ", doge,"was recorded on ",c_doge[c_doge['Marketcap'] == doge].index.values[0])
print("Highest average market capitalization of USDC ", usdc,"was recorded on ",c_usdc [c_usdc ['Marketcap'] == usdc].index.values[0])
print("Highest average market capitalization of DOT ", dot,"was recorded on ",c_dot[c_dot['Marketcap'] == dot].index.values[0])
print("Highest average market capitalization of SOL ", sol,"was recorded on ",c_sol[c_sol['Marketcap'] == sol].index.values[0])
data = {"Bitcoin":btc,"Ethereum  ":eth,"Binance Coin":bnb,"Cardano":ada,"Tether":usdt,"XRP":xrp,"Dogecoin":doge,"USD Coin":usdc,"Polkadot":dot,"Solana":sol}
Cryptocurrencies = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(Cryptocurrencies, values,color ='purple',width = 0.4)
plt.xlabel("Cryptocurrencies")
plt.ylabel("Highest Marketcap")
plt.title("Comparision of highest Marketcap in a day between March 2013 and 2021-07-06")
plt.show()

# tìm xu hướng từng đồng tiền

#Bitcoin
sns.set_theme(style="darkgrid")
plt.figure(figsize=[15,5])
plt.title("Bitcoin")
sns.lineplot(x = c_btc.index , y = 'Close', data = c_btc)
plt.show()
#Ethereum
plt.figure(figsize=[15,5])
plt.title("Ethereum")
sns.lineplot(x = c_eth.index , y = 'Close', data = c_eth)
plt.show()
#Binance Coin
plt.figure(figsize=[15,5])
plt.title("Binance Coin")
sns.lineplot(x = c_bnb.index , y = 'Close', data = c_bnb)
plt.show()
#Cardano
plt.figure(figsize=[15,5])
plt.title("Cardano")
sns.lineplot(x = c_ada.index , y = 'Close', data = c_ada)
plt.show()
#Tether
plt.figure(figsize=[15,5])
plt.title("Tether")
sns.lineplot(x = c_usdt.index , y = 'Close', data = c_usdt)
plt.show()
#XRP
plt.figure(figsize=[15,5])
plt.title("XRP")
sns.lineplot(x = c_xrp_c.index , y = 'Close', data = c_xrp_c)
plt.show()
#Dogecoin
plt.figure(figsize=[15,5])
plt.title("Dogecoin")
sns.lineplot(x = c_doge.index , y = 'Close', data = c_doge)
plt.show()
#USD Coin
plt.figure(figsize=[15,5])
plt.title("USD Coin")
sns.lineplot(x = c_usdc.index , y = 'Close', data = c_usdc)
plt.show()
#Polkadot
plt.figure(figsize=[15,5])
plt.title("Polkadot")
sns.lineplot(x = c_dot.index , y = 'Close', data = c_dot)
plt.show()
#Solana
plt.figure(figsize=[15,5])
plt.title("Solana")
sns.lineplot(x = c_sol.index , y = 'Close', data = c_sol)
plt.show()

# Phân tích các xu hướng kết hợp
# Average closing value



plt.figure(figsize=(15,8))
(c_btc['Close']).plot(color='darkorange', label='Bitcoin')
(c_eth['Close']).plot(color='magenta', label='Ethereum')
(c_bnb['Close']).plot(color='blue', label='Binance Coin')
(c_ada['Close']).plot(color='yellow', label='Cardano')
(c_usdt['Close']).plot(color='purple', label='Tether')
(c_xrp_c['Close']).plot(color='red', label='XRP')
(c_doge['Close']).plot(color='green', label='Dogecoin')
(c_usdc['Close']).plot(color='grey', label='USD Coin')
(c_dot['Close']).plot(color='cyan', label='Polkadot')
(c_sol['Close']).plot(color='black', label='Solana')
plt.legend()
plt.title('Top10 Cryptocurrency closing value)')
plt.show()




plt.figure(figsize=(15,8))
(c_btc['Close']).plot(color='darkorange', label='Bitcoin')
(c_eth['Close']).plot(color='magenta', label='Ethereum')
(c_bnb['Close']).plot(color='blue', label='Binance Coin')
(c_ada['Close']).plot(color='yellow', label='Cardano')
(c_usdt['Close']).plot(color='purple', label='Tether')
(c_xrp_c['Close']).plot(color='red', label='XRP')
(c_doge['Close']).plot(color='green', label='Dogecoin')
(c_usdc['Close']).plot(color='grey', label='USD Coin')
(c_dot['Close']).plot(color='cyan', label='Polkadot')
(c_sol['Close']).plot(color='black', label='Solana')
plt.legend()
plt.yscale('log')
plt.title('Comparision Top10 Cryptocurrency closing value ')
plt.show()



# Closing volume

plt.figure(figsize=(15,8))
(c_btc['Volume']).plot(color='#FF7F50', label='Bitcoin')
(c_eth['Volume']).plot(color='#DDA0DD', label='Ethereum')
(c_bnb['Volume']).plot(color='#7FFFD4', label='Binance Coin')
(c_ada['Volume']).plot(color='#FFD700', label='Cardano')
(c_usdt['Volume']).plot(color='#FF81C0', label='Tether')
(c_xrp_c['Volume']).plot(color='#808000', label='XRP')
(c_doge['Volume']).plot(color='#029386', label='Dogecoin')
(c_usdc['Volume']).plot(color='#D1B26F', label='USD Coin')
(c_dot['Volume']).plot(color='#04D8B2', label='Polkadot')
(c_sol['Volume']).plot(color='#C875C4', label='Solana')
plt.legend()
plt.yscale('log')
plt.title('Top10 Cryptocurrency Volume ')
plt.show()


#Marketcap


plt.figure(figsize=(15,8))
(c_btc['Marketcap']).plot(color='#FF7F50', label='Bitcoin')
(c_eth['Marketcap']).plot(color='#DDA0DD', label='Ethereum')
(c_bnb['Marketcap']).plot(color='#7FFFD4', label='Binance Coin')
(c_ada['Marketcap']).plot(color='#FFD700', label='Cardano')
(c_usdt['Marketcap']).plot(color='#FF81C0', label='Tether')
(c_xrp_c['Marketcap']).plot(color='#808000', label='XRP')
(c_doge['Marketcap']).plot(color='#029386', label='Dogecoin')
(c_usdc['Marketcap']).plot(color='#D1B26F', label='USD Coin')
(c_dot['Marketcap']).plot(color='#04D8B2', label='Polkadot')
(c_sol['Marketcap']).plot(color='#C875C4', label='Solana')
plt.legend()
plt.yscale('log')
plt.title('Top10 Cryptocurrency Marketcap ')
plt.show()



startdate = pd.to_datetime("2020-01-01").date()
enddate = pd.to_datetime("2020-12-31").date()
btc_2020 = c_btc.loc[startdate:enddate]
eth_2020 = c_eth.loc[startdate:enddate]
bnb_2020 = c_bnb.loc[startdate:enddate]
ada_2020 = c_ada.loc[startdate:enddate]
usdt_2020 = c_usdt.loc[startdate:enddate]
xrp_2020 = c_xrp_c.loc[startdate:enddate]
doge_2020 = c_doge.loc[startdate:enddate]
usdc_2020 = c_usdc.loc[startdate:enddate]
dot_2020 = c_dot.loc[startdate:enddate]
sol_2020 = c_sol.loc[startdate:enddate]


btc_2020.head()




btc_2020.tail()


startdate = pd.to_datetime("2021-01-01").date()
enddate = pd.to_datetime("2021-12-31").date()
btc_2021 = c_btc.loc[startdate:enddate]
eth_2021 = c_eth.loc[startdate:enddate]
bnb_2021 = c_bnb.loc[startdate:enddate]
ada_2021 = c_ada.loc[startdate:enddate]
usdt_2021 = c_usdt.loc[startdate:enddate]
xrp_2021 = c_xrp_c.loc[startdate:enddate]
doge_2021 = c_doge.loc[startdate:enddate]
usdc_2021 = c_usdc.loc[startdate:enddate]
dot_2021 = c_dot.loc[startdate:enddate]
sol_2021 = c_sol.loc[startdate:enddate]


btc_2021.head()

btc_2021.tail()

crypto=["Bitcoin 2020","Bitcoin 2021","Ethereum 2020","Ethereum 2021","Binance Coin 2020","Binance Coin 2021","Cardano 2020","Cardano 2021","Tether 2020","Tether 2021","XRP 2020","XRP 2021","Dogecoin 2020","Dogecoin 2021","USD Coin 2020","USD Coin 2021","Polkadot 2020","Polkadot 2021","Solana 2020","Solana 2021"]
cryptoDf=[btc_2020,btc_2021,eth_2020,eth_2021,bnb_2020,bnb_2021,ada_2020 ,ada_2021,usdt_2020 ,usdt_2021,xrp_2020 ,xrp_2021,doge_2020 ,doge_2021,usdc_2020 ,usdc_2021,dot_2020 ,dot_2021 ,sol_2020 ,sol_2021 ]
num_plots = 20
total_cols = 2
total_rows = 10
fig, axs = plt.subplots(nrows=total_rows, ncols=total_cols, figsize=(14*total_cols, 7*total_rows), constrained_layout=True)
for i, var in enumerate(crypto):
    row = i//total_cols
    pos = i % total_cols
    sns.set_context('paper', font_scale = 2)
    plot =  sns.lineplot(data=cryptoDf[i], x="Date", y="Close",color='#0000FF',palette ='coolwarm',ax=axs[row][pos])
    axs[row][pos].set_title(crypto[i])




cl_btc = c_btc[['Close']]
cl_btc.columns = ['Close_btc']
vol_btc = c_btc[['Volume']]
vol_btc.columns = ['volume_btc']
cl_eth = c_eth[['Close']]
cl_eth.columns = ['Close_eth']
vol_eth = c_eth[['Volume']]
vol_eth.columns = ['volume_eth']
cl_bnb = c_bnb[['Close']]
cl_bnb.columns = ['Close_bnb']
vol_bnb = c_bnb[['Volume']]
vol_bnb.columns = ['volume_bnb']
cl_ada = c_ada[['Close']]
cl_ada.columns = ['Close_ada']
vol_ada = c_ada[['Volume']]
vol_ada.columns = ['volume_ada']
cl_usdt = c_usdt[['Close']]
cl_usdt.columns = ['Close_usdt']
vol_usdt = c_usdt[['Volume']]
vol_usdt.columns = ['volume_usdt']
cl_xrp_c = c_xrp_c[['Close']]
cl_xrp_c.columns = ['Close_xrp_c']
vol_xrp_c = c_xrp_c[['Volume']]
vol_xrp_c.columns = ['volume_xrp_c']
cl_doge = c_doge[['Close']]
cl_doge.columns = ['Close_doge']
vol_doge = c_doge[['Volume']]
vol_doge.columns = ['volume_doge']
cl_usdc = c_usdc[['Close']]
cl_usdc.columns = ['Close_usdc']
vol_usdc = c_usdc[['Volume']]
vol_usdc.columns = ['volume_usdc']
cl_dot = c_dot[['Close']]
cl_dot.columns = ['Close_dot']
vol_dot = c_dot[['Volume']]
vol_dot.columns = ['volume_dot']
cl_sol = c_sol[['Close']]
cl_sol.columns = ['Close_sol']
vol_sol = c_sol[['Volume']]
vol_sol.columns = ['volume_sol']
cry_coins = pd.concat([cl_btc,vol_btc ,cl_eth,vol_eth,cl_bnb,vol_bnb,cl_ada,vol_ada,cl_usdt,vol_usdt,cl_xrp_c,vol_xrp_c,cl_doge,vol_doge,cl_usdc,vol_usdc,cl_dot,vol_dot,cl_sol,vol_sol,], axis=1, join='inner')

cry_coins.head()





#Correlation Heatmap between Cryptocurrencies
plt.figure(figsize=(30,10))
#sns.heatmap(cry_coins.corr(),vmin=0, vmax=1, cmap='coolwarm', annot=True)
#sns.heatmap(cry_coins.corr(),vmin=0, vmax=1, cmap='PiYG', annot=True)
sns.heatmap(cry_coins.corr(),vmin=0, vmax=1, cmap='YlGnBu', annot=True)
plt.title('Correlation Heatmap between Cryptocurrencies')





