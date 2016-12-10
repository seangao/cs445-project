library(ggplot2)
acc = c(0.64634146341463417,0.64349593495934965,0.65243902439024393,0.64715447154471539)
model = c('RF', 'svm','logistic', 'elo')
acc_df = data.frame(model, acc)
acc_df$model <- factor(acc_df$model, levels = unique(acc_df$model))
ggplot(acc_df, aes(x=model, y=acc, fill=model)) +
  geom_bar(stat="identity") +
  scale_fill_brewer(palette="Set1") +
  labs(x = "Model Type", y="Acc", title="Model Accuracy") +
  coord_cartesian(ylim = c(0.5, 0.7)) +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14))
ggsave("acc_plot.png")
