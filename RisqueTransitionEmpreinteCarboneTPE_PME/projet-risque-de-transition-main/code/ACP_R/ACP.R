library(pacman)
setwd("D:/01_ENSAI/Sem_2/Projet_Statistique/projet-risque-de-transition/bdd/Base_finale")

p_load(FactoMineR,tidyverse,dplyr,corrplot,factoextra)

base_multi_var<- read.csv('base_multi_var.csv')
bd_acp<-base_multi_var %>%
  select(where( is.numeric ))

str(base_multi_var)

bd_acp=scale(bd_acp,
             center = TRUE,
             scale = TRUE)

ACP <- PCA(bd_acp,
           ncp = 4, graph = F)

summary(ACP)

ACP$var$contrib

fviz_eig(ACP,
         addlabels = TRUE,
         ylim = c(0, 30))

res <- get_pca_var(ACP)

res$cos2

fviz_contrib(ACP, choice = "var", axes = 2)


fviz_pca_var(ACP,col.var = "contrib",repel = TRUE, axes = c(1,2))
fviz_pca_var(ACP,col.var = "contrib",repel = TRUE, axes = c(1,3))
fviz_pca_var(ACP,col.var = "contrib",repel = TRUE, axes = c(2,3))



var$cos2

corrplot(var$cor,is.corr = FALSE)



