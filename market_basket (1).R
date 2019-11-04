library(datasets)
install.packages('datasets')
data=read.csv('Groceries.csv')
data(Groceries)
itemFrequencyPlot(Groceries,topN=20,type='absolute')

rules<-apriori(Groceries,parameter = list(supp=0.001,conf=0.8))
inspect(rules[1:5])
rules<-sort(rules,decreasing = TRUE,by='confidence')
inspect(rules[1:5])
options(digits = 2)

redundant_rules1=is.redundant(rules)
redundant_rules1
summary(redundant_rules1)
rules<-rules[!redundant_rules1]
rules

rules<-apriori(Groceries,parameter = list(supp=0.001,conf=0.8),
               appearance = list(default='lhs',rhs='whole milk'),control = list(verbose=F))

inspect(rules[1:10])

rules<-apriori(Groceries,parameter = list(supp=0.0001,conf=0.10),
               appearance = list(default='rhs',lhs='whole milk'))
inspect(rules[1:5])
rules<-sort(rules,by='confidence',decreasing = TRUE)

plot(rules[1:5],method="graph",engine='interactive',shading=NA)