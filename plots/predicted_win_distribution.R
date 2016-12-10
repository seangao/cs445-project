spurs_wins = read.csv('../csv/spurs_wins.csv', header=FALSE)
ggplot(data=spurs_wins, aes(spurs_wins)) + geom_bar(stat="count", fill="dodgerblue1") +
  labs(x = "Number of wins", y="Count", title="Spurs 2016 simulated win distribution") +
  geom_vline(xintercept = 67, color="red") +
  geom_text(aes(67,90,label = "Actual", hjust = -0.25))
ggsave("spurs_wins_plot.png")
