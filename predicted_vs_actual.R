library(ggplot2)

multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}

svm_cl = read.csv('csv/svm_cl.csv', header=FALSE)
names(svm_cl) = c('Team', 'Predicted', 'Actual')
svm_pr = read.csv('csv/svm_pr.csv', header=FALSE)
names(svm_pr) = c('Team', 'Predicted', 'Actual', 'Color')
rf_cl = read.csv('csv/random_forest.csv', header=FALSE)
names(rf_cl) = c('Team', 'Predicted', 'Actual')
rf_pr = read.csv('csv/random_forest_prob.csv', header=FALSE)
names(rf_pr) = c('Team', 'Predicted', 'Actual')
elo_cl = read.csv('csv/elo_cl.csv', header=FALSE)
names(elo_cl) = c('Team', 'Predicted', 'Actual')
elo_pr = read.csv('csv/elo_pr.csv', header=FALSE)
names(elo_pr) = c('Team', 'Predicted', 'Actual')
log_cl = read.csv('csv/logistic_cl.csv', header=FALSE)
names(log_cl) = c('Team', 'Predicted', 'Actual')
log_pr = read.csv('csv/logistic_pr.csv', header=FALSE)
names(log_pr) = c('Team', 'Predicted', 'Actual')
c <- as.character(svm_pr$Color)
t <- as.character(svm_pr$Team)
p1 <- ggplot(svm_cl, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('SVM Binary Classification') + theme(plot.margin=unit(c(0,1,1,0),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p2 <- ggplot(rf_cl, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('Random Forest Binary Classification') + theme(plot.margin=unit(c(1,1,0,0),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16), plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p3 <- ggplot(elo_cl, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('Elo Model Binary Classification') + theme(plot.margin=unit(c(0,0,1,1),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p4 <- ggplot(log_cl, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('Logistic Regression Binary Classification') + theme(plot.margin=unit(c(1,0,0,1),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p5 <- ggplot(svm_pr, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('SVM Probability Classification') + theme(plot.margin=unit(c(0,1,1,0),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p6 <- ggplot(rf_pr, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('Random Forest Probability Classification') + theme(plot.margin=unit(c(1,1,0,0),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p7 <- ggplot(elo_pr, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('Elo Model Probability Classification') + theme(plot.margin=unit(c(0,0,1,1),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

p8 <- ggplot(log_pr, aes(Predicted, Actual, label=Team, fill=Team, color=Team, group=1)) + geom_abline(slope=1, color='gray',group=2) + geom_point() + geom_text(nudge_y=3,size=5) + coord_cartesian(xlim=c(0,82), ylim=c(0,82)) + scale_fill_manual(values=as.character(colors)) + scale_color_manual(values=c[order(t)])+ theme(legend.position="none") + ggtitle('Logisitic Regression Probability Classification') + theme(plot.margin=unit(c(1,0,0,1),"cm"),axis.title=element_text(size=22),axis.text=element_text(size=16),plot.title = element_text(size=26)) + xlab('Predicted Wins') + ylab('Actual Wins')

multiplot(p1, p2, p3, p4, cols=2)