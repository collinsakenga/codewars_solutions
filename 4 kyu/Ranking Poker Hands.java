import java.util.*;
    
public class PokerHand
{      
    public enum Result { TIE, WIN, LOSS }
    public enum Combo {
    Highcard, Pair, Pairs, Three, Straight, Flush, fullHouse, Four, StraightFlush, Royal
    }
    public enum Card {
    Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace 
    }
    private List<String> value;
    private List<String> suit;
    private String rec="";
    private String rec2="";
    private String rec3="";
    private String rec4="";
    public PokerHand(String hand) {
        String []temp=hand.split(" ");
        this.value=new ArrayList<>();
        this.suit=new ArrayList<>();
        for (String string : temp) {
            this.value.add(string.substring(0,1));
            this.suit.add(string.substring(1,2));
        }
    }
    public boolean suitEqual() {
        String temp=suit.get(0);
        for (String string : suit) {
            if (!string.equals(temp)) {
                return false;
            }
        }
        return true;
    }
    public int pairs () {
        int pairs=1;
        int compare=1;
        for (int i = 0; i < value.size(); i++) {
            String temp=value.get(i);
            for (int j = i+1; j < value.size(); j++) {
                if (value.get(j).equals(temp)) {
                    pairs+=1;
                }
                if (pairs>compare) {
                    compare=pairs;
                }
            }
            pairs=1;
        }
        return compare;
    }
    public boolean isTwoPairs() {
        if (cardNum(value.get(0))==cardNum(value.get(1))
                && cardNum(value.get(2))==cardNum(value.get(3))) {
            rec3=value.get(3);
            rec2=value.get(1);
            rec=value.get(4);
            return true;
        } else if (cardNum(value.get(0))==cardNum(value.get(1))
                && cardNum(value.get(3))==cardNum(value.get(4))) {
            rec3=value.get(3);
            rec2=value.get(1);
            rec=value.get(2);
            return true;
        } else if (cardNum(value.get(1))==cardNum(value.get(2))
                && cardNum(value.get(3))==cardNum(value.get(4))) {
            rec3=value.get(3);
            rec2=value.get(1);
            rec=value.get(0);
            return true;
        }
        if (cardNum(value.get(0))==cardNum(value.get(1))) {
            rec4=value.get(0);
            rec3=value.get(4);
            rec2=value.get(3);
            rec=value.get(2);
        } else if (cardNum(value.get(1))==cardNum(value.get(2))) {
            rec4=value.get(1);
            rec3=value.get(4);
            rec2=value.get(3);
            rec=value.get(0);
        } else if (cardNum(value.get(2))==cardNum(value.get(3))) {
            rec4=value.get(2);
            rec3=value.get(4);
            rec2=value.get(1);
            rec=value.get(0);
        } else if (cardNum(value.get(3))==cardNum(value.get(4))) {
            rec4=value.get(3);
            rec3=value.get(2);
            rec2=value.get(1);
            rec=value.get(0);
        }
        return false;
    }
    public int cardNum(String s) {
        if (s.equals("2")) {
            return Card.Two.ordinal();
        }
        else if (s.equals("3")) {
            return Card.Three.ordinal();
        }
        else if (s.equals("4")) {
            return Card.Four.ordinal();
        }
        else if (s.equals("5")) {
            return Card.Five.ordinal();
        }        
        else if (s.equals("6")) {
            return Card.Six.ordinal();
        }        
        else if (s.equals("7")) {
            return Card.Seven.ordinal();
        }        
        else if (s.equals("8")) {
            return Card.Eight.ordinal();
        }        
        else if (s.equals("9")) {
            return Card.Nine.ordinal();
        }        
        else if (s.equals("T")) {
            return Card.Ten.ordinal();
        }        
        else if (s.equals("J")) {
            return Card.Jack.ordinal();
        }        
        else if (s.equals("Q")) {
            return Card.Queen.ordinal();
        }        
        else if (s.equals("K")) {
            return Card.King.ordinal();
        }        
        else if (s.equals("A")) {
            return Card.Ace.ordinal();
        }                    
        return -1;
    }
    public List<String> getValue() {
        return value;
    }

    public List<String> getSuit() {
        return suit;
    }

    public int getRec() {
        return cardNum(rec);
    }

    public int getRec2() {
        return cardNum(rec2);
    }

    public int getRec3() {
        return cardNum(rec3);
    }

    public int getRec4() {
        return cardNum(rec4);
    }
    
    public void sort() {
        String temp1;
        String temp2;
        for (int i = 0; i < value.size(); i++) {
            for (int j = 0; j < value.size()-1; j++) {
                if (cardNum(value.get(j))>cardNum(value.get(j+1))) {
                    temp1=value.get(j);
                    temp2=suit.get(j);
                    value.set(j, value.get(j+1));
                    suit.set(j, suit.get(j+1));
                    value.set(j+1, temp1);
                    suit.set(j+1, temp2);
                }
            }
        }
    }
    public void biggerFour() {
        if (cardNum(value.get(0))!=cardNum(value.get(1))) {
            rec2=value.get(2);
            rec=value.get(0);
        } else if (cardNum(value.get(3))!=cardNum(value.get(4))) {
            rec=value.get(4);
            rec2=value.get(2);
        }
    }
    public boolean isStraight() {
        for (int i = 1; i < value.size(); i++) {
            if ((cardNum(value.get(i))-cardNum(value.get(i-1)))!=1) {
                return false;
            }
        }
        return true;
    }
    public Boolean isFullHouse() {
        if (cardNum(value.get(0))==cardNum(value.get(1))
                &&((cardNum(value.get(2))==cardNum(value.get(3)))
                && (cardNum(value.get(3))==cardNum(value.get(4))))) {
            rec=value.get(0);
            rec2=value.get(2);
            return true;
        } else if (cardNum(value.get(3))==cardNum(value.get(4)) 
                &&((cardNum(value.get(2))==cardNum(value.get(1)))
                && (cardNum(value.get(1))==cardNum(value.get(0))))){
            rec2=value.get(2);
            rec=value.get(3);
            return true;
        }
        if (cardNum(value.get(0))==cardNum(value.get(1)) 
                && cardNum(value.get(1)) ==cardNum(value.get(2))) {
            rec3=value.get(2);
            rec2=value.get(4);
            rec=value.get(3);
        } else if (cardNum(value.get(1))==cardNum(value.get(2)) 
                && cardNum(value.get(2)) ==cardNum(value.get(3))) {
            rec3=value.get(2);
            rec2=value.get(4);
            rec=value.get(0);
        } else if (cardNum(value.get(2))==cardNum(value.get(3)) 
                && cardNum(value.get(3)) ==cardNum(value.get(4))) {
            rec3=value.get(2);
            rec2=value.get(1);
            rec=value.get(0);
        }
        return false;
    }
    public int compute() {
        sort();
        if (suitEqual()) {
            if (isStraight()) {
                if (cardNum(value.get(0))==Card.Ten.ordinal()) {
                    return Combo.Royal.ordinal();
                }
                return Combo.StraightFlush.ordinal();
            }
            return Combo.Flush.ordinal();
        }
        if (isStraight()) {
            return Combo.Straight.ordinal();
        }
        if (pairs()==4) {
            biggerFour();
            return Combo.Four.ordinal();
        } else if (pairs()==3) {
            if (isFullHouse()) {
                return Combo.fullHouse.ordinal();
            }
            return Combo.Three.ordinal();
        } else if (pairs()==2) {
            if (isTwoPairs()) {
                return Combo.Pairs.ordinal();
            }
            return Combo.Pair.ordinal();
        }
        return Combo.Highcard.ordinal();
    }
    public Result compareWith(PokerHand poker) {        
        if (poker.compute()>this.compute()) {
            return Result.LOSS;
        } else if (poker.compute()<this.compute()) {
            return Result.WIN;          
        }
        List<String> temp=poker.getValue();
        if (poker.compute()==Combo.Royal.ordinal()) {
            return Result.TIE;
        } else if (poker.compute()==Combo.StraightFlush.ordinal() 
                || poker.compute()==Combo.Flush.ordinal() 
                || poker.compute()==Combo.Straight.ordinal()
                || poker.compute()==Combo.Highcard.ordinal()) {
            for (int i = value.size()-1; i > -1; i--) {
                if (cardNum(temp.get(i))>cardNum(value.get(i))) {
                    return Result.LOSS;
                } else if (cardNum(temp.get(i))<cardNum(value.get(i))) {
                    return Result.WIN;
                }
            }
            return Result.TIE;
        } else if (poker.compute()==Combo.Four.ordinal()) {            
            if (this.getRec2()<poker.getRec2()) {
                return Result.LOSS;
            } else if (this.getRec2()>poker.getRec2()) {
                return Result.WIN;
            } else {
                if (this.getRec()>poker.getRec()) {
                    return Result.WIN;
                } else if (this.getRec()<poker.getRec()) {
                    return Result.LOSS;
                }
                return Result.TIE;
            }
        } else if (poker.compute()==Combo.Pair.ordinal()) {
            if (this.getRec4()<poker.getRec4()) {
                return Result.LOSS;
            } else if (this.getRec4()>poker.getRec4()) {
                return Result.WIN;
            } else {
                if (this.getRec3()>poker.getRec3()) {
                    return Result.WIN;
                } else if (this.getRec3()<poker.getRec3()) {
                    return Result.LOSS;
                } else {
                    if (this.getRec2()>poker.getRec2()) {
                        return Result.WIN;
                    } else if (this.getRec2()<poker.getRec2()) {
                        return Result.LOSS;
                    } else {
                        if (this.getRec()>poker.getRec()) {
                            return Result.WIN;
                        } else if (this.getRec()<poker.getRec()) {
                            return Result.LOSS;
                        } else {
                            return Result.TIE;
                        }
                    }
                }                
            }
        } else if (poker.compute()==Combo.Pairs.ordinal()) {
            if (this.getRec3()<poker.getRec3()) {
                return Result.LOSS;
            } else if (this.getRec3()>poker.getRec3()) {
                return Result.WIN;
            } else {
                if (this.getRec2()>poker.getRec2()) {
                    return Result.WIN;
                } else if (this.getRec2()<poker.getRec2()) {
                    return Result.LOSS;
                } else {
                    if (this.getRec()>poker.getRec()) {
                        return Result.WIN;
                    } else if (this.getRec()<poker.getRec()) {
                        return Result.LOSS;
                    } else {
                        return Result.TIE;
                    }
                }                
            }
        } else if (poker.compute()==Combo.Three.ordinal()) {
            if (this.getRec3()<poker.getRec3()) {
                return Result.LOSS;
            } else if (this.getRec3()>poker.getRec3()) {
                return Result.WIN;
            } else {
                if (this.getRec2()>poker.getRec2()) {
                    return Result.WIN;
                } else if (this.getRec2()<poker.getRec2()) {
                    return Result.LOSS;
                } else {
                    if (this.getRec()>poker.getRec()) {
                        return Result.WIN;
                    } else if (this.getRec()<poker.getRec()) {
                        return Result.LOSS;
                    } else {
                        return Result.TIE;
                    }
                }
            }
        } else if (poker.compute()==Combo.fullHouse.ordinal()) {
            if (this.getRec3()<poker.getRec3()) {
                return Result.LOSS;
            } else if (this.getRec3()>poker.getRec3()) {
                return Result.WIN;
            } else {
                if (this.getRec2()>poker.getRec2()) {
                    return Result.WIN;
                } else if (this.getRec2()<poker.getRec2()) {
                    return Result.LOSS;
                } else {
                    if (this.getRec()>poker.getRec()) {
                        return Result.WIN;
                    } else if (this.getRec()<poker.getRec()) {
                        return Result.LOSS;
                    } else {
                        return Result.TIE;
                    }
                }                
            }
        }
        return Result.TIE;
    }
}