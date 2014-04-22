#elbow function
data=read.csv("kmeans.csv",head=FALSE)
data1<-data[3:11]
wss <- (nrow(data1)-1)*sum(apply(data1,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(data1,centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")
