public class User {
  public int rank;
  public int progress;
  private boolean flag=true;
  public User() {
    this.rank=-8;
    this.progress=0;
  }
  public int rank() {
    return rank;
  }
  public int progress() {
    return progress;
  }
  private void advance(int xp) {
    if (rank==8) {
      return;
    }
    progress+=xp;
    if (progress>=100) {
      int level=progress/100;
      rank+=level;
      progress=progress%100;
      if (flag && rank>=0) {
        flag=false;
        rank+=1;
      }
    }
    if (rank>=8) {
      rank=8;
      progress=0;
    }
  }
  public void incProgress(int level) {
    if (level>8 || level <-8 || level==0) {
      throw new IllegalArgumentException();
    }
    int difference=level-rank;
    if (level>=1 && rank<=-1) {
      difference-=1;
    } else if (rank>=1 && level<=-1) {
      difference+=1;
    }
    if (difference<=-2) {
      return;
    }
    int xp;
    if (difference==0) {
      xp=3;
    } else if (difference==-1) {
      xp=1;
    } else {
      xp=10*difference*difference;
    }
    advance(xp);
  }
}