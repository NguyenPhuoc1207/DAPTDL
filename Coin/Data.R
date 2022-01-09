Data <- X2_12_21

Do_thi <- ggplot(Data) +geom_point(mapping =aes(x= b_name, y=d_price))
Do_thi

Do_thi <- ggplot(Data) +geom_point(mapping =aes(x= b_name, y=g_marketCap))
Do_thi

#ggplot(Data) +geom_point(mapping =aes(x= b_name, y= d_price, color =class))

#ggplot(Data) +geom_point(mapping = aes(x= b_name, y= d_price, color = class))
#Do_thi2 <- ggplot(Data) +geom_point(mapping =aes(x= b_name, y= d_price, color = "red")) +facet_wrap(~red, nrow =2)
#Do_thi2                                              

ggplot(Data, mapping =aes(x=  b_name, y= d_price)) +geom_point() +geom_smooth()
Data1 <- Data[, c("b_name","d_price")]

ggplot(Data1) +geom_bar(mapping =aes(x= b_name))
#hist(Data1, beak = 100, freq = FALSE)
ggp <- ggplot(Data, aes(x= b_name, y= d_price))
ggp + geom_col(color='blue', fill= 'yellow')
#sap xep lai theo thu 
ggp <- ggplot(Data, aes(x= reorder(b_name,d_price), y= d_price))
ggp + geom_col(color='blue', fill= 'yellow')
# Thêm phu de vào
ggp <- ggplot(Data, aes(x=b_name, y= d_price))
ggp + geom_col(color='blue', fill= 'yellow') + labs(title = 'Top10 cryptocurrency',
                                                    subtitle = '21/12/2021',
                                                    caption = 'Data Source: coinmarketcap.com,') +
  theme(plot.title =  element_text(color = '#731313', size =24, face = 'bold'),
        plot.subtitle =  element_text(color = '#254721', size =15, face = 'italic'),
        plot.caption=  element_text(color = '#142751', size =8, face = 'italic'))

ggp2 <- ggplot(Data, aes(x=b_name, y= g_marketCap))
ggp2 + geom_col(color='green', fill='red')


ggplot(Data, mapping =aes(x=b_name , y= d_price)) +geom_boxplot(fill ="plum")

ggp2 <- ggplot(Data, aes(x=b_name, y= Data$h_volumnUSD))
ggp2 + geom_col(color='green', fill='green')
library(ggcorrplot)
Data3 <- Data[, c( "e_P24h")]
ggcorrplot()
summary(Data)
              


