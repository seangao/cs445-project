library(ggplot2)
model = c('RF', 'RF', 'svm', 'svm', 'logistic', 'logistic', 'elo', 'elo', '538', '538')
method = c('binary', 'prob', 'binary', 'prob', 'binary', 'prob', 'binary', 'prob', '538', 'binary')
rms = c(17.28390388, 10.229010715221683, 17.704048501213876, 10.444044981405741,
        15.7786775956, 9.93646483078, 17.6427511082, 10.0255933378, 8.06, 0)
df = data.frame(model, method, rms)
df$model <- factor(df$model, levels = unique(df$model))
ggplot(df, aes(x=factor(model), y=rms, fill=method)) +
  geom_bar(stat="identity", position="dodge") +
  scale_fill_brewer(palette="Set1") +
  labs(x = "Model Type", y="RMS", title="RMS per model")
ggsave("rms_plot.png")
