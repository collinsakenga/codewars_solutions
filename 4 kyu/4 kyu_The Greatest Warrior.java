import java.util.*;
public class Warrior {
    private int level;
    private int experience;
    private List<String> levelsList;
    private String rank;
    private List<String> awards;
    public Warrior() {
        this.experience=100;
        this.level=experience/100;
        this.levelsList=new ArrayList<String>(Arrays.asList("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"));
        this.rank=levelsList.get(0);
        this.awards=new ArrayList<>();
    }
    public String rank() {
        return levelsList.get(rankInt());
    }
    public int rankInt() {
        return level()/10;
    }
    public int level() {
        return experience()/100;
    }
    public int experience() {
        int temp=experience;
        if (temp>10000) {
            temp=10000;
        }
        return temp;
    }
    public String battle(int level) {
        if (level<1 || level >100) {
            return "Invalid level";
        }
        if (level()>=level) {
            if (level()==level) {
                experience+=10;
                return "A good fight";
            } else if (level()==level+1) {
                experience+=5;
                return "A good fight";
            }
            return "Easy fight";          
        } else {
            int diff=level-level();
            int compare=rankInt();
            int compare2=level/10;
            if (compare2>10) {
                compare2=10;
            }
            if (compare2>compare && diff>=5) {
                return "You've been defeated";
            }
            experience+=20*(diff)*(diff);
            return "An intense fight";
        }
    }
    public String training(String name, int xp, int level) {
        if (level>level()) {
            return "Not strong enough";
        }
        this.experience+=xp;
        awards.add(name);
        return name;
    }
    public List<String> achievements() {
        return awards;
    }
}